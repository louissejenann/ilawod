################################################################################
## DANCE MINIGAME — Sili-Sili's performance
################################################################################
init python:
    DANCE_NOTE_SIZE = 50  

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
                active.append([note[1], 1.05, i])
                spawned.add(i)

    def dance_move(active, speed):
        for note in active:
            note[1] -= speed

    def dance_miss(active, miss_box, last_action):
        for note in active[:]:
            if note[1] < 0.0:
                active.remove(note)
                miss_box[0] += 1
                last_action[0] = "miss"
                renpy.restart_interaction()

    dance_active      = []
    dance_hit_box     = [0]
    dance_miss_box    = [0]
    dance_spawned     = set()
    dance_last_action = ["idle"]

    def dance_key_press(lane):
        for note in dance_active[:]:
            if note[0] == lane and abs(note[1] - DANCE_HIT_X) < 0.04:
                dance_active.remove(note)
                dance_hit_box[0] += 1
                dance_last_action[0] = "hit"
                renpy.restart_interaction()
                return
        ## No note in range — counts as a miss
        dance_last_action[0] = "miss"
        renpy.restart_interaction()

screen minigame_dance():
    default elapsed      = 0.0
    default done         = False
    default last_action  = "idle"

    on "show":
        action [
            Function(dance_active.clear),
            Function(dance_spawned.clear),
            Function(dance_hit_box.__setitem__, 0, 0),
            Function(dance_miss_box.__setitem__, 0, 0),
            Function(dance_last_action.__setitem__, 0, "idle"),
        ]

    add "images/bg dance_stage.png"

    ## Sync last_action from global each frame
    $ last_action = dance_last_action[0]

    ## Dancer reacts to last action
    if last_action == "hit":
        add "images/dancer_great.png" xpos 30 ypos 100
    elif last_action == "miss":
        add "images/dancer_okay.png"  xpos 30 ypos 100
    else:
        add "images/dancer_idle.png"  xpos 30 ypos 100

    ## Crowd reacts to last action
    if last_action == "hit":
        add "images/crowd_cheering.png" xpos 950 ypos 80
    elif last_action == "miss":
        add "images/crowd_bored.png"    xpos 950 ypos 80
    else:
        add "images/crowd_watching.png" xpos 950 ypos 80

    ## Hit targets — one circle per lane at DANCE_HIT_X
    for lane_index, lane_y in enumerate(DANCE_LANE_Y):
        add "images/rhythm_hitzone.png":
            xalign DANCE_HIT_X
            yalign lane_y
            zoom (DANCE_NOTE_SIZE / 50.0)

    ## Lane labels Arrow Symbols
    $ arrow_labels = ["↑", "←", "→", "↓"]
    for lane_index, (lane_y, label) in enumerate(zip(DANCE_LANE_Y, arrow_labels)):
        text label:
            xalign (DANCE_HIT_X - 0.05)
            yalign lane_y
            xoffset 10
            yoffset -5
            style "rhythm_key"

    ## Hit counter
    text "Hits: [dance_hit_box[0]]" xpos 550 ypos 20 style "minigame_title"

    ## Reset reaction to idle after 0.5s
    if last_action == "hit":
        timer 1.5 action [
            Function(dance_last_action.__setitem__, 0, "idle"),
            SetScreenVariable("last_action", "idle"),
        ]

    ## Game tick
    if not done:
        timer 0.03 repeat True action [
            SetScreenVariable("elapsed", elapsed + 0.03),
            Function(dance_spawn, elapsed, dance_active, dance_spawned),
            Function(dance_move, dance_active, 0.008),
            Function(dance_miss, dance_active, dance_miss_box, dance_last_action),
            If(
                elapsed > 8.0 and len(dance_spawned) == dance_total and len(dance_active) == 0,
                true = [SetScreenVariable("done", True), Return(dance_hit_box[0])]
            ),
        ]

    ## Draw notes
    for note in dance_active:
        add "images/rhythm_note_dance.png":
            xalign note[1]
            yalign DANCE_LANE_Y[note[0]]
            zoom (DANCE_NOTE_SIZE / 50.0)

    ## Key bindings
    key "K_UP" action [Function(dance_key_press, 0), NullAction()]
    key "K_LEFT" action [Function(dance_key_press, 1), NullAction()]
    key "K_RIGHT" action [Function(dance_key_press, 2), NullAction()]
    key "K_DOWN" action [Function(dance_key_press, 3), NullAction()]


label minigame_dance_start:
    narrator "Show them what the performance can be! Press the arrowkeys when the notes reach the line!"
    narrator "Same roots. Different flower. Press the keys to match the rhythm!"
    call screen minigame_dance

    $ dance_hits = _return

    if dance_hits >= 24:
        $ score_dance = 3
        jump BS_good
    elif dance_hits >= 15:
        $ score_dance = 2
        jump BS_neutral
    else:
        $ score_dance = 1
        jump BS_bad

    return
