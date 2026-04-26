## ============================================================
## COSTUME MINIGAME — Sigay's costumes
## Target: 7 costumes, drag + stitch
## ============================================================

init python:
    def costume_piece_dropped(drags, drop):
        if drop is None:
            return False
        piece = drags[0].drag_name
        slot  = drop.drag_name
        correct_map = {
            "piece_headdress" : "slot_headdress",
            "piece_top"       : "slot_top",
            "piece_skirt"     : "slot_skirt",
            "piece_sash"      : "slot_sash",
            "piece_shoes"     : "slot_shoes",
        }
        return correct_map.get(piece) == slot

screen minigame_costume():
    default costumes_done = 0
    default current_slots = []
    default stitched      = []

    add "images/bg costume_workshop.png"

    text "Costumes: [costumes_done] / 7" xalign 0.5 ypos 20 style "minigame_title"

    add "images/costume_outline.png" xalign 0.5 ypos 60

    if "slot_headdress" in stitched:
        add "images/costume_headdress.png" xalign 0.5 ypos 70
    if "slot_top" in stitched:
        add "images/costume_top.png"       xalign 0.5 ypos 160
    if "slot_skirt" in stitched:
        add "images/costume_skirt.png"     xalign 0.5 ypos 310
    if "slot_sash" in stitched:
        add "images/costume_sash.png"      xalign 0.5 ypos 290
    if "slot_shoes" in stitched:
        add "images/costume_shoes.png"     xalign 0.5 ypos 490

    draggroup:

        drag:
            drag_name "slot_headdress"
            droppable True
            xpos 560 ypos 70
            xsize 80 ysize 70
            if "slot_headdress" not in stitched:
                add "images/slot_dashed.png"

        drag:
            drag_name "slot_top"
            droppable True
            xpos 545 ypos 155
            xsize 110 ysize 130
            if "slot_top" not in stitched:
                add "images/slot_dashed.png"

        drag:
            drag_name "slot_sash"
            droppable True
            xpos 545 ypos 280
            xsize 110 ysize 50
            if "slot_sash" not in stitched:
                add "images/slot_dashed.png"

        drag:
            drag_name "slot_skirt"
            droppable True
            xpos 540 ypos 300
            xsize 120 ysize 180
            if "slot_skirt" not in stitched:
                add "images/slot_dashed.png"

        drag:
            drag_name "slot_shoes"
            droppable True
            xpos 555 ypos 480
            xsize 90 ysize 60
            if "slot_shoes" not in stitched:
                add "images/slot_dashed.png"

        if "slot_headdress" not in current_slots and "slot_headdress" not in stitched:
            drag:
                drag_name "piece_headdress"
                draggable True
                xpos 80 ypos 80
                dragged costume_piece_dropped
                dropped SetScreenVariable("current_slots", current_slots + ["slot_headdress"])
                add "images/piece_headdress.png"

        if "slot_top" not in current_slots and "slot_top" not in stitched:
            drag:
                drag_name "piece_top"
                draggable True
                xpos 80 ypos 180
                dragged costume_piece_dropped
                dropped SetScreenVariable("current_slots", current_slots + ["slot_top"])
                add "images/piece_top.png"

        if "slot_sash" not in current_slots and "slot_sash" not in stitched:
            drag:
                drag_name "piece_sash"
                draggable True
                xpos 1060 ypos 180
                dragged costume_piece_dropped
                dropped SetScreenVariable("current_slots", current_slots + ["slot_sash"])
                add "images/piece_sash.png"

        if "slot_skirt" not in current_slots and "slot_skirt" not in stitched:
            drag:
                drag_name "piece_skirt"
                draggable True
                xpos 1060 ypos 300
                dragged costume_piece_dropped
                dropped SetScreenVariable("current_slots", current_slots + ["slot_skirt"])
                add "images/piece_skirt.png"

        if "slot_shoes" not in current_slots and "slot_shoes" not in stitched:
            drag:
                drag_name "piece_shoes"
                draggable True
                xpos 80 ypos 430
                dragged costume_piece_dropped
                dropped SetScreenVariable("current_slots", current_slots + ["slot_shoes"])
                add "images/piece_shoes.png"

    for slot in current_slots:
        if slot not in stitched:
            imagebutton:
                idle  "gui/btn_stitch.png"
                hover "gui/btn_stitch.png"
                xalign 0.5
                ypos 570
                action SetScreenVariable("stitched", stitched + [slot])

    text "Stitched: [len(stitched)] / 5" xpos 60 ypos 600 color "#ffffff"

    if len(stitched) == 5:
        timer 0.5 action [
            SetScreenVariable("costumes_done", costumes_done + 1),
            SetScreenVariable("current_slots", []),
            SetScreenVariable("stitched", []),
        ]
        text "Costume complete!" xalign 0.5 ypos 630 style "minigame_success"

    if costumes_done >= 7:
        timer 0.5 action Return(7)


label minigame_costume_start:
    sigay "The costumes need to come alive. Help me put them together — drag each piece and stitch it in place!"
    narrator "Drag pieces to the dashed slots, then click Stitch to confirm. Complete all 7 costumes!"
    call screen minigame_costume

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
