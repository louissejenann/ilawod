## ============================================================
## UTILS — Shared styles and scoring
## ============================================================

## ------------------------------------------------------------
## Styles
## ------------------------------------------------------------

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


## ------------------------------------------------------------
## Scoring
## Max = 15 (3 per game x 5 games)
## ------------------------------------------------------------

label calculate_final_score:
    $ total_score = score_food + score_costume + score_dance + score_music + score_props

    narrator "The preparations are complete. The festival is about to begin."

    if total_score >= 13:
        jump good_ending
    elif total_score >= 8:
        jump neutral_ending
    else:
        jump bad_ending
