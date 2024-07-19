label kayden_1:
    #(unlocked by terry 2)
    scene couch with fade
    "Parvez has been messaging with this person on the hook up app for a while."
    "Looking back through the messages since Terry started the account, this person was one of the first to talk to Parvez."
    "Their profile is wild. NEON PUNK CUNTBOY it reads. SPIT IN MY FACE AND MAKE ME CALL YOU DADDY."
    "It's a bit much for Parvez, seems like the sort of thing that would attract chasers who will treat you like shit."
    "This dude had been intense in their messages right away too."
    # use app chat interface??
    npc "is it real????"
    npc "can i touch it owo ???"
    npc "please if it's real i want to suck it"
    npc "i want to feel it wriggling around inside me"
    npc "lay ur plant eggs in me"
    "In spite of himself, Parvez had started to chat with them."
    #cg: pics??
    "They asked for pictures of Parvez's cock constantly."
    "He wasn't really in the practice of taking nudes before, let alone highlighting his new body part."
    "But no matter what he sent, this person would lose their mind over it."
    npc "daddyyyyyy :drool emoji:"
    npc "it's so weird and big"
    npc "please fuck my guts up with that thing"
    "They sent back tons of videos too, sometimes even several times a day."
    "Them moaning, grinding on toys, sticking their fingers in their sloppy cunt."
    "They were always so noisy."
    "Parvez had to go in the bathroom to watch their videos,"
    "turning the fan on and straining to hear their sticky pussy noises and moans coming out from his tinny phone speaker."
    "It embarrassed him to say it turned him on."
    "They also were kind of needy, messaging him lots, sending messages back to back when he didn't respond."
    "It was hard to pinpoint what made Parvez keep talking to him."
    "No one had ever really wanted Parvez so desperately in that way before...{w} at least not as a top."
    "Plenty of straight men had been gross and pushy toward him before, but their desperation was menacing."
    "This on the other hand was naked, bratty greed."
    npc "come on boss"
    npc "are you gonna mess up my pussy with that freaky plant cock or what"
    menu:
        "give it to the brat":
            jump meet_kayden
        "something is off about this person ...":
            pass
    "The vibe just isn't right."
    "It's been fun to tease this person but they're a bit too intense. It doesn't feel safe to actually meet them."
    "They seem a bit unstable, obsessive."
    npc "daddyyyyy {w} i want you to fuck meeeee"
    pdm "sorry dude I actually don't think I want to meet"
    npc "what. {w} what the fuck is wrong with you."
    "They sent another video, spreading themself and taunting him."
    "Parvez watched it at his desk while Terry was watching TV in the other room."
    npc "come on daddy"
    npc "don't you want to feel this boyhole clenching around you"
    npc "do you know how many men this pussy has driven insane"
    "It's so sloppy as they finger themself, the noise so loud through the phone."
    "Surely Terry can hear it."
    "Inside their cunt is so pink, so pale and juicy. Hairless, like a little kid."
    "It blinks wetly open and closed on the video, like they're winking it intentionally."
    "Parvez is mesmerised by the sight of it."
    "He watches the video several times in a row, rock hard, listening to this weirdo insult him."
    "He strokes himself as he does, riding his deeply unsatisfying wavelike orgasms for ages."
    menu:
        "Finally, he makes his decision."
        "maybe i should give it a try ...":
            jump meet_kayden
        "no, this is definitely a bad idea":
            pass
    pdm "sorry man it's just. {w} it's just too weird."
    npc "fuck you."
    npc "fucking pussy."
    npc "you're just a worthless cuck. you don't deserve this sloppy boi pussy anyway."
    "Despite this, they keep messaging him over a couple of weeks."
    "They keep sending more nudes, more videos working clear toys into their hole and degrading him."
    "Parvez watches them all but he forces himself not to respond. In some of the videos they seem out of it, inebriated."
    "When he doesn't respond for a couple of weeks, they eventually give up."
    "After that, he keeps seeing them on the app for a few months before they disappear."
    jump nav_menu
