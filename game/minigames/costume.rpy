################################################################################
## COSTUME MINIGAME — Sigay's Workshop (Final Positions)
##################################################################################

init python:
    SIGAY_ITEMS = [
        {
            "name"    : "green_geometrical",
            "correct" : True,
            "label"   : "Green Geometrical Fabric",
            "xpos"    : 485, "ypos" : 131, "xsize" : 115, "ysize" : 230,
            "image"   : "images/item_greengeometricalfabric.png",
        },
        {
            "name"    : "pincushion",
            "correct" : True,
            "label"   : "Pincushion",
            "xpos"    : 1030, "ypos" : 486, "xsize" : 100, "ysize" : 80,
            "image"   : "images/item_pincushion.png",
        },
        {
            "name"    : "design_sketches",
            "correct" : True,
            "label"   : "Design Sketches",
            "xpos"    : 1410, "ypos" : 150, "xsize" : 210, "ysize" : 170,
            "image"   : "images/item_sketches.png",
        },
        {
            "name"    : "lavender_fabric",
            "correct" : True,
            "label"   : "Lavender Fabric",
            "xpos"    : 104,  "ypos" : 629, "xsize" : 100, "ysize" : 160,
            "image"   : "images/item_lavenderfabric.png",
        },
        {
            "name"    : "orange_flower",
            "correct" : True,
            "label"   : "Orange Flower Fabric",
            "xpos"    : 204, "ypos" : 118, "xsize" : 130, "ysize" : 470,
            "image"   : "images/item_orangeflowerfabric.png",
        },
        {
            "name"    : "red_thread",
            "correct" : True,
            "label"   : "Red Thread",
            "xpos"    : 1731, "ypos" : 354, "xsize" : 35,  "ysize" : 85,
            "image"   : "images/item_redthread.png",
        },
        {
            "name"    : "scissors",
            "correct" : True,
            "label"   : "Scissors",
            "xpos"    : 1042, "ypos" : 889, "xsize" : 130, "ysize" : 110,
            "image"   : "images/item_scissor.png",
        },
    ]

screen sigay_search_screen():
    default time_left       = 60
    default found           = []
    default last_item_label = ""
    default flash_timer     = 0

    add "images/Sigays workshop.png"

    timer 1.0 repeat True action If(
        time_left > 0,
        true = SetScreenVariable("time_left", time_left - 1),
        false = Return(len(found))
    )

    ## ── Header UI ──
    frame:
        background Solid("#00000088")
        xalign 0.5 
        ypos 38
        padding (20, 10)
        
        vbox:
            spacing 5
            if time_left > 35:
                text "Sigay: \"I need my sketches, the pincushion, and all the fabrics—especially the lavender and green ones! Find them quickly!\"" xalign 0.5 size 22 color "#FFF"
            else:
                text "Sigay: \"Hurry! Find the scissors and the red thread so we can finish the festival attire!\"" xalign 0.5 size 22 color "#FFD700"

    ## ── Stats UI ──
    hbox:
        xalign 0.5 ypos 110
        spacing 150
        text "Time: [time_left]s" style "minigame_title"
        text "Items: [len(found)] / 7" style "minigame_title"

    ## ── Interactive Items ──
    for item in SIGAY_ITEMS:
        if item["name"] not in found:
            imagebutton:
                idle item["image"]
                hover item["image"]
                xpos item["xpos"] ypos item["ypos"]
                at transform:
                    on hover:
                        matrixcolor BrightnessMatrix(0.15)
                    on idle:
                        matrixcolor BrightnessMatrix(0.0)
                
                action [
                    SetScreenVariable("found", found + [item["name"]]),
                    SetScreenVariable("last_item_label", item["label"]),
                    SetScreenVariable("flash_timer", 2),
                    If(len(found) + 1 >= 7, true = Return(len(found) + 1), false = NullAction())
                ]
        else:
            add item["image"] xpos item["xpos"] ypos item["ypos"] alpha 0.4 matrixcolor TintMatrix("#9FE1CB")

    ## ── Feedback Text ──
    if flash_timer > 0:
        timer 0.5 repeat True action SetScreenVariable("flash_timer", max(0, flash_timer - 1))
       
        frame:
            xalign 0.5 
            ypos 100 #\
            background Solid("#00000088")
            padding (10, 10)
            
            text "✓ Found the [last_item_label]!" style "minigame_success" size 35

label minigame_costume_start:
    sigay "I can't find my tools in this mess! Help me gather the fabrics and my sewing kit."
    call screen sigay_search_screen
    $ costumes_made = _return

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