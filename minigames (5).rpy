## ============================================================
## ILAWOD MINIGAMES — Aligned to script.rpy
## Drop this file into your game/ folder
## ============================================================

## ============================================================
## 1. FOOD MINIGAME — Ba-O's ceremonial dish
## ============================================================

init python:
    food_answers = {
        "plate"   : "coral_plate",
        "dishes"  : "sea_dish",
        "garnish" : "sea_flower",
    }

    food_options = {
        "plate"   : ["coral_plate",  "shell_plate",  "leaf_plate"],
        "dishes"  : ["sea_dish",     "reef_dish",    "river_dish"],
        "garnish" : ["sea_flower",   "seaweed",      "coral_bits"],
    }

screen minigame_food():
    default category     = "plate"
    default option_index = 0
    default mistakes     = 0
    default selections   = {}
    default feedback     = ""

    add "images/bg food_station.png"

    text "[category.capitalize()]" xpos 60 ypos 30 style "minigame_title"

    imagebutton:
        idle  "gui/btn_refresh.png"
        hover "gui/btn_refresh.png"
        xpos 1150 ypos 20
        action [
            SetScreenVariable("option_index", 0),
            SetScreenVariable("feedback", "")
        ]

    add "images/food_plate_empty.png" xalign 0.5 ypos 80

    if "plate" in selections:
        add "images/food_[selections['plate']].png" xalign 0.5 ypos 100
    if "dishes" in selections:
        add "images/food_[selections['dishes']].png" xalign 0.5 ypos 130
    if "garnish" in selections:
        add "images/food_[selections['garnish']].png" xalign 0.5 ypos 115

    hbox:
        xalign 0.5
        ypos 420
        spacing 30
        text "Plate"   color ("#FFD700" if "plate"   in selections else "#ffffff")
        text "→"       color "#ffffff"
        text "Dishes"  color ("#FFD700" if "dishes"  in selections else "#ffffff")
        text "→"       color "#ffffff"
        text "Garnish" color ("#FFD700" if "garnish" in selections else "#ffffff")

    if option_index > 0:
        imagebutton:
            idle  "gui/btn_arrow_left.png"
            hover "gui/btn_arrow_left.png"
            xpos 200 ypos 490
            action SetScreenVariable("option_index", option_index - 1)

    hbox:
        xalign 0.5
        ypos 470
        spacing 20

        for i, opt in enumerate(food_options[category]):
            if i == option_index:
                imagebutton:
                    idle  "images/ingredient_[opt].png"
                    hover "images/ingredient_[opt].png"
                    action If(
                        opt == food_answers[category],
                        true  = [
                            SetScreenVariable("selections", dict(list(selections.items()) + [(category, opt)])),
                            SetScreenVariable("feedback", "Correct!"),
                            SetScreenVariable("option_index", 0),
                        ],
                        false = [
                            SetScreenVariable("mistakes", mistakes + 1),
                            SetScreenVariable("feedback", "Wrong! Try again."),
                        ]
                    )
            else:
                add "images/ingredient_[opt].png" zoom 0.7 alpha 0.5

    if option_index < 2:
        imagebutton:
            idle  "gui/btn_arrow_right.png"
            hover "gui/btn_arrow_right.png"
            xpos 1000 ypos 490
            action SetScreenVariable("option_index", option_index + 1)

    text food_options[category][option_index] xalign 0.5 ypos 600 color "#cccccc"

    if feedback != "":
        text "[feedback]" xalign 0.5 ypos 640 style "minigame_success"

    if "plate" in selections and category == "plate":
        timer 0.8 action SetScreenVariable("category", "dishes")
    if "dishes" in selections and category == "dishes":
        timer 0.8 action SetScreenVariable("category", "garnish")

    if len(selections) == 3:
        timer 1.0 action Return(mistakes)


## ba_o gives the intro — consistent with script.rpy kitchen section
label minigame_food_start:
    ba_o "The ingredients are before you. Build the ceremonial dish, layer by layer. Choose wisely."
    narrator "Use the arrows to browse. Click the correct ingredient for each category."
    call screen minigame_food

    $ food_mistakes = _return

    if food_mistakes == 0:
        $ score_food = 3
    elif food_mistakes <= 2:
        $ score_food = 2
    else:
        $ score_food = 1

    return


## ============================================================
## 2. DANCE MINIGAME — Sili-Sili's performance
## Speed: FAST
## ============================================================

