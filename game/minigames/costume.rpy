## ============================================================
## COSTUME MINIGAME — Sigay's Workshop
## Mechanic: Timed search — click correct items Sigay describes.
## Correct items = joy materials. Wrong items = decoys.
## Score routing preserved from original:
##   >= 7 correct clicks → good   (sigay_good)
##   >= 4 correct clicks → neutral (sigay_neutral)
##   < 4 correct clicks  → bad    (sigay_bad)
##
## IMAGE FILES NEEDED:
##   images/bg_sigay_workshop.png        ← your workshop background
##   images/sigay_workshop_items.png     ← optional overlay layer
##
##   Correct (joy) items — should glow warmly, feel alive:
##   images/item_teal_weave.png          ← teal diagonal fabric
##   images/item_pincushion.png          ← the red pin cushion
##   images/item_thread_spool.png        ← thread spool on table
##   images/item_jellyfish_sketch.png    ← design sketch on wall
##   images/item_sea_green_fabric.png    ← hanging sea-green swatch
##   images/item_light_sash.png          ← the light flowing sash
##   images/item_biolum_trim.png         ← glowing trim piece
##
##   Wrong (fear/decoy) items — dull, rigid, or heavy:
##   images/item_orange_bolt.png         ← plain heavy orange fabric
##   images/item_hoop_frame.png          ← the rigid circular frame
##   images/item_brown_roll.png          ← the rolled brown bolt
##   images/item_dark_drape.png          ← heavy dark drape
##   images/item_broken_hanger.png       ← empty broken hanger
##
##   Feedback overlays:
##   images/item_glow_correct.png        ← glow flash on correct click
##   images/item_flash_wrong.png         ← red flash on wrong click
## ============================================================


init python:

    # ── Item definitions ──────────────────────────────────────
    # Each item: position on screen, image, whether it's correct,
    # and a hint label (shown briefly on hover if you want it)

    SIGAY_ITEMS = [

        # ── CORRECT items (joy materials) ──
        {
            "name"    : "teal_weave",
            "correct" : True,
            "hint"    : "Something that moves like water",
            "xpos"    : 120,
            "ypos"    : 180,
            "xsize"   : 110,
            "ysize"   : 130,
            "image"   : "images/item_teal_weave.png",
        },
        {
            "name"    : "pincushion",
            "correct" : True,
            "hint"    : "Something to hold it all together",
            "xpos"    : 860,
            "ypos"    : 340,
            "xsize"   : 80,
            "ysize"   : 80,
            "image"   : "images/item_pincushion.png",
        },
        {
            "name"    : "thread_spool",
            "correct" : True,
            "hint"    : "The one that catches the light",
            "xpos"    : 1340,
            "ypos"    : 290,
            "xsize"   : 70,
            "ysize"   : 90,
            "image"   : "images/item_thread_spool.png",
        },
        {
            "name"    : "jellyfish_sketch",
            "correct" : True,
            "hint"    : "Last year's memory",
            "xpos"    : 1100,
            "ypos"    : 60,
            "xsize"   : 160,
            "ysize"   : 130,
            "image"   : "images/item_jellyfish_sketch.png",
        },
        {
            "name"    : "sea_green_fabric",
            "correct" : True,
            "hint"    : "The color of the sea igniting",
            "xpos"    : 310,
            "ypos"    : 40,
            "xsize"   : 100,
            "ysize"   : 160,
            "image"   : "images/item_sea_green_fabric.png",
        },
        {
            "name"    : "light_sash",
            "correct" : True,
            "hint"    : "Something that breathes",
            "xpos"    : 530,
            "ypos"    : 260,
            "xsize"   : 90,
            "ysize"   : 110,
            "image"   : "images/item_light_sash.png",
        },
        {
            "name"    : "biolum_trim",
            "correct" : True,
            "hint"    : "It glows from below",
            "xpos"    : 750,
            "ypos"    : 460,
            "xsize"   : 100,
            "ysize"   : 70,
            "image"   : "images/item_biolum_trim.png",
        },

        # ── WRONG items (fear materials / decoys) ──
        {
            "name"    : "orange_bolt",
            "correct" : False,
            "hint"    : "",
            "xpos"    : 420,
            "ypos"    : 40,
            "xsize"   : 110,
            "ysize"   : 160,
            "image"   : "images/item_orange_bolt.png",
        },
        {
            "name"    : "hoop_frame",
            "correct" : False,
            "hint"    : "",
            "xpos"    : 870,
            "ypos"    : 120,
            "xsize"   : 130,
            "ysize"   : 130,
            "image"   : "images/item_hoop_frame.png",
        },
        {
            "name"    : "brown_roll_left",
            "correct" : False,
            "hint"    : "",
            "xpos"    : 820,
            "ypos"    : 380,
            "xsize"   : 140,
            "ysize"   : 130,
            "image"   : "images/item_brown_roll.png",
        },
        {
            "name"    : "brown_roll_right",
            "correct" : False,
            "hint"    : "",
            "xpos"    : 1230,
            "ypos"    : 390,
            "xsize"   : 140,
            "ysize"   : 130,
            "image"   : "images/item_brown_roll.png",
        },
        {
            "name"    : "dark_drape",
            "correct" : False,
            "hint"    : "",
            "xpos"    : 600,
            "ypos"    : 40,
            "xsize"   : 110,
            "ysize"   : 170,
            "image"   : "images/item_dark_drape.png",
        },
        {
            "name"    : "broken_hanger",
            "correct" : False,
            "hint"    : "",
            "xpos"    : 660,
            "ypos"    : 220,
            "xsize"   : 80,
            "ysize"   : 60,
            "image"   : "images/item_broken_hanger.png",
        },
    ]


