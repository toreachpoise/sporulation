label ahmed_1:
    scene coffeeshop1
    show ahmed at midleft with dissolve
    play music friendcore if_changed
    "They meet Ahmed during Parvez's monthly cycle of getting a little bulb at the end of his dick."
    "Ahmed was very particular that they get the timing right, asking them multiple times to make sure it was exactly a month after the last time."
    "He's short, almost as short as Parvez, with a scraggly little beard."
    "His hair stands out at odd angles, kinky in places and lanky in others."
    "He looks rumpled, but it's kind of cute. Like a mad scientist or a writer who scarcely gets up from his desk."
    show parvez n terry at right with moveinright
    "Terry pushes Parvez when they walk into the coffee shop."
    t "See? I told you he'd be cute!"
    "Ahmed half-stands when they get to the table, shakes both their hands awkwardly."
    show ahmed speaking with dissolve
    a "Hey, I'm, um, well, you know, I guess."
    menu:
        "try to make him smile":
            $ made_ahmed_smile = True
            $ bullied_ahmed = False #redundant but needed for testing lol
            "Something about this dude is really endearing."
            "He's so awkward and shy, but it's charming."
            "Parvez wants to cheer him up, to make him laugh, to see who Ahmed is underneath his quiet exterior."
            jump ahmed_conversation
        "bully him hehe":
            $ bullied_ahmed = True
            $ made_ahmed_smile = False
            "Something about this dude makes Parvez want to bother him."
            "Not in a mean way, he's just. Tightly held. Restrained."
            "It's more than just shyness, he's uptight. Protected."
            "Even though it's September and still pretty hot, Ahmed is wearing so many layers."
            "Parvez wonders what he looks like underneath all that."
            "He hopes Ahmed is hairy."
            "He wonders what Ahmed would look like, naked, squirming on his cock."
            "Parvez resolves to tease Ahmed, to see how easily he can get him flustered."
            jump ahmed_conversation
label ahmed_conversation:
    "He's an office worker, engineering of course."
    if bullied_ahmed:
        p "Does that mean you're good at erecting things?"
        show ahmed bottomy with dissolve
        "Terry looks at him and raises an eyebrow. Ahmed flushes. This will be very easy."
    if made_ahmed_smile:
        "Ahmed has big hands and soft-fringed eyes. He seems sad."
    show ahmed with dissolve
    "He tells them how this is his first time on a date from the app."
    "He'd only just come out as trans to his parents a few months ago, after years of secretly taking testosterone."
    "He lives in a basement suite with three girls."
    if bullied_ahmed:
        "It's kind of pathetic. This guy is kind of pathetic. It's kinda hot though."
        "Parvez scoots his foot toward Ahmed's along the ground, nudging it."
        show ahmed bottomy with dissolve
        "Ahmed moves his foot away."
        "Parvez maintains his pursuit, placing his foot direcly next to Ahmed's as soon as he puts it down."
        "Ahmed can't seem to focus on his conversation with Terry."
        "Parvez isn't really listening either. Something about siblings."
        "He can see that Ahmed is starting to sweat though. His foot presses back against Parvez's though. Interesting."
    if made_ahmed_smile:
        "Parvez feels sorry for Ahmed. It sounds like he's had a hard life."
        "It's odd cuz from Parvez's perspective, Ahmed looks like he would be having a good time."
        "He passes seemingly effortlessly. He just seems like a normal, nice, kind of nerdy guy."
        "If Parvez looked like Ahmed, his life would be so much easier."
        "But his sadness is kind of humanizing. It makes Parvez really like him."
        "Ahmed is a bit like a stray puppy. Parvez just wants to make him feel good."
    hide ahmed with moveoutleft
    "Ahmed excuses himself to go to the bathroom. Terry turns to face Parvez immediately."
    if bullied_ahmed:
        t "Dude, what are you up to?"
        p "He's just so ... bullyable. I just wanna bother him."
        "Terry laughs."
        t "So does that mean you like him?"
        menu:
            "nah he's kinda pathetic":
                t "Damn, okay, if you say so. It's up to you I guess."
                jump no_ahmed_fuck
            "yeah it's fun to wind him up":
                jump fuck_ahmed
    if made_ahmed_smile:
        t "So, what do you think?"
        p "He's sweet. I kind of feel bad for him, but in a good way?"
        p "... I want to make him feel nice."
        t "Damn, are you going soft on me babe? That's kinda unlike you."
        t "So, should we go home with him?"
        menu:
            "yeah":
                jump fuck_ahmed
            "I don't know, I'm nervous":
                t "What are you nervous about?"
                p "Just, like, ..."
                p "Just, like, what if my cock doesn't work? Or he gets freaked out?? What if he thinks it's gross??"
                "Terry laughs."
                t "That's how pretty much everyone feels before a hookup. It means you like him."
                t "So should we do it?"
                menu:
                    "yeah":
                        jump fuck_ahmed
                    "no, I don't really want to":
                        "Terry takes your hand under the table and squeezes it."
                        t "Okay baby. Say no more. I'll still suck your weird cock tonight."
                        jump no_ahmed_fuck
