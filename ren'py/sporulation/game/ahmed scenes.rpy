label ahmed_1:
    $ made_ahmed_smile = False
    $ bullied_ahmed = False
    # needs coffeeshop bg
    show ahmed at midleft
    "They meet Ahmed a month later to the day."
    "He's short, almost as short as Parvez, with a scraggly little beard."
    "His hair stands out at odd angles, kinky in places and lanky in others."
    "He looks rumpled, but it's kind of cute. Like a mad scientist or a writer who scarcely gets up from his desk."
    show parvez n terry at midright
    "Terry pushes Parvez when they walk into the coffee shop."
    t "See? I told you he'd be cute!"
    "Ahmed half-stands when they get to the table, shakes both their hands awkwardly."
    a "Hey, I'm, um, well, you know, I guess."
    menu:
        "try to make him smile":
            $ made_ahmed_smile = True
            "Something about this dude is really endearing."
            "He's so awkward and shy, but it's charming."
            "Parvez wants to cheer him up, to make him laugh, to see who Ahmed is underneath his quiet exterior."
            jump ahmed_conversation
        "bully him hehe":
            $ bullied_ahmed = True
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
        "Terry looks at him and raises an eyebrow. Ahmed flushes. This will be very easy."
    if made_ahmed_smile:
        "Ahmed has big hands and soft-fringed eyes. He seems sad."
    "He tells them how this is his first time on a date from the app."
    "He'd only just come out as trans to his parents a few months ago, after years of secretly taking testosterone."
    "He lives in a basement suite with three girls."
    if bullied_ahmed:
        "It's kind of pathetic. This guy is kind of pathetic. It's kinda hot though."
        "Parvez scoots his foot toward Ahmed's along the ground, nudging it."
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
    hide ahmed
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
    show ahmed at midleft
    "When Ahmed comes back from the bathroom, Terry tells him you have to go take care of something family related."
    "Ahmed seems a bit sad to hear this but not surprised."
    if bullied_ahmed:
        "It makes him seem even more pathetic."
    if made_ahmed_smile:
        "It makes you feel even more bad for him."
    "You all pay your bills and leave pretty quickly after that."
    jump nav_menu
label fuck_ahmed:
    scene cardboard
    # are we gonna be fancy and have a subway bg
    "Parvez and Terry ride the subway back to their apartment on either side of Ahmed,"
    if bullied_ahmed:
        "rubbing his thighs surreptitiously with the backs of their hands."
    if made_ahmed_smile:
        "resting their cheeks on his shoulders."
    "Ahmed is beet red, sweating in the cramped subway car."
    scene bed
    show ahmed at midleft
    show parvez n terry at midright
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
    p "Are you s--"
    a "{nw}I said 'fuck me'"
    "Parvez groans. He lines himself up and eases into Ahmed's pussy."
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
    hide ahmed
    "When Parvez and Terry wake up, Ahmed is gone."
    "A week later, Ahmed texts Terry a picture of his pussy. 'It's growing.'"
    "Sure enough, in the center of his purple-brown labia, there is a pearl of green."
    jump nav_menu