## ============================================================
## DANCE MINIGAME — Sili-Sili's performance
## Speed: FAST
## Notes travel right to left into lane targets on the left side
## ============================================================

init python:
    DANCE_NOTE_SIZE = 50  ## px — change this to match rhythm_note_dance.png

    ## Lane Y positions as fractions of screen height (0.0 to 1.0)
    ## A=top, D=bottom, evenly spaced
    DANCE_LANE_Y = [0.25, 0.40, 0.55, 0.70]

    ## Hit zone X position as fraction of screen width
    DANCE_HIT_X = 0.40

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
                ## note = [lane, xpos_fraction, index]
                active.append([note[1], 1.05, i])
                spawned.add(i)

    def dance_move(active, speed):
        ## speed is a fraction of screen width per tick
        for note in active:
            note[1] -= speed

    def dance_miss(active, miss_box):
        for note in active[:]:
            if note[1] < 0.0:
                active.remove(note)
                miss_box[0] += 1

    def dance_key_press(lane, active, hit_box):
        for note in active[:]:
            if note[0] == lane and abs(note[1] - DANCE_HIT_X) < 0.04:
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

    ## Dancer reacts to hits
    if hit_box[0] > 20:
        add "images/dancer_great.png" xpos 30 ypos 100
    elif hit_box[0] > 10:
        add "images/dancer_okay.png"  xpos 30 ypos 100
    else:
        add "images/dancer_idle.png"  xpos 30 ypos 100

    ## Crowd reacts to hits
    if hit_box[0] > 20:
        add "images/crowd_cheering.png" xpos 950 ypos 80
    elif hit_box[0] > 10:
        add "images/crowd_watching.png" xpos 950 ypos 80
    else:
        add "images/crowd_bored.png"    xpos 950 ypos 80

    ## Hit targets — one circle per lane at DANCE_HIT_X
    for lane_index, lane_y in enumerate(DANCE_LANE_Y):
        add "images/rhythm_hitzone.png":
            xalign DANCE_HIT_X
            yalign lane_y
            zoom (DANCE_NOTE_SIZE / 50.0)

    ## Lane labels A/B/C/D just left of the hit targets
    for lane_index, (lane_y, label) in enumerate(zip(DANCE_LANE_Y, ["A", "B", "C", "D"])):
        text label:
            xalign (DANCE_HIT_X - 0.05)
            yalign lane_y
            style "rhythm_key"

    ## Hit counter
    text "Hits: [hit_box[0]]" xpos 550 ypos 20 style "minigame_title"

    ## Game tick
    if not done:
        timer 0.03 repeat True action [
            SetScreenVariable("elapsed", elapsed + 0.03),
            Function(dance_spawn, elapsed, active, spawned),
            Function(dance_move, active, 0.008),
            Function(dance_miss, active, miss_box),
        ]

    ## Draw notes
    for note in active:
        add "images/rhythm_note_dance.png":
            xalign note[1]
            yalign DANCE_LANE_Y[note[0]]
            zoom (DANCE_NOTE_SIZE / 50.0)

    ## Key bindings
    key "K_a" action Function(dance_key_press, 0, active, hit_box)
    key "K_b" action Function(dance_key_press, 1, active, hit_box)
    key "K_c" action Function(dance_key_press, 2, active, hit_box)
    key "K_d" action Function(dance_key_press, 3, active, hit_box)

    if elapsed > 8.0 and len(active) == 0 and not done:
        $ done = True
        timer 0.5 action Return(hit_box[0])


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