init python:
    dance_notes = [
        (0.6, 0), (0.9, 2),
        (1.2, 1), (1.4, 3),
        (1.6, 0), (1.8, 2),
        (2.0, 1), (2.0, 3),
        (2.3, 0), (2.5, 1),
        (2.7, 2), (2.9, 3),
        (3.1, 0), (3.2, 2),
        (3.4, 1), (3.6, 3),
        (3.8, 0), (3.8, 1),
        (4.0, 2), (4.2, 3),
        (4.4, 0), (4.6, 2),
        (4.8, 1), (5.0, 3),
        (5.2, 0), (5.2, 2),
        (5.5, 1), (5.8, 3),
        (6.0, 0), (6.2, 1),
    ]
    dance_total = len(dance_notes)

    def dance_spawn(elapsed, active, spawned):
        for i, note in enumerate(dance_notes):
            if i not in spawned and elapsed >= note[0]:
                active.append([note[1], -30, i])
                spawned.add(i)

    def dance_move(active, speed):
        for note in active:
            note[1] += speed

    def dance_miss(active, miss_box):
        for note in active[:]:
            if note[1] > 660:
                active.remove(note)
                miss_box[0] += 1

    def dance_key_press(lane, active, hit_box):
        for note in active[:]:
            if note[0] == lane and 570 <= note[1] <= 650:
                active.remove(note)
                hit_box[0] += 1
                return True
        return False

screen minigame_dance():
    default elapsed  = 0.0
    default active   = []
    default spawned  = set()
    default hit_box  = [0]
    default miss_box = [0]
    default done     = False

    add "images/bg dance_stage.png"

    if hit_box[0] > 20:
        add "images/dancer_great.png" xpos 30 ypos 100
    elif hit_box[0] > 10:
        add "images/dancer_okay.png"  xpos 30 ypos 100
    else:
        add "images/dancer_idle.png"  xpos 30 ypos 100

    if hit_box[0] > 20:
        add "images/crowd_cheering.png" xpos 950 ypos 80
    elif hit_box[0] > 10:
        add "images/crowd_watching.png" xpos 950 ypos 80
    else:
        add "images/crowd_bored.png"    xpos 950 ypos 80

    add "images/rhythm_hitzone.png" xalign 0.5 ypos 600

    hbox:
        xalign 0.5
        ypos 620
        spacing 80
        text "A" style "rhythm_key"
        text "B" style "rhythm_key"
        text "C" style "rhythm_key"
        text "D" style "rhythm_key"

    text "Hits: [hit_box[0]]" xpos 550 ypos 20 style "minigame_title"

    if not done:
        timer 0.03 repeat True action [
            SetScreenVariable("elapsed", elapsed + 0.03),
            Function(dance_spawn, elapsed, active, spawned),
            Function(dance_move, active, 10),
            Function(dance_miss, active, miss_box),
        ]

    for note in active:
        add "images/rhythm_note_dance.png":
            xpos (370 + note[0] * 90)
            ypos int(note[1])

    key "K_a" action Function(dance_key_press, 0, active, hit_box)
    key "K_b" action Function(dance_key_press, 1, active, hit_box)
    key "K_c" action Function(dance_key_press, 2, active, hit_box)
    key "K_d" action Function(dance_key_press, 3, active, hit_box)

    if elapsed > 8.0 and len(active) == 0 and not done:
        $ done = True
        timer 0.5 action Return(hit_box[0])


## sili gives the dance intro — consistent with script.rpy
label minigame_dance_start:
    sili "Show them what the performance can be! Press A, B, C, D when the notes reach the line!"
    narrator "Same roots. Different flower. Press the keys to match the rhythm!"
    call screen minigame_dance

    $ dance_hits = _return

    if dance_hits >= 24:
        $ score_dance = 3
        sili "Incredible! The dancers moved like the tide itself!"
    elif dance_hits >= 15:
        $ score_dance = 2
        sili "Not bad! The crowd was mostly with you."
    else:
        $ score_dance = 1
        sili "The rhythm was lost. The dancers stumbled. We will... manage."

    return


## 3. MUSIC MINIGAME — Bilong-Bilo conducts
## Speed: MODERATELY FAST

