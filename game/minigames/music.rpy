## ============================================================
## MUSIC MINIGAME — Kasag conducts
## Speed: MODERATELY FAST
## Notes travel right to left into lane targets on the left side
## ============================================================

init python:
    MUSIC_NOTE_SIZE = 50  ## px — change this to match rhythm_note_music.png

    ## Lane Y positions as fractions of screen height (0.0 to 1.0)
    ## A=top, D=bottom, evenly spaced
    MUSIC_LANE_Y = [0.25, 0.40, 0.55, 0.70]

    ## Hit zone X position as fraction of screen width
    MUSIC_HIT_X = 0.40

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
                active.append([note[1], 1.05, i])
                spawned.add(i)

    def music_move(active, speed):
        for note in active:
            note[1] -= speed

    def music_miss(active, miss_box, last_action):
        for note in active[:]:
            if note[1] < 0.0:
                active.remove(note)
                miss_box[0] += 1
                last_action[0] = "miss"
                renpy.restart_interaction()

    music_active      = []
    music_hit_box     = [0]
    music_miss_box    = [0]
    music_spawned     = set()
    music_last_action = ["idle"]

    def music_key_press(lane):
        for note in music_active[:]:
            if note[0] == lane and abs(note[1] - MUSIC_HIT_X) < 0.04:
                music_active.remove(note)
                music_hit_box[0] += 1
                music_last_action[0] = "hit"
                renpy.restart_interaction()
                return
        ## No note in range — counts as a miss
        music_last_action[0] = "miss"
        renpy.restart_interaction()

screen minigame_music():
    default elapsed      = 0.0
    default done         = False
    default last_action  = "idle"

    on "show":
        action [
            Function(music_active.clear),
            Function(music_spawned.clear),
            Function(music_hit_box.__setitem__, 0, 0),
            Function(music_miss_box.__setitem__, 0, 0),
            Function(music_last_action.__setitem__, 0, "idle"),
        ]

    add "images/bg music_hall.png"

    ## Sync last_action from global each frame
    $ last_action = music_last_action[0]

    ## Conductor reacts to last action
    if last_action == "hit":
        add "images/conductor_great.png" xpos 30 ypos 100
    elif last_action == "miss":
        add "images/conductor_okay.png"  xpos 30 ypos 100
    else:
        add "images/conductor_idle.png"  xpos 30 ypos 100

    ## Crowd reacts to last action
    if last_action == "hit":
        add "images/crowd_cheering.png" xpos 950 ypos 80
    elif last_action == "miss":
        add "images/crowd_bored.png"    xpos 950 ypos 80
    else:
        add "images/crowd_watching.png" xpos 950 ypos 80

    ## Hit targets — one circle per lane at MUSIC_HIT_X
    for lane_index, lane_y in enumerate(MUSIC_LANE_Y):
        add "images/rhythm_hitzone.png":
            xalign MUSIC_HIT_X
            yalign lane_y
            zoom (MUSIC_NOTE_SIZE / 50.0)

    ## Lane labels A/B/C/D just left of the hit targets
    for lane_index, (lane_y, label) in enumerate(zip(MUSIC_LANE_Y, ["A", "B", "C", "D"])):
        text label:
            xalign (MUSIC_HIT_X - 0.05)
            yalign lane_y
            xoffset 10
            yoffset -5
            style "rhythm_key"

    ## Hit counter
    text "Cues: [music_hit_box[0]]" xpos 550 ypos 20 style "minigame_title"

    ## Reset reaction to idle after 1.5s
    if last_action == "hit":
        timer 1.5 action [
            Function(music_last_action.__setitem__, 0, "idle"),
            SetScreenVariable("last_action", "idle"),
        ]

    ## Game tick
    if not done:
        timer 0.03 repeat True action [
            SetScreenVariable("elapsed", elapsed + 0.03),
            Function(music_spawn, elapsed, music_active, music_spawned),
            Function(music_move, music_active, 0.008),
            Function(music_miss, music_active, music_miss_box, music_last_action),
            If(
                elapsed > 11.0 and len(music_spawned) == music_total and len(music_active) == 0,
                true = [SetScreenVariable("done", True), Return(music_hit_box[0])]
            ),
        ]

    ## Draw notes
    for note in music_active:
        add "images/rhythm_note_music.png":
            xalign note[1]
            yalign MUSIC_LANE_Y[note[0]]
            zoom (MUSIC_NOTE_SIZE / 50.0)

    ## Key bindings
    key "K_a" action [Function(music_key_press, 0), NullAction()]
    key "K_b" action [Function(music_key_press, 1), NullAction()]
    key "K_c" action [Function(music_key_press, 2), NullAction()]
    key "K_d" action [Function(music_key_press, 3), NullAction()]


label minigame_music_start:
    kasag "Fine. Show me what you've got. Cue the musicians — press A, B, C, D in time!"
    narrator "Conduct the musicians before the notes pass the line!"
    call screen minigame_music

    $ music_hits = _return

    if music_hits >= 20:
        $ score_music = 3
        jump kasag_good
    elif music_hits >= 12:
        $ score_music = 2
        jump kasag_neutral
    else:
        $ score_music = 1
        jump kasag_bad

    return