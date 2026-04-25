## ============================================================
## FOOD MINIGAME — Ba-O's ceremonial dish
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