label meet_kayden:
    $ met_kayden = True
    pdm "okay, where do you want to meet?"
    scene skatepark ramps with wipeleft
    "As soon as Parvez shows up to the location that NEON PUNK CUNTBOY had chosen, he regrets his decision to come."
    "It's a grimy and badly maintained skate park under the old highway at the edge of town."
    "The orange of the setting sun picks out all the rust in the steel girders and the rebar hanging out from under the road."
    "While it's not visible from the highway down there, the sound of passing cars overhead reverberates the whole space, showering down bits of concrete."
    "Every surface is covered in rubber skidmarks and graffiti. Layers of street art from generations of outcast kids skating here."
    "One piece of writing, high up on a curve that you can't get to from above, reads FAGGOTNESS."
    "Parvez wonders if that's NPC's work."
    "Parvez checks his phone. They're late."
    "He's starting to consider leaving ..."
    menu:
        "wait five more minutes":
            $ plantasy = True
            "Parvez decides to wait a bit longer."
            "It's kind of beautiful down here in a strange way."
            "Beyond the highway there isn't much, and the green kudzu vines that blanket all the scrublands around here have started to creep in."
            scene skatepark hill with Dissolve(1)
            "The ramps toward the back are all partly covered in a growing mass of green."
            "Parvez goes over and sits on one of the thickly foliated concrete ramps."
            "The leaves are squishy, cushioning him. He could easily sleep on this thick mat of vines."
            "He imagines himself laying there, the vines slowly twining around his arms and legs. Holding him in place."
            "Parvez gets up suddenly. He hears someone coming."
            "He realizes with a start that he is flushed and semi-hard."
            "He brushes the leaves off himself and tries to calm down as footsteps approach."
            jump kayden_arrives
        "go":
            $ tried_to_leave = True
            "Parvez feels a hand on his shoulder just as he's turning to go."
            pass
label kayden_arrives:
    show kayden
    k "Sorry I'm late. I'm Kayden."
    if tried_to_leave:
        "Parvez shrugs their hand off his shoulder instinctively, annoyance bubbling up in him."
    p "Dude, what is this place?"
    "Kayden leads Parvez to a section of the skatepark near the side of the underpass."
    scene skatepark interior with dissolve
    show kayden at midleft
    show parvez at midright
    with moveinleft
    k "This is my sanctuary."
    "Kayden looks around like he's seeing the space for the first time."
    k "I've been coming here since I was a kid."
    k "It used to be a popular place for kids to skate until the new highway got built."
    k "Now no one comes here any more."
    "Their voice sounds wistful for a moment before they continue."
    "Turning their feral gaze on Parvez they say:"
    k "That makes it perfect for grimy nasty fucking out in the open."
    show parvez worried with dissolve
    "Parvez feels his face color."
    p "Jeez, dude."
    "They grin, openmouthed, tongue pressed to one of their unusually sharp teeth. They continue in a girlish high voice."
    k "I'm sorry, have I offended the good gentleman?"
    show kayden threatening at center
    show parvez worried:
        xalign 0.75
    with move
    "They advance toward him. Parvez is slightly frightened."
    k "Please sir, insert thine member into my nubile pussy."
    k "I am but a fair maiden, good sir, please ... deflower me gently."
    show kayden threatening at midright
    show parvez worried:
        xalign 0.9
    with MoveTransition(0.2)
    "They have Parvez pressed up against a wall."
    "They grab his hand and press it under their skirt."
    "Their tights are already torn, the hole sopping wet around his cunt."
    "Their clitoris and labia are swollen, bright pink and slick. They've clearly been touching themself already."
    "They lean in and speak the next words directly into Parvez's ear, their breath tickling his neck."
    k "So are you just a little pansy bitch, or are you going to fuck me?"
    menu:
        "f-fuck ...":
            jump fuck_kayden
        "this is too weird actually":
            "Parvez tries to withdraw his hand. Their grip is strong."
            k "What, gonna pussy out?"
            "Their face is too close, their eyes wild, their breath hot and acrid."
            "Their voice drops to a growl, too loud and too close."
            show parvez crying with dissolve
            k "You're a little bitch man, you're not strong enough to admit this is what you want."
            "They force Parvez's fingertips into their wet pussy, clenching down on him."
            p "Holy fuck what is wrong with you??"
            "Parvez shoves them with the point of his shoulder in their chest, as hard as he can."
            "They keep their grip on his hand and they both fall over, unbalanced."
            show kayden threatening at center:
                zoom 0.75
                yalign 0.75
            with move
            "This shakes them enough for Parvez to break free and start moving away."
            k "You're just a cunt like me. You could never be a real man."
            "Parvez starts running out of there."
            hide kayden with moveoutleft
            "They start laughing, not even trying to follow. Their last words follow Parvez out."
            k "I hope a real man comes and rapes your bitch hole and shows you what you truly are."
            scene black with pushleft
            "Parvez drives home, shaking all the way, covered in cold sweat."
            "He's angry with himself for going, and for being so unsettled."
            scene couch
            show terry at center:
                zoom 1.5
                yalign 0
            with wipeleft
            "He finds Terry on the couch watching a cooking anime."
            hide terry
            show parvez n terry at center:
                zoom 1.5
                yalign 0
            with dissolve
            "He snuggles himself under Terry's arm, saying nothing, just burrowing toward the warmth of Terry's body."
            t "Bad date, huh?"
            "Parvez grumbles into the meat of Terry's armpit, not even coherent words."
            "Terry rubs his back as the sweat all over his body dries until he finally feels warm and safe."
            jump nav_menu
