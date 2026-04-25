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
    default advancing  = False

    python:
        _cat       = food_category_order[cat_index] if cat_index < 4 else "sauces"
        _opts      = food_options.get(_cat, [])
        _cur       = _opts[opt_index] if _opts else ""
        _cur_label = food_ingredient_labels.get(_cur, _cur.replace("_", " ").title())
        _cat_label = _cat.capitalize()
        _is_good   = (_cur == food_good.get(_cat, ""))

    add "bg_food_station.png"

    ## ── Plate preview ───────────────────────────────────────
    add "food_plate_empty.png" xalign 0.5 ypos 60

    if "plate" in selections:
        add ("images/food_" + selections["plate"] + ".png") xalign 0.5 ypos 80
    if "dishes" in selections:
        add ("images/food_" + selections["dishes"] + ".png") xalign 0.5 ypos 110
    if "garnish" in selections:
        add ("images/food_" + selections["garnish"] + ".png") xalign 0.5 ypos 95
    if "sauces" in selections:
        add ("images/food_" + selections["sauces"] + ".png") xalign 0.5 ypos 125

    ## ── Category label ──────────────────────────────────────
    text "[_cat_label]" xpos 60 ypos 28 style "minigame_title"

    ## ── Remove button (only shows if current category already has a pick) ──
    if _cat in selections and not advancing:
        imagebutton auto "gui/btn_remove_%s.png" xpos 1150 ypos 20 action [
            SetScreenVariable("selections", food_set_selection_remove(selections, _cat)),
            SetScreenVariable("cat_index", food_category_order.index(_cat)),
            SetScreenVariable("feedback", ""),
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

    ## ── Left arrow ──────────────────────────────────────────
    if opt_index > 0 and not advancing and cat_index < 4:
        imagebutton auto "gui/btn_arrow_left_%s.png" xpos 180 ypos 490 action [
            SetScreenVariable("opt_index", opt_index - 1),
            SetScreenVariable("feedback", ""),
        ]

    ## ── Ingredient thumbnail (click to select) ──────────────
    if cat_index < 4 and not advancing:
        imagebutton auto ("images/ingredient_" + _cur + "_%s.png") xalign 0.5 ypos 460 action [
            SetScreenVariable("selections", food_set_selection(selections, _cat, _cur)),
            SetScreenVariable("bad_picks",  bad_picks if _is_good else bad_picks + 1),
            SetScreenVariable("feedback",   "A fine choice." if _is_good else "Hmm... something feels off."),
            SetScreenVariable("advancing",  True),
        ]

    ## ── Right arrow ─────────────────────────────────────────
    if opt_index < 2 and not advancing and cat_index < 4:
        imagebutton auto "gui/btn_arrow_right_%s.png" xpos 1000 ypos 490 action [
            SetScreenVariable("opt_index", opt_index + 1),
            SetScreenVariable("feedback", ""),
        ]

    ## ── Ingredient name ─────────────────────────────────────
    if cat_index < 4:
        text "[_cur_label]" xalign 0.5 ypos 590 color "#cccccc" size 26

    ## ── Feedback ────────────────────────────────────────────
    if feedback != "":
        text "[feedback]" xalign 0.5 ypos 630 style "minigame_success"

    ## ── Auto-advance to next category ───────────────────────
    if advancing:
        timer 1.0 action [
            SetScreenVariable("cat_index", cat_index + 1),
            SetScreenVariable("opt_index", 0),
            SetScreenVariable("feedback",  ""),
            SetScreenVariable("advancing", False),
        ]

    ## ── All done → return bad_picks count ───────────────────
    if len(selections) == 4 and not advancing:
        timer 0.5 action Return(bad_picks)


label minigame_food_start:
    ba_o "The ingredients are before you. Build the ceremonial dish, layer by layer."
    ba_o "Each ingredient matters. Not everything on the table belongs here — choose with care."
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
