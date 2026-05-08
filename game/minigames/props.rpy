## ============================================================
## PROPS MINIGAME — Lusay's lanterns (Timing Bar Version)
## Target: 7 lanterns before time runs out
## ============================================================

screen minigame_props():
    # Game State
    default time_left     = props_time_left
    default lanterns_done = props_lanterns_done
    default clicks_needed = 3
    default current_clicks = 0

    # Slider Logic
    default bar_val = 0
    default moving_forward = True
    default zone_start = 42
    default zone_end = 58

    add "images/Lusays workshop.png"

    # Main Game Loop (Movement & Timer)
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

    ## ── Header (Similar to food.rpy style) ──────────────────
    hbox:
        xalign 0.5 ypos 30
        spacing 100
        text "Time: [time_left:.1f]s" style "minigame_title"
        text "Lanterns: [lanterns_done] / 7" style "minigame_title"

    ## ── Lantern Preview Area ────────────────────────────────
    frame:
        background None
        xalign 0.5 ypos 150
        xsize 800 ysize 500
        
        if current_clicks < clicks_needed:
            add "images/unorganize lantern squid.jpg" xalign 0.5 yalign 0.5
            text "Assembly: [current_clicks]/3" xalign 0.5 ypos 450 style "minigame_title" size 30
        else:
            add "images/organize lantern squid.jpg" xalign 0.5 yalign 0.5
            text "Success!" xalign 0.5 ypos 450 style "minigame_success"
            
            # Reset for next lantern after a brief pause
            timer 0.6 action [
                SetScreenVariable("lanterns_done", lanterns_done + 1),
                SetScreenVariable("current_clicks", 0)
            ]

    ## ── Timing Bar & Controls (Bottom) ──────────────────────
    vbox:
        xalign 0.5 ypos 750
        spacing 30

        # The Visual Slider
        fixed:
            xsize 600 ysize 60
            
            # Track
            bar value 100 range 100 xsize 600 yalign 0.5
            
            # The Green Sweet Spot
            frame:
                xpos (zone_start * 6)
                xsize ((zone_end - zone_start) * 6)
                ysize 40
                background "#00ff00"
                yalign 0.5

            # The Moving Indicator
            frame:
                xpos (bar_val * 6)
                xsize 15 ysize 60
                background "#ffffff"
                yalign 0.5

        # Interaction Button
        imagebutton:
            idle "gui/btn_assemble_idle.png" # Make sure this asset exists
            hover "gui/btn_assemble_hover.png"
            xalign 0.5
            action If(bar_val >= zone_start and bar_val <= zone_end,
                true = [
                    SetScreenVariable("current_clicks", current_clicks + 1),
                    Play("sound", "audio/water_drop.ogg") # From your audio defines
                ],
                false = [
                    SetScreenVariable("current_clicks", 0),
                    Play("sound", "audio/kadyos_whimper.ogg")
                ]
            )

    ## ── Win Condition ───────────────────────────────────────
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