label no_ahmed_fuck:
    show ahmed at midleft with moveinleft
    "When Ahmed comes back from the bathroom, Terry tells him you have to go take care of something family related."
    "Ahmed seems a bit sad to hear this but not surprised."
    if bullied_ahmed:
        "It makes him seem even more pathetic."
    if made_ahmed_smile:
        "It makes you feel even more bad for him."
    "You all pay your bills and leave pretty quickly after that."
    scene cardboard with fade
    call screen chapterselect
label fuck_ahmed:
    scene black with dissolve
    play music maintheme
    # are we gonna be fancy and have a subway bg (prolly not)
    "Parvez and Terry ride the subway back to their apartment on either side of Ahmed,"
    if bullied_ahmed:
        "rubbing his thighs surreptitiously with the backs of their hands."
    if made_ahmed_smile:
        "resting their cheeks on his shoulders."
    "Ahmed is beet red, sweating in the cramped subway car."
    scene bed
    show ahmed bottomy at midleft
    show parvez n terry at right
    with dissolve
    "In the bedroom he doesn't want to take his shirt off."
    "He had walked in, taken his pants off, sat down on the bed, and then waited in awkward silence."
    p "Are you sure you want to do this?"
    a "Yes."
    "Parvez kisses Ahmed, then trails off to kiss his neck as Terry takes over kissing his mouth."
    "Together, they smooth their hands along Ahmed's arms, up from his ankles toward his knees."
    "Ahmed sighs. Parvez starts kissing him as Terry goes down on Parvez."
    if bullied_ahmed:
        "Parvez bites Ahmed's lip, winning a sharp squeak."
        "It just makes him want to bite him more, so he starts sucking on Ahmed's neck, nibbling it."
        a "W-wait, don't leave hickeys."
        "Parvez stops and looks at him."
        menu:
            "be pushy with him":
                p "Are you sure?"
                a "N-no, you can do it."
                "Parvez sinks his teeth into the loose skin at the base of Ahmed's neck."
                a "Ahh !"
                "Parvez grabs him by the shoulders to hold him in place and perfect the hickey."
                "Ahmed squirms but doesn't try to get away."
            "leave it be":
                pass
    if made_ahmed_smile:
        "Parvez cups Ahmed's face and kisses him."
        "He draws back to look into his eyes."
        p "Damn, you are so cute."
        "Ahmed seems the most embarrassed and turned on by this. It's really adorable."
    "As Parvez gets hard, he notices that Ahmed is staring."
    "Parvez moans."
    a "Can you ... feel that?"
    p "Yeah."
    "Ahmed moans and reaches for Parvez."
    scene cg A1A with dissolve
    pause
    "With his eyes fixed on Parvez's cock, he starts rubbing him, stroking up and down. Parvez moans again."
    a "H-how?"
    p "We'd like to try it with you, if you're still into that?"
    "Ahmed screws his eyes up and nods."
    a "I've never had anything inside my vagina before."
    "Terry rubs Ahmed's shoulder."
    t "We'll make it feel good for you, baby."
    "Ahmed nods again."
    if made_ahmed_smile:
        label nicer_ahmed_scene:
        "Terry moves down to nuzzle Ahmed's clit."
        t "Your bush is so soft!"
        "Parvez turns Ahmed's face toward him again, kissing him deeply."
        "Ahmed is a nervous kisser but his lips are soft. His hand is still resting on Parvez's cock."
        p "You can stroke it a little, if you want."
        "Ahmed complies, looking a bit stunned down at Parvez's cock and Terry's head bobbing between his legs."
        "He's trying to be quiet, face scrunched together with effort."
        t "Hey, Parvez, do you want a taste down here?"
        menu:
            "yeah":
                scene cg A1B with dissolve
                pause
                "Parvez gets on the ground standing between Ahmed's legs."
                "Terry reaches around and taps Ahmed's knee."
                t "Here, move back a bit."
                "Ahmed climbs fully onto the bed, with Parvez kneeling on all fours in front of him."
                "He parts Ahmed's labia with his hands, drawing a little sigh before jumping in."
                "He licks and sucks at Ahmed."
                "Behind him, Parvez can feel Terry lining themself up with his ass."
                "He moans against Ahmed's pussy as Terry slides in."
                "Once Ahmed is sloppily wet, Parvez brings his finger to begin circling his opening."
                "He isn't putting it in, just stroking around the outside in time with his mouth and Terry's pounding."
                jump keep_fucking_ahmed
            "no thanks":
                t "Fair enough, you don't gotta ask me twice to eat pussy."
                "Terry dives back into Ahmed's bush with relish."
                jump keep_fucking_ahmed
    if bullied_ahmed:
        p "I bet you've always wanted it, though."
        "Ahmed goes dead still and colors further. Parvez leans in to whisper in his ear."
        p "I bet you've touched yourself thinking about it. How it would feel to get your insides messed up by a big cock."
        "Parvez makes Ahmed kneel on the floor in front of Terry and gets down beside him."
        "Terry takes their cock out of their pants. Ahmed stares at it."
        p "I bet you've never sucked a cock before either."
        "Ahmed shakes his head, apparently unable to speak."
        p "Do you want to?"
        "Ahmed nods."
        p "Well then what are you waiting for?"
        "Parvez grabs a fistful of Ahmed's hair and shoves his head down onto Terry's cock."
        "Then he reaches around to feel Ahmed's pussy from behind. It's soaking wet."
        "Parvez sticks a finger in right away, making Ahmed moan and choke on Terry's cock."
        "Parvez leans to whisper in Ahmed's ear:"
        p "Is this too much?"
        menu:
            "y-yeah, sorry":
                p "Don't be sorry babe, it's okay."
                "Terry reaches down to raise Ahmed back up, kissing him gently."
                "They guide Ahmed to the bed, as Parvez sits beside him and Terry takes his place on his knees."
                $ made_ahmed_smile = True
                $ bullied_ahmed = False
                jump nicer_ahmed_scene
            "no, I like it":
                p "Yeah? You like being made to suck the cock of someone you just met?"
                "Terry puts their hand on Ahmed's head and starts forcing it down. Ahmed chokes but doesn't try to get away."
                p "You just sit there in your office, pretending to be a boring normal straight guy, dreaming about choking on cocks?"
                "Ahmed moans louder than he has yet as Parvez shoves a second finger inside him."
                "Ahmed keeps grinding down on Parvez's fingers, slobbering on Terry's cock, Parvez rubbing his against Ahmed's ass."
                jump keep_fucking_ahmed
