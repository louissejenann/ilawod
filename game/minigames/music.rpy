## ============================================================
## MUSIC MINIGAME — Kasag conducts
## Speed: MODERATELY FAST
## ============================================================

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
