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
            "piece_1"  : "slot_1",
            "piece_2"  : "slot_2",
            "piece_3"  : "slot_3",
            "piece_4"  : "slot_4",
            "piece_5"  : "slot_5",
            "piece_6"  : "slot_6",
            "piece_7"  : "slot_7",
            "piece_8"  : "slot_8",
            "piece_9"  : "slot_9",
            "piece_10" : "slot_10",
            "piece_11" : "slot_11",
        }
        return correct_map.get(piece) == slot

screen minigame_props():
    default time_left     = 60
    default lanterns_done = 0
    default current_slots = []

    add "images/Lusays workshop.png"

    text "Time: [time_left]s"            xpos 60  ypos 30 style "minigame_title"
    text "Lanterns: [lanterns_done] / 7" xpos 850 ypos 30 style "minigame_title"

    timer 1.0 repeat True action If(
        time_left > 0,
        true  = SetScreenVariable("time_left", time_left - 1),
        false = Return(lanterns_done)
    )

    add "images/Lantern_Line_Jellyfish.png" xalign 0.5 ypos 120

    draggroup:

        drag:
            drag_name "slot_1"
            droppable True
            xpos 570 ypos 125
            xsize 60 ysize 50
            if "slot_1" in current_slots:
                add "images/Lantern_1P_Jellyfish.png"
            else:
                add "images/slot_empty.png"

        drag:
            drag_name "slot_2"
            droppable True
            xpos 555 ypos 175
            xsize 90 ysize 70
            if "slot_2" in current_slots:
                add "images/Lantern_2P_Jellyfish.png"
            else:
                add "images/slot_empty.png"

        drag:
            drag_name "slot_3"
            droppable True
            xpos 530 ypos 250
            xsize 140 ysize 150
            if "slot_3" in current_slots:
                add "images/Lantern_3P_Jellyfish.png"
            else:
                add "images/slot_empty.png"

        drag:
            drag_name "slot_4"
            droppable True
            xpos 555 ypos 400
            xsize 90 ysize 60
            if "slot_4" in current_slots:
                add "images/Lantern_4P_Jellyfish.png"
            else:
                add "images/slot_empty.png"

        drag:
            drag_name "slot_5"
            droppable True
            xpos 400 ypos 125
            xsize 60 ysize 50
            if "slot_5" in current_slots:
                add "images/Lantern_5P_Jellyfish.png"
            else:
                add "images/slot_empty.png"

        drag:
            drag_name "slot_6"
            droppable True
            xpos 400 ypos 175
            xsize 90 ysize 70
            if "slot_6" in current_slots:
                add "images/Lantern_6P_Jellyfish.png"
            else:
                add "images/slot_empty.png"

        drag:
            drag_name "slot_7"
            droppable True
            xpos 400 ypos 250
            xsize 140 ysize 150
            if "slot_7" in current_slots:
                add "images/Lantern_7P_Jellyfish.png"
            else:
                add "images/slot_empty.png"

        drag:
            drag_name "slot_8"
            droppable True
            xpos 400 ypos 400
            xsize 90 ysize 60
            if "slot_8" in current_slots:
                add "images/Lantern_8P_Jellyfish.png"
            else:
                add "images/slot_empty.png"

        drag:
            drag_name "slot_9"
            droppable True
            xpos 700 ypos 250
            xsize 90 ysize 60
            if "slot_9" in current_slots:
                add "images/Lantern_9P_Jellyfish.png"
            else:
                add "images/slot_empty.png"

        drag:
            drag_name "slot_10"
            droppable True
            xpos 700 ypos 320
            xsize 90 ysize 60
            if "slot_10" in current_slots:
                add "images/Lantern_10P_Jellyfish.png"
            else:
                add "images/slot_empty.png"

        drag:
            drag_name "slot_11"
            droppable True
            xpos 700 ypos 390
            xsize 90 ysize 60
            if "slot_11" in current_slots:
                add "images/Lantern_11P_Jellyfish.png"
            else:
                add "images/slot_empty.png"

        if "slot_1" not in current_slots:
            drag:
                drag_name "piece_1"
                draggable True
                xpos 80 ypos 130
                dragged lantern_piece_dropped
                add "images/Lantern_1P_Jellyfish.png"

        if "slot_2" not in current_slots:
            drag:
                drag_name "piece_2"
                draggable True
                xpos 80 ypos 200
                dragged lantern_piece_dropped
                add "images/Lantern_2P_Jellyfish.png"

        if "slot_3" not in current_slots:
            drag:
                drag_name "piece_3"
                draggable True
                xpos 80 ypos 270
                dragged lantern_piece_dropped
                add "images/Lantern_3P_Jellyfish.png"

        if "slot_4" not in current_slots:
            drag:
                drag_name "piece_4"
                draggable True
                xpos 80 ypos 340
                dragged lantern_piece_dropped
                add "images/Lantern_4P_Jellyfish.png"

        if "slot_5" not in current_slots:
            drag:
                drag_name "piece_5"
                draggable True
                xpos 1050 ypos 130
                dragged lantern_piece_dropped
                add "images/Lantern_5P_Jellyfish.png"

        if "slot_6" not in current_slots:
            drag:
                drag_name "piece_6"
                draggable True
                xpos 1050 ypos 200
                dragged lantern_piece_dropped
                add "images/Lantern_6P_Jellyfish.png"

        if "slot_7" not in current_slots:
            drag:
                drag_name "piece_7"
                draggable True
                xpos 1050 ypos 270
                dragged lantern_piece_dropped
                add "images/Lantern_7P_Jellyfish.png"

        if "slot_8" not in current_slots:
            drag:
                drag_name "piece_8"
                draggable True
                xpos 1050 ypos 340
                dragged lantern_piece_dropped
                add "images/Lantern_8P_Jellyfish.png"

        if "slot_9" not in current_slots:
            drag:
                drag_name "piece_9"
                draggable True
                xpos 1050 ypos 410
                dragged lantern_piece_dropped
                add "images/Lantern_9P_Jellyfish.png"

        if "slot_10" not in current_slots:
            drag:
                drag_name "piece_10"
                draggable True
                xpos 80 ypos 410
                dragged lantern_piece_dropped
                add "images/Lantern_10P_Jellyfish.png"

        if "slot_11" not in current_slots:
            drag:
                drag_name "piece_11"
                draggable True
                xpos 80 ypos 480
                dragged lantern_piece_dropped
                add "images/Lantern_11P_Jellyfish.png"

    if len(current_slots) == 11:
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
        jump lusay_good
    elif props_lanterns >= 4:
        $ score_props = 2
        jump lusay_neutral
    else:
        $ score_props = 1
        jump lusay_bad

    return