label keep_fucking_ahmed:
    "Finally, Ahmed can't take it any more."
    a "Fuck me."
    p "Are you s--{nw}"
    a "I said 'fuck me'"
    "Parvez groans. He lines himself up and eases into Ahmed's pussy."
    scene cg A1C with dissolve
    pause
    "Terry takes their place behind Parvez, pressing into his ass."
    p "Is that okay?"
    a "Yeah. More."
    "Inside, Ahmed's pussy feels hot and slick."
    "It's less tight than Terry's ass had been, wetter."
    "Riding back against Terry and into Ahmed, Parvez feels almost overwhelmed."
    "He's buffeted by waves of heat and pleasure. His whole body feels hot and sweaty and alien to him somehow."
    "He is ecstatic: both out of body and in it."
    "Suddenly Ahmed screams and Parvez realizes he's shooting inside Ahmed."
    "Ahmed cums too, arching up against him. Terry follows close behind."
    "They lay in a sticky pile for a few seconds until Ahmed asks if he could take a shower."
    "Terry points him to the bathroom."
    "Parvez is half asleep already. His belly is covered in sticky seed goo and the bulb on his dick is deflated."
    scene bed with fade
    "When Parvez and Terry wake up, Ahmed is gone."
    "A week later, Ahmed texts Terry a picture of his pussy. 'It's growing.'"
    "Sure enough, in the center of his purple-brown labia, there is a pearl of green."
    $ ahmed_1_complete = True
    scene cardboard with fade
    call screen chapterselect