label fuck_kayden:
    "Parvez shoves his fingers up inside them."
    "He draws them out again before forcing them back in, rough, uncareful."
    show kayden bottomy with dissolve
    "Kayden has their arms around him, hanging off his body, whining into his ear."
    k "Yes, Daddy ... {w} fuck me up."
    "Parvez grabs their shoulders, catching them off guard and turning them around."
    # needs flip lmao
    show kayden bottomy at right
    show parvez toppy at farright
    with move
    "He has them boxed in to the wall now. Even though they are taller than him, they shrink in front of him."
    "Their gaze is still sharp though: defying, taunting, evaluating."
    "Parvez drops his pants. They had arranged for it to be 'his time of the month,' as Terry calls it."
    "The head of his cock was bulbous, thick in a way that made Terry struggle to get it inside."
    "Kayden stares at it openmouthed."
    "They move to kneel before him{fast} but Parvez grabs them by the thighs and shoves them back against the wall, pressing inside them right away."
    "They gasp as the air is punched out of their lungs."
    "Parvez fucks them roughly against the wall and they scream."
    "They bunch their nails into his back. {w} They're sharp.{w} Parvez feels them break the skin in places."
    "Parvez pounds against them without regard for their comfort or pleasure, which seems to be how they like it."
    k "ahh!! Daddy !!!"
    k "force that dick into me!!"
    k "wreck me with that monster cock!!"
    k "make me yours daddy !!!"
    "They keep clenching tighter and tighter and before Parvez knows it he's busting inside them."
    "Goo splatters to the floor as he pulls out."
    "They reach inside themself and scoop some to their lips, before kneeling to suck the rest of it off Parvez's cock."
    "He shoves himself into their mouth unceremoniously a few times to finish pumping the goo down their throat. Then he withdraws."
    "He leaves them on their knees in the nasty old underpass, spiky hair bent out of shape and black eyeliner running down their face."
    scene kitchen with wipeleft
    "When he gets home he isn't able to find Kayden on the app again."
    p "Weird, they must have blocked me ..."
    jump nav_menu