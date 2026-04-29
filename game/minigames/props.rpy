## ============================================================
## PROPS MINIGAME — Lusay's lanterns
## Target: 7 lanterns before time runs out
## ============================================================

init python:
    def lantern_piece_dropped(drags, drop):
        if drop is None:
            return

        piece = drags[0].drag_name
        slot  = drop.drag_name
        
        correct_map = {f"piece_{i}": f"slot_{i}" for i in range(1, 12)}

        if correct_map.get(piece) == slot:
            drags[0].snap(drop.x, drop.y)
            
            if slot not in renpy.store.current_slots:
                renpy.store.current_slots.append(slot)
            return
        else:
            drags[0].snap(drags[0].start_x, drags[0].start_y)
            return

screen minigame_props():
    default time_left     = props_time_left
    default lanterns_done = props_lanterns_done

    add "images/Lusays workshop.png"

    text "Time: [time_left]s"            xpos 60  ypos 30 style "minigame_title"
    text "Lanterns: [lanterns_done] / 7" xpos 1630 ypos 30 style "minigame_title"

    timer 1.0 repeat True action If(
        time_left > 0,
        true  = SetScreenVariable("time_left", time_left - 1),
        false = Return(lanterns_done)
    )

    add "images/Lantern_Line_Jellyfish.png" xalign 0.5 ypos 0

    draggroup:
        # SLOTS (Targets)
        drag:
            drag_name "slot_1" droppable True xpos 570 ypos 125 xsize 60 ysize 50
            if "slot_1" in current_slots:
                add "images/Lantern_1P_Jellyfish.png"
        drag:
            drag_name "slot_2" droppable True xpos 555 ypos 175 xsize 90 ysize 70
            if "slot_2" in current_slots:
                add "images/Lantern_2P_Jellyfish.png"
        drag:
            drag_name "slot_3" droppable True xpos 530 ypos 250 xsize 140 ysize 150
            if "slot_3" in current_slots:
                add "images/Lantern_3P_Jellyfish.png"
        drag:
            drag_name "slot_4" droppable True xpos 555 ypos 400 xsize 90 ysize 60
            if "slot_4" in current_slots:
                add "images/Lantern_4P_Jellyfish.png"
        drag:
            drag_name "slot_5" droppable True xpos 400 ypos 125 xsize 60 ysize 50
            if "slot_5" in current_slots:
                add "images/Lantern_5P_Jellyfish.png"
        drag:
            drag_name "slot_6" droppable True xpos 400 ypos 175 xsize 90 ysize 70
            if "slot_6" in current_slots:
                add "images/Lantern_6P_Jellyfish.png"
        drag:
            drag_name "slot_7" droppable True xpos 400 ypos 250 xsize 140 ysize 150
            if "slot_7" in current_slots:
                add "images/Lantern_7P_Jellyfish.png"
        drag:
            drag_name "slot_8" droppable True xpos 400 ypos 400 xsize 90 ysize 60
            if "slot_8" in current_slots:
                add "images/Lantern_8P_Jellyfish.png"
        drag:
            drag_name "slot_9" droppable True xpos 700 ypos 250 xsize 90 ysize 60
            if "slot_9" in current_slots:
                add "images/Lantern_9P_Jellyfish.png"
        drag:
            drag_name "slot_10" droppable True xpos 700 ypos 320 xsize 90 ysize 60
            if "slot_10" in current_slots:
                add "images/Lantern_10P_Jellyfish.png"
        drag:
            drag_name "slot_11" droppable True xpos 700 ypos 390 xsize 90 ysize 60
            if "slot_11" in current_slots:
                add "images/Lantern_11P_Jellyfish.png"

        # PIECES (Draggables)
        if "slot_1" not in current_slots:
            drag:
                drag_name "piece_1" draggable True xpos 50 ypos 80
                dragged lantern_piece_dropped
                add "images/Lantern_1P_Jellyfish.png"
        if "slot_2" not in current_slots:
            drag:
                drag_name "piece_2" draggable True xpos 1200 ypos 30
                dragged lantern_piece_dropped
                add "images/Lantern_2P_Jellyfish.png"
        if "slot_3" not in current_slots:
            drag:
                drag_name "piece_3" draggable True xpos 1300 ypos 340
                dragged lantern_piece_dropped
                add "images/Lantern_3P_Jellyfish.png"
        if "slot_4" not in current_slots:
            drag:
                drag_name "piece_4" draggable True xpos 1490 ypos 500
                dragged lantern_piece_dropped
                add "images/Lantern_4P_Jellyfish.png"
        if "slot_5" not in current_slots:
            drag:
                drag_name "piece_5" draggable True xpos 344 ypos 40
                dragged lantern_piece_dropped
                add "images/Lantern_5P_Jellyfish.png"
        if "slot_6" not in current_slots:
            drag:
                drag_name "piece_6" draggable True xpos 1610 ypos 280
                dragged lantern_piece_dropped
                add "images/Lantern_6P_Jellyfish.png"
        if "slot_7" not in current_slots:
            drag:
                drag_name "piece_7" draggable True xpos 230 ypos 300
                dragged lantern_piece_dropped
                add "images/Lantern_7P_Jellyfish.png"
        if "slot_8" not in current_slots:
            drag:
                drag_name "piece_8" draggable True xpos 980 ypos 500
                dragged lantern_piece_dropped
                add "images/Lantern_8P_Jellyfish.png"
        if "slot_9" not in current_slots:
            drag:
                drag_name "piece_9" draggable True xpos 660 ypos 60
                dragged lantern_piece_dropped
                add "images/Lantern_9P_Jellyfish.png"
        if "slot_10" not in current_slots:
            drag:
                drag_name "piece_10" draggable True xpos 60 ypos 750
                dragged lantern_piece_dropped
                add "images/Lantern_10P_Jellyfish.png"
        if "slot_11" not in current_slots:
            drag:
                drag_name "piece_11" draggable True xpos 420 ypos 580
                dragged lantern_piece_dropped
                add "images/Lantern_11P_Jellyfish.png"

    if len(current_slots) == 11:
        timer 0.5 action [
            SetScreenVariable("lanterns_done", lanterns_done + 1),
            SetVariable("current_slots", [])
        ]
        text "Lantern complete!" xalign 0.5 ypos 560 style "minigame_success"

    if lanterns_done >= 7:
        timer 0.5 action Return(lanterns_done)

label minigame_props_start:
    lusay "Okay! Let's finish these lanterns — drag each piece to its place!"
    narrator "Assemble all 7 lanterns before time runs out!"
    
    $ current_slots = []
    $ props_time_left = 60
    $ props_lanterns_done = 0
    
    call screen minigame_props

    $ props_lanterns = _return

    if props_lanterns >= 7:
        $ score_props = 3
    elif props_lanterns >= 4:
        $ score_props = 2
    else:
        $ score_props = 1

    return