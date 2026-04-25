## ============================================================
## PROPS MINIGAME — Lusay's lanterns
## Target: 7 lanterns before time runs out
## ============================================================

init python:
    def lantern_piece_dropped(drags, drop):
        if drop is None:
            return False
        piece = drags[0].drag_name
        slot  = drop.drag_name
        correct_map = {
            "piece_top"   : "slot_top",
            "piece_body"  : "slot_body",
            "piece_base"  : "slot_base",
            "piece_flame" : "slot_flame",
        }
        return correct_map.get(piece) == slot

screen minigame_props():
    default time_left     = 60
    default lanterns_done = 0
    default current_slots = []

    add "images/bg props_workshop.png"

    text "Time: [time_left]s"            xpos 60  ypos 30 style "minigame_title"
    text "Lanterns: [lanterns_done] / 7" xpos 850 ypos 30 style "minigame_title"

    timer 1.0 repeat True action If(
        time_left > 0,
        true  = SetScreenVariable("time_left", time_left - 1),
        false = Return(lanterns_done)
    )

    add "images/lantern_outline.png" xalign 0.5 ypos 120

    draggroup:

        drag:
            drag_name "slot_flame"
            droppable True
            xpos 570 ypos 125
            xsize 60 ysize 50
            if "slot_flame" in current_slots:
                add "images/lantern_flame.png"
            else:
                add "images/slot_empty.png"

        drag:
            drag_name "slot_top"
            droppable True
            xpos 555 ypos 175
            xsize 90 ysize 70
            if "slot_top" in current_slots:
                add "images/lantern_top.png"
            else:
                add "images/slot_empty.png"

        drag:
            drag_name "slot_body"
            droppable True
            xpos 530 ypos 250
            xsize 140 ysize 150
            if "slot_body" in current_slots:
                add "images/lantern_body.png"
            else:
                add "images/slot_empty.png"

        drag:
            drag_name "slot_base"
            droppable True
            xpos 555 ypos 400
            xsize 90 ysize 60
            if "slot_base" in current_slots:
                add "images/lantern_base.png"
            else:
                add "images/slot_empty.png"

        if "slot_flame" not in current_slots:
            drag:
                drag_name "piece_flame"
                draggable True
                xpos 80 ypos 130
                dragged lantern_piece_dropped
                add "images/lantern_flame.png"

        if "slot_top" not in current_slots:
            drag:
                drag_name "piece_top"
                draggable True
                xpos 80 ypos 220
                dragged lantern_piece_dropped
                add "images/lantern_top.png"

        if "slot_body" not in current_slots:
            drag:
                drag_name "piece_body"
                draggable True
                xpos 1050 ypos 220
                dragged lantern_piece_dropped
                add "images/lantern_body.png"

        if "slot_base" not in current_slots:
            drag:
                drag_name "piece_base"
                draggable True
                xpos 1050 ypos 380
                dragged lantern_piece_dropped
                add "images/lantern_base.png"

    if len(current_slots) == 4:
        timer 0.5 action [
            SetScreenVariable("lanterns_done", lanterns_done + 1),
            SetScreenVariable("current_slots", [])
        ]
        text "Lantern complete!" xalign 0.5 ypos 560 style "minigame_success"

    if lanterns_done >= 7:
        timer 0.5 action Return(7)


label minigame_props_start:
    lusay "Okay! Let's finish these lanterns — drag each piece to its place!"
    narrator "Assemble all 7 lanterns before time runs out!"
    call screen minigame_props

    $ props_lanterns = _return

    if props_lanterns >= 7:
        $ score_props = 3
    elif props_lanterns >= 4:
        $ score_props = 2
    else:
        $ score_props = 1

    return