init python:
    music_notes = [
        (1.0, 0), (1.5, 1),
        (2.0, 2), (2.5, 3),
        (3.0, 0), (3.3, 2),
        (3.7, 1), (4.0, 3),
        (4.3, 0), (4.6, 1),
        (5.0, 2), (5.3, 3),
        (5.6, 0), (5.9, 2),
        (6.2, 1), (6.5, 3),
        (6.8, 0), (7.0, 1),
        (7.3, 2), (7.6, 3),
        (8.0, 0), (8.3, 2),
        (8.6, 1), (9.0, 3),
    ]
    music_total = len(music_notes)

    def music_spawn(elapsed, active, spawned):
        for i, note in enumerate(music_notes):
            if i not in spawned and elapsed >= note[0]:
                active.append([note[1], -30, i])
                spawned.add(i)

    def music_move(active, speed):
        for note in active:
            note[1] += speed

    def music_miss(active, miss_box):
        for note in active[:]:
            if note[1] > 660:
                active.remove(note)
                miss_box[0] += 1

    def music_key_press(lane, active, hit_box):
        for note in active[:]:
            if note[0] == lane and 570 <= note[1] <= 650:
                active.remove(note)
                hit_box[0] += 1
                return True
        return False

screen minigame_music():
    default elapsed  = 0.0
    default active   = []
    default spawned  = set()
    default hit_box  = [0]
    default miss_box = [0]
    default done     = False

    add "images/bg music_hall.png"
    add "images/conductor.png" xpos 20 ypos 80

    add "images/rhythm_hitzone.png" xalign 0.5 ypos 600

    hbox:
        xalign 0.5
        ypos 620
        spacing 80
        text "A" style "rhythm_key"
        text "B" style "rhythm_key"
        text "C" style "rhythm_key"
        text "D" style "rhythm_key"

    text "Cues: [hit_box[0]]" xpos 550 ypos 20 style "minigame_title"

    if not done:
        timer 0.03 repeat True action [
            SetScreenVariable("elapsed", elapsed + 0.03),
            Function(music_spawn, elapsed, active, spawned),
            Function(music_move, active, 8),
            Function(music_miss, active, miss_box),
        ]

    for note in active:
        add "images/rhythm_note_music.png":
            xpos (370 + note[0] * 90)
            ypos int(note[1])

    key "K_a" action Function(music_key_press, 0, active, hit_box)
    key "K_b" action Function(music_key_press, 1, active, hit_box)
    key "K_c" action Function(music_key_press, 2, active, hit_box)
    key "K_d" action Function(music_key_press, 3, active, hit_box)

    if elapsed > 11.0 and len(active) == 0 and not done:
        $ done = True
        timer 0.5 action Return(hit_box[0])


## kasag calls this — consistent with script.rpy
label minigame_music_start:
    kasag "Fine. Show me what you've got. Cue the musicians — press A, B, C, D in time!"
    narrator "Conduct the musicians before the notes pass the line!"
    call screen minigame_music

    $ music_hits = _return

    if music_hits >= 20:
        $ score_music = 3
        kasag "...Hmph. I will admit that was not terrible."
    elif music_hits >= 12:
        $ score_music = 2
        kasag "Passable. A few missed cues but the melody held."
    else:
        $ score_music = 1
        jump kasag_bad

    return


## ============================================================
## 4. PROPS MINIGAME — Lusay's lanterns
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


## lusay gives the props intro — consistent with script.rpy
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


## ============================================================
## 5. COSTUME MINIGAME — Sigay's costumes
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


## sigay gives the costume intro — consistent with script.rpy
label minigame_costume_start:
    sigay "The costumes need to come alive. Help me put them together — drag each piece and stitch it in place!"
    narrator "Drag pieces to the dashed slots, then click Stitch to confirm. Complete all 7 costumes!"
    call screen minigame_costume

    $ costumes_made = _return

    if costumes_made >= 7:
        $ score_costume = 3
    elif costumes_made >= 4:
        $ score_costume = 2
    else:
        $ score_costume = 1

    return


## ============================================================
## STYLES
## ============================================================

style minigame_title:
    size 32
    color "#ffffff"
    outlines [(2, "#000000", 0, 0)]

style minigame_success:
    size 36
    color "#FFD700"
    outlines [(2, "#000000", 0, 0)]

style rhythm_key:
    size 40
    color "#ffffff"
    outlines [(2, "#000000", 0, 0)]
    xsize 80
    xalign 0.5


## ============================================================
## CALCULATE TOTAL SCORE
## Max = 15 (3 per game x 5 games)
## Fixed to match label names in script.rpy
## ============================================================

label calculate_final_score:
    $ total_score = score_food + score_costume + score_dance + score_music + score_props

    narrator "The preparations are complete. The festival is about to begin."

    if total_score >= 13:
        jump good_ending       ## matches label in script.rpy
    elif total_score >= 8:
        jump neutral_ending    ## matches label in script.rpy
    else:
        jump bad_ending        ## matches label in script.rpy
