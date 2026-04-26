## ============================================================
## FOOD MINIGAME — Ba-O's ceremonial dish
## ============================================================

init python:

    food_options = {
        "plate"   : ["coral_plate", "seaweed_wrap_plate", "clam_plate"],
        "dishes"  : ["fish_slice", "crab_soften_coral", "vegetable_ring"],
        "garnish" : ["anemone_petals", "fragmented_coral_stars", "mangrove_propagule_slices"],
        "sauces"  : ["bioluminescent_oil", "fermented_spirit_sauce", "mangrove_propagule_slices"],
    }

    food_good = {
        "plate"   : "coral_plate",
        "dishes"  : "fish_slice",
        "garnish" : "anemone_petals",
        "sauces"  : "bioluminescent_oil",
    }

    food_category_order = ["plate", "dishes", "garnish", "sauces"]

    food_ingredient_labels = {
        "coral_plate"               : "Coral Plate",
        "seaweed_wrap_plate"        : "Seaweed Wrap, Plate",
        "mangrove_propagule_slices" : "Mangrove Propagule Slices",
        "fish_slice"                : "Fish Slice",
        "crab_soften_coral"         : "Crab, Soften Coral",
        "clam_plate"                : "Clam Plate",
        "anemone_petals"            : "Anemone Petals",
        "fragmented_coral_stars"    : "Fragmented Coral Stars",
        "vegetable_ring"            : "Vegetable Ring",
        "bioluminescent_oil"        : "Bioluminescent Oil",
        "fermented_spirit_sauce"    : "Fermented Spirit Sauce",
    }

    def food_set_selection(selections, cat, opt):
        result = dict(selections)
        result[cat] = opt
        return result

    def food_set_selection_remove(selections, cat):
        result = dict(selections)
        result.pop(cat, None)
        return result


screen minigame_food():
    default cat_index  = 0
    default opt_index  = 0
    default selections = {}
    default bad_picks  = 0
    default feedback   = ""

    python:
        _cat       = food_category_order[cat_index] if cat_index < 4 else "sauces"
        _opts      = food_options.get(_cat, [])
        _cur       = _opts[opt_index] if _opts else ""
        _cur_label = food_ingredient_labels.get(_cur, _cur.replace("_", " ").title())
        _cat_label = _cat.capitalize()

    add "bg food_station.png" fit "cover" xalign 0.5 yalign 0.5

    ## ── Plate preview ───────────────────────────────────────

    if "plate" in selections:
        add ("images/food_" + selections["plate"] + ".png") xalign 0.5 ypos 0
    if "dishes" in selections:
        add ("images/food_" + selections["dishes"] + ".png") xalign 0.5 ypos 0
    if "garnish" in selections:
        add ("images/food_" + selections["garnish"] + ".png") xalign 0.5 ypos 0
    if "sauces" in selections:
        add ("images/food_" + selections["sauces"] + ".png") xalign 0.5 ypos 0

    ## ── Category label ──────────────────────────────────────
    text "[_cat_label]" xpos 60 ypos 28 style "minigame_title"

    ## ── Refresh / Reset button (top right) ─────────────────────
    imagebutton idle "gui/btn_refresh.png" xalign 0.95 yalign 0.05 action [
        SetScreenVariable("cat_index",  0),
        SetScreenVariable("opt_index",  0),
        SetScreenVariable("selections", {}),
        SetScreenVariable("bad_picks",  0),
        SetScreenVariable("feedback",   ""),
    ]

    ## ── Progress indicators ─────────────────────────────────
    hbox:
        xalign 0.5
        ypos 430
        spacing 30
        text "Plate"   color ("#FFD700" if "plate"   in selections else ("#ffffff" if cat_index == 0 else "#888888"))
        text "→"       color "#555555"
        text "Dishes"  color ("#FFD700" if "dishes"  in selections else ("#ffffff" if cat_index == 1 else "#888888"))
        text "→"       color "#555555"
        text "Garnish" color ("#FFD700" if "garnish" in selections else ("#ffffff" if cat_index == 2 else "#888888"))
        text "→"       color "#555555"
        text "Sauces"  color ("#FFD700" if "sauces"  in selections else ("#ffffff" if cat_index == 3 else "#888888"))

    ## ── All 3 ingredient thumbnails displayed at once ──────────
    if cat_index < 4:
        hbox:
            xalign 0.5
            ypos 460
            spacing 20
            for _i, _opt in enumerate(_opts):
                python:
                    _opt_good = (_opt == food_good.get(_cat, ""))
                imagebutton idle ("images/ingredient_" + _opt + ".png") action [
                    SetScreenVariable("opt_index",  _i),
                    SetScreenVariable("selections", food_set_selection(selections, _cat, _opt)),
                    SetScreenVariable("bad_picks",  bad_picks if _opt_good else bad_picks + 1),
                    SetScreenVariable("feedback",   "A fine choice." if _opt_good else "Hmm... something feels off."),
                ]

        ## ── Ingredient name for currently hovered/selected ──
        text "[_cur_label]" xalign 0.5 ypos 590 color "#cccccc" size 26

    ## ── Feedback ────────────────────────────────────────────
    if feedback != "":
        text "[feedback]" xalign 0.5 ypos 630 style "minigame_success"

    ## ── << Back button (shows when not on first category) ──────
    if cat_index > 0:
        imagebutton idle "gui/btn_arrow_left.png" xalign 0.15 ypos 490 action [
            SetScreenVariable("cat_index", cat_index - 1),
            SetScreenVariable("opt_index", 0),
            SetScreenVariable("feedback",  ""),
        ]

    ## ── >> Next button (shows after a pick is made, except on last category) ──
    if _cat in selections and cat_index < 3:
        imagebutton idle "gui/btn_arrow_right.png" xalign 0.85 ypos 490 action [
            SetScreenVariable("cat_index", cat_index + 1),
            SetScreenVariable("opt_index", 0),
            SetScreenVariable("feedback",  ""),
        ]

    ## ── All done → return bad_picks count ───────────────────
    if len(selections) == 4:
        timer 0.5 action Return(bad_picks)


label minigame_food_start:
    ba_o "Each ingredient matters. Not everything on the table belongs here, choose with care."
    narrator "Browse each category with the arrows. Click an ingredient to place it on the dish."
    call screen minigame_food

    $ food_bad = _return

    if food_bad == 0:
        $ score_food = 3
        jump bao_good
    elif food_bad <= 2:
        $ score_food = 2
        jump bao_neutral
    else:
        $ score_food = 1
        jump bao_bad
    return
