# The script of the game goes in this file.

define kilaw = Character("Kilaw", window_style="character_window", who_style="namebox_kilaw_label", callback=typewriter_sfx, cb_who="Kilaw")
define kadyos = Character("Kadyos", window_style="character_window", who_style="namebox_kadyos_label", callback=typewriter_sfx, cb_who="Kadyos")
define ba_o = Character("[bao_name]", window_style="character_window", who_style="namebox_ba_o_label", callback=typewriter_sfx, cb_who="Ba-O")
define toto = Character("[toto_name]", window_style="character_window", who_style="namebox_toto_label", callback=typewriter_sfx, cb_who="Toto")
define lusay = Character("Lusay", window_style="character_window", who_style="namebox_lusay_label", callback=typewriter_sfx, cb_who="Lusay")
define sili = Character("Sili-Sili", window_style="character_window", who_style="namebox_sili_label", callback=typewriter_sfx, cb_who="Sili-Sili")
define bilo = Character("Bilong-Bilong", window_style="character_window", who_style="namebox_bilo_label", callback=typewriter_sfx, cb_who="Bilong-Bilong")
define kasag = Character("Kasag", window_style="character_window", who_style="namebox_kasag_label", callback=typewriter_sfx, cb_who="Kasag")
define sigay = Character("Sigay", window_style="character_window", who_style="namebox_sigay_label", callback=typewriter_sfx, cb_who="Sigay")
define dawa = Character("Dawa", window_style="character_window", who_style="namebox_dawa_label", callback=typewriter_sfx, cb_who="Dawa")
define unknown = Character("???", window_style="character_window", who_style="namebox_unknown_label", 
callback=typewriter_sfx, cb_who="???")
default bao_name = "???"
default toto_name = "???"

## No name is narrator
define narrator = Character(None, callback=typewriter_sfx, cb_who="")

## Choices tracking
default seen_what_is_this = False
default seen_who_are_you  = False

## Timer 
screen choice_timer(time, label_to_jump):
    timer time action Jump(label_to_jump)
    
    # Visual countdown bar
    bar value AnimatedValue(0, time, time, time) xalign 0.5 ypos 0.1 xsize 500

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

# Human Form
transform left_char:
    xalign 0.2
    yalign 1.0

image kilaw normal    = "kilaw_normal_sprite.png"
image kilaw happy     = "kilaw_happy_sprite.png"
image kilaw focused   = "kilaw_focused_sprite.png"
image kilaw worried   = "kilaw_worried_sprite.png"
image kilaw shocked   = "kilaw_shock_sprite.png"
image kilaw sad       = "kilaw_sad_sprite.png"
image kilaw determined = "kilaw_determined_sprite.png"

# Spirit/Fish Form
image kilawfish normal = "kilawfish_normal_sprite.png"
image kilawfish happy  = "kilawfish_happy_sprite.png"
image kilawfish sad    = "kilawfish_sad_sprite.png"
image kilawfish shocked = "kilawfish_shock_sprite.png"

# Normal Dog Form
image kadyos normal = "kadyos_normal_sprite.png"
image kadyos happy  = "kadyos_happy_sprite.png"
image kadyos sad    = "kadyos_sad_sprite.png"

# Dawa
image dawa serious = "dawa_serious_sprite.png"
image dawa happy   = "dawa_happy_sprite.png"
image dawa wry     = "dawa_wry_sprite.png"
image dawa crab    = "dawa_crab_sprite.png"

image spirit_npc = "spiritnpc_sprite.png"
image rocky      = "rocky_sprite.png"
image fish_npc   = "fish_sprite.png"
image jellyfish  = "jellyfish_sprite.png"

# Spirit/Fish Form
image kadyosfish normal = "kadyosfish_normal_sprite.png"
image kadyosfish happy  = "kadyosfish_happy_sprite.png"
image kadyosfish sad    = "kadyosfish_sad_sprite.png"

# Toto
image toto normal = "toto_normal_sprite.png"
image toto happy  = "toto_happy_sprite.png"
image toto calm   = "toto_calm_sprite.png"

# BS
image sili happy   = "sili_happy_sprite.png"
image sili worried = "sili_worried_sprite.png"
image sili mad     = "sili_mad_sprite.png"
image sili relief  = "sili_relief_sprite.png"

image bilo formal    = "bilo_formal_sprite.png"
image bilo serious   = "bilo_serious_sprite.png"
image bilo irritated = "bilo_irritated_sprite.png"
image bilo surprise  = "bilo_surprise_sprite.png"

## Background
image background moving = Movie(play= "images/Comp1.webm", loop=False, keep_last_frame=True)
image intro village = Movie(play= "images/intro village.webm", Loop=False, keep_last_frame=True)
image intro village2 = Movie(play= "images/intro village2.webm")
image intro caught fish = Movie(play= "images/intro caught fish.webm")
image intro dawa = Movie(play= "images/intro dawa.webm", loop=False, keep_last_frame=True)
image intro dawa noticed = Movie(play= "images/intro dawa noticed.webm")
image intro moon = Movie(play= "images/intro moon.webm")
image intro moon2 = Movie(play= "images/intro moon2.webm", loop=False, keep_last_frame=True)
image intro night = Movie(play= "images/intro night.webm", loop=False, keep_last_frame=True)
image intro sun = Movie(play= "images/intro sun.webm", loop=False, keep_last_frame=True)
image intro frog = Movie(play= "images/intro frog.webm")
image intro dawa mc = Movie(play= "images/intro dawa mc.webm", loop=False, keep_last_frame=True)
image intro bakawan = Movie(play= "images/intro bakawan.webm", loop=False, keep_last_frame=True)
image intro bye1 = Movie(play= "images/intro bye1.webm")
image sunset = Movie(play= "images/sunset.webm", loop=False, keep_last_frame=True)
image intro children = Movie(play= "images/intro children.webm", loop=False, keep_last_frame=True)
image intro festival prep1 = Movie(play= "images/intro festival prep1.webm", loop=False, keep_last_frame=True)
image intro feet running = Movie(play= "images/intro feet running.webm", loop=False, keep_last_frame=True)

## Audios
## Atmosphere & Environment
define audio.morning_birds = "audio/morning birds intro sound.ogg"
define audio.flowing_water = "audio/flowing water sound.ogg"
define audio.water_drop    = "audio/water drop sound.ogg"
define audio.fell_underwater = "audio/fell underwater sound.ogg"
define audio.wood_running = "audio/wood running sound.ogg"
define audio.night_village = "audio/night village.ogg"


## Character & Narrative SFX
define audio.dawa_humming  = "audio/dawa humming sound.ogg"
define audio.children_laughing = "audio/children laughing sound.ogg"
define audio.woman_laughter = "audio/woman laughter sound.ogg"
define audio.kadyos_bark    = "audio/kadyos bark sound.ogg"
define audio.kadyos_whimper = "audio/kadyos whimpering sound.ogg"
define audio.kadyos_silent_whimper = "audio/kadyos silent whimper sound.ogg"
define audio.festival_drums = "audio/festival drums sound.ogg"

## Music Tracks
define audio.music_beginning = "audio/music beginning.ogg"
define audio.music_gate      = "audio/music gate spirit realm.ogg"
define audio.music_spirit_realm = "audio/music spirit realm.ogg"

## ──────────────────────────────────────────────────────────────


label start:
    stop music fadeout 4.0

    #$ renpy.music.set_volume(2.9, channel="typewriter")

    #ACT 01 ---------- EXPOSITION

    #PROLOGUE -- PANHUY-AN

    scene intro sun with Fade(0.5, 0.3, 0.9)
    play music music_beginning volume 0.1
    play audio morning_birds volume 0.1
    
    voice "narration/intro1.wav"

    narrator "There is a place where the sea does not end and the land does not begin."

    voice "narration/intro2.wav"
    
    scene intro village with Dissolve(2.0)
    "At the far edge of the island, where the land loosens its grip and gives way to the tide, lies a quiet village called Panhuy-an."

    voice "narration/intro3.wav"

    narrator "The houses stand on stilts above shallow breathing water. Wooden floors creak with every step."

    voice "narration/intro4.wav"
    
    #scene intro morning village with Dissolve(2.0)
    "Banca boats rest loosely tied to posts, hollowed from trees older than the people who carved them."

    voice "narration/intro5.wav"
    
    #scene intro fisher #parang same lng siya with int vuillage2
    "The sea feeds the village." 
    
    show intro village2 with Dissolve(2.0)
    #splash sound from fish

    voice "narration/intro6.wav"

    "The village, in turn, learns never to take more than it is given."
    voice "narration/intro7.wav"
    
    #scene intro village3
    "In the mornings, the elders watch the horizon."

    voice "narration/intro8.wav"
    
    "Morning smells of salt and smoke. Children run between the stilts"
    
    voice "narration/intro9.wav"
    scene intro caught fish with Dissolve(2.0)
    play sound woman_laughter volume 0.2

    "Neighbors call to each other across the water."
    
    scene intro children with Dissolve(2.0)
    voice "narration/intro10.wav"

    play audio children_laughing volume 0.4
    play sound wood_running volume 0.1

    "The old lecturing the young."

    voice "narration/intro11.wav"

    "The whole village moves with the easy rhythm of a place that knows itself."

    voice "narration/intro12.wav"

    scene intro night with Dissolve(2.0)
    play audio night_village volume 1.0 fadein 2.7

    "The evening carries distant laughter, the sound of wind and waves folding into each other."

    voice "narration/intro13.wav"

    "The people here speak of tides, and moon, and seasons when the fish are plentiful."

    voice "narration/intro14.wav"
   
    "...and seasons when even the nets come back empty."

    voice "narration/intro15.wav"

    "Beyond the village, the sea stretches wide and honest."
    #zoom intro night

    voice "narration/intro16.wav"

    "But behind it," 
    scene intro moon with Dissolve(2.0)

    voice "narration/intro17.wav"
    
    "behind the stilts and the smoke and the festival drums already beginning their preparations," 
    scene intro moon2 with Fade(0.5, 0.3, 0.9)

    voice "narration/intro18.wav"
    
    "stands the bakawan."
    scene intro frog with Dissolve(2.0)
    #Add frog sounds 

    voice "narration/intro19.wav"
    "Not planted." 
    #scene intro frog2 with Dissolve(1.0

    voice "narration/intro20.wav"
    
    "Older than any name the villagers could give it." 
    #scene intro frog3 with Dissolve(1.0)

    voice "narration/intro21.wav"
    
    "The roots twist deep into the earth and the deeper it still into stories passed down by those who came before." 
    #scene intro frog jump with Dissolve(1.0)
    
    voice "narration/intro22.wav"
    
    "The locals call it simply the bakawan," 
    
    scene intro bakawan with Dissolve(1.0)
    show intro bakawan at Transform(zoom=1.0):
        linear 6.0 zoom 1.3

    voice "narration/intro23.wav"

    "but they speak of it the way one speaks of something that deserves caution. "

    voice "narration/intro24.wav"

    "Not forbidden." 

    voice "narration/intro25.wav"
    
    "Just... not meant for staying too long."

    voice "narration/intro26.wav"

    "The men of Panhuy-an know this instictively."

    voice "narration/intro27.wav"
    
    show intro bakawan at Transform(zoom=1.3):
        linear 6.0 zoom 1.0

    voice "narration/intro28_1.wav"

    "Every evening at dusk, they face the treeline and stand."

    voice "narration/intro28.wav"

    "Not in fear" 

    voice "narration/intro29.wav"
    
    "but in witness." 

    voice "narration/intro30.wav"
    
    "Showing the old things that the village remembers."

    voice "narration/intro31.wav"

    "Attention, in Panhuy-an, is a kind of offering."
    scene intro feet running with Dissolve(2.0)

    voice "narration/intro32.wav"

    "Children are told not to wander near the roots after dark."

    voice "narration/intro33.wav"

    stop audio fadeout 2.0

    "Some of them listen."

    # BY THE WATERS -- DAWA --------------------
    scene intro dawa with Fade(0.5, 0.3, 0.8)
    play sound dawa_humming volume 0.9
    play audio flowing_water volume 0.2

    voice "narration/intro34.wav"

    "A woman crouches by the water, hands deep in a fishing net."

    voice "narration/intro35.wav"

    "She hums something old."

    voice "narration/intro36.wav"

    scene intro dawa noticed with Dissolve(2.0)
    "Kadyos sniffs nearby."
    
    scene intro dawa mc with Dissolve(2.0)
    dawa "Your dog's got more sense than you."

    kilaw "He just wants food."
    
    scene panahuyan village 
    show dawa happy
    show kilaw happy at left_char

    with Dissolve(2.0)

    dawa "Mm. Don't we all."

    narrator "You grinned slightly at that, leaning against a root as you watched her work."

    kilaw "We haven't caught anything since yesterday."
    
    #scene intro dawa screen2 ung may hawak siyang crab
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
    
    menu:
        "They're just old stories":
            $ kilaw_personality = "skeptic"
            kilaw "Stories like that are meant for children, Dawa. I'm not afraid."
            dawa "Stubborn as a mule. Just remember, the silence is where the sea listens the hardest."

        "I believe in them":
            $ kilaw_personality = "believer"
            kilaw "I know. The village elders don't face the treeline for nothing. I'll be careful."
            dawa "Good. Caution is a better friend than courage when the tide turns."

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

    kilaw "Before I head into the bakawan, I should bring an offering..."

    menu:
        "Handful of coarse sea salt":
            $ player_offering = "salt"
            "The elders say salt is a barrier between our world and theirs."

        "Small brass bell":
            $ player_offering = "noise"
            "The Bakunawa hates the sound of metal and noise. If I get lost, perhaps a sharp sound will startle the shadows away."

        "Pouch of white rice":
            $ player_offering = "white_rice"
            "An offering of peace. Pure and white, it represents the light of the moon that the Great Serpent hungers for."

        "I'll bring nothing":
            $ player_offering = "none"
            kilaw "My independence is my offering."
            kilaw "Dawa says I'm stubborn. Maybe she's right, but I'll find my own way."
    
    scene intro festival prep1 with Dissolve(2.0)
    play audio festival_drums volume 0.1 fadein 2.0

    "The afternoon light is golden and low." 
    
    "Somewhere, further down the shoreline, you can hear the faint pulse of drums — the festival preparations already beginning."

    scene panahuyan village 
    show dawa
    with Dissolve(2.0)
    #scene intro into bakawan
    #whistle audio

    "Dawa called after you."

    "Her voice carries over the water, easy as the wind."

    dawa "Make sure you're back before the festival starts." 
    dawa "Your mother will have both our heads if you're not at the lantern lighting!"

    if kilaw_personality == "skeptic":
        dawa "And try not to let your big head get stuck in a root! Keep your ears open."
    else:
        dawa "And stay on the path where the sun hits. Don't go wandering!"

    scene intro bye1 with Dissolve(2.0)

    "You wave a hand without turning around."

    "It's still three moons away, but the village never waits until the last moment."

    "The lantern-hanging hadn't started yet but you could feel it coming."
    #scene intro bye

    "You'll be back in time. You're always on time."

    # INTO THE WOODS -------------
    show background moving with Fade(0.5, 0.3, 0.8)

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

    if kilaw_personality == "skeptic":
        "You pat his head firmly, ignoring the way the trees seem to lean closer to listen."
        kilaw "Just a forest, Kadyos. Don't let Dawa's ghost stories get to you. We're just here for fish." 
    else:
        "You pull him close, feeling the thrum of his heart against your palm." 
        kilaw "It feels different today, doesn't it? We'll be quick, I promise."

    kilaw "Come on, partner. Let's find something for dinner before the sun goes down, hmmm?"
    
    show happy kilaw kadyos:
                xpos 900
                linear 3.0 xpos -900

    narrator "Kadyos barks and trots ahead."

    hide happy kilaw kadyos
    scene wood upwards with dissolve
    
    "Together, they made their way deeper into the mangrove."

    "The air grew thicker, the trees taller, their roots twisting like ancient arms reaching for the sky."
    
    scene bushes background with fade
    
    # BOATT! ----------- 

    narrator "You saw something at the corner of your eyes."

    transform gentle_jump:
        yoffset 0
        ease 0.1 yoffset -15   
        ease 0.1 yoffset 0      

    scene bushes background2
    show kilaw looking at gentle_jump

    "You push through a wall of bushes and gasp."

    "You found it in a small clearing where the water had pulled back, an old wooden boat."
    "Worn and patient, sitting half-in, half-out of the mud."

    if kilaw_personality == "skeptic":
        hide kilaw looking
        show kilaw looking happy

        narrator "A boat. Just sitting here, abandoned."
        narrator "Dawa would probably say it was a trap, but it looks like a lucky find to you."
    else:
        narrator "A boat. It sits in the mud like a silent witness."
        narrator "You remember the rituals, the swaying, the blessings. A cold shiver runs down your back."

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

        scene normal mangrove with dissolve

        "You foraged for nearby fruit, young leaves, seeds, and fish you could catch near land."

        kilaw "Okay. Land food it is. No mysterious glowing water required."

        narrator "The mangrove offered more than you expected."
        
        "Ripe bayabas along the bank, mudskippers in the shallows you could scoop with your hands." 
        
        "Even some wild kangkong near the water's edge."

        kilaw "Ha. Mom would be proud. Fresh greens, fresh fish. Better than the ones our own traders brought."

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

            show boat in with dissolve

            kilaw "...Ugh. Okay. Just a little look. Ten minutes. Then we go home."

            scene boat scene3 
            with Fade(0.5, 0.3, 0.8)

            transform boat_move:
                xpos 50 ypos -300       
                linear 4.0 xpos -1000 ypos 1010

            show rowing boat at boat_move
            with None
            pause 4.0                     
            hide rowing boat

            narrator "You grab Kadyos and tie your food for later. Both of you stepping into the boat together."

            transform fog1_pan:
                xpos 0 ypos -10
                linear 45.0 xpos -1920

            scene spiritual realm at pan_bg
            show rowing at rowing_move
            show fog1 at fog1_pan
            with Dissolve(4.0)

            "You both wandered into the mangrove until evening and got lost." 
            
            "You ate your food, sharing it with Kadyos, until you saw something below the waters." 
            
            "A shimmer, a shadow, something moving with purpose."

            kilaw "Okay that is...definitely something. Definitely not a normal fish."

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

            narrator "The mudfish appears."
            
            "You reach for it without thinking."

            scene waves underwater with Fade(0.5, 0.3, 1.0)
            show drowning:
                zoom 1.6
                xpos 1920
                ypos -3000
                alpha 5.0
                easein 5.0 xpos -1920 ypos 0 alpha 0.0

            pause 3.5
            scene black with Dissolve(3.0)

            "You fell out of the boat and into the water below."
            jump welcome_spiritrealm_main


        label route_go_home: 
            narrator "You shoulder your foraged bundle and walks past without looking back."

            kilaw "Nope. Not my boat. Home time, Kadyos."

            narrator "Kadyos trots after you, tail going. He glances back at the boat once, just once, then follows"

            scene sunset with Dissolve(2.0)

            "By the time you reach the stilts the sky is the color of cooling embers."
            "The smell of woodsmoke and neighbor-cooking is the best thing you've encountered all day." 
            
            "Your mother scolds you for coming back without fish."
            "You show her the kangkong and the bayabas and the mudskippers, and she scolds you less."
            
            "You cook together."
            "It's good. It was a normal evening."

            scene black with Dissolve(3.0)

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

            scene ending1 with Fade(0.5, 0.3, 0.8)

            scene black with Dissolve(3.0)
            $ MainMenu(confirm=False)()
            #return #ENDING 1: BAD (YOU IGNORED THE CALLING)


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
        pause 4.0                     
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

        kilaw "I'm starving Kadyos. If we don't find anything soon, we'll be force to eat this boat."

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

        show splash with dissolve
        show splash2 with Dissolve(0.9)

        kilaw "Wait... Whoa—!"

        scene underwater with Fade(0.5, 0.3, 0.9)

        narrator "You tumbled into the glowing water. Bubbles rise. You gasped, trying to swim up."

        kilaw "Kadyos... Help! The water is pulling me!"

        show hand:
            xpos 0
            ypos 1080
            alpha 0.0

            ease 2.0 ypos 50 alpha 1.0
            pause 0.2
            ease 0.3 ypos 20
            ease 0.3 ypos 60

            ease 0.7 ypos 100
            ease 0.4 ypos 250
            ease 0.5 ypos 150
            ease 0.4 ypos 300
            linear 2.5 ypos 1080 alpha 0.0

        narrator "The shallow tide rose like a living thing — spinning, dragging you beneath the glowing current."

        show screen choice_timer(3.0, "route_vortex_timeout")

        menu:
            "Grab onto the boat":
                hide screen choice_timer
                jump route_grab_boat
            
            "Grab onto Kadyos":
                hide screen choice_timer
                jump route_grab_kadyos
        
    #ROUTE
    label route_vortex_timeout:
        hide screen choice_timer
        narrator "The water is too fast! Before you can reach for anything, the current pulls you under."

        scene waves underwater with Fade(0.5, 0.3, 0.9)
        show drowning:
            zoom 1.6
            xpos 1920
            ypos -3000
            alpha 5.0
            easein 5.0 xpos -1920 ypos 0 alpha 0.0

        pause 3.5
        scene black with Dissolve(3.0)
        jump welcome_spiritrealm_main


    label route_grab_boat:
        narrator "You reach for the edge of the boat, fingers catching the worn wood. For one breathless moment, you hold on"

        kilaw "Got it — I've got it—!"

        narrator "But the vortex pulls harder. You can feel your grip loosening, the water like cold hands around your wrists."

        "From above, Kadyos barks frantically. You felt the splash before you see him trying to jump in."

        kilaw "No — Kadyos, stay back! Stay—!"

        scene waves underwater with Fade(0.5, 0.3, 0.9)
        show drowning:
            zoom 1.6
            xpos 1920
            ypos -3000
            alpha 5.0
            easein 5.0 xpos -1920 ypos 0 alpha 0.0

        pause 3.5
        scene black with Dissolve(3.0)

        narrator "The boat lists sideways. The current claims you both. Darkness swallows the last shiver of light."
        jump welcome_spiritrealm_no_kadyos
        

    label route_grab_kadyos: 
        narrator "You reach for Kadyos instead, arms closing around the warm weight of your dog."

        kilaw "I've got you, boy — hold on—"

        narrator "Kadyos paddles furiously, eyes wide with effort. For a breath they almost make it"

        "Then the vortex catches them together — one spiral, pulling two."

        "It is, somehow, less terrifying this way. You hold him tighter."

        kilaw "...It's okay, Kadyos. We'll be—"

        scene waves underwater with Fade(0.5, 0.3, 0.9)
        show drowning:
            zoom 1.6
            xpos 1920
            ypos -3000
            alpha 5.0
            easein 5.0 xpos -1920 ypos 0 alpha 0.0
        
        pause 3.5
        scene black with Dissolve(3.0)

        narrator "Darkness. Then silence."
        jump welcome_spiritrealm_main

    #ROUTE: WELCOME TO THE SPIRIT REALM ---------------------------
    label welcome_spiritrealm_no_kadyos: 
        narrator "There is no falling, exactly. It's more like the moment you step off a boat and realize the water is far deeper than your feet expected." 
        
        narrator "One second the roots are solid beneath you. The next second — they aren't anything at all."

        narrator "Then; silence. Before lights came from below."

        narrator "Then the sound of water, not rushing, not still."

        narrator "You open your eyes."

        scene spirit map with Fade(0.5, 0.3, 0.9)

        narrator "You are lying on something solid. Stone, maybe, or old root, so thick and wide it feels like ground."

        narrator "Above you: the underside of the mangrove, but wrong."

        narrator "The roots here arch upward, tall, braided together into something that looks less like a tree and more like a doorframe." 
        
        narrator "Old and enormous, trailing kelp and blossoms you don't have a name for, its wood dark and warm."

        narrator "You are outside something. Just outside." 
        
        narrator "Through the arch, there is light."

        narrator "Before you can sit up fully, a voice arrives."

        narrator "It belongs to a small spirit — narrow, silver-finned, hovering at the edge of the root-arch with the particular energy." 
        narrator "Like someone who looked like a child that was sent to do a task and is now reconsidering the task."

        unknown "Oh — oh good, you're awake." 

        narrator "Their fins won't quite stay still. They are holding what appears to be a paper??"
        
        "It seems to have been crumpled and re-smoothed at least twice."

        unknown "We felt you came through."  
        unknown "Well. Everyone felt you came through"

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
        narrator "One second the roots are solid beneath you."
        narrator "The next second — they aren't anything at all."
        
        narrator "You reached for Kadyos. You aren't sure if you found him or if he found you first."

        narrator "Then; silence. Before lights came from below."

        narrator "You open your eyes."

        scene spirit map with Fade(0.5, 0.3, 0.9)

        narrator "You are lying on something solid. Stone, maybe, or old root, so thick and wide it feels like ground." 
        
        narrator "Above you: the underside of the mangrove, but wrong. "

        narrator "The roots here arch upward, tall, braided together into something that looks less like a tree and more like a doorframe." 
        
        narrator "Old and enormous, trailing kelp and blossoms you don't have a name for, its wood dark and warm."

        narrator "You are outside something. Just outside." 
        
        narrator "Through the arch, there is light."

        narrator "Before you can sit up fully, a voice arrives."

        narrator "It belongs to a small spirit — narrow, silver-finned, hovering at the edge of the root-arch with the particular energy." 
        "Like someone who looked like a child that was sent to do a task and is now reconsidering the task."

        unknown "Oh — oh good, you're awake. We felt you come through."
        narrator "A beat. Kadyos shakes water off his ears."

        narrator "Their fins won't quite stay still. They are holding what appears to be a paper??"
        narrator "and the schedule has been crumpled and re-smoothed at least twice."

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
        
        narrator "Kadyos comes barreling in, scattering a nearby spirit entirely, and hits Kilaw at full speed."

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
        scene village house with Dissolve(2.0)

        narrator "Sili-Sili leads you through the root-arch."

        kilaw "Woah..."

        narrator "Kadyos runs past you excitedly."

        narrator "The light. It comes from below as much as above — water running in shallow channels between stone paths." 
        "The whole ground lit from underneath. Every shadow falls upward." 
        
        narrator "The sky looks like the sea" 
        
        narrator "You're in underwater right now."

        scene marketplace with Dissolve(2.0)
        
        narrator "What you thought was a small clearing turns out to be a marketplace, enormous." 
        narrator "Stalls of woven sea-grass and old fishing net, clay pots big enough to sleep in, lanterns strung between crooked posts." 
        
        narrator "At the center: a great stone basin of the same glowing water. The paths all converge on it."

        narrator "The smell is brine and food and something sweet you don't quite have a name for."
        "Two voices argue from somewhere to the left. Something crashes from behind a stall."

        narrator "None of the spirits stop. None of them look up."
        narrator "Except that's not quite right. Because here and there, ones and twos, you catch the sideways glance."
        narrator "The way someone pretends to check a stall display while actually looking elsewhere." 
        narrator "They know you're here. They felt you arrive. They're just letting someone else handle it."

        narrator "Someone is waiting at the edge of the plaza."

        narrator "She is small and ancient-looking, she's holding something on her head." 
        narrator "Built like a great tidal clam, her shell smoothed by centuries of water. Flour-dusted hands." 
        
        narrator "An expression of someone who has set down one problem to deal with a second problem." 
        narrator "And would very much like both problems to resolve quickly. She is holding a clay ladle."

        narrator "She appears to have forgotten she is holding it."
        narrator "Beside her is someone taller, calmly standing there as they seem to be in a deep discussion." 

        narrator "Then they look at you. She looks at Kadyos infront of you. She gave a small nods"

        unknown "Good. You're upright. And the dog is... also upright."

        narrator "Kadyos tail wags."

        if kilaw_personality == "skeptic":
            unknown "You have the eyes of someone who doesn't believe what they see. That will change soon enough."
        else:
            unknown "You carry the weight of your elders' respect. It is rare for a mortal to arrive with so much reverence still intact."

        unknown "Come. Walk with me. There is a great deal to explain and very little time to explain it in."

        narrator "Beside her, keeping pace in the way of someone who has always kept pace with her, is a spirit who moves like still water."
        narrator "Unhurried, present, draped in the particular calm of someone who has seen most things already,"
        "and larger than the space they occupy."  
        narrator "They do not introduce themselves."
        
        narrator "When you catch their eye, there's a quality to the look that's somewhere between curiosity and recognition."
        
        narrator "They did not rush, but they don't slow down either — they move automatically." 
        narrator "Dodging other creatures with ease. You had to actually keep up."

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
        ba_o "Did Sili-Sili not tell you? This is the realm of the spirits. Under the mangrove's roots."
        
        ba_o "You came through the boundary when the current took you—through the rift of our world."

        narrator "A pause. Somewhere nearby, something falls and breaks"

        ba_o "You got here by falling off somewhere. Which is, I will admit, not the traditional method." 
        
        ba_o "But the tide does not ask how you arrived. Only that you have."

        narrator "The tall creature speaks, then, low and even, in the manner of someone who chooses their words with care."

        toto "It has happened before. A mortal crossing the boundary by accident."

        ba_o "Very rarely."

        toto "Two centuries, perhaps three, since the last. A child from the northern shore." 
        
        toto "Fell in following something bright, the same as you. The tide has particular feelings about children."

        narrator "They say this without pretense, the way one recounts a thing that is simply true."

        toto "He made it back."

        narrator "A beat." 
        "That hangs in the air, not as comfort, but as information."
        "You are not the first." 
        "Others have gone home."

        narrator "A short silent filled the space as you followed them."
        jump introduction_choices
         
    label route_who_are_you:
        $ seen_who_are_you = True
        $ bao_name = "Ba-O"
        $ toto_name = "Toto"

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

        toto "You came here by tide, child. The tide does not send things without reason, even if the reason reveals itself slowly."

        if kilaw_personality == "skeptic":
            toto "The tide does not care if you believe in it. It will carry you regardless." 
            toto "Perhaps your 'logic' will be the anchor we need in this chaos." 
        else:
            toto "You have been witness to our world from the other side of the treeline for years." 
            toto "The Bakunawa values a heart that remembers. Do not let that reverence turn into fear."

        narrator "Ba-O stops. Looks at you steadily."

        ba_o "You came through the boundary. The tide brought you here, whether you chose it or not." 
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
        narrator "You watched, but after the second day."
        narrator "Something about the way Ba-O's hands shake as she carries numerous offerings and ingredients made your chest hurt."

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

        scene ending2 with Fade(0.5, 0.3, 0.8)

        scene black with Dissolve(3.0)
        $ MainMenu(confirm=False)()
        
        #return 
        #ENDING 2: BAD ENDING, YOU SHOULD'VE HELPED
    

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

        scene bao kitchen with Dissolve(2.0)

        narrator "The kitchen opens up enormous clay pots the size of fishing boats, fires lit with bioluminescent coral."
        "The smell of sea and something warm and familiar."
        "Your stomach growls."

        ba_o "I would offer you something, but I can't trust my own taste right now. That is the problem."

        kilaw "...What do you normally make? For the festival?"
        ba_o "Everything. Seafood layered in the olden way, each ingredient placed with intention, a prayer."
        ba_o "We call it the ceremonial dish. Every realm has one. Ours is from the deep."

        narrator "Ba-O pauses, her ancient shell creaking as she leans in to get a better look at you."

        if player_offering == "salt":
            ba_o "You carry the scent of the upper tides, child. Coarse salt... 'asin'."
            ba_o "The elders of your village taught you well. Salt is the memory of the sea, and it keeps the flavors of this realm from fading into the mist."
        elif player_offering == "white_rice":
            ba_o "White rice? The grain of the moon and sun."
            ba_o "It is a pure offering. Using it as a foundation shows you have a respectful hand. It makes me think you might actually be able to handle these ingredients."
        else:
            ba_o "A brass bell? You brought a noise-maker to a kitchen?"
            ba_o "Hmph. Just make sure you don't ring it over the broth."
            ba_o "The Bakunawa has a long memory for the sounds that drive it back, but my food prefers silence."

        scene bao kitchen2 with Dissolve(2.0)

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
        ba_o "Ah, honesty. A rare seasoning these days. Let me explain once more, slowly."

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
        ba_o "Wait, this is it! the taste, the texture, the feeling.....it's the recipe I'd forgotten!"
        ba_o "This is… absolutely wonderful, you're such a wonderful cook!"
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
        narrator "You follow the sound of frustrated sighing, which leads you, eventually..." 

        scene sigays_workshop with Dissolve(2.0) 

        "to a studio that appears to have been recently hit by a typhoon." 
        "Bolts of luminescent fabric spill across the floor. Half-finished headdresses lean against walls like tired dancers." 
        "In the center of the chaos, a jellyfish the color of a sunset sits surrounded by crumpled designs."
        kilaw "Right. Costumes next. I can do costumes."
        sigay " I thought I had it all under control... but why does it still feel like I'm missing something?"
        kilaw "Need a hand with those costumes? I can help figure it out."
        sigay "Oh... thank you I really need some assistance"
        narrator "Sigay holds up a half-made headdress—layers of sea glass and woven thread, technically accomplished, completely lifeless."
        sigay "Every year, the costumes are the highlight of the festival. "
        sigay "Every year, I know exactly what to do. But this year... it's like the current dried up inside me. Nothing flows."
        kilaw "What did last year's look like?"
        sigay "Magnificent. Sea greens and deep blues. Woven like—oh, what do you mortals call it—that fabric from your islands?" 
        sigay "The one that takes three moons to make?"
        kilaw "Hablon?"
        sigay "Yes! Like hablon, but of bioluminescent thread. The dancers glowed as they moved. It was... it was alive."
        kilaw "So what changed?"
        narrator "Sigay's tentacles droop."
        sigay "The Bakunawa has been circling for many cycles now. The realm is... frightened."
        sigay "When you design from fear, everything looks like armor. Nothing looks like celebration."
        kilaw "Then let's design from something else. What does the celebration actually feel like?" 
        kilaw "Not what it's supposed to look like, what does it feel like?"
        narrator "Sigay is quiet. Then, slowly:"
        sigay "Like when the bioluminescent sea ignites all at once. Like everyone gasping the same breath at the same time."
        sigay "The feeling of hopefulness? Being alive?"
        narrator "You're not sure if you got it. But you think you do."
        kilaw "Okay. Start there."
        narrator "Sigay sighed, frustrated and tired."
        sigay "It's not that simple."
        kilaw "It's alright. I'll help you as much as I can"
        
        if kilaw_personality == "skeptic":
            kilaw "It's just fabric and light, Sigay. If it worked once, we can make it work again with a little effort." 
            sigay "Effort? How... practical. Maybe a little human 'fix-it' energy is exactly what we need." 
        else:
            kilaw "It's about the soul of the celebration."
            kilaw "My lola said the threads have to remember the joy to really glow." 
            sigay "Wise words. Yes... let's try to find that joy together." 

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
        scene village house with Dissolve(2.0)

        narrator "You said your goodbyes and went to the next spirit in need, the performance committee." 
        narrator "It was held by two spirits, Bilong-Bilong and Sili-Sili."
        narrator "You heard them before you saw them, two voices, one sharp and declarative, one fluid and insistent,"
        narrator "talking over each other in perfect disharmony."

        scene dance area with Dissolve(2.0)

        narrator "When you got where they were, the two dancers were locked in a bitter disagreement over choreography."
        narrator "One favors traditional movements, the other demands something more fresh and modern in expression."

        bilo "The steps have not changed in many cycles for a REASON, Sili-Sili! The Bakunawa recognizes the old forms."
        bilo "It is what makes its memory!"
        sili "And that's exactly the problem!"
        sili "It's been how many long—the Bakunawa has seen the same performance many times since the past centuries!" 
        sili "We need something that catches it off guard, something it hasn't seen before!"
        bilo "You want to improvise at the most important ceremony of the century?!"
        sili "I want to perform something worth watching!"
        narrator "They stop when they saw you."
        bilo "Ah. The mortal girl. Are you here to talk some sense into this current-brained flounder?"
        sili "They meant me, I'm the flounder."
        kilaw "I could hear you from the other side of the village, just so you know."
        bilo "Good. Someone needed to hear this. Since Sili-Sili won't."
        sili "I hear fine. I simply choose not to drown in your nonsense."
        kilaw "Okay. Show me. Both of you. Show me what you mean, not tell me. Show me."

        narrator "Bilong-Bilo demonstrates the traditional form first, slow, deliberate, weighted with centuries of intention."
        "Each movement connects to the next like the current connecting islands. You feel something ancient in it."
        "Then Sili-Sili performs, quick, surprising, every movement a question that the next movement answers. It's alive in a different way." 
        "Something profoundly new."
        kilaw " ...You're both right."
        narrator "..."
        bilo "Excuse me?"
        kilaw "You're both right and you're both not looking at the other's work properly."
        kilaw "Bilong-Bilong, the old forms have weight. Real weight. You can feel it." 
        kilaw "But Sili-Sili, the surprise, the life in it, that's what makes a crowd gasp." 
        kilaw "I think the foundations should never changes, the rhythm, the footwork, but every year the expression is new."
        kilaw "Same roots. Different flower"
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
        scene village house with Dissolve(2.0)

        narrator "You focused your attention on Lusay. A young oyster brimming with brilliant ideas for props and effects."
        "But you had to find her first. The other spirits already told you about her and her general direction."
        "The Props workshop sounded like a small disaster from outside: things rolling, falling, someone groaning quietly"

        narrator "A young oyster brimming with brilliant ideas for props and effects. However lacking the confidence to execute them. Or so they said."

        scene lusays_workshop with Dissolve(2.0)

        "Their workshop is absolute chaos. Dozens of started projects, but nothing finished."
        "You step over three unfinished lanterns, a net of sea glass that has been tangled rather than woven."
        "It appears to be an entire installation of hanging coral that has fallen sideways."
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
        narrator "Together they completed something spectacular, moving with coordination and at ease."
        "The decoration was finished, and so is the morning."
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
        narrator "Now fighting panic about your own transformation, your breath trying to push through your own fears."
        "You muttered quietly to yourself as you took a deep breath."

        kilaw "Okay. Okay, breathe. Scales—yes. Tail—yes, still there. Ears—fin-shaped, gross."
        kilaw "Am I still...me?"

        narrator "Kadyos licks your scaled hand. His tail is fully finned now too."
        narrator "He looks up at you with the same stupid adoring expression he always has."
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

        scene ending3 with Fade(0.5, 0.3, 0.8)
        
        scene black with Dissolve(3.0)
        $ MainMenu(confirm=False)()
        
        #return 
        #BAD ENDING: Your fear was real. So was everything it cost you. 

    
    ## ═══════════════════════════════════════════════════
    ## KASAG — MUSIC COMMITTEE
    ## ═══════════════════════════════════════════════════
    label kasag_intro:
        scene village house with Dissolve(2.0)

        narrator "Outside you heard a booming voice, proud and loud, filling the whole corridor of the festival grounds like a wave filling a cave."
        "Kadyos's fin-tail stiffened. Even he seemed uncertain about approaching."
        kilaw "That's... the music committee?"
        narrator "A passing spirit nodded, eyes wide."
        unknown "Kasag. Old crab."
        unknown "Been conducting the music for three hundred years, but this cycle—the younger musicians have been pushing back."
        unknown "Makes his claws very... clicky."
        narrator "You took a breath. Scales itched along your collarbone. You walked toward the sound."

        scene kasag_music_workshop with Dissolve(2.0)

        kilaw "Kasag? I'm here to help with the music—"
        kasag "Help? HAH! Who said I needed help? You?"
        narrator "He berated a nearby spirit for even holding their instrument in a wrong way."
        "He said a lot of unwarranted things towards them, before they turn to you."
        kasag "I've been conducting this festival's music for many cycles before you, mortal, was even born."
        kasag "What I need is MY direction followed properly!"
        kasag "My music kept the Bakunawa away from eating the last moon we have! It would've been eaten if I didn't take charge."

        if player_offering == "noise":
            narrator "As he puffs out his chest, the small brass bell in your pocket gives a sharp, clear ring."
            kilaw "I brought this from the village. I thought... well, I thought the serpent might need reminding of that sound."
            kasag "HAH! A noise-maker! You understand then!"
            kasag "We don't just play music for the ears, mortal. We play to keep the darkness at bay."
            kasag "Your preparation shows you have more spine than these other musicians!"

        elif player_offering == "salt":
            kasag "And what do you have there? Salt? You think you can preserve a melody like a piece of dried fish?"
            kasag "Hmph. At least you’re prepared to protect yourself. But here, only the rhythm will save you."

        elif player_offering == "white_rice":
            kasag "White rice. A peaceful gift for a creature that wants to swallow the sky."
            kasag "You have a quiet heart, child. Let's see if that quiet can find the strength to beat a drum."

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
            narrator "The other nearby spirits were muttering between themselves, busying themselves with idle tasks."
            "Kasag took a deep breath."
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
            narrator "The musicians begin to play—Kasag's strength meeting the young spirits' innovation."
            narrator "Kasag's voice soften in awe. The musicians seems happy with themselves."
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
            "It was a disaster. It left you nothing but disappointment."
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

        narrator "The bioluminescent sea ignites below and up the festival grounds, the same glow you followed from the boat." 
        narrator "What felt like a lifetime ago."
        "The same light that started everything."
        "You looks at your hands and saw the scales spreading, fast"
        kilaw "How much more do we have before..."
        narrator "You don't finish the thought. Kadyos whimpers, his tail now fully finned."

        scene sunset with Dissolve(2.0)

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

        scene black with Dissolve(3.0)
        jump pre_ending


    ## ═══════════════════════════════════════════════════
    ## CALCULATE SCORE AND ENDINGS
    ## ═══════════════════════════════════════════════════
    label pre_ending:
        narrator "The water beneath the festival grounds begins to tremble — not the frantic churning of the vortex that brought you here."
        narrator "But something deeper. Deliberate. Aware."
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

        scene ending4 with Fade(0.5, 0.3, 0.8)
        
        scene black with Dissolve(3.0)
        $ MainMenu(confirm=False)()

        #return 
        #You made it.

    #NEUTRAL OUTCOME
    label neutral_ending:
        narrator "The Bakunawa rises, vast and patient, the way old things are patient."
        "It doesn't rush. It has seen three hundred festivals. It is taking the measure of this one."
        "The music falters for just a moment. Then holds."
        "The Bakunawa is massive, ancient, neither angry nor pleased. It circles the moon, considering."
        "The festival bought time, but nothing more."
        ba_o "Child, quickly, you can return home, partially transformed, or stay and help us find a new way."
        narrator "You stand between two worlds, unsure which path to choose."
        menu:
            "Stay":
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

            scene ending7 with Fade(0.5, 0.3, 0.8)

            scene black with Dissolve(3.0)
            $ MainMenu(confirm=False)()

            #return 
            #You stayed in the spirit realm. You are not sure how long you will stay, but you know you will be here for a while.

        label leave_here:
            narrator "You look at the portal. You think of the mangrove at dawn. You think of your village. Your mom."
            "You think of all the lanterns your neighbors hung for the festival you missed, the drums you heard from the water three moons ago."
            "The way you always forget how much you love home until you're standing at the edge of losing it."
            kilaw "I need to go home."
            ba_o "We understand, child. We'll be here. We always are."
            narrator "When you went back to the surface, the aquatic features don't entirely recede."
            "Faint scales along your wrist, ears that catch the sound of running water differently now, a sensitivity to tides you didn't have before." 
            "You don't mind. They're a reminder. Proof that something happened, that it was real, that you were there and came back."

            scene ending6 with Fade(0.5, 0.3, 0.8)
            
            scene black with Dissolve(3.0)
            $ MainMenu(confirm=False)()

            #return 
            #You returned to the mortal world, forever changed.

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

        scene ending5 with Fade(0.5, 0.3, 0.8)
        
        scene black with Dissolve(3.0)
        $ MainMenu(confirm=False)()
        
        #return
        #BAD ENDING: Your efforts were not enough. The moon was devoured, and you are left in the darkness of what could have been.

    return