## ── Screen ────────────────────────────────────────────────────

screen sigay_search_screen():

    # Variables local to this screen
    default time_left    = 55           # seconds — adjust here if needed
    default found        = []           # list of correct item names found
    default wrong_clicks = []           # wrong items clicked (greyed out)
    default last_click   = ""          # "correct" / "wrong" / "" for flash
    default flash_timer  = 0           # counts down the flash display

    # ── Background ──
    add "images/Sigays workshop.png"

    # ── Timer countdown ──
    timer 1.0 repeat True action If(
        time_left > 0,
        true  = SetScreenVariable("time_left", time_left - 1),
        false = Return(len(found))
    )

    # ── Sigay's request — changes as timer gets low ──
    if time_left > 35:
        text "Sigay: \"Find me something that moves like the sea igniting — warm, alive, light from below.\"":
            xalign 0.5 ypos 16 size 19 color "#F0E6C8"
    elif time_left > 15:
        text "Sigay: \"Hurry — something flowing, something that glows — not the heavy ones, not the rigid ones—\"":
            xalign 0.5 ypos 16 size 19 color "#FAC775"
    else:
        text "Sigay: \"Anything — just not the dull ones — please—\"":
            xalign 0.5 ypos 16 size 19 color "#F09595"

    # ── Timer display ──
    text "[time_left]s":
        xpos 30 ypos 20 size 26
        color ("#F09595" if time_left <= 15 else "#FAC775")

    # ── Found counter ──
    text "Found: [len(found)] / 7":
        xpos 1180 ypos 20 size 22 color "#9FE1CB"

    # ── Items ──
    for item in SIGAY_ITEMS:

        $ already_found  = item["name"] in found
        $ already_wrong  = item["name"] in wrong_clicks

        if not already_found and not already_wrong:
            imagebutton:
                idle  item["image"]
                hover item["image"]
                xpos  item["xpos"]
                ypos  item["ypos"]
                xsize item["xsize"]
                ysize item["ysize"]

                action If(
                    item["correct"],
                    # Correct — add to found, trigger correct flash
                    true = [
                        SetScreenVariable("found", found + [item["name"]]),
                        SetScreenVariable("last_click", "correct"),
                        SetScreenVariable("flash_timer", 3),
                        If(
                            len(found) + 1 >= 7,
                            true = Return(len(found) + 1),
                            false = NullAction()
                        )
                    ],
                    # Wrong — grey it out, trigger wrong flash
                    false = [
                        SetScreenVariable("wrong_clicks", wrong_clicks + [item["name"]]),
                        SetScreenVariable("last_click", "wrong"),
                        SetScreenVariable("flash_timer", 3),
                    ]
                )

        # Greyed out — already grabbed (wrong) or found (correct)
        elif already_found:
            add item["image"]:
                xpos  item["xpos"]
                ypos  item["ypos"]
                xsize item["xsize"]
                ysize item["ysize"]
                alpha 0.35

        elif already_wrong:
            add item["image"]:
                xpos  item["xpos"]
                ypos  item["ypos"]
                xsize item["xsize"]
                ysize item["ysize"]
                alpha 0.2

    # ── Click feedback flash ──
    if flash_timer > 0:
        timer 0.3 repeat True action SetScreenVariable(
            "flash_timer", max(0, flash_timer - 1)
        )
        if last_click == "correct":
            text "✓ That's it!":
                xalign 0.5 ypos 580 size 28 color "#9FE1CB"
        elif last_click == "wrong":
            text "✗ Not this one.":
                xalign 0.5 ypos 580 size 28 color "#F09595"

    # ── Time up overlay ──
    if time_left <= 0:
        frame:
            xalign 0.5 yanchor 0.5 ypos 360
            background "#000000CC"
            padding (40, 24)
            vbox:
                spacing 14
                text "The tide turned.":
                    xalign 0.5 size 28 color "#FAC775"
                text "Items found: [len(found)] / 7":
                    xalign 0.5 size 22 color "#C8B89A"
                textbutton "Show Sigay what you found →":
                    xalign 0.5
                    action Return(len(found))
                    background "#1A3A1A"
                    hover_background "#2A5A2A"
                    padding (16, 10)


## ── Label ─────────────────────────────────────────────────────

label minigame_costume_start:

    sigay "The studio is — I know it looks like chaos, it IS chaos, but everything I need is in here somewhere."
    sigay "Find me what I'm looking for. Something that moves. Something alive. Not the heavy ones. Not the rigid ones."
    narrator "Click the right materials before the tide turns. Listen to what Sigay is describing."

    call screen sigay_search_screen

    $ costumes_made = _return

    ## ── Score routing — preserved from original ──
    if costumes_made >= 7:
        $ score_costume = 3
        jump sigay_good
    elif costumes_made >= 4:
        $ score_costume = 2
        jump sigay_neutral
    else:
        $ score_costume = 1
        jump sigay_bad

    return
