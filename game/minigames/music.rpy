################################################################################
## MUSIC MINIGAME — Kasag conducts
################################################################################

init python:

    ################################################################################
    MUSIC_NOTE_SIZE  = 50    
    MUSIC_HIT_Y      = 0.70   
    MUSIC_LANE_X     = [0.35, 0.45, 0.55, 0.65]  
    MUSIC_TIMING_WINDOW = 0.08  

    ##speed per phase (higher = faster)
    MUSIC_SPEED_P1   = 0.004  #slow 
    MUSIC_SPEED_P2   = 0.006  #warmup
    MUSIC_SPEED_P3   = 0.009  # full rhythm

    ## Phase time boundaries (seconds)
    MUSIC_PHASE_1_END = 9.0
    MUSIC_PHASE_2_END = 18.0

    #how long after last note before game ends
    MUSIC_END_BUFFER  = 28.0

    ## Score thresholds
    MUSIC_SCORE_GOOD    = 20
    MUSIC_SCORE_NEUTRAL = 12
    

    ## Each note is (spawn_time, lane)
    ## Phase 1 (0-9s):    slow, one at a time, very wide gaps
    ## Phase 2 (9-18s):   medium, occasional pairs, more breathing room
    ## Phase 3 (18-26s):  faster, tighter but not overwhelming
    music_notes = [
        ## Phase 1 one at a time, very relaxed
        (1.0, 0),
        (3.0, 2),
        (5.0, 1),
        (7.0, 3),
        (9.0, 0),

        ## Phase 2  slight pairs, 
        (11.0, 1),
        (12.5, 3),
        (14.0, 0), (14.0, 2),
        (16.0, 1),
        (17.0, 3),
        (18.0, 2), (18.0, 0),

        ## Phase 3 
        (21.0, 3),
        (22.0, 0), (22.0, 2),
        (23.0, 1),
        (23.8, 3),
        (24.6, 0), (24.6, 2),
        (25.4, 1), (25.4, 3),
    ]
    music_total = len(music_notes)

    def music_spawn(elapsed, active, spawned):
        for i, note in enumerate(music_notes):
            if i not in spawned and elapsed >= note[0]:
                active.append([note[1], -0.05, i])  
                spawned.add(i)

    def music_move(active, elapsed):
        if elapsed < MUSIC_PHASE_1_END:
            speed = MUSIC_SPEED_P1
        elif elapsed < MUSIC_PHASE_2_END:
            speed = MUSIC_SPEED_P2
        else:
            speed = MUSIC_SPEED_P3
        for note in active:
            note[1] += speed

    def music_miss(active, miss_box, last_action):
        for note in active[:]:
            if note[1] > 1.05:  
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
            if note[0] == lane and abs(note[1] - MUSIC_HIT_Y) < MUSIC_TIMING_WINDOW:
                music_active.remove(note)
                music_hit_box[0] += 1
                music_last_action[0] = "hit"
                renpy.restart_interaction()
                return
        ## No note in range would counts as a miss
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

    $ last_action = music_last_action[0]

    ## Musicians react to last action 
    if last_action == "hit":
        add "images/musicians_normal.png" xpos 100 ypos 80
    elif last_action == "miss":
        add "images/musicians_shame.png"  xpos 100 ypos 80
    else:
        add "images/musicians_normal.png" xpos 100 ypos 80

    ## Conductor reacts to last action 
    if last_action == "hit":
        add "images/conductor_okay.png" xpos 30 ypos 100
    elif last_action == "miss":
        add "images/conductor_bad.png"  xpos 30 ypos 100
    else:
        add "images/conductor_idle.png" xpos 30 ypos 100

    ## Hit targets 
    for lane_index, lane_x in enumerate(MUSIC_LANE_X):
        add "images/rhythm_hitzone.png":
            xalign lane_x
            yalign MUSIC_HIT_Y
            zoom (MUSIC_NOTE_SIZE / 50.0)

    ## Lane labels Arrow Symbols
    for lane_index, (lane_x, label) in enumerate(zip(MUSIC_LANE_X, ["↑", "←", "→", "↓"])):
        text label:
            xalign lane_x
            yalign (MUSIC_HIT_Y + 0.05)
            xoffset -5
            yoffset 25
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
            Function(music_move, music_active, elapsed),
            Function(music_miss, music_active, music_miss_box, music_last_action),
            If(
                elapsed > MUSIC_END_BUFFER and len(music_spawned) == music_total and len(music_active) == 0,
                true = [SetScreenVariable("done", True), Return(music_hit_box[0])]
            ),
        ]

    ## Draw notes
    for note in music_active:
        add "images/rhythm_note_dance.png":
            xalign MUSIC_LANE_X[note[0]]
            yalign note[1]
            zoom (MUSIC_NOTE_SIZE / 50.0)

    ## Key bindings
    key "K_UP" action [Function(music_key_press, 0), NullAction()]
    key "K_LEFT" action [Function(music_key_press, 1), NullAction()]
    key "K_RIGHT" action [Function(music_key_press, 2), NullAction()]
    key "K_DOWN" action [Function(music_key_press, 3), NullAction()]


label minigame_music_start:
    kasag "Fine. Show me what you've got."
    narrator "Cue the musicians, press the arrow keys in time before the notes pass the line!!"
    call screen minigame_music

    $ music_hits = _return

    if music_hits >= MUSIC_SCORE_GOOD:
        $ score_music = 3
        jump kasag_good
    elif music_hits >= MUSIC_SCORE_NEUTRAL:
        $ score_music = 2
        jump kasag_neutral
    else:
        $ score_music = 1
        jump kasag_bad

    return