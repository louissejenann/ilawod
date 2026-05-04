# The script of the game goes in this file.

#define e = Character("Eileen") -- DEFAULT ALREADY THERE

define narrator = Character(None,            window_style="narrator_window", what_style="narrator_dialogue")
define kilaw    = Character("Kilaw",         window_style="character_window", who_style="namebox_kilaw_label")
define kadyos   = Character("Kadyos",        window_style="character_window", who_style="namebox_kadyos_label")
define ba_o     = Character("Ba-O",          window_style="character_window", who_style="namebox_ba_o_label")
define toto     = Character("Toto",          window_style="character_window", who_style="namebox_toto_label")
define lusay    = Character("Lusay",         window_style="character_window", who_style="namebox_lusay_label")
define sili     = Character("Sili-Sili",     window_style="character_window", who_style="namebox_sili_label")
define bilo     = Character("Bilong-Bilong", window_style="character_window", who_style="namebox_bilo_label")
define kasag    = Character("Kasag",         window_style="character_window", who_style="namebox_kasag_label")
define sigay    = Character("Sigay",         window_style="character_window", who_style="namebox_sigay_label")
define dawa     = Character("Dawa",          window_style="character_window", who_style="namebox_dawa_label")
define unknown  = Character("???",           window_style="character_window", who_style="namebox_unknown_label")

## Choices tracking
default seen_what_is_this = False
default seen_who_are_you  = False

## Minigame scores
default score_food        = 0
default score_costume     = 0
default score_dance       = 0
default score_music       = 0
default score_props       = 0
default total_score       = 0

## Layers
init python:
    config.layers = ["master", "foreground", "transient", "screens", "overlay"]

## Background
image background moving = Movie(play= "images/Comp1.webm")
image intro village = Movie(play= "images/intro village.webm")
image intro village2 = Movie(play= "images/intro village2.webm")

## Images

## Music

## ──────────────────────────────────────────────────────────────


label start:

    #ACT 01 ---------- EXPOSITION

    #PROLOGUE -- PANHUY-AN

    scene intro sun with Fade(0.5, 0.3, 0.9)
    narrator "There is a place where the sea does not end and the land does not begin."
    
    scene intro village with Dissolve(2.0)
    "At the far edge of the island, where the land loosens its grip and gives way to the tide, lies a quiet village called Panhuy-an."

    narrator "The houses stand on stilts above shallow breathing water. Wooden floors creak with every step."
    
    scene intro morning village
    "Banca boats rest loosely tied to posts, hollowed from trees older than the people who carved them."
    
    scene intro fisher #parang same lng siya with int vuillage2
    "The sea feeds the village." 
    
    show intro village2 with Dissolve(2.0)
    "The village, in turn, learns never to take more than it is given."
    
    scene intro village3
    "In the mornings, the elders watch the horizon."
    
    "Morning smells of salt and smoke. Children run between the stilts"
    
    scene intro caught fish
    "Neighbors call to each other across the water."
    
    scene intro children
    "The old lecturing the young."

    "The whole village moves with the easy rhythm of a place that knows itself."

    "The evening carries distant laughter, the sound of wind and waves folding into each other."

    scene intro night #with zoom 
    "The people here speak of tides, and moon, and seasons when the fish are plentiful."
   
    "...and seasons when even the nets come back empty."

    "Beyond the village, the sea stretches wide and honest."
    #zoom intro night

    "But behind it," 
    scene intro moon 
    
    "behind the stilts and the smoke and the festival drums already beginning their preparations," 
    scene intro moon2 with Dissolve(2.0)
    
    "stands the bakawan."
    scene intro frog 

    "Not planted." 
    scene intro frog2 with Dissolve(1.0)
    
    "Older than any name the villagers could give it." 
    scene intro frog3 with Dissolve(1.0)
    
    "Its roots twist deep into the earth and deeper still into stories passed down by those who came before." 
    scene intro frog jump with Dissolve(1.0)
    
    "The locals call it simply the bakawan," 
    scene intro bakawan #with zoom in
    
    "but they speak of it the way one speaks of something that deserves caution. "

    "Not forbidden." 
    
    "Just... not meant for staying too long."

    "The men of Panhuy-an know this instictively."
    scene intro bakawan #with zoom out

    "Every evening at dusk, they face the treeline and stand."

    "Not in fear" 
    
    "but in witness." 
    
    "Showing the old things that the village remembers."

    "Attention, in Panhuy-an, is a kind of offering."
    scene intro feet running

    "Children are told not to wander near the roots after dark."

    "Some of them listen."


    # BY THE WATERS -- DAWA --------------------
    scene intro dawa with Fade(0.5, 0.3, 0.8)
    narrator "A woman crouches by the water, hands deep in a fishing net."
    
    "She hums something old."

    scene intro dawa noticed
    "Kadyos sniffs nearby."
    
    scene intro dawa mc
    dawa "Your dog's got more sense than you."

    kilaw "He just wants food."
    
    scene intro dawa screen

    dawa "Mm. Don't we all."

    narrator "You grinned slightly at that, leaning against a root as you watched her work."

    kilaw "We haven't caught anything since yesterday."
    
    scene intro dawa screen2
    narrator "Dawa pulls a crab from the net, tosses it into a basket without looking."

    dawa "Then you waited too long. Tide's already turning."
    kilaw "Then i'll go deeper." 
    kilaw "There's always something in the bakawan."

    narrator "Dawa paused at that, just a moment, before tossing you a net."

    kilaw "Hey!"
    dawa "There's always something, yes."
    kilaw "You say that like it's a bad thing."
    dawa "I say it like it's true. I've lived longer than you."
    dawa "Go if you must. But don't follow quiet water."

    narrator "You looked at her like she was saying something silly again"
    
    kilaw "Water is always quiet."

    narrator "Dawa shook her head, like you were being silly."

    dawa "No. Water always has noise."  
    dawa "It's the silence that should trouble you."
    dawa "Because, you never know when you'll be taken."

    narrator "She pokes your shoulder abruptly. Lightly, in a joking manner"

    "You huffed and gently swatted her hands away. She was already smiling at you."

    kilaw "Whatever. I'm going." 
    
    kilaw "I have to show mom how independent I can be. I'm planning to make her dinner."

    dawa "Are you now? Just be careful." 
    dawa "Take an adult with you." 
    dawa "And don't forget to excuse yourself."

    kilaw "Yeah, yeah, okay."
    dawa "I'm serious, Kilaw."
    kilaw "So am I!" 
    kilaw "Don't worry, I'll remember."

    narrator "With that you went on your way."
    
    scene intro festival prep1

    "The afternoon light is golden and low." 
    
    "Somewhere, further down the shoreline, you can hear the faint pulse of drums — the festival preparations already beginning."

    scene intro into bakawan
    "Dawa called after you."

    "Her voice carries over the water, easy as the wind."

    dawa "Make sure you're back before the festival starts." 
    dawa "Your mother will have both our heads if you're not at the lantern lighting!"

    "You wave a hand without turning around."
    scene intro bye1

    "It's still three moons away, but the village never waits until the last moment."

    "The lantern-hanging hadn't started yet but you could feel it coming."
    scene intro bye

    "You'll be back in time. You're always on time."

    # INTO THE WOODS -------------
    scene wood upwards with Fade(0.5, 0.3, 0.8)

    narrator "In search of dinner, you wandered into the forbidden mangrove, a place whispered about in old stories."
    "You didn't bring anyone."
    "You brought someone better."
    "Your trusted friend and companion."
    scene bg mangrove with dissolve
    show fg leaves 

    show kilaw walking:
            xpos 900
            linear 3.0 xpos -600 
    
    kilaw "We don't need any adults, right Kadyos?"
    "..."
    kilaw "Kadyos?"

    "You turned around looking for any sign of him, before you heard a rustle nearby."

    "The bushes shook." 

    hide kilaw walking
    show shock kilaw kadyos with hpunch

    "Then, a brown dog, Kadyos, pops out."
    "Tail wagging like he didn't just washed ten years off your life"

    hide shock kilaw kadyos
    show happy kilaw kadyos 
    
    kilaw "Kadyos! You scared me! Where have you been, silly boy?"
    kilaw "Come on, partner. Let's find something for dinner before the sun goes down, hmmm?"
    
    show happy kilaw kadyos:
                xpos 900
                linear 3.0 xpos -900

    narrator "Kadyos barks and trots ahead."

    hide happy kilaw kadyos
    show background moving
    
    "Together, they made their way deeper into the mangrove."

    "The air grew thicker, the trees taller, their roots twisting like ancient arms reaching for the sky."
    
    scene bushes background with fade
    
    # BOATT! ----------- 

    narrator "You saw something at the corner of your eyes."

    transform gentle_jump:
        yoffset 0
        ease 0.1 yoffset -15    # jump up a little
        ease 0.1 yoffset 0      # settle back down

    scene bushes background2
    show kilaw looking at gentle_jump

    "You push through a wall of bushes and gasp."

    "You found it in a small clearing where the water had pulled back, an old wooden boat, worn and patient, sitting half-in, half-out of the mud."

    hide kilaw looking
    show kilaw looking happy

    kilaw "A boat?"

    scene boat scene with dissolve

    narrator "You looked at the boat with careful attention."
    "In your village, there was a rituals seafarers practiced which involved chanting before fishing or sea raids."
    "If the boat swayed, the spirits blessed the trip."

    scene boat light with dissolve

    "The greater the movement, the greater the fortune!"
    "Or so they say."
    "The boat shifted, barely, just a lean, before settling." 
    "You blinked your eyes. you thought you saw a light." 
    "The water reflection hitting your eyes."

    kilaw "Huh."
    
    narrator "You blinked, before approaching the boat."

    kilaw "Looks sturdy enough. It's probably from one of our neighbors... maybe this will take us to the fattest fish out there!"
    kilaw "I don't think they would mind us borrowing it."
    kilaw "What do you think, Captain Kadyos? Ready to sail?"
    
    narrator "Kadyos barks, doing his tippy-taps as his tail wags"

    # CHOICES: YOU FOUND A BOAT ------------------
    menu: 
        "Take the boat with Kadyos":
            jump route_take_the_boat
        
        "Stay on Land":
            jump route_stay_on_land

    #ROUTE
    label route_stay_on_land:
        narrator "You look at the boat — then at the dark water beyond it. You take a step back."

        kilaw "...No. I don't think so. Something doesn't feel right about that water tonight."

        narrator "Kadyos presses against your side, as if agreeing. You and Kadyos decided to just stay on land, finding other ways to get food." 

        "You foraged for nearby fruit, young leaves, seeds, and fish you could catch near land."

        kilaw "Okay. Land food it is. No mysterious glowing water required."

        narrator "The mangrove offered more than you expected."
        
        "Ripe bayabas along the bank, mudskippers in the shallows you could scoop with your hands." 
        
        "Even some wild kangkong near the water's edge."

        kilaw "Ha. Mom would be proud. Fresh greens, fresh fish. Better than the our own traders brought."

        show boat light with dissolve

        narrator "You passed by the boat as you went home. It still sits there, old and patient, as if waiting."

        menu:
            "Go for a little adventure":
                jump route_go_for_an_adventure
        
            "Ignore it and go home":
                jump route_go_home

        
        label route_go_for_an_adventure:
            show boat scene2 with dissolve

            narrator "You paused. You look at the boat. You look at Kadyos."

            kilaw "...Ugh. Okay. Just a little look. Ten minutes. Then we go home."

            show boat in with dissolve

            narrator "You grab Kadyos and tie your food for later. You step into the boat together."

            "They wandered into the mangrove until evening and got lost." 
            
            "They ate their food, sharing it with Kadyos, until they saw something below the waters" 
            
            "A shimmer, a shadow, something moving with purpose."

            kilaw "Okay that is...definitely something. Definitely not a normal fish."

            narrator "The mudfish appears. You reach for it without thinking. The rest follows."
            jump welcome_spiritrealm_main


        label route_go_home: 
            narrator "You shoulder your foraged bundle and walks past without looking back."

            kilaw "Nope. Not my boat. Home time, Kadyos."

            narrator "Kadyos trots after you, tail going. He glances back at the boat once, just once, then follows"

            "By the time you reach the stilts the sky is the color of cooling embers."
            "The smell of woodsmoke and neighbor-cooking is the best thing you've encountered all day." 
            
            "Your mother scolds you for coming back without fish."
            "You show her the kangkong and the bayabas and the mudskippers, and she scolds you less."
            
            "You cook together."
            "It's good. It was a normal evening."
            "You went to sleep."

            "Behind the village, in the deep water hours, the mangrove is very quiet."
            
            "The men on the night watch stand at the treeline and face it, the way they always do."

            "The festival does not fall apart loudly."
            "It falls apart the way a net comes undone, one thread, then another, then a hole where the fish slip through."

            "You wake to darkness."
            "Not the soft darkness of early morning."
            "The other kind. The kind that sits wrong on the skin."

            "You light a lantern."

            "Through your window, the mangrove stands the same as it always has."

            "You don't know what you missed. You won't. The water keeps what it keeps."

            "Kadyos puts his head in your lap. His tail moves once, slowly."

            return #ENDING 1: BAD (YOU IGNORED THE CALLING)


    label route_take_the_boat:
        show boat scene2 with dissolve

        kilaw "I'll take that as a yes. Let's go!"

        narrator "You grab the edge of the old wooden hull and haul yourself in, arm already extended."

        scene boat in with dissolve

        kilaw "All aboard! Let's see what secrets this mangrove's been hiding."
        
        scene boat scene3 
        with Fade(0.5, 0.3, 0.8)

        transform boat_move:
            xpos 50 ypos -300       
            linear 4.0 xpos -1000 ypos 1010

        show rowing boat at boat_move
        with None
        pause 4.0                     # wait for animation to finish
        hide rowing boat

        narrator "The sun hung low, painting the mangrove in warm orange light. The water glimmered softly, catching the last fire of the day."
        
        transform pan_bg:
            xpos -1920 ypos 0
            linear 45.0 xpos 0

        transform fog_pan:
            xpos -1920 ypos 55
            linear 45.0 xpos 0

        transform rowing_move:
            xpos 1020 ypos 210    
            linear 45.0 xpos -200      

        scene mangrove long at pan_bg
        show fog at fog_pan
        show rowing at rowing_move
        with Fade(0.5, 0.3, 0.8)

        "As you drifted deeper, the shadows grew longer, and the forest started to whisper in the wind."

        transform fog1_pan:
            xpos 0 ypos -10
            linear 45.0 xpos -1920

        scene spiritual realm at pan_bg
        show rowing at rowing_move
        show fog1 at fog1_pan
        with Dissolve(4.0)

        "Your eyes widened as the light faded, the roots beneath you shimmered faintly."

        kilaw "It's beautiful."

        narrator "You whispered, the word forms in your chest like a held breath."

        "Unaware of the world you knew was slowly slipping away."

        "The tide came and went. Your stomach grumbled."

        scene hungry kilaw with fade

        "The glow of the mangrove was lovely but unfortunately it wasn't food. You sighed."

        kilaw "I'm starving Kadyos. If we don't find anything soon, we'll force to eat this boat."

        narrator "Kadyos whines softly."

        scene tree water with Dissolve(2.0)

        show fish spirit:
            xpos -1920        
            ypos 1080        
            linear 3.0 xpos 0 ypos 0 

        $ renpy.pause(4.0)

        show water effect with Dissolve(0.2)
        pause 0.15
        hide water effect 
        show water effect2 with Dissolve(0.2)   
        pause 0.15
        hide water effect2 
        show water effect3 with Dissolve(0.2)
        pause 0.15

        "Suddenly, the glowing water rippled. A mudfish appears near the boat."

        scene kilaw kadyos hungry 
        #show text grumble
        with dissolve

        kilaw "Hey! Did you see that? Dinner's served!"

        scene time for fishing with hpunch
        #show text splash 

        narrator "You try to time it properly before lunging on the fish's direction with half of your body still on the boat."
        #hide text splash with dissolve

        kilaw "Almost... got you!"

        narrator "You try to pull the fish to the surface. Before—"

        show splash with Dissolve(0.2)
        show splash2 with Dissolve(0.4)

        kilaw "Wait... Whoa—!"

        narrator "You tumbled into the glowing water. Bubbles rise. You gasped, trying to swim up."

        kilaw "Kadyos... Help! The water is pulling me!"

        narrator "The shallow tide rose like a living thing — spinning, dragging you both beneath the glowing current."

        menu:
            "Grab onto the boat":
                jump route_grab_boat
            
            "Grab onto Kadyos":
                jump route_grab_kadyos
        
    #ROUTE
    label route_grab_boat:
        narrator "You lunge for the edge of the boat, fingers catching the worn wood. For one breathless moment, you hold on"

        kilaw "Got it — I've got it—!"

        narrator "But the vortex pulls harder. You can feel your grip loosening, the water like cold hands around your wrists."

        "From above, Kadyos barks frantically. You felt the splash before you see him trying to jump in."

        kilaw "No — Kadyos, stay back! Stay—!"

        narrator "The boat lists sideways. The current claims them both. Darkness swallows the last shiver of light."
        jump welcome_spiritrealm_no_kadyos
        

    label route_grab_kadyos: 
        narrator "You reach for Kadyos instead, arms closing around the warm weight of your dog."

        kilaw "I've got you, boy — hold on—"

        narrator "Kadyos paddles furiously, eyes wide with effort. For a breath they almost make it"

        "Then the vortex catches them together — one spiral, pulling two."

        "It is, somehow, less terrifying this way. You hold him tighter."

        kilaw "...It's okay, Kadyos. We'll be—"

        narrator "Darkness. Then silence."
        jump welcome_spiritrealm_main

    #ROUTE: WELCOME TO THE SPIRIT REALM ---------------------------
    label welcome_spiritrealm_no_kadyos: 
        narrator "There is no falling, exactly. It's more like the moment you step off a boat and realize the water is far deeper than your feet expected." 
        
        "One second the roots are solid beneath you. The next second — they aren't anything at all."

        "Then; silence. Before lights came from below."

        "Then the sound of water, not rushing, not still."

        "You open your eyes."

        "You are lying on something solid. Stone, maybe, or old root, so thick and wide it feels like ground." 
        
        "Above you: the underside of the mangrove, but wrong."

        "The roots here arch upward, tall, braided together into something that looks less like a tree and more like a doorframe." 
        
        "Old and enormous, trailing kelp and blossoms you don't have a name for, its wood dark and warm."

        "You are outside something. Just outside." 
        
        "Through the arch, there is light."

        "Before you can sit up fully, a voice arrives."

        "It belongs to a small spirit." 
        
        "Narrow, silver-finned, hovering at the edge of the root-arch with the particular energy of someone who looked like a child that was sent to do a task and is now reconsidering the task."

        unknown "Oh — oh good, you're awake." 

        "Their fins won't quite stay still. They are holding what appears to be a paper??"
        
        "It seems to have been crumpled and re-smoothed at least twice."

        unknown "We felt you come through."  
        unknown "Well. Everyone felt you come through"

        unknown "When something crosses the boundary — falls through the rift — the whole surrouding shift." 
        
        unknown "It seems like you hit the boundaries of our world pretty hard, are you okay?"

        narrator "They gesture vaguely at you."

        sili "You. Anyway. I'm Sili-Sili. Ba-O sent me to bring you in."
        sili "Are you — can you walk? "

        menu:
            "Where's Kadyos?":
                jump route_wheres_kadyos
            
            "Where are we?":
                jump route_where_are_we
            
            "Sure. Lead the way.":
                jump route_lead_way

    label welcome_spiritrealm_main:
        narrator "There is no falling, exactly. It's more like the moment you step off a boat and realize the water is far deeper than your feet expected." 
        "One second the roots are solid beneath you."
        "The next second — they aren't anything at all."
        
        "You reached for Kadyos. You aren't sure if you found him or if he found you first."

        "Then; silence. Before lights came from below."

        "You open your eyes."

        "You are lying on something solid. Stone, maybe, or old root — so thick and wide it feels like ground. Above you: the underside of the mangrove, but wrong. "

        "The roots here arch upward, tall, braided together into something that looks less like a tree and more like a doorframe." 
        
        "Old and enormous, trailing kelp and blossoms you don't have a name for, its wood dark and warm."

        "You are outside something. Just outside." 
        
        "Through the arch, there is light."

        "Before you can sit up fully, a voice arrives."

        "It belongs to a small spirit — narrow, silver-finned, hovering at the edge of the root-arch with the particular energy of someone who looked like a child that was sent to do a task and is now reconsidering the task."

        unknown "Oh — oh good, you're awake. We felt you come through."
        narrator "A beat. Kadyos shakes water off his ears."

        "Their fins won't quite stay still. They are holding what appears to be a paper??, and the schedule has been crumpled and re-smoothed at least twice."

        unknown "Well." 
        unknown "Everyone felt you come through"

        unknown "When something crosses the boundary — falls through the rift — the whole surrouding shift." 
        
        unknown "It seems like you hit the boundaries of our world pretty hard, are you okay?"

        narrator "They gesture vaguely at you two."

        sili "You. Anyway. I'm Sili-Sili. Ba-O sent me to bring you in."
        sili "Are you — can you walk? "

        menu:
            "Where are we?":
                jump route_where_are_we
            
            "Sure. Lead the way.":
                jump route_lead_way
    
    #ROUTE ------------------------------------
    label route_wheres_kadyos:
        kilaw "Kadyos — where's—"
        
        narrator "A bark, from somewhere very close. Kadyos materializes from behind the root-arch with a piece of dried sea-grass in his mouth, tail going."
        
        "Kadyos comes barreling in, scattering a nearby spirit entirely, and hits Kilaw at full speed."

        kilaw "Oh — okay — okay, I've got you—"

        narrator "You do, for a moment, simply hold Kadyos. He smells like the spirit sea. His tail hasn't stopped."

        sili "He came through the same rift."
        sili "Arrived a few minutes ahead of you, actually. We tried to offer him dried mudfish while he waited."

        narrator "Kadyos drops the sea-grass."

        sili "He declined."

        narrator "A beat. Sili-Sili gestures through the root-arch."

        sili "Come in. Ba-O's waiting."
        jump route_inside_gate_main

    label route_where_are_we:
        kilaw "Where...where is this?"

        sili "The spirit realm. The deep part — under the mangrove's roots, where the old tides go." 
        sili "It's — it's easier to show you than explain."
        
        narrator "A beat. Sili-Sili gestures through the root-arch."

        sili "Come in. Ba-O will explain the rest. She's better at explaining than me"
        jump route_inside_gate_main

    label route_lead_way:
        narrator "You get to your feet. Your legs hold. Kadyos presses against your side."

        kilaw "...Uhh, sure. Lead the way then."

        narrator "She looked visibly relieved by your easy agreement as her fins settle slightly."

        kilaw "...Uhh, sure. Lead the way then."
        jump route_inside_gate_main

    #ROUTE: INSIDE THE WOODLAND GATES ----------------------------------
    label route_inside_gate_main: 
        narrator "Sili-Sili leads you through the root-arch."

        kilaw "Woah..."

        narrator "Kadyos runs past you excitedly."

        "The light. It comes from below as much as above — water running in shallow channels between stone paths, the whole ground lit from underneath. Every shadow falls upward." 
        
        "The sky looks like the sea" 
        
        "You're in underwater right now."
        
        "What you thought was a small clearing turns out to be a marketplace, enormous." 
        "Stalls of woven sea-grass and old fishing net, clay pots big enough to sleep in, lanterns strung between crooked posts." 
        
        "At the center: a great stone basin of the same glowing water. The paths all converge on it."

        "The smell is brine and food and something sweet you don't quite have a name for. Two voices argue from somewhere to the left. Something crashes from behind a stall."

        "None of the spirits stop. None of them look up."
        "Except that's not quite right. Because here and there, ones and twos, you catch the sideways glance — the way someone pretends to check a stall display while actually looking elsewhere." 
        "They know you're here. They felt you arrive. They're just letting someone else handle it."

        "Someone is waiting at the edge of the plaza."

        "She is small and ancient-looking, she's holding something on her head, built like a great tidal clam, her shell smoothed by centuries of water. Flour-dusted hands." 
        
        "An expression of someone who has set down one problem to deal with a second problem and would very much like both problems to resolve quickly. She is holding a clay ladle."

        "She appears to have forgotten she is holding it. Beside her is someone taller, calmly standing there as they seem to be in a deep discussion." 

        "Then they look at you. She looks at Kadyos infront of you. She gave a small nods"

        unknown "Good. You're upright. And the dog is — also upright."

        narrator "Kadyos tail wags."

        unknown "Come. Walk with me. There is a great deal to explain and very little time to explain it in."

        narrator "Beside her, keeping pace in the way of someone who has always kept pace with her, is a spirit who moves like still water."
        "Unhurried, present, draped in the particular calm of someone who has seen most things already, and larger than the space they occupy."  
        "They do not introduce themselves."
        
        "When you catch their eye, there's a quality to the look that's somewhere between curiosity and recognition."
        
        "They did not rush, but they don't slow down either — they move automatically, dodging other creatures with ease. You had to actually keep up."

        #CHOICES: YOU FOLLOW THEM AND SAID...
        label introduction_choices:
        menu:
            "What is this?" if not seen_what_is_this:
                jump route_what_is_this

            "Who are you?" if not seen_who_are_you:
                jump route_who_are_you

            "Look at surrounding" if seen_what_is_this and seen_who_are_you:
                jump route_after_the_introduction
        
    #ROUTE REPLY
    label route_what_is_this:
        $ seen_what_is_this = True
        unknown "Did Sili-Sili not tell you? This is the realm of the spirits. Under the mangrove's roots."
        
        unknown "You came through the boundary when the current took you — through the rift of our world."

        narrator "A pause. Somewhere nearby, something falls and breaks"

        unknown "You got here by falling off somewhere. Which is, I will admit, not the traditional method." 
        
        unknown "But the tide does not ask how you arrived. Only that you have."

        narrator "The tall creature speaks, then, low and even, in the manner of someone who chooses their words with care."

        unknown "It has happened before. A mortal crossing the boundary by accident."

        unknown "Very rarely."

        unknown "Two centuries, perhaps three, since the last. A child from the northern shore." 
        
        unknown "Fell in following something bright, the same as you. The tide has particular feelings about children."

        narrator "They say this without pretense, the way one recounts a thing that is simply true."

        unknown "He made it back."

        narrator "A beat." 
        "That hangs in the air, not as comfort, but as information."
        "You are not the first." 
        "Others have gone home."

        "A short silent filled the space as you followed them."
        jump introduction_choices
         
    label route_who_are_you:
        $ seen_who_are_you = True
        ba_o "Ba-O. I keep the ceremonial table. Every offering, every dish, every ingredient placed with intention before the Bakunawa."
        ba_o "Also one of those who oversees this festivity."

        toto "And I am Toto. I handle the majority of the festivities. I oversee the costumes, music, dances, and food."

        narrator "He lay a gentle hand on Ba-O's shoulder." 

        toto "Of course, I'm not alone in what I handle."

        narrator "Ba-O nodded to Toto, she gestures broadly at the marketplace — the stumbling, crashing, slightly desperate marketplace. She continue."

        ba_o "We are the Spirit Committee. All of us together. The ones who keep the old arrangements."
        
        ba_o "And this, this is three days before the awaited festival, which is the most important event in three centuries, and we are—"

        narrator "A stack of offering trays tips, slides, crashes. A nearby spirit lunges. Misses."

        ba_o "Behind. We are behind."
        jump introduction_choices 

    #AFTER THE CHOICES -----
    label route_after_the_introduction:
        narrator "Toto watches the crash with the expression of someone who has already mentally filed it away."
        
        "Their gaze returns to you. Something settles in it — a decision."

        toto "The mortal world holds its own festival in three days also. The Bakunawa has watched both shores."

        narrator "You think of the drums you heard from the village." 
        "The lanterns your neighbors would be stringing."
        "Your mother's voice over the water." 
        "The feeling, already old enough to have settled in your chest, that you were supposed to be home before dark."

        toto "You came here by tide, child. The tide does not send things without reason, even if the reason reveals itself slowly"

        narrator "Ba-O stops. Looks at you steadily."

        ba_o " You came through the boundary. The tide brought you here, whether you chose it or not." 
        ba_o "We won't force your hand. But it knows we needed help."

        narrator "She glances back at the chaos of the marketplace. The ladle is still in her hand."

        ba_o "And if you happened to have free hands..."

        narrator "Toto holds your gaze for a moment longer. Their expression is not unkind." 
        "It is the expression of someone who knows what comes next and trusts that you will find your way to it."

        toto "I have other things to see to. The boundary. The night watch. The preparations that cannot wait."

        narrator "They rest a hand, brief, light, on the top of your head. You do not know why, but it feels like something."

        toto "Ba-O will take care of you. She is good at that."

        narrator "And then they are gone, easing back into the crowd with the easy unhurry of the sea finding its level."
        "Ba-O does not watch them go. She is already looking at you."

        ba_o "Come. Let us start at the beginning, and the beginning, always, is the kitchen. So, would you help?"

        menu:
            "I'll help":
                jump route_help

            "I'll pass":
                jump route_pass

    #ROUTE: -----------------
    label route_help:
        narrator "With no way back home, you and Kadyos had only one choice."
        "Help them finish the festival.... and find a way to return."
        "It would also be a good story to tell the others"

        ba_o "Excellent, lets get this festival up and running!"
        jump route_kitchen

    label route_pass:
        narrator "You step back, pulling Kadyos with you."

        kilaw "I...I don't know. This isn't my world. Is it really my problem? I wasn't even supposed to be here."

        "A hush falls over the two, and to those who heard. Ba-O lowers her great shell slowly." 
        
        "Sili-sili wrings their translucent fins together."

        ba_o "That is your right, child. We won't force your tide."

        narrator "Another voice pop up,"

        sili "But...current-ly, you've no way home either. You're caught in the same deep water as us."

        narrator "You forgotten they were there."
        "You hesitate." 
        "The spirits drift back to their preparations, anxious, stumbling, clearly overwhelmed."

        "You watched as they move around in organize chaos."
        "The sun came and went, and you're surprised by all the things they can do with all this chaos"
        "You think you can get more done if you offered."
        menu:
            "Help them":
                jump route_help_them
            "Watch":
                jump route_watch

    #ROUTE: --------------------
    label route_help_them:
        narrator "You watched, but after the second day, something about the way Ba-O's hands shake as she carries numerous offerings and ingredients made your chest hurt."

        kilaw "...Okay. Okay, fine. But only because you all look like you're floundering out there. No offense."

        ba_o "None taken, child. Thank you."

        narrator "You rolled your sleeves. You'd help — at arm's length, just wanting to get it done."
        "Your feelings and your effort would be written into the work of your hands, whether you meant it or not."
        "Because of your hesitation, the Bakunawa will neither leave nor strike — it will watch, just as you watched."
        jump neutral_ending

    label route_watch:
        narrator "You cross your arms. You don't move. You watch as the committees argue, drop things, dissolve into a cascade of small disasters."

        kilaw "They'll figure it out. They said so themselves, they have done this for centuries, right? What does me being here change?"

        narrator "Kadyos whimpers and presses against your leg. You ignore the sound of something cracking in the Props room."
        "You ignore Ba-O sighing quietly over cold dishes. Three days of watching. Three days of nothing."

        toto "The festival will begin whether we are ready or not, child. The Bakunawa does not wait."

        narrator "You said nothing. Your actions showed it clearly. The scales begin appearing on your arms that night, and you don't notice until morning."
        
        narrator "You watched."
        "Three days of watching."
        "The committees argued, dropped things, dissolved into cascades of small disasters."
        
        "They did it without you."
        "They did it anyway, because that is what you do when you have no other choice."
        
        "The festival happened."
        "What it could do without you, it did."
        "What it needed you for, it couldn't."

        "The Bakunawa did not pause when it arrived."
        "It was simply there, and then the moon was not."
        "Darkness swallowed both realms." 
        "The transformation completed." 
        "No longer mortal, not fully spirit, either." 
        "Something in between, caught in the boundary you entered without asking permission, and never resolved"
        "Later, much later, you sit at the water's edge and watch where the moon used to be."
        "You can see it clearly from here." 
        "Every moment."
        "Every hand you could have offered." 
        "Every word you could have said."
        "You can see the whole shape of what it could have been."
        "Kadyos leans against you. He is all fin now and spirit-light, but he still leans against you exactly the same way. His tail moves, once." 
        "Slowly. You put your hand on his back."
        "You look up as you muttered to yourself very quietly."
        
        kilaw "I should have tried."

        "There's no use for regrets in the end."
        return #ENDING 2: BAD ENDING, YOU SHOULD'VE HELPED
    

    ## ═══════════════════════════════════════════════════
    ## BA-O — FOOD COMMITTEE
    ## ═══════════════════════════════════════════════════
    label route_kitchen:
        narrator "Ba-O leads you through a passage where the walls are woven from dried sea-grass and old fishing nets."
        "The kind of weave, you think, that looks almost like hablon from back home, if hablon were made of wood itself. It looks natural."

        ba_o "You cook, child?"
        kilaw "A little. My lola taught me."
        ba_o "Good. Then you understand that food is memory." 
        ba_o "Every dish I have forgotten is a piece of this realm lost. We cannot let the Bakunawa come to an empty table."

        narrator "The kitchen opens up enormous clay pots the size of fishing boats, fires lit with bioluminescent coral."
        "The smell of sea and something warm and familiar."
        "Your stomach growls."

        ba_o "I would offer you something, but I can't trust my own taste right now. That is the problem."

        kilaw "...What do you normally make? For the festival?"
        ba_o "Everything. Seafood layered in the olden way, each ingredient placed with intention, a prayer."
        ba_o "We call it the ceremonial dish. Every realm has one. Ours is from the deep."

        narrator "She slides a tray of ingredients toward you. It glows faintly."

        ba_o "You will build the ceremonial dish layer by layer. After that, dress it with colors and textures from our realm."

        ba_o "Do you understand what must be done?"

        menu:
            "Yes":
                jump route_understood
            "No":
                jump route_no 

    label route_understood:
        ba_o "Good. Begin when you're ready. My memories are waiting to be awakened."
        
        call minigame_food_start
        if score_food >= 3:
            jump bao_good
        elif score_food >= 2:
            jump bao_neutral
        else:
            jump bao_bad

    label route_no:
        ba_o "Ah, honesty. A rare seasoning these days. Let me explain once more, slowly"

        ba_o "You will build the ceremonial dish layer by layer. After that, dress it with colors and textures from our realm."

        ba_o "The ingredients are before you. Each one holds a piece of our realm's spirit."

        ba_o "Choose wisely, but also choose with feeling."
        
        menu:
            "Yes":
                jump route_understood
            "No":
                jump route_no_again

    label route_no_again:
        ba_o "Again, you will build the ceremonial dish layer by layer. After that, dress it with colors and textures from our realm."

        menu:
            "Yes":
                jump route_understood
            "No":
                jump route_no_again


    ## ── BA-O FEEDBACK ──────────────────────────────────

    label bao_good:
        ba_o "Wait, this is it! the taste, the texture, the feeling.....it's the recipe I'd forgotten! This is… absolutely wonderful, you're such a wonderful cook!"
        ba_o "Well, thanks to you, my memory's back, and I couldn't be happier!"
        ba_o "Anyway, the others definitely need your help."
        ba_o "And Sigay needed some help with their costumes, but with you pitching in, I'm pretty sure it will turn out beautifully."
        ba_o "I'm sure you'll be of good use to them."
        narrator "Ba-O waves you off with one fin, already back at the pot, muttering recipes under her breath like a prayer she's relearning."
        jump sigay_intro
    
    label bao_neutral:
        ba_o "Oh, that's delicious. It brings back a faint memory......just a little."
        ba_o "Well, atleast you've managed to shake my memory."
        ba_o "Anyway, I shouldn't keep you, the others surely need your help"
        narrator "Ba-O waves you off with one fin, already back at the pot, muttering recipes under her breath like a prayer she's relearning."
        jump sigay_intro
        
    label bao_bad:
        ba_o "Ergh."
        narrator "She holds her fin clenched to her lips, as she swallows slowly."
        ba_o "That's… well, an experience. Great. A memory I won't truly forget. Too bad it doesn't help at all."
        ba_o "Looks like helping me didn't go so well...but don't worry, your next task awaits. Sigay will need your help with her costumes."
        ba_o "I'm sure you'll be more of good use to them."
        narrator "Ba-O waves you off with one fin, already back at the pot, muttering recipes under her breath like a prayer she's relearning."
        jump sigay_intro


    ## ═══════════════════════════════════════════════════
    ## SIGAY — COSTUME COMMITTEE
    ## ═══════════════════════════════════════════════════
    label sigay_intro:
        narrator "You follow the sound of frustrated sighing, which leads you, eventually, to a studio that appears to have been recently hit by a typhoon." 
        "Bolts of luminescent fabric spill across the floor. Half-finished headdresses lean against walls like tired dancers." 
        "In the center of the chaos, a jellyfish the color of a sunset sits surrounded by crumpled designs."
        kilaw "Right. Costumes next. I can do costumes."
        sigay " I thought I had it all under control... but why does it still feel like I'm missing something?"
        kilaw "Need a hand with those costumes? I can help figure it out."
        sigay "Oh... thank you I really need some assistance"
        narrator "Sigay holds up a half-made headdress — layers of sea glass and woven thread, technically accomplished, completely lifeless."
        sigay "Every year, the costumes are the highlight of the festival. Every year, I know exactly what to do. But this year... it's like the current dried up inside me. Nothing flows."
        kilaw "What did last year's look like?"
        sigay "Magnificent. Sea greens and deep blues. Woven like—oh, what do you mortals call it —that fabric from your islands? The one that takes three moons to make?"
        kilaw "Hablon?"
        sigay "Yes! Like hablon, but of bioluminescent thread. The dancers glowed as they moved. It was... it was alive."
        kilaw "So what changed?"
        narrator "Sigay's tentacles droop."
        sigay "The Bakunawa has been circling for many cycles now. The realm is... frightened. When you design from fear, everything looks like armor. Nothing looks like celebration."
        kilaw " Then let's design from something else. What does the celebration actually feel like?" 
        kilaw "Not what it's supposed to look like, what does it feel like?"
        narrator "Sigay is quiet. Then, slowly:"
        sigay "Like when the bioluminescent sea ignites all at once. Like everyone gasping the same breath at the same time."
        sigay "The feeling of hopefulness? Being alive?"
        narrator "You're not sure if you got it. But you think you do."
        kilaw "Okay. Start there."
        narrator "Sigay sighed, frustrated and tired."
        sigay "It's not that simple."
        kilaw "It's alright. I'll help you as much as I can"

        call minigame_costume_start
        if score_costume >= 3:
            jump sigay_good
        elif score_costume >= 2:
            jump sigay_neutral
        else:
            jump sigay_bad

        narrator "They work. Sigay's tentacles move slowly at first, then with growing sureness, pulling colors you didn't know existed, weaving patterns that seem to breathe." 
        "You suggest shapes from your own festivals you grew up watching; the bold angles of your warriors, the way their costumes were built to be seen from a distance and still hold detail up close."
        sigay "Your festival, it has vibrant color. The color feels like it's breathing. I like that."
        kilaw "My lola said our festival was never about the dancing. It was about the feeling you got watching it."
        sigay "Yes. Yes, exactly that."

    ## ── SIGAY FEEDBACK ─────────────────────────────────

    label sigay_good:
        narrator "Sigay holds up the finished costume. It catches the bioluminescent light and fractures it into a thousand small suns."
        narrator "The both of you did your best."
        sigay "Oh...oh, this is out of my usual fin entirely. In the best way. I haven't made something like this in three centuries."
        sigay "You brought something back, Kilaw. Something I didn't know I'd lost."
        jump bilo_sili_intro

    label sigay_neutral:
        narrator "The costume is good. Technically accomplished. Better than what was there before."
        narrator "The both of you did your best."
        sigay "It's...yes. It will do. The dancers can work with this."
        sigay "Thank you. You gave my fins somewhere to start again. That is not nothing."
        jump bilo_sili_intro

    label sigay_bad:
        narrator "The both of you did your best."
        narrator "The costume exists. That's the most generous thing you can say about it."
        sigay "Well. It covers the body and holds together, so...we're at least above bare-finned."
        sigay "Go help the others, child. You tried. The current doesn't always flow where we want it to."
        jump bilo_sili_intro


    ## ═══════════════════════════════════════════════════
    ## BILO + SILI — PERFORMANCE COMMITTEE
    ## ═══════════════════════════════════════════════════
    label bilo_sili_intro:
        narrator "You said your goodbyes and went to the next spirit in need, the performance committee." 
        "It was held by two spirits, Bilong-Bilo and Sili-Sili. You heard them before you saw them, two voices, one sharp and declarative, one fluid and insistent, talking over each other in perfect disharmony."
        "When you got where they were, the two dancers were locked in a bitter disagreement over choreography. One favors traditional movements, the other demands something more fresh and modern in expression."
        bilo "The steps have not changed in many cycles for a REASON, Sili-Sili! The Bakunawa recognizes the old forms. It is what makes its memory!"
        sili "And that's exactly the problem! It's been how many long—the Bakunawa has seen the same performance many times since the past centuries!" 
        sili "We need something that catches it off guard, something it hasn't seen before!"
        bilo "You want to improvise at the most important ceremony of the century?!"
        sili "I want to perform something worth watching!"
        narrator "They stop when they saw you."
        bilo "Ah. The mortal girl. Are you here to talk some sense into this current-brained flounder?"
        sili "They meant me, I'm the flounder."
        kilaw "I could hear you from Sigay's studio, just so you know."
        bilo "Good. Someone needed to hear this. Since Sili-Sili won't."
        sili "I hear fine. I simply choose not to drown in your nonsense."
        kilaw "Okay. Show me. Both of you. Show me what you mean, not tell me. Show me."

        narrator "Bilong-Bilo demonstrates the traditional form first, slow, deliberate, weighted with centuries of intention."
        "Each movement connects to the next like the current connecting islands. You feel something ancient in it."
        "Then Sili-Sili performs, quick, surprising, every movement a question that the next movement answers. It's alive in a different way." 
        "A New-river-finding-old-riverbed energy."
        kilaw " ...You're both right."
        narrator "..."
        bilo "Excuse me?"
        kilaw "You're both right and you're both not looking at the other's work properly."
        kilaw "Bilong-Bilong, the old forms have weight. Real weight. You can feel it." 
        kilaw "But Sili-Sili, the surprise, the life in it, that's what makes a crowd gasp." 
        kilaw "I think the foundations should never changes, the rhythm, the footwork, but every year the expression is new. Same roots. Different flower"
        bilo "Same roots..."
        sili "...Different flower."
        narrator "They look at each other. Something shifts."

        call minigame_dance_start
        if score_dance >= 3:
            jump BS_good
        elif score_dance >= 2:
            jump BS_neutral
        else:
            jump BS_bad

    ## ── BILO/SILI FEEDBACK ─────────────────────────────

    label BS_good:
        narrator "You mediate between the two, helping each see value in the other's approach." 
        "Blending their styles into something seamless and unified, where both honor the past and the present."
        bilo "I...did not think that was possible."
        sili "Neither did I. But here we are, swimming in the same direction for once."
        bilo "Don't push your fin, Sili-Sili."
        narrator "Sili-Sili can't help but smile widely, their fins curl as they barely suppressing delight"
        jump lusay_intro

    label BS_neutral:
        narrator "A compromise is reached, not a true blend, but a structure where the traditional verses anchor Sili-Sili's more inventive choruses."
        bilo "It is...workable."
        sili "It's a high praise coming from them, honestly."
        jump lusay_intro

    label BS_bad:
        narrator "The argument continues. You had to pick one side to support, and the other carries the wound into the performance."
        bilo "You've made your choice, mortal. I hope it is the right one."
        sili "Or wrong one. We'll see at the festival."
        jump lusay_intro


    ## ═══════════════════════════════════════════════════
    ## LUSAY — PROPS COMMITTEE
    ## ═══════════════════════════════════════════════════
    label lusay_intro:
        narrator "You focused your attention on Lusay. A young oyster brimming with brilliant ideas for props and effects."
        "But you had to find her first. The other spirits already told you about her and her general direction."
        "The Props workshop sounded like a small disaster from outside: things rolling, falling, someone groaning quietly"

        narrator "A young oyster brimming with brilliant ideas for props and effects. However lacking the confidence to execute them. Or so they said."
        "Their workshop is absolute chaos. Dozens of started projects, but nothing finished."
        "You step over three unfinished lanterns, a net of sea glass that has been tangled rather than woven, and what appears to be an entire installation of hanging coral that has fallen sideways."
        lusay "Oh! You're... you're the mortal girl. Kilaw, right? I heard about you."
        kilaw "Good things, I hope."
        kilaw "You're Lusay right?"
        narrator "Lusay smiled brightly as she moved away from her unfinished projects."
        lusay "That's me! No worries, they all say great things! Wonderful things!"
        lusay "Unlike me..."
        narrator "She gestures helplessly at the chaos."
        lusay " Every idea I have is the best idea I've ever had until I actually start it. And then it becomes the worst thing I've ever made." 
        "I don't know how to finish anything. I have twelve great beginnings and zero endings."
        kilaw "What was the one you were most excited about?"
        lusay "...The lights. Lanterns made from dried jellyfish membrane—they catch the bioluminescence from the sea and hold it." 
        lusay "When you string hundreds of them across the festival grounds they look like the night sky fell sideways. But I—"
        lusay "I've started fourteen of them. None are finished even."
        narrator "..."
        kilaw "Then we finish one. Just one. Then another. That's all."
        lusay "But what if it comes out wrong?"
        kilaw "Then it's a wrong lantern that exists, which is more useful than a perfect one that doesn't."
        narrator "Lusay considers this with the earnest seriousness of someone who has never thought about it that way before."
        kilaw "I once made something for my lola's birthday using vinegar that was a little too sharp and fish that was a little too fresh."
        kilaw "She said it was the most alive dish she'd ever eaten."
        kilaw "It's a mess of flavors and it works."
        narrator "You look wistfully distracted, not noticing the fond look that Lusay is giving you."
        lusay "A mess that works. I like that."

        call minigame_props_start
        if score_props >= 3:
            jump lusay_good
        elif score_props >= 2:
            jump lusay_neutral
        else:
            jump lusay_bad

    ## ── LUSAY FEEDBACK ─────────────────────────────────

    label lusay_good:
        narrator "Together they completed something spectacular, moving with coordination and at ease. The decoration was finished, and so is the morning."
        lusay "It's—oh. Oh, it actually works. It's actually beautiful."
        kilaw "See? Wrong lanterns and all."
        lusay "The mess works! The mess absolutely works!"
        narrator "Lusay laughs, they shined brightly, wide with relief and joy. You both shared a relieved look as the lanterns begin to glow."
        jump transformation

    label lusay_neutral:
        narrator "Not everything they built works. Some lanterns glow. Some don't."
        lusay "It's...not everything I imagined. But it's something."
        kilaw "Something is always enough to start with."
        jump transformation

    label lusay_bad:
        narrator "The workshop remains largely in chaos. A few pieces are done, not enough."
        "You both sat on the floor surrounded by unfinished ideas. Tired."
        lusay "I'm sorry. I know I wasted your time. My ideas are always better in my head."
        narrator "You bumped your shoulders together, getting her out of her own head."
        kilaw "They're not wasted. You know what doesn't work now. That's worth something."
        jump transformation


    ## ═══════════════════════════════════════════════════
    ## TRANSFORMATION AND MUTATION
    ## ═══════════════════════════════════════════════════
    label transformation:
        narrator "You decided to sleep there until sunrise. You curled up in their provided room, courtesy of Ba-O." 

        "Kadyos warm against your back, and closed your eyes to the soft pulse of the bioluminescent sea." 
        "You dreamed of the mangrove. You dreamed of being underwater and finding everything easy."

        "You noticed something different behind your back, everything felt...more sensitive."
        "You opened your eyes to something different." 

        "You sit up, rolling your shoulders."
        "Somethings wrong."

        kilaw "Did I sleep in a weird position?"
        
        narrator "Then you saw it."
        "It was alarming: small, iridescent scales had appeared on your arms."
        "Something twitched on the side of your head."
        "There was a tail. Your ears were completely different as well."
        "Your legs were forming scales creeping higher. Your ears fluttered like fins with every step."
        
        kilaw "Okay... okay, focus. Everything's fine."
        kilaw "I'm just turning into one giant fish but... I still have to help the other spirit members. I can't stop now. Not yet."

        narrator "It feels like everything is closing in. You feel trapped."

        menu:
            "Kadyos":
                jump kadyos
            "Scales":
                jump scales

    label kadyos:
        narrator "Now fighting panic about your own transformation, your breathe trying to push through your own fears."
        "You muttered quietly to yourself as you take a deep breathe."

        kilaw "Okay. Okay, breathe. Scales—yes. Tail—yes, still there. Ears—fin-shaped, gross."
        kilaw "Am I still...me?"

        narrator "Kadyos licks your scaled hand. His tail is fully finned now too. He looks up at you with the same stupid adoring expression he always has."
        "Exhaling shakily, you reached out as you touch Kadyos face."

        kilaw "...Yeah. Still us."

        narrator "You stand up. Your legs are strange under you but they hold." 
        "With shaking hands you ventured out to help any remaining spirit."
        "The festival is tomorrow. You have one day left. You can do this."

        kilaw "One day. We can do one day, Kadyos. Then we go home. Whatever home looks like after this."
        narrator "Kadyos barks, one short, firm ARF. An agreement."
        jump kasag_intro

    label scales:
        narrator "The scales catch the light beautifully. You're not thinking about that."
        "You are thinking how wrong this is. This all is wrong"
        "The words going round and round without your permission, and the room going small around you." 
        "You hear Kadyos whimpering somewhere that feels very far away even though he is right there, pressed against your leg, and you cannot reach down to touch him because you can't move."

        kilaw "No—no no no—I can't—this isn't—please"

        narrator "You felt like choking, but you're breathing more easily than before."
        "You back against the wall. Kadyos whimpers. You slide to the floor."
        "You know, distantly, that the festival is tomorrow." 
        "You know that Ba-O's hands shake because of her tender age and the music committee is one argument away from collapsing.."
        "Everything isn't ready."
        "You know all of this. You can't get up off the floor."
        "It isn't weakness, exactly."
        "It's more like the moment when everything arrives at once—all the water you've been treading since you fell into the vortex, your body simply decides that this is as far as it goes."
        "The scales are spreading past your wrists now."
        "Your ears catch sound differently." 
        "You are changing into something and you have no way of knowing, and you are still so young, but so far away from home, and you have hit the floor pass what you can carry."
        "Kadyos licks your scaled hand. You don't respond."
        "The sun had passed. Then the moon. Then the festival."
        "Outside, the festival stumbles forward without you, and what it can is not enough, and they know it."
        "And they do it anyway because that is what you do when you have no other choice." 
        "A lot of things are missing. Not complete. Not enough."
        "The Bakunawa arrives before the last lantern is lit."
        "You don't see any of it. You are still on the floor when the darkness comes."
        "Later—much later—you sit at the water's edge and watch where the moon used to be."
        "You are not crying anymore."
        "You are just sitting, the way people sit when they have gone past the part where crying helps."
        "You look below, not bothering to look at the underwater sky, you can't bring yourself to look at something that isn't there anymore."
        kilaw "I should have gotten up. I should have tried."

        narrator "You know, now, what you could have done. You can see it clearly from here—every moment, every hand you could have offered, every word you could have said. You can see the whole shape of it."
        "Kadyos leans against you. He is all fin now, and still— somehow—entirely him."
        "His tail moves, once. Slowly. You put your hand on his back."
        "Somewhere far away, you thought, you don't think can ever find a way back home, you can't even recognize yourself anymore."
        
        return #BAD ENDING: Your fear was real. So was everything it cost you. 

    
    ## ═══════════════════════════════════════════════════
    ## KASAG — MUSIC COMMITTEE
    ## ═══════════════════════════════════════════════════
    label kasag_intro:
        narrator "Outside you heard a booming voice, proud and loud, filling the whole corridor of the festival grounds like a wave filling a cave."
        "Kadyos's fin-tail stiffened. Even he seemed uncertain about approaching."
        kilaw "That's... the music committee?"
        narrator "A passing spirit nodded, eyes wide."
        unknown "Kasag. Old crab."
        unknown "Been conducting the music for three hundred years, but this cycle—the younger musicians have been pushing back."
        unknown "Makes his claws very... clicky."
        narrator "You took a breath. Scales itched along your collarbone. You walked toward the sound."
        kilaw "Kasag? I'm here to help with the music—"
        kasag "Help? HAH! Who said I needed help? You?"
        narrator "He berated a nearby spirit for even holding their instrument in a wrong way."
        "He said a lot of unwarranted things towards them, before they turn to you."
        kasag "I've been conducting this festival's music for many cycles before you, mortal, was even born."
        kasag "What I need is MY direction followed properly!"
        kasag "My music kept the Bakunawa away from eating the last moon we have! It would've been eaten if I didn't take charge."
        kilaw "Hmn..."

        narrator "He's very..."
        narrator "Insistent."

        menu:
            "You're being too controlling.":
                jump argue_controlling
            "Screw this.":
                jump screw_this
            "What if you combine both?":
                jump combination

        #ROUTE ---------------------------
        label argue_controlling:
            kilaw "A strong leader lifts others up. You're just pushing them down."
            kasag "You don't know anything. I'm ensuring quality!"
            kilaw "You're ensuring obedience. There's a difference."
            narrator "The other nearby spirits were muttering between themselves, busying themselves with idle task."
            "Kasag took a deep breathe."
            kasag "Mistakes are not allowed, child. Too many risk."
            kasag "Why fix something that doesn't need to be fix?"
            kilaw "The question is whether the same sound, performed without feeling, carries the same power it once did."
            kilaw "There's no passion on what you do. Just routine."
            narrator "..."
            kasag "Perhaps... perhaps my shell has grown too thick."
            kasag "Fine. Child, show me your ideas. But make them GOOD."
            call minigame_music_start
            if score_music >= 3:
                jump kasag_good
            elif score_music >= 2:
                jump kasag_neutral
            else:
                jump kasag_bad

        label screw_this:
            kilaw "You know what? I don't have time for this. Figure it out yourself."
            kasag "What? You dare walk away from—"
            kilaw "You don't want help. You just want an audience."
            narrator "Numerous spirits tried to persuade you to stay."
            unknown "Please! Wait!"

            narrator "The music committee fractures."
            "The ensemble plays discordantly, some following Kasag's rigid tempo, others rebelling with their own."
            "The result is something that doesn't sound pleasant to your human ear."
            "You looks at your hands and saw the scales spreading, fast."
            jump before_festival

        label combination:
            kilaw "What if you combine both?"
            kasag "Impossible. Music needs ONE conductor—"
            kilaw "From where I'm from, music has layers."
            kilaw "Your powerful foundation with their fresh melodies. Like waves and currents—both part of the same ocean."
            unknown "We could play traditional beats in the chorus, our style in the verses?"
            kasag "That... might work. IF done with precision."
            kilaw "Then try it. Together."
            call minigame_music_start

            if score_music >= 3:
                jump kasag_good
            elif score_music >= 2:
                jump kasag_neutral
            else:
                jump kasag_bad

    ## ── KASAG FEEDBACK ──────────────────────────────────

        label kasag_good:
            narrator "The musicians begin to play—Kasag's strength meeting the young spirits' innovation. Kasag's voice soften in awe. The musicians seems happy with themselves."
            kasag "This... this sounds like—something forgotten."
            narrator "The music becomes something new yet familiar—tradition evolving like the tides."
            "On festival night, the melody moves spirits to tears, reminding them why they celebrate."
            jump before_festival

        label kasag_neutral:
            narrator "The music improves, but tension remains. Kasag allows input but still dominates."
            "The result is technically proficient but lacks true harmony, a performance that satisfies tradition without inspiring joy."
            jump before_festival

        label kasag_bad:
            narrator "The music was nothing but a mix and match of chaos and disorder."
            "It was a disaster. It left you nothing but dissapointment."
            "Kasag maintains an even look, but you can't help but feel his disapointment."
            "He reached out towards you, ruffling your hair."
            kasag "I thank you, child. For your effort."
            kasag "But next time, do not meddle with things you don't understand."
            jump before_festival


    ## ═══════════════════════════════════════════════════
    ## BEFORE FESTIVAL
    ## ═══════════════════════════════════════════════════
    label before_festival:
        narrator "As the final sunset before the festival descends, You take stock of your work. You did your best."
        "You can only hope that would be enough."
        "You find Kadyos near the festival grounds entrance, sitting perfectly still, watching the lights come on one by one."
        kilaw "It's really happening, isn't it."

        narrator "It wasn't really a question. Kadyos leans against your transformed legs."
        kilaw "Whatever the Bakunawa decides, we did something real here. All of us. Even the parts that went wrong."

        narrator "The bioluminescent sea ignites below and up the festival grounds, the same glow you followed from the boat, what felt like a lifetime ago."
        "The same light that started everything."
        "You looks at your hands and saw the scales spreading, fast"
        kilaw "How much more do we have before..."
        narrator "You don't finish the thought. Kadyos whimpers, his tail now fully finned."
        "The final sunset paints the spirit realm in golden light."
        "You kneel beside Kadyos on the festival grounds, exhausted but reflective."
        kilaw "We did it, Kadyos. Well... most of it, anyway."
        narrator "Kadyos whimpers, nuzzling against you."
        kilaw "I know, boy. I'm scared too. Look at us... we're barely recognizable."
        kilaw "But maybe... maybe this meant something. Three moons ago, they were falling apart. Now they're—"

        narrator "You closes your eyes, holding Kadyos tighter as the sunset fades to twilight."
        "Three moons of work now shine before you."
        "You watched as the celebration you helped create comes to life, your transformed body aching with every breath."
        "Spirits dance in new costumes, feast on rediscovered flavors, move to harmonized music."
        "The preparations are complete. Now, they wait."
        "You wait along them."
        "Scales have spread to your neck. Kadyos is more fish than dog." 
        "Will the Bakunawa accept your offering? Will you ever see home again?"
        jump pre_ending


    ## ═══════════════════════════════════════════════════
    ## CALCULATE SCORE AND ENDINGS
    ## ═══════════════════════════════════════════════════
    label pre_ending:
        narrator "The water beneath the festival grounds begins to tremble — not the frantic churning of the vortex that brought you here, but something deeper. Deliberate. Aware."
        sigay "It's coming. The Bakunawa comes."
        narrator "Bao looks on quietly. She stayed close, her presence felt. Warmth against the cold waters. She does not reach for you."
        ba_o "Stay where you are, child. Let the festival speak for itself now."
        narrator "You stand still. Kadyos presses against you. The music plays."
        jump calculate_final_score


    ## ═══════════════════════════════════════════════════
    ## ENDINGS
    ## ═══════════════════════════════════════════════════

    #GOOD OUTCOME
    label good_ending:
        narrator "The Bakunawa sees the sincerity woven into every detail. Satisfied, it circles the moon as guardian, then descends peacefully into the depths."
        "Light surrounds you. The scales fade. The gills close." 
        "A portal shimmers open before you, warm, golden-edged, and on the other side you can smell salt and woodsmoke and the particular smell of a village morning."
        "Home"
        "You were about to step forward before someone calls you."
        ba_o "Child, Before you go walk the shore first. Let the tide run over your feet. Let it take what followed you. Then you may go home."
        narrator "You nod. You understand. "
        ba_o "Accident or not, thank you for being here. Safe travels"
        narrator "You look at Ba-O for a moment and let it sink to you that this will probably be the last time you'll see this."
        "Both of you are left standing there as the festival continues around you. The music, the dancing, the food felt very real at the moment."
        kilaw "Thank you too."
    
        narrator "With that you stepped onto the portal home."
        "Dawn breaks over the mangrove. You and Kadyos emerge through the portal, onto the shore, into the early morning light."
        "Fully restored. The scales are gone."
        "Kadyos shakes the last of the spirit water from his fur, normal fur, entirely, wonderfully, gloriously dog."
        "He looks at you like he's been waiting for this moment this whole time and is very pleased with how it turned out"
        "You walk the shoreline. You let the tide come over your feet. Cold, real, present."
        "You paddle home after that. The boat still where you left it."
        "The mangrove looks exactly the same as it always did, roots, water, morning light filtering down in long gold threads."
        "Nothing about it announces what is underneath. Nothing tells you that you were there."
        "You muttered softly, barely above the sound of the paddle."

        kilaw "Kadyos. We made it."
        narrator "Kadyos shakes his fur one more time. He is very happy about this."
        "Just then, a mudfish that started it all jumps into the boat." 
        "A meal. Or a thank-you. Or just a reminder that being lost led to finding what you never thought you needed."

        narrator "You look at the water. You're not sure if anyone can hear you. You said it anyway."
        kilaw "Thank you..."
        return

    #NEUTRAL OUTCOME
    label neutral_ending:
        narrator "The Bakunawa rises, vast and patient, the way old things are patient."
        "It doesn't rush. It has seen three hundred festivals. It is taking the measure of this one."
        "The music falters for just a moment. Then holds."
        "The Bakunawa is massive, ancient, neither angry nor pleased. It circles the moon, considering. The festival bought time, but nothing more."
        ba_o "Child, quickly, you can return home, partially transformed, or stay and help us find a new way."
        narrator "You stand between two worlds, unsure which path to choose."
        menu:
            "Stay.":
                jump stay_here

            "Leave":
                jump leave_here

        label stay_here:
            narrator "You look at Kadyos. He looks at you." 
            "You think of your mother's house. You think of the drums you heard from the village, the festival that happened without you." 
            "You think of Ba-O's kitchen, and Sigay's light-fractured costumes, and Lusay's wrong lanterns that worked."
            kilaw "...I'll stay. For now."
            narrator "Ba-O looks at you. Something in her expression is careful"
            ba_o "Then you are one of us. For as long as the tide asks it."
            narrator "You nod. The scales don't fully recede."
            "You find, with some surprise, that you mind less than you expected. They catch the bioluminescent light beautifully."

            "Kadyos leans against you. His tail moves, once." 
            "He is content here, because you are here. That is all he has ever required." 
            "Quietly, you think to yourself"
            kilaw "I'll write something in the water. Mom will find it eventually."
            return

        label leave_here:
            narrator "You look at the portal. You think of the mangrove at dawn. You think of your village. Your mom."
            "You think of all the lanterns your neighbors hung for the festival you missed, the drums you heard from the water three moons ago."
            "The way you always forget how much you love home until you're standing at the edge of losing it."
            kilaw "I need to go home."
            ba_o "We understand, child. We'll be here. We always are."
            narrator "When you went back to the surface, the aquatic features don't entirely recede."
            "Faint scales along your wrist, ears that catch the sound of running water differently now, a sensitivity to tides you didn't have before." 
            "You don't mind. They're a reminder. Proof that something happened, that it was real, that you were there and came back."
            return 

    #BAD OUTCOME
    label bad_ending:
        narrator "The Bakunawa does not pause when it arrives. It does not circle. It does not consider. It is simply here, and then the moon is not."

        "The silence that follows is not the silence of things that are quiet. It is the silence of something that was there and is gone now and will not come back."
        
        "The Bakunawa arrived in fury. The festival's failure is an insult to centuries of negotiation. No pleading can stop what comes next."
        "The moon disappears into the serpent's jaws. Darkness swallows both realms. You watch, helpless, as everything is consumed."
        "The transformation completes. No longer mortal. No longer entirely spirit. Something the boundary has decided to keep, because it was not returned in time."
        "In the mortal world, your village lights lanterns every night. Mourning. Warning." 
        "The water no longer glows. Your name becomes a cautionary tale; the girl who came and went, and was never to be seen again"
        
        "The men on the night watch face the treeline at dusk. They stand there longer now. Not in tribute. In grief."
        "You sit at the water's edge of the spirit realm, your realm now, and watch where the moon used to be."
        "Kadyos sits beside you. He is all fin and gills, but he still leans against you the same way."
        "You hold onto Kadyos, as you muttered to yourself."

        kilaw "I should have helped more. I should have tried harder."
        narrator "Somewhere in the mortal world, your village lights another lantern."
        return

    return