label ahmed_2:
    play music friendcore if_changed
    "Parvez arrives at Ahmed's place a bit sweaty."
    "It's a hot day and there were too many people on the street car, he feels sticky with all of their presences."
    "Ahmed had texted him a few days before, after not messaging at all in the couple of months that had passed since they had hooked up."
    "Parvez was honestly not expecting to hear from him again at all."
    "But Ahmed had messaged, out of the blue, with a picture of him holding a little potted plant."
    mm "grew this cutie from my own seeds"
    mm "wanna come over so i can harvest some more from u  :p"
    "So there he is, sticky and gross at Ahmed's doorstep, not exactly a great way to show up to a hookup."
    scene ahmedshelves
    show ahmed speaking at center
    with hpunch
    "Ahmed opens the door before Parvez has a chance to knock."
    p "(He must have been waiting behind the door ...)"
    "He seems really excited, much more so than Parvez had seen in their first encounter."
    a "Hi!!"
    "He bustles Parvez in without stopping to ask how he is or explaining why he hadn't messaged for so long,{nw}"
    show ahmed flip speaking at right
    show parvez flip at midright
    with move
    "He bustles Parvez in without stopping to ask how he is or explaining why he hadn't messaged for so long,{fast} showing him the corner of his tiny apartment near the only large window, positively bursting with plants."
    a "So, last month after the weird bulb thingy happened to me I saved some of the seeds, and I tried sprouting them, and look!!"
    show ahmed flip speaking:
        xalign 0.9
    with hpunch
    "Ahmed brandishes a plant at Parvez, way too close to his face."
    "It's a tiny succulent, little more than a green bead on top of the soil."
    p "What is{nw}"
    a "It's the same plant as the one you found in the woods! Pretty amazing, right?"
    p "But how did you ..."
    a "The cum is seeds! I already kind of thought it was when you did it inside me, but then when I got some of my own ..."
    show ahmed flip bottomy with dissolve
    show ahmed flip speaking with dissolve
    a "... I tried sprouting them and they totally grew!"
    a "I figured based on the location you described finding them in that it was some kind of peat bog, probably acidic and somewhat poor soil."
    a "I still tried a couple of other kinds, a free draining cactus soil was my second idea because of how succulenty the plant is, but it liked the acidic soil better."
    p "Wow you're ...{nw}"
    if bullied_ahmed:
        play music maintheme
        p "Wow you're ...{fast} such a fucking nerd."
        show ahmed flip with dissolve
        a "H...hey ..."
        show parvez flip toppy:
            xalign 0.72
        with move
        p "I mean, it's kind of cute."
        p "You're such a little weirdo, you hardly talk at all at first, and then you're so obsessed with my cum."
        show ahmed flip bottomy:
            xalign 0.85
        with dissolve
        a "Ah, I ..."
        show parvez flip toppy:
            xalign 0.75
        p "That's what you want, right? More of my cum."
        a "W... well, yeah..."
        p "Then go ahead and help me make some, you little freak."
        show ahmed flip bottomy:
            yalign 2.0
        with hpunch
        "Parvez grabs Ahmed by the shoulders and shoves him to his knees."
        a "Wah!"
        "Parvez unbuckles his pants and takes his sweaty dick out, poking Ahmed in the cheek with it."
        a "Ew, it's all sweaty."
        p "Yeah, well, you asked for it."
        "He pushes it against Ahmed's lips."
        menu:
            "Ahmed ..."
            "opens his mouth":
                jump ahmed_2_rough_scene
            "refuses":
                show ahmed flip overwhelmed with dissolve
                a "No! You have to wash it, it's gross."
                p "Damn, you're right, I was kind of being a dick."
                show ahmed flip speaking with dissolve
                "Ahmed smiles kind of mischieviously, his tongue poking out the corner of his mouth."
                a "Plus, y'know, I need a sterile sample."
                "Parvez rolls his eyes at him."
                p "You're such a dork."
                jump ahmed_2_nicer_scene
        label ahmed_2_rough_scene:
            scene cg A2A with dissolve
            pause
            "Parvez shoves his dick down Ahmed's throat, making him release a strangled 'weghgh!'"
            "Ahmed's choking a bit, his eyes start to well up with tears, but he doesn't push Parvez away."
            "His fingers are clenched into Parvez's ass, pulling him in fervently even as he gags."
            "Parvez fists his hands in Ahmed's hair, pressing his head further down onto him."
            p "You like being made to suck my nasty cock?"
            "Parvez feels rather than hears Ahmed's assent, the vibrations passing through the tip of his nose where it's pressed against Parvez's pubic bone."
            "Parvez punctuates his words by shoving his cock against the opening at the top of Ahmed's throat."
            p "Ugh, look at you, fuckin choking on this dick I didn't even wash this morning."
            "Ahmed moans, slurping on Parvez's cock messily."
            p "You're such a nasty little bitch."
            p "What a cock hungry slut you are."
            "Ahmed groans around Parvez's cock, gagging and spluttering."
            "He's fully crying and snot is running down his face onto Parvez's cock."
            "He seems totally unbothered by this, delighting in sucking down his own fluids and Parvez's dirty dick."
            "Ahmed pulls back for a second, a string of spit and snot and precum connecting him to Parvez."
            "He leans his head down to lick Parvez's labia, nuzzling his nose in the sweaty hair and inhaling deeply."
            a "Mmmmmm..."
            "Parvez grabs Ahmed's hair and shoves his mouth back onto his cock."
            "He fucks Ahmed's head roughly for a few minutes before pulling back to finish on his face."
            "Ahmed yelps and dives back down onto Parvez's cock, making sure to catch the precious seeds."
            jump ahmed_2_ending
    if made_ahmed_smile:
        show parvez flip happy with dissolve
        p "Wow you're ...{fast} so knowledgeable about this stuff. It's amazing!"
        show ahmed flip bottomy with dissolve
        a "Th-thanks!"
        "He gets flustered and then tries to refocus himself."
        show ahmed flip with dissolve
        a "Anyway um, since the sample needs to be sterile and all ... u hh ..."
        show ahmed flip bottomy with dissolve
        a "d-do you want to take a shower with me?"
        menu:
            "yeah":
                show parvez flip happy with dissolve
                p "That sounds really nice!"
                jump ahmed_2_nicer_scene
            "no thanks":
                p "Actually if you don't mind, I can just make the sample for you on my own."
                show ahmed flip with dissolve
                a "Oh ... um ... okay, yeah. The bathroom is over there ..."
                "He hands Parvez a clean jar and points to the only door in the apartment, kind of unnecessarily."
                scene black with pushleft
                "As Parvez looks around, he sees how crappy the place is."
                "It's just a run down little attic apartment. The sink in the bathroom is stained and kind of grimy."
                "Parvez steps into the shower and turns it on."
                "Ahmed hardly has any products, just a bottle of men's 5-in-1 soap, some shaving cream, and a bar of soap."
                "Parvez just rinses himself off, not really wanting to touch anything."
                "Afterwards he starts touching himself, trying to get hard."
                "He doesn't know what to think about."
                "He just feels kind of put off."
                "For some reason when Ahmed mentioned taking a shower it made him feel really self-conscious and gross."
                "Parvez scrunches his eyes closed and squeezes his dick, trying desperately to get hard so he can cum."
                "After a few minutes of him rubbing his dick raw under the water, Parvez gets uncomfortable and decides to just go."
                scene ahmedshelves
                show ahmed flip at center
                with wipeleft
                p "Sorry man, I'm just not into it today."
                "Ahmed looks disappointed."
                a "It's okay, you can just send me the sample later if you want I guess ..."
                scene black with dissolve
                "Parvez leaves, feeling sweaty and uncomfortable all over again."
                scene bed with pushleft
                "He takes a really hot shower when he gets home, feeling gross about himself."
                scene cg T2 with dissolve
                "Afterwards he asks Terry to help him collect the sample, which they're happy to do."
                "He drops the jar of cum off at Ahmed's place the next day, but he isn't home."
                scene cardboard with fade
                call screen chapterselect
        label ahmed_2_nicer_scene:
            play music maintheme if_changed
            $ made_ahmed_smile = True
            scene ahmedbed #actually needs shower bg lol
            show ahmed bottomy at left
            show parvez toppy at midleft
            with pushright
            "Ahmed leads Parvez into his bathroom."
            "It's definitely a bachelor's bathroom, with only some men's 5-in-1 soap and shaving supplies in the tub."
            "Ahmed starts stripping down facing away from Parvez, out of shyness or maybe locker room habit."
            "Parvez places a hand on his shoulder and Ahmed jumps."
            a "Ah!"
            p "Sorry, I just ... wanna see you, if that's okay."
            "Ahmed blushes even deeper but he turns to face Parvez."
            "He's taken his pants off but not his sweater or underwear. His chubby and slightly hairy legs are poking out of his boxers."
            "His shoulders are hunched forward, hiding his chest area."
            a "I've never ... taken my shirt off in front of anyone before."
            "Parvez takes his shirt off, showing Ahmed his small but pointy tits."
            p "Hey man, I get it. I haven't even had top surgery yet."
            show ahmed overwhelmed with dissolve
            "Ahmed scrunches up his face."
            a "Yeah, sorry, I should be grateful ... I just--{nw}"
            show parvez worried with dissolve
            p "That's not what I meant--"
            a "--I just still feel really uncomfortable."
            a "I don't like showing people my scars."
            "Parvez places his hands on Ahmed's shoulders."
            p "You don't have to show me if you don't want to."
            p "I can have a shower alone and we can continue this afterwards."
            a "N-no. {w}I want to."
            show ahmed bottomy with dissolve
            "He clenches his fists in the hem of his sweater, and pulls it and his button-down shirt off at the same time."
            "Forgetting that he's still wearing his glasses, he gets them all caught up in the fabric for a moment."
            "Parvez chuckles as Ahmed struggles to untangle himself, reaching to help him get his shirts off."
            a "Thanks haha."
            show parvez with dissolve
            p "Sure, buddy."
            "Parvez drops his shorts, and they stand in front of each other fully naked."
            "Ahmed's top surgery scars snake across the chest and join in the middle with a little dimple. Not like the scars most people show off that are a neat separated pair."
            "With clothes on his body is masculine looking enough, but naked he's unmistakeably dumpy, soft around the middle, kind of like Parvez is but moreso."
            "Ahmed seems to Parvez almost like a mirror, like a possible future version of himself."
            "At the same moment he thinks this he realizes that Ahmed is beautiful."
            show ahmed overwhelmed with dissolve
            a "What are you staring at?"
            show parvez toppy with dissolve
            p "Sorry, you're just ... really cute ..."
            show ahmed bottomy with dissolve
            "Ahmed gets into the shower, turns the water on, and gestures for Parvez to follow."
            "Parvez rushes in to kiss him, pushing Ahmed into the cold water."
            a "Ah!"
            show parvez bottomy with dissolve
            p "Sorry ... I just really wanted to kiss you."
            a "It's okay."
            "Ahmed kisses him back kind of hesitantly, mouth closed."
            "Parvez scrunches his hands in Ahmed's hair, pulling him closer and out of the cold water."
            "Ahmed relaxes into him, their wet bodies sliding together as Parvez eases his tongue into Ahmed's mouth."
            "Ahmed hums against his lips, making Parvez smile. They pass the moments together softly kissing until the water gets warm."
            a "Here, let me wash you."
            "He lathers the chemical-smelling soap onto a washcloth and gestures for Parvez to turn around."
            "He does so and closes his eyes."
            scene black with dissolve
            "Ahmed dilligently scrubs his back and his arms, lifting them gently and rubbing Parvez all over."
            "He turns Parvez around with a gentle tug on his shoulder and Parvez does so with his eyes still closed."
            "He loses himself for a moment in the sensation of the soft cloth scrubbing his chest and legs, before he feels Ahmed's warm breath on his cock."
            "Parvez's eyes snap open. Ahmed is on his knees in front of him, with his lips parted."
            scene cg A2A with dissolve
            pause
            p "Whoa."
            "Ahmed grins toothily."
            a "I think you're clean enough now."
            "He kisses Parvez's head, cautiously at first, the same way he had kissed his mouth."
            "Parvez places his hand on Ahmed's shoulder to steady himself, leaning back against the cold shower tile."
            "Ahmed's mouth is so warm as it closes around him, his tongue nubbly and almost prickly, overstimulating."
            p "Waugh!!"
            "Ahmed pulls back, a thread of spit connecting his lips to Parvez's cock."
            a "Is it okay?"
            p "Yeah."
            "Ahmed suckles him earnestly, using his hand to stimulate Parvez's shaft."
            "The water keeps washing the lubrication of Ahmed's saliva, heightening Parvez's sensation."
            p "Shit, it's so intense."
            "Ahmed groans and dives deeper, almost taking Parvez down to the base, before choking and lifting up slightly, bringing his hand back."
            "It doesn't take long for Parvez to cum, filling Ahmed's mouth."
            jump ahmed_2_ending
