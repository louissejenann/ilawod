## ============================================================
## PROPS MINIGAME — Lusay's lanterns
## ============================================================

init python:
    lantern_types = [
        "squid", "jellyfish", "plant", 
        "moon", "seed", "mushroom", "lotus"
    ]

screen minigame_props():
    # Game State
    default time_left     = props_time_left
    default lanterns_done = props_lanterns_done
    default clicks_needed = 3
    default current_clicks = 0
    default is_switching   = False 

    # Slider Logic
    default bar_val = 0
    default moving_forward = True
    default zone_start = 42
    default zone_end = 58

    python:
    
        current_index = min(lanterns_done, 6)
        l_name = lantern_types[current_index]

    # Background
    add "images/Lusays workshop blurr.png"

    # Main Game Loop
    timer 0.02 repeat True action [
        If(moving_forward,
            [If(bar_val < 100, SetScreenVariable("bar_val", bar_val + 2), SetScreenVariable("moving_forward", False))],
            [If(bar_val > 0, SetScreenVariable("bar_val", bar_val - 2), SetScreenVariable("moving_forward", True))]
        ),
        If(time_left > 0,
            SetScreenVariable("time_left", max(0, time_left - 0.02)),
            Return(lanterns_done)
        )
    ]

    ## ── Full Screen Images 
    if current_clicks < clicks_needed and not is_switching:
        add ("images/unorganize lantern " + l_name + ".png") align (0.5, 0.5)
        text "Assembly: [current_clicks]/3" xalign 0.5 ypos 700 style "minigame_title" size 30
    else:
        # This block now correctly stays on the current lantern while the timer runs
        add ("images/organize lantern " + l_name + ".png") align (0.5, 0.5)
        text "Success!" xalign 0.5 ypos 700 style "minigame_success"
        
        if not is_switching:
            timer 0.6 action [
                SetScreenVariable("is_switching", True),
                SetScreenVariable("lanterns_done", lanterns_done + 1),
                SetScreenVariable("current_clicks", 0),
                SetScreenVariable("is_switching", False)
            ]

    ## ── Header
    hbox:
        xalign 0.5 ypos 30
        spacing 100
        text "Time: [time_left:.1f]s" style "minigame_title"
        text "Lanterns: [lanterns_done] / 7" style "minigame_title"

    ## ── Timing Bar & Control
    vbox:
        xalign 0.5 ypos 820
        spacing 20

        fixed:
            xsize 600 ysize 60
            bar value 100 range 100 xsize 600 yalign 0.5
            
            frame:
                xpos (zone_start * 6)
                xsize ((zone_end - zone_start) * 6)
                ysize 30
                background "#00ff00"
                yalign 0.5

            frame:
                xpos (bar_val * 6)
                xsize 15 ysize 50
                background "#ffffff"
                yalign 0.5

        imagebutton:
            idle "gui/assemble_idle.png" 
            hover "gui/assemble_hover.png" # You can add a hover file here later
            xalign 0.5
            
            # Disable button during the success animation
            action If(not is_switching, 
                If(bar_val >= zone_start and bar_val <= zone_end,
                    true = [
                        SetScreenVariable("current_clicks", current_clicks + 1),
                        Play("sound", "audio/water_drop.ogg")
                    ],
                    false = [
                        SetScreenVariable("current_clicks", 0),
                        Play("sound", "audio/kadyos_whimper.ogg")
                    ]
                ),
                None
            )

    if lanterns_done >= 7:
        timer 0.5 action Return(lanterns_done)

label minigame_props_start:
    lusay "Okay! Let's finish these lanterns — catch the light at the right moment!"
    narrator "Click when the pointer is in the green zone. You need 3 perfect hits per lantern!"
    
    $ props_time_left = 60
    $ props_lanterns_done = 0
    
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