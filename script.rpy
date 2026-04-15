# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define e = Character("Eileen") -- DEFAULT ALREADY THERE

define narrator = Character(None, window_style="narrator_window")
define kilaw     = Character("Kilaw",     window_style="character_window")
define kadyos    = Character("Kadyos",    window_style="character_window")
define ba_o      = Character("Ba-O",      window_style="character_window")
define toto      = Character("Toto",      window_style="character_window")
define lusay     = Character("Lusay",     window_style="character_window")
define sili      = Character("Sili-Sili", window_style="character_window")
define bilo      = Character("Bilo-Bilo", window_style="character_window")
define kasag     = Character("Kasag",     window_style="character_window")
define sigay     = Character("Sigay",     window_style="character_window")
define dawa     = Character("Dawa",     window_style="character_window")
define unknown     = Character("???",     window_style="character_window")

# NOTES FROM DEFAULT -------------------

# The game starts here.
# label start 

# Show a background. This uses a placeholder by default, but you can
# add a file (named either "bg room.png" or "bg room.jpg") to the
# images directory to show it.
   
#scene title of image with is use for transition 
    
# This shows a character sprite. A placeholder is used, but you can
# replace it by adding a file named "eileen happy.png" to the images
# directory.

#show kilaw walking

# These display lines of dialogue.

#name of character "dialogue"

label start:

    #ACT 01 ---------- EXPOSITION

    #PROLOGUE -- PANHUY-AN

    narrator "There is a place where the sea does not end and the land does not begin."

    "At the far edge of the island, where the land loosens its grip and gives way to the tide, lies a quiet village called Panhuy-an."

    "The houses stand on stilts above shallow breathing water. Wooden floors creak with every step."

    "Banca boats rest loosely tied to posts, hollowed from trees older than the people who carved them."

    "The sea feeds the village." 
    
    "The village, in turn, learns never to take more than it is given."

    "In the mornings, the elders watch the horizon."

    "Morning smells of salt and smoke. Children run between the stilts."

    "Neighbors call to each other across the water."

    "The old lecturing the young."

    "The whole village moves with the easy rhythm of a place that knows itself."

    "The evening carries distant laughter, the sound of wind and waves folding into each other."

    "The people here speak of tides, and moon, and seasons when the fish are plentiful."
    
    "... and seasons when even the nets come back empty."

    "Beyond the village, the sea stretches wide and honest."

    "But behind it," 
    
    "behind the stilts and the smoke and the festival drums already beginning their preparations," 
    
    "stands the bakawan."

    "Not planted." 
    
    "Older than any name the villagers could give it." 
    
    "Its roots twist deep into the earth and deeper still into stories passed down by those who came before." 
    
    "The locals call it simply the bakawan," 
    
    "but they speak of it the way one speaks of something that deserves caution. "

    "Not forbidden." 
    
    "Just... not meant for staying too long."

    "The men of Panhuy-an know this instictively."

    "Every evening at dusk, they face the treeline and stand."

    "Not in fear" 
    
    "but in witness." 
    
    "Showing the old things that the village remembers."

    "Attention, in Panhuy-an, is a kind of offering."

    "Children are told not to wander near the roots after dark."

    "Some of them listen."


    # BY THE WATERS -- DAWA --------------------

    narrator "A woman crouches by the water, hands deep in a fishing net."

    "She hums something old."

    "Kadyos sniffs nearby."

    dawa "Your dog's got more sense than you."
    kilaw "He just wants food."
    dawa "Mm. Don't we all."

    narrator "You grinned slightly at that, leaning against a root as you watched her work."

    kilaw "We haven't caught anything since yesterday."
    
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
    "The afternoon light is golden and low." 
    
    "Somewhere, further down the shoreline, you can hear the faint pulse of drums — the festival preparations already beginning."

    "Dawa called after you."

    "Her voice carries over the water, easy as the wind."

    dawa "Make sure you're back before the festival starts." 
    dawa "Your mother will have both our heads if you're not at the lantern lighting!"

    "You wave a hand without turning around."

    "It's still three days away, but the village never waits until the last moment."

    "The lantern-hanging hadn't started yet but you could feel it coming."

    "You'll be back in time. You're always on time."

    # INTO THE WOODS -------------
    
    scene bg mangrove with dissolve
    show fg leaves 

   
    show kilaw walking:
            xpos 900
            linear 3.0 xpos -600 

    narrator "In search of dinner, you wandered into the forbidden mangrove, a place whispered about in old stories."
    "You didn't bring anyone."
    "You brought someone better."
    "Your trusted friend and companion."
    
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
                linear 3.0 xpos -700

    narrator "Kadyos barks and trots ahead."
    "Together, they made their way deeper into the mangrove."
    "The air grew thicker, the trees taller, their roots twisting like ancient arms reaching for the sky."

    # BOATT! ----------- 

    narrator "You saw something at the corner of your eyes."
    "You push through a wall of bushes and gasp."
    "You found it in a small clearing where the water had pulled back, an old wooden boat, worn and patient, sitting half-in, half-out of the mud."

    kilaw "A boat?"

    narrator "You looked at the boat with careful attention."
    "In your village, there was a rituals seafarers practiced which involved chanting before fishing or sea raids."
    "If the boat swayed, the spirits blessed the trip."
    "The greater the movement, the greater the fortune! Or so they say."
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
        "Take the boat along with Kadyos":
            jump route_take_the_boat
            #Route2
        
        "Stay on Land":
            jump route_stay_on_land
            #Route1
    
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

        narrator "You passed by the boat as you went home. It still sits there, old and patient, as if waiting."

        #CHOICES: GO HOME OR GO FOR AN ADVENTURE
        menu:
            "Go for a little adventure":
                jump route_go_for_an_adventure
                #Route2
        
            "Ignore it and go home":
                jump route_go_home
                #Route1 leading to bad ending

        
        label route_go_for_an_adventure:
            narrator "You paused. You look at the boat. You look at Kadyos."

            kilaw "...Ugh. Okay. Just a little look. Ten minutes. Then we go home."

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

            "By the time you reach the stilts the sky is the color of cooling embers, and the smell of woodsmoke and neighbor-cooking is the best thing you've encountered all day." 
            
            "Your mother scolds you for coming back without fish. You show her the kangkong and the bayabas and the mudskippers, and she scolds you less."
            
            "You cook together. It's good. It's a normal evening.
            You sleep."

            "Behind the village, in the deep water hours, the mangrove is very quiet."
            
            "The men on the night watch stand at the treeline and face it, the way they always do. They don't know what they're waiting for. They never do." 
            
            "They just stand there, the way their fathers stood there, the way their fathers' fathers did."

            "The festival does not fall apart loudly. It falls apart the way a net comes undone, one thread, then another, then a hole where the fish slip through."

            "You wake to darkness. Not the soft darkness of early morning before the birds remember they exist, the other kind. The kind that sits wrong on the skin."

            "You light a lantern."

            "Through your window, the mangrove stands the same as it always has. Roots and water and the nothing-particular dark between the trees."

            "You don't know what you missed. You won't. The water keeps what it keeps, and it does not explain itself to the living."

            "Kadyos puts his head in your lap. His tail moves once, slowly."

            return #ENDING 1: BAD (YOU IGNORED THE CALLIING)


    label route_take_the_boat:
        kilaw "I'll take that as a yes. Let's go!"

        narrator "You grab the edge of the old wooden hull and haul yourself in, arm already extended."

        kilaw "All aboard! Let's see what secrets this mangrove's been hiding."

        narrator "The sun hung low, painting the mangrove in warm orange light. The water glimmered softly, catching the last fire of the day."

        "As you drifted deeper, the shadows grew longer, and the forest started to whisper in the wind."

        "Your eyes widened as the light faded, the roots beneath you shimmered faintly."

        kilaw "It's beautiful."

        narrator "You whispered, he word forms in your chest like a held breath."

        "Unaware of the world you knew was slowly slipping away."

        "The tide came and went. Your stomach grumbled."

        "The glow of the mangrove was lovely but unfortunately it wasn't food. You sighed."

        kilaw "I'm starving Kadyos. If we don't find anything soon, we'll force to eat this boat."

        narrator "Kadyos whines softly."
        
        "Suddenly, the glowing water rippled. A mudfish appears near the boat."

        kilaw "Hey! Did you see that? Dinner's served!"

        narrator "You try to time it properly before lunging on the fish's direction with half of your body still on the boat."

        kilaw "Almost... got you!"

        narrator "You try to pull the fish to the surface. Before—"

        kilaw "Wait... Whoa—!"

        narrator "You tumbled into the glowing water. Bubbles rise. You gasped, trying to swim up."

        kilaw "Kadyos... Help! The water is pulling me!"

        narrator "The shallow tide rose like a living thing — spinning, dragging you both beneath the glowing current."

        #CHOICE: YOU GRAB ONTO
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

        #CHOICES: Where/Kadyos/Okay ------------------------
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

        #CHOICES: Where/Okay ------------------------
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

        #CHOICES: YOU FOLLOW THEM AND SAID... -------------
        label introduction_choices:
        menu:
            "What is this?" if not seen_what_is_this:
                jump route_what_is_this

            "Who are you?" if not seen_who_are_you:
                jump route_who_are_you

            "Look at surrounding" if seen_what_is_this and seen_who_are_you:
                jump route_after_the_introduction
        
    #ROUTE REPLY ----------------------------------------------
    label route_what_is_this:
        $ seen_what_is_this = True
        default seen_what_is_this = False    
        #BAO
        unknown "Did Sili-Sili not tell you? This is the realm of the spirits. Under the mangrove's roots."
        
        #BAO
        unknown "You came through the boundary when the current took you — through the rift of our world."

        narrator "A pause. Somewhere nearby, something falls and breaks."

        #BAO
        unknown "You got here by falling off somewhere. Which is, I will admit, not the traditional method." 
        
        #BAO
        unknown "But the tide does not ask how you arrived. Only that you have."

        narrator "The tall creature speaks, then, low and even, in the manner of someone who chooses their words with care."

        #TOTO
        unknown "It has happened before. A mortal crossing the boundary by accident."

        #BAO
        unknown "Very rarely."

        #TOTO
        unknown "Two centuries, perhaps three, since the last. A child from the northern shore." 
        
        #TOTO
        unknown "Fell in following something bright, the same as you. The tide has particular feelings about children."

        narrator "They say this without pretense, the way one recounts a thing that is simply true."

        #TOTO
        unknown "He made it back."

        narrator "A beat." 
        "That hangs in the air, not as comfort, but as information."
        "You are not the first." 
        "Others have gone home."

        "A short silent filled the space as you followed them."
        jump introduction_choices
         
    label route_who_are_you:
        $ seen_who_are_you = True 
        default seen_who_are_you = False 
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

        #CODE track which choices have been seen using variables

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

        narrator "Ba-O stops. Looks at you steadily."

        ba_o " You came through the boundary. The tide brought you here, whether you chose it or not." 
        ba_o "We won't force your hand. But it knows we needed help."

        narrator "She glances back at the chaos of the marketplace. The ladle is still in her hand."

        ba_o "And if you happened to have free hands..."

        narrator "Toto holds your gaze for a moment longer. Their expression is not unkind." 
        "It is the expression of someone who knows what comes next and trusts that you will find your way to it."

        toto "I have other things to see to. The boundary. The night watch. The preparations that cannot wait."

        narrator "They rest a hand , brief, light, on the top of your head. You do not know why, but it feels like something."

        toto "Ba-O will take care of you. She is good at that."

        narrator "And then they are gone, easing back into the crowd with the easy unhurry of the sea finding its level."
        "Ba-O does not watch them go. She is already looking at you."

        ba_o "Come. Let us start at the beginning, and the beginning, always, is the kitchen. So, would you help?"

        menu:
            "I'll help":
                jump route_help

            "I'll help":
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
        #jump to NEUTRAL ENDING 

    label route_watch:
        narrator "You cross your arms. You don't move. Youwatch as the committees argue, drop things, dissolve into a cascade of small disasters."

        kilaw "They'll figure it out. They said so themselves, they have done this for centuries, right? What does me being here change?"

        narrator "Kadyos whimpers and presses against your leg. You ignore the sound of something cracking in the Props room."
        "You ignore Ba-O sighing quietly over cold dishes.Three days of watching. Three days of nothing."

        toto "The festival will begin whether we are ready or not, child. The Bakunawa does not wait."

        narrator "You said nothing. Your actions showed it clearly. The scales begin appearing on your arms that night, and you don't notice until morning."
        
        #BAD ENDING ----------------------
        narrator "You watched."
        "Three days of watching."
        "The committees argued, dropped things, dissolved into cascades of small disasters."
        
        "They did it without you."
        "They did it anyway, because that is what you do when you have no other choice."
        
        "The festival happened."
        "What it could do without you, it did."
        "What it needed you for, it couldn't."

        "The Bakunawa arrived in the small hours, when the last lantern had not yet been lit." 
        "It did not pause." 
        "It did not circle." 
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
        return #ENDING 2: BAD ENDING, YOU SHOULD'VE HELP --------------------
    
    #ROUTE BAO MINIGAME INTO AND BEGINNING ---------------------    
    label route_kitchen:
        narrator "Ba-O leads you through a passage where the walls are woven from dried sea-grass and old fishing nets — the kind of weave, you think, that looks almost like hablon from back home, if hablon were made of wood itself. It looks natural."

        ba_o "You cook, child?"
        kilaw "A little. My lola taught me."
        ba_o "Good. Then you understand that food is memory. Every dish I have forgotten is a piece of this realm lost, naman. We cannot let the Bakunawa come to an empty table."

        narrator "The kitchen opens up enormous — clay pots the size of fishing boats, fires lit with bioluminescent coral, the smell of sea and something warm and familiar. Your stomach growls."

        ba_o "I would offer you something, but I can't trust my own taste right now. That is the problem."

        kilaw "...What do you normally make? For the festival?"
        ba_o "Everything. Seafood layered in the olden way — each ingredient placed with intention, a prayer. We call it the ceremonial dish. Every realm has one. Ours is from the deep."

        narrator "She slides a tray of ingredients toward you. It glows faintly."

        ba_o "You will build the ceremonial dish layer by layer. After that, dress it with colors and textures from our realm."

        ba_o "Do you understand what must be done?"

        menu:
            "Yes":
                jump route_understood
            "NO":
                jump route_no 

    #ROUTE CHOICES --------------------------------
    label route_understood:
        ba_o "Good. Begin when you're ready. My memories are waiting to be awakened."
        jump route_game_bao

    label route_no:
        ba_o "Ah, honesty. A rare seasoning these days. Let me explain once more, slowly"

        ba_o "You will build the ceremonial dish layer by layer. After that, dress it with colors and textures from our realm."

        ba_o "The ingredients are before you. Each one holds a piece of our realm's spirit."

        ba_o "Choose wisely, but also choose with feeling."
        
        menu:
            "Yes":
                jump route_understood
            "NO":
                jump route_no_again

    label route_no_again:
        ba_o "Again, you will build the ceremonial dish layer by layer. After that, dress it with colors and textures from our realm."

        menu:
            "Yes":
                jump route_understood
            "NO":
                jump route_no_again

    #BAO FEEDBACK MINIGAME
    default score_bao = 0
    ba_o "Well done, child."
    #good feedback

    ba_o "Could be better."
    #neutral feedback



        



    # This ends the game.

    return