label ahmed_2_ending:
    scene cg A2B with dissolve
    pause
    "Ahmed opens his lips to reveal a mouthful of glistening goo."
    "The seeds are suspended in the gel like passionfruit, oozing out of Ahmed's mouth as he struggles to contain it."
    "He gets up in a hurry and rushes to spit them out into a little jar."
    p "That's not very sterile, you know."
    "Ahmed flushes."
    a "Sh-shut up, I know okay."
    "Parvez pulls Ahmed up to his feet, kissing him."
    p "I know, bud."
    scene ahmedshelves
    show ahmed flip bottomy at midright
    show parvez flip happy at midleft
    with fade
    "Before he goes, Ahmed presses a small plant into his hand. It looks like a tiny aloe vera plant, a little rosette of green fingers."
    a "This is one of mine ..."
    a "Maybe when you see it in your place ... it'll make you think of me ..."
    "Parvez grinned."
    show parvez flip toppy with dissolve
    p "I'll think of you alright."
    hide parvez with moveoutleft
    "Parvez leaves Ahmed's place with the taste of himself on his lips, green and clean and vegetal."
    "He feels refreshed as he rides the train back to his own place."
    $ ahmed_2_complete = True
    if inanna_sent_me == False:
        scene cardboard with fade
        call screen chapterselect
    else:
        $ obedience_points -= 5
        "Then a twinge of guilt passes through him."
        "Inanna had told him not to fuck anyone ... did oral count??"
        "How would she know anyway??"
        $ inanna_sent_me = False
        jump obedience_check_3


            