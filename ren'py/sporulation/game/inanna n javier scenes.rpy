label inanna_n_javier_1:
    scene kitchen
    show parvez at midleft
    with dissolve
    "Inanna and Parvez keep messaging lots after their first meetup."
    "She keeps inviting him to community events down at the camp but Parvez is too nervous to go."
    "Growing up, his parents always told him to keep his head down and try not to be noticed."
    "They really cared about being normal, seeming like regular Americans."
    "Obviously they couldn't help being brown, Parvez knew that. But maybe they thought that by making themselves smaller they would make it harder to notice and they'd blend in."
    "Parvez thought he wasn't like that, that being trans by definition made him stand out."
    "But Inanna's constant invitations to show up more, to do more were making him wonder if that was really true."
    "He stood out with the way he looked, with the way he dressed and presented himself, but it was in a way that didn't directly confront people."
    "He found it way more scary to actually do stuff, to be part of something."
    pdm "look i'm sorry i just ..."
    pdm "large groups of people make me nervous ..."
    pdm "... and strangers ..."
    pdm "and being around white people ..."
    lj "hahaha"
    lj "yeah there are a lot of white hippies at the camp"
    lj "there's lots of cool folks though, including some of them"
    lj "anyway do you wanna come over instead?"
    lj "javier is really excited to meet you!"
    pdm "oh! sure, i can probably do that"
    lj "and maybe if it's your time of the month xe can meat u too hehe"
    pdm "oh my god ..."
    menu:
        "actually i'd rather not":
            "Parvez feels nervous all of a sudden."
            pdm "i think i would wanna message them first before doing any stuff with them"
            "Inanna had sent him pictures of Javier and they seemed ... intimidatingly hot."
            "Their fierce glare and sharp makeup marked them to Parvez as one of those queers that was too cool for him."
            "They were a local drag performer and he had seen clips of them online and it was just ... he was just a loser by comparison."
            "The more he thought about meeting them, trying to flirt and be cool in front of them, the more a knot formed in Parvez's stomach."
            "He felt himself breaking out in a cold sweat."
            lj "sure i can give you their contact info if you wanna chat first"
            pdm "in the meantime can we just ... do stuff alone for now ?"
            lj "sure baby"
            # if havent completed inanna 2 jumps to inanna 2, otherwise jsut skips
            call screen chapterselect
        "let's do it":
            pass
    "Parvez grins alone at his kitchen table."
    pdm "sure, I got a veggie roll i can give xem"
    lj "cringe, man"
    lj "seeya for dinner tomorrow"
    scene balcony with Fade(0.5, 1.0, 0.5)
    show inanna n javier at midright
    show parvez at midleft
    "Terry made Parvez take a bottle of fancy kombucha they had been saving to Inanna's house."
    "It turns out this was the right choice. Inanna and Javier had laid out a whole table of dumplings, steam buns, scallion pancakes, and garlicky greens."
    "The steamer basket is five tiers tall, all with homemade dumplings."
    j "One of Inanna's ''community building activities'' is to invite tons of people over to make potstickers and take them home."
    i "We call it pinching dumps!!"
    "Javier rolls xer eyes but xe's smiling."
    "Parvez had been kind of intimidated by meeting Javier before this. Xe is a local drag performer, Parvez had seen xer pictures online."
    "Xer makeup is always immaculate in pictures, as it somehow still is now, even though they cooked this dinner for him."
    "But in person the sharpness of xer eyeliner is offset by xer small stature and grumpy cat energy."
    j "Only fae calls it pinching dumps."
    "Inanna pushes xem playfully."
    i "You do too!! Don't try and be all cool about it now."
    "Javier scrunches xer face. Parvez wonders if xe's blushing under xer makeup."
    "Parvez is actually able to chat with them easily over dinner, feeling way less nervous."
    "He had been kinda worried about interacting with a couple on their own turf."
    # if ahmed 1 completed
    "He realizes with a pang that this is probably how Ahmed had felt meeting him and Terry. {w}Maybe that's why he was so awkward, and why he left so suddenly."
    "After they're done eating and the dishes are loaded into the dishwasher, Inanna announces they're going to play a game and rushes out of the room."
    hide inanna n javier
    show javier happy at midright
    with dissolve
    j "Jesus christ. She always does this and she thinks she's so smooth."
    "Inanna yells from the other room."
    i "Hey!! I heard that!"
    "Javier laughs. Xer genuine smile is really cute."
    i "Why don't y'all come in here."
    j "Okay mami jeez."
    "Javier clearly meant the nickname as a joke, but the mention of it sends a thrill of arousal through Parvez. Oh right. They were gonna do it."
    "This realization made him nervous all over again."
    "Javier turned to look at him in the door, shooting him a real smile."
    j "You coming?"
    scene couch
    show parvez at left
    show inanna at right
    show javier at center
    with pushleft
    "Inanna had set out a board game on the coffee table."
    "The game seemed old, the graphic design was kind of retro and the box was dirty."
    "There were many piles of cards stacked around the box, with the board itself still folded inside."
    i "We don't have to play the actual game, it's kinda old and weird."
    i "But the questions are pretty fun."
    "Javier leaned in to whisper in Parvez's ear."
    j "She just uses this as a way to segue into fucking, it's kinda unnecessary."
    i "Don't be giving away all my secrets!"
    $ panicked = False
    menu:
        "wait, actually, i think this is too much for me":
            $ panicked = True
            "Parvez feels panic well up inside him at the sight of Inanna and Javier sitting on the couch, both looking at him intently."
            p "Wait, I just. I need."
            "He's struggling to breathe. They're both really hot and they're both looking at him and why won't they stop LOOKING AT HIM."
            "He's not hot enough for them to fuck. They're both so cool and brave and talented. And he's just a loser, a fuckup."
            "Maybe this is some kind of joke, some kind of prank."
            "Maybe they're filming this and they're going to expose him as a fake not good enough queer."
            "And his family and all the people he grew up with will see it. And they'll know he's not only a freak but not even a cool freak, a brave freak."
            "He realizes dimly that he's hyperventilating. The room is kind of swimming, too."
            scene spiral:
                zoom 3.0
                yalign 0.5
            show inanna happy:
                zoom 2.0
            with fade
            "Inanna comes over and puts her hand on his shoulder."
            i "Are you okay hon? What's wrong?"
            p "I just, it's just. I just."
            i "Shh, baby, just breathe."
            "Parvez can't, he's trying but he can't and it makes him even more freaked out."
            i "Wait, it's okay. Look at me."
            "He meets her eyes, still feeling like he's choking."
            i "Shh, it's okay."
            "Her gaze is strong, her eyes honey-brown and warm. She's looking right at him. It's almost too much to keep looking at her, but Parvez forces himself to keep doing it."
            i "Good boy, focus on me."
            i "Just listen to my voice, okay?"
            i "You're here. You're safe. We're here with you."
            i "You don't have to do anything you don't want to do. We can just hang out."
            i "Just keep your eyes on me."
            i "Good job baby."
            i "Now, keeping your focus on me, count down from 100."
            "Parvez starts counting in his head."
            i "Out loud."
            p "100, 99, 98 ..."
            i "Good boy."
            p "... 91, 90, 89 ..."
            i "As you count down feel how your breath is already getting deeper and deeper."
            "Parvez realizes he's not hyperventilating anymore"
            i "Keep counting, son."
            p "S-sorry, um ... 80, 79, 78 ..."
            i "Good boy."
            "Parvez feels himself flushing but he doesn't feel embarrassed, he feels ... good."
            p "... 66, 65, 64, 63, 62 ..."
            i "Feel yourself settling into your body as you count down and breathe slower and slower."
            i "Feel how good and comfortable you feel."
            p "... 54, 53, 52, 51 ..."
            i "You're warm, you're safe, you're full of food."
            "Her hand is warm on Parvez's shoulder."
            i "You're gonna be okay ..."
            "Parvez keeps counting with slow shuddering breaths, all the way down to 1."
            scene couch
            show parvez at midleft
            show inanna:
                zoom 1.0
                xalign 0.1
                ypos 300
            show javier at midright
            with fade
            "He blinks his eyes open to find himself back in Inanna and Javier's living room."
            "Javier is sitting next to him on the couch, and Inanna is kneeling beside him on the floor."
            j "You okay, man?"
            p "Y-yeah, sorry."
            i "Ain't no sorry, panic attacks are no joke."
            show inanna at left
            with move
            "She gets up and her knees crack loudly."
            i "But my old lady ass can't be squatting on the floor any more."
            show inanna happy at right
            with move
            "She gets up and sits back down on the couch. Parvez misses her warm presence beside him right away."
            hide javier with moveoutleft
            "Javier goes and gets Parvez a glass of water, and then comes and sits beside him again."
            show javier at left
            with moveinleft
            show parvez at center
            with move
            "Xe pushes xer leg against his gently."
            j "So, what do you want to do?"
            menu:
                "play a board game":
                    p "Can we play the board game but uh, not do anything sexual?"
                    j "Yeah man, of course."
                    jump chaste_boardgame
                "get hypno'd and fuck":
                    jump hypno
                "go home":
                    show parvez worried with dissolve
                    p "Sorry I just kinda feel like a loser right now."
                    p "That was really uncool of me and now I really want to lie down."
                    p "I'm sorry for ruining the night."
                    "Inanna puts her hand on his leg."
                    i "It's okay babe, you didn't ruin anything."
                    i "I'm sorry you got freaked out."
                    "Parvez rises to his feet awkwardly and makes his exit."
                    call screen chapterselect
        "how do you use a retro board game to fuck??":
            jump horny_boardgame
label chaste_boardgame:
    "Inanna takes out the board and starts laying out the game pieces."
    "It's a weird get to know you game from the 80s that they had found in a thrift store."
    "It asks you questions about morality, pop culture, and relationships. They're all kind of awkward and outdated."
    j "''If you were on a third date with a woman, expecting to go home with her, and she revealed to you that in her past she lived as a man, what would you do?''{nw}"
    i "Suck her cock under the table right then and there."
    show javier happy with dissolve
    j "Goddamn it Inanna that's not one of the options."
    i "Yeah, but it should be!"
    show parvez happy with dissolve
    p "It really should."
    "Parvez finds himself enjoying their company and relaxing."
    "They're both goofy and weird, he's not sure why he was intimidated by them at first."
    "He had already known Inanna was like that, why would Javier have been any different."
    "They make their way around the board answering uncomfortable 80s questions about Nancy Reagan's head giving skills and marital cheating drama."
    i "Hell yeah I would watch the video of her sucking it if there was one--"
    j "--why couldn't they form a polycule instead?"
    p "I guess if I was a failing professional athlete supporting my dying wife I would have no choice but to take steroids."
    "Javier kicks both of their asses, though Parvez was still not exactly sure how points were scored. It was partly based on them correctly guessing one another's responses, but there was also a spinning wheel involved."
    "Halfway through Parvez had gotten all the way back to the start, and from that point on he was struggling to catch up."
    j "You bitches didn't stand a chance."
    i "Yeah, yeah, good game."
    "She turns to look at Parvez."
    i "So ..."
    show inanna toppy with dissolve
    i "You seemed pretty nervous earlier, but we do really like you."
    i "Would you want to try this technique to relax you so we can have a little fun?"
    show parvez worried with dissolve
    p "Uhh ... it's not like drugs or anything is it?"
    i "No, it's a psychological trick, kind of like meditation{nw}"
    j "Bro she's gonna brainwash you.{w} But go with it, it's hot."
    "Parvez feels himself flush."
    menu:
        "uhh ... that sounds ..."
        "hot":
            show parvez toppy with dissolve
            p "What would it involve exactly?"
            if panicked:
                i "It's kind of like what we did earlier. I would just talk to you and make you feel calm and warm. But in a sexy way."
            else:
                i "Basically it's a guided meditation, so I'll make you feel in tune with your body and warm, and suggestible."
                j "... and then fuck you."
            p "Th-that sounds really fun."
            i "Good boy, that's what I wanted to hear."
            jump hypno
        "scary":
            p "Sorry, I had a great time but that sounds like a bit too much for me."
            "Inanna smacks Javier's shoulder lightly."
            i "See? You didn't have to say I was gonna brainwash him!"
            j "Hey man don't worry, we don't gotta do anything."
            p "Okay, um. I'm gonna go. But I enjoyed myself."
            j "Me too dude. It was nice to meet you."
            j "Maybe we can hang out together another time?"
            menu:
                "y... yeah...":
                    pass
                "I'd like that":
                    pass
            j "Okay, bye bro."
            call screen chapterselect
label horny_boardgame:
    "Javier rolls xer eyes."
    j "You'll see."
    "It's a weird get to know you game from the 80s that they had found in a thrift store."
    i "We don't have to play the actual game, just answer some of the questions."
    "It asks you questions about morality, pop culture, and relationships. They're all kind of awkward and outdated."
    j "''If you were on a third date with a woman, expecting to go home with her, and she revealed to you that in her past she lived as a man, what would you do?''{nw}"
    i "Suck her cock under the table right then and there."
    show javier happy with dissolve
    j "Goddamn it Inanna that's not one of the options."
    i "Yeah, but it should be!"
    show parvez happy with dissolve
    p "It really should."
    "Parvez finds himself enjoying their company and relaxing."
    "They're both goofy and weird, he's not sure why he was intimidated by them at first."
    "He had already known Inanna was like that, why would Javier have been any different."
    "Inanna picks up a card and reads it."
    i "If you met a really hot woman, and she wanted you to give up your free will and surrender to her infinite and loving power, would you: a) do it immediately like a good boy, b) question her authority, c) refuse outright, or d) try to dominate her instead?{nw}"
    j "Jesus fucking christ Inanna you couldn't even wait till the second round this time?"
    p "Should I be offended that this is apparently a recurring move of hers?"
    j "It's just cuz she's an old lady with no rizz."
    i "How dare you! This is my rizz, it's just awkward and direct. It works great on twinky little hoes like you."
    "Javier sighs."
    j "Yeah, I guess it did."
    i "Good kitten, now kneel down next to mommy."
    show javier happy:
            xalign 1.2
            ypos 700
    "Javier gets to xer knees beside Inanna. Inanna pats xer head"
    i "Good kitty."
    "Javier's expression is serene. Xe looks both incredibly happy and only half there."
    i "You like being mommy's little kitten don't you."
    "Javier's voice is soft and faraway."
    j "Yes mommy."
    i "Louder."
    j "Yes mommy."
    i "Good kitty."
    "Parvez watches them, transfixed. Javier doen't seem embarrassed at all by being made to kneel in front of him, or to address Inanna as mommy, or be called a kitten."
    "Xe seems to love it. Xe rubs xer head against Inanna's leg like a cat."
    "Inanna turns her gaze on Parvez."
    i "So, answer the question."
    p "Uhh, what were my options?"
    menu:
        "Inanna's eyes bore into Parvez as she pretends to read the card again."
        "a) surrender immediately like a good boy":
            p "umm ... A?"
            label surrender:
                i "Look me in the eyes and tell me what you want me to do to you."
                show parvez bottomy with dissolve
                "Parvez struggles to meet her gaze."
                p "I ... ah ..."
                p "I want you to take control of me."
                i "Good boy."
                jump hypno
        "b) question her authority":
            p "What does that even mean, 'her infinite and loving power'?"
            p "Sounds kinda goofy to me. You can't really control my mind."
            "Inanna grins at him."
            i "Of course I can't really, I can just make you suggestible."
            "Fae looks at Javier."
            i "Kitty, strip."
            "Javier stands and drops their clothes before kneeling down between Inanna's legs."
            p "They just did that because you asked, because they wanted to."
            i "Of course. I can't make xer do anything xe doesn't really want, no one can do that without coercion."
            "Inanna places faer hand on Javier's head and xe nuzzles it."
            i "But what xe wants most right now is to obey me and be taken care of by me."
            i "Isn't that right pet?"
            j "Meow."
            "Inanna looks at Parvez again."
            i "So, do you want to try it?"
            menu:
                "y-yeah ...":
                    jump surrender
                "no":
                    jump refuse
        "c) refuse outright":
            label refuse:
                show parvez worried with dissolve
                p "Fuck no, sorry. That sounds corny as hell."
                p "I can't do embarrassing shit like pretend to be a cat."
                show javier worried
                show inanna worried
                with dissolve
                "Parvez gets up."
                p "This is too weird."
                i "W-wait, Parvez--{nw}"
                p "Nope sorry I gotta go."
                hide parvez with moveoutleft
                call screen chapterselect
        "d) try to dominate her instead":
            show parvez toppy with dissolve
            p "I bet she's not even that powerful."
            p "I bet she just hasn't met a man strong enough to take her over."
            "Inanna growls."
            i "Is that what you think you little twink?"
            show inanna:
                zoom 1.5
                yalign 0.0
            with zoomin
            "She stands up, looking down into Parvez's eyes."
            "Her gaze is intense, boring into him. Parvez makes himself stare back at her."
            "She holds his eyes for uncomfortably long."
            i "I keep hearing all this talk from you about how big of a man you are. How strong, how powerful."
            i "You ain't shit. You're just a scared little bitch."
            i "You just a little boy who thinks he's too big for his britches."
            scene spiral:
                zoom 3.0
                yalign 0.5
            show inanna toppy:
                zoom 2.0
            with dissolve
            i "Deep down inside you know you don't deserve to be in charge."
            i "You need a mommy to take care of you, to tell you what to do."
            i "You don't deserve to be in control of your life."
            i "You want to be taken over and used like a toy by a power that's way bigger than you are."
            i "You want to be held and treasured, a little object with no responsibilities."
            i "Don't you, slut?"
            menu:
                "y-yes mommy":
                    jump surrender
                "fuck no":
                    scene couch
                    show parvez worried at left
                    show inanna toppy at right
                    show javier happy:
                        xalign 1.2
                        ypos 300
                    with dissolve
                    "Parvez snaps out of it immediately."
                    "That was freaky, how the fuck did she do that?"
                    jump refuse
label hypno:
    i "Kneel in front of me."
    scene spiral:
        zoom 3.0
        yalign 0.5
    show inanna toppy:
        zoom 2.0
    with dissolve
    i "That's right. Now look into my eyes."
    i "Focus on just my voice."
    i "Breathe deeply."
    i "Deeper and deeper with every breath."
    i "Feel the sound of my words filling your entire body."
    i "Feel how warm you feel, how safe."
    i "How comfortable you are sitting there on your knees, beneath me."
    i "Look up at me and know that you're in your rightful place."
    p "Yes mommy ..."
    i "Good boy, but don't interrupt me again."
    i "Just listen and focus on me."
    i "Feel yourself being drawn toward me,{w} like your brain is being siphoned toward me by the sound of my voice."
    i "All your thoughts, all your ideas, all your worries, they're with me now."
    i "I'm holding them for you. You can have them back later if you want, but for now they're mine."
    i "Whenever I tell you you're my good boy you'll find your way back here, to the place where I'm holding all the grown up responsibilities and thoughts you have."
    i "Find yourself here where you're safe and all you have to do is obey."
    i "You want that, don't you boy?"
    p "Yes mommy."
    i "That's good."
    i "Focus all your attention on how much you want to please me and do what I say."
    i "It fills you with so much pleasure and joy to serve me, just like this kitty here."
    i "It might even be your life's purpose."
    "Parvez felt a doubt bubble up inside him, but it burst, drawn toward the silken sound of Inanna's voice."
    i "You don't need to be a person, you don't need to do anything or have any responsibilities."
    i "You just need to do what mommy says, isn't that right?"
    p "Yes mommy."
    i "Good boy, now open your eyes."
    "Parvez hadn't realized he had them closed, he had been so focused on Inanna's voice, her consciousness taking over his completely."
    #cg 1
    "He opens his eyes to see Javier kneeling between Inanna's legs, licking up and down her cock like a kitten."
    i "Well, aren't you going to join xem?"
    "Parvez hesitates for a moment."
    i "That's an order, boy."
    "He feels himself being drawn in."
    "Javier's hand cups his face and they kiss, Javier tonguing and licking all over his mouth. It's sloppy and messy but cute."
    "Even partway down, Parvez admires Javier's unselfconsciousness. He still has enough awareness to feel a bit embarrassed."
    "He wants to be like Javier, hollowed out by a benevolent force of love, made empty and perfectly able to receive."
    "He kisses Javier back harder, gaining a little yip from xem."
    "Inanna places her hands on their heads."
    i "Focus on me, pets."
    "Parvez directs himself back to the task at hand, kissing Inanna's shaft like Javier had before taking her down."
    i "Ahh, that's it. Good boy."
    "Her hand is firm on the back of his head, not pressing him down, but keeping him on her, not letting him up."
    i "Suck on mommy just like that."
    "Her cock is somewhat soft, still kind of floppy between their lips."
    "Parvez takes it all the way down and enjoys the sensation of sucking on the squishy tube of her. She moans in appreciation."
    i "Good boy, now let Javi have a turn."
    "Javier takes her all the way down in one slurp before pulling back up, licking at her head, and diving back down."
    "Inanna pushes xer head down, fucking into xer mouth."
    "Javier is clearly practiced at this, her cock making rhythmic gulping sounds at the back of xer throat."
    "Javier pulls back, drooling."
    j "Puahhhh."
    "Inanna pets xer cheek."
    i "Good kitty."
    "Xe licks her hand."
    p "Now it's your turn, boy."
    "Parvez places his mouth over her cock and waits for her hand to land on his head."
    "He slides his lips down, taking it about halfway. Even though she's soft, she's still pretty big."
    i "Good boy, now swallow."
    "He obliges and she takes the opportunity to shove her dick down past his gullet."
    "He chokes and tears well up in his eyes, but her hand keeps him down."
    i "Good boy, now breathe in when I pull out."
    "He gasps a breath in before she punches it back out again. He chokes again but less so, and she does it again."
    "By the third or fourth thrust he's breathing evenly with her rhythm as she fucks his throat."
    "Her soft cock feels strange pushing down his neck and pulling back out. He slurps it eagerly, her juices dripping down his throat and spilling out his lips."
    "Parvez is a mess, his face is covered in drool as she humps his face."
    "He surrenders to it, he loves it."
    "He's just a fucktube for her, just a collection of holes and body parts for her to use."
    "It feels good, easy. All he has to do is hold his throat open and breathe right."
    "Inanna thrusts a little too deep and Parvez gags, this time for real. She pulls him off her dick."
    i "Sorry babe."
    p "It's okay."
    i "I think we're ready to move on to the next step anyway."
    "Inanna gestures down and Parvez sees himself, fully clothed and rock hard, next to Javier, who is naked and fingering their wet pussy."
    i "It's time for you to plant your seeds inside this little kitty."
    scene inannabed
    show inanna toppy at left
    show parvez bottomy at midright
    show javier happy at midleft
    with wipeleft
    "Inanna leads them into the room and ordered Parvez to strip."
    i "Good boy, lay on the bed."
    i "Get on top of him kitty."
    show javier happy at center
    "Javier climbs onto Parvez and straddles him, their slick cunt just above his cock, dripping down onto him."
    i "You're such a little tease, pussy!"
    show inanna even more toppy at right
    with move
    "Inanna gets on the bed behind Javier, grabbing xem by the hips. She leans in to whisper in xer ear."
    i "Take him in all the way."
    #cg
    j "Nya! Ahhh"
    "Xer pussy is so wet, Parvez feels totally engulfed."
    "He wants to fuck up into xem but he knows he isn't supposed to do anything without being told."
    "She kisses xer neck."
    i "Good kitty. Lean forward."
    "Parvez sees Inanna doing something behind Javier."
    j "Wah!! Ahh!! Mommy!!"
    i "Shh kitty, be a good little pussy for mama."
    "She pulls her hand away from behind them and embraces Javier from behind."
    j "Ahh!!!"
    "Javier's cunt gets tighter as Parvez feels something fill their ass."
    p "Sh-it..."
    "Inanna snakes her legs forward to pin Parvez's arms, as if she knows he wants to grab Javier and stuff them."
    i "No, this is our little pussy's job, isn't it kitty?"
    j "Yes mommy."
    "Javier starts to ride up and down on their cocks, whimpering as xe does so like xe is being stretched to xer limit."
    "Every time xe moves up xe clenches and presses their dicks together inside xem before bearing back down."
    "It's incredible and all Parvez can do is ride the waves of sensation."
    i "Yes, good kitty, ride him, milk him for all he's worth."
    "Inanna is starting to get out of breath, too, radiant with sweat but still holding all the energy as she fucks Javier onto Parvez."
    "She is murmuring into the side of Javier's neck as xe gasps and yelps on top of them."
    "Xe clenches tighter and tighter as xe rides."
    "Parvez knew he wasn't going to last long but he's shocked by how fast he cums."
    p "Waugh!!"
    "He can't stop his hips bucking then, throwing Inanna's legs off him."
    "He digs deeper and deeper inside Javier, filling them up with his goo."
    "By the sound of it Inanna was right behind him."
    i "Good kitty, yes, ahh, ahh, ahhhhhh."
    "Javier collapses back onto Inanna as she pulls out of xem."
    "Seedy goo oozes out of their open pussy, their ass gaping slightly."
    "Inanna kisses xer neck."
    i "Good kitty."
    # end of cg
    "She reaches to grab Parvez's foot."
    i "You did a great job too, boy."
    "Parvez is full of a warm glow and couldn't speak."
    "He lays on their bed for a while before Inanna gets up."
    i "Want some hot chocolate and to finish the game?"
    "Javier groans."
    j "Jeez Inanna we just got our brains destroyed, have mercy."
    "She grins brightly."
    i "Nah, come on, you want to, don't you Parvez?"
    p "Yeah, alright."
    $ inanna_n_javier_1_complete = True
    call screen chapterselect

label inanna_n_javier_2:
    ## starting this sequence removes kayden 1 and locks the kayden storyline
    scene couch
    show parvez at right
    with dissolve
    "Parvez has decided to turn over a new leaf and become a person who goes out and does things in the world."
    "His experience with Javier and Inanna showed him that meeting people wasn't as scary as he previously thought."
    "And now he's starting to wonder if he could maybe start organizing things and making a community of his own."
    if met_kayden == True:
        "He doesn't really know where to start, but he can't stop thinking about that abandoned skatepark where he met Kayden."
        "He just felt really drawn back to the space."
        "Kayden said it was their secret place, but they seemed to have vanished, so it couldn't hurt to go there again, right?"
    else:
        "He found himself one night browsing the messageboard for #WeirdThingsYouSeeInBlinkwood and happened upon photos of this abandoned industrial skatepark."
        "It was on the outskirts of town. Based on the photos Parvez thought it looked like it was under the old highway."
        "It was so strange, though. Looking at the photos he could see the skate ramps covered in graffiti underneath the crumbling concrete of the underpass."
        "At the edges there were mats of greenery climbing over the cement, eroding the harsh lines and carpeting them."
    "The weird mixture of abandoned industrial architecture, graffiti, and overgrowth makes him feel strangely hopeful. Like a vision of a world after the capitalist hellhole it is now."
    "He doesn't know why but he wants to tell Inanna about it."
    pdm "hey you know how you were saying that like"
    pdm "the judys keep invading our spaces and we don't really have that many"
    pdm "there's this weird place in town im kinda obsessed with"
    pdm "this abandoned skatepark"
    pdm "and i can't get out of my head like"
    pdm "weird gay skatepark garden????"
    pdm "do u wanna come check it out w me??"
    lj "bro i have no idea what you're talking about"
    lj "but i'm game"
    lj "..."
    lj "can i bring javi??"
    pdm "yeah of course"
    lj "hell yea sounds gay, i'll pack a picnic"
    scene skatepark ramps
    show inanna at left
    show javier at midleft
    show parvez at right
    with fade
    "Inanna's idea of a small picnic turned out to be a massive feast."
    "They brought an actual picnic basket stuffed with summer rolls, a homegrown sprout salad, and herbal iced tea."
    j "Fae woke me up way too early to roll these today."
    "Parvez brought cookies, without having to be reminded by Terry this time, but he still felt his contribution was a little inadequate."
    p "Yeah, so ... this is the place ..."
    p "... Sorry, it was probably dumb and weird to bring you here, it's kinda grimy."
    i "No way babe!"
    j "It's actually kinda sick here."
    "Javier produces a fancy looking DSLR camera from xer bag and starts taking pictures."
    show javier at right
    show parvez at farleft
    with move
    j "I would love to do a photoshoot out here all dragged up."
    "Xe turns the monitor around and starts attempting to take a selfie with a tag that said HOMOS GO HOMo, the last letter having obviously been added by someone else at a later time."
    i "Babe, do you want me to take your picture?"
    "Javier looks embarrassed."
    j "Yes please ..."
    show inanna happy at center
    with move
    i "I knew you did"
    "Javier begins to pose in front of various bits of interesting graffiti, broken down concrete columns, and greenery."
    i "So, like, what were you thinking about for this place, Parvez?"
    p "I don't really know, honestly."
    p "I'm not good at like. Making space or organizing or whatever."
    p "I just saw that it was a cool empty place. That's about as far as I got."
    i "That's super fair, it is a cool place."
    "They are interrupted by Javier's stomach growling."
    j "Y'all, let's eat lunch."
    scene skatepark hill
    show parvez at center
    show inanna at farright
    show javier at right
    with wiperight
    "They climb up one of the skate ramps to an area that is covered in green vines."
    if plantasy:
        "Parvez realizes it's the same ramp he had hung out on waiting for Kayden."
    i "Babe did you remember to bring a picnic blanket?"
    j "Of course not you know I don't remember that kind of shit."
    "Inanna sighs."
    "She takes off her beautiful jacket and lays it on the ground, perching on top of the mess of vines."
    "Parvez does the same with his jacket, regretting that he didn't think to bring a blanket either."
    "Javier sits right down and kind of sinks into the greenery."
    if plantasy:
        "Parvez strokes the kudzu with his hand idly as he sits down. It's soft. He remembers his fantasy of being tangled up in it before returning his attention to Inanna and Javier."
    j "Time to eat!! Time to eat!!"
    i "Okay, okay, settle down cranky kitty."
    j "Nuuuuu, feed meeeeeeee"
    "Inanna hands xem a summer roll and xe immediately starts monching on it without realizing that there is plastic wrap on it."
    j "Blehhhhhhh"
    "Xe spits the plastic out onto the ground."
    i "Gross, babe."
    j "The plastic was yuckyyy"
    "Inanna shakes her head and laughs, handing Parvez a summer roll as well."
    p "Damn, these are really good."
    i "Thanks! It's my auntie's recipe."
    "Javier is already done eating, wiping xer hands on the kudzu vines."
    "Xe gets up."
    j "Time to explore !!"
    "Parvez isn't even halfway through his roll, and Inanna is in the midst of pouring herself some homegrown pansy tea."
    i "Why don't you go explore on your own kitty? We're not done here."
    j "Nyehhh"
    "Xe sticks xer tongue out at them and scampers off."
    hide javier with moveoutleft
    show inanna happy with dissolve
    i "Xe is cute but xe's kinda annoying sometimes."
    "Her expression betrays her affection for them. Parvez laughs."
    p "I mean, I admire the energy haha"
    p "Though if I ate that fast and then got up right away like that it would probably make my stomach hurt."
    i "It makes my stomach hurt just to watch xem sometimes."
    "Javier is only gone a couple of minutes before returning."
    show javier happy at right
    with moveinleft
    j "Yo!! You guys gotta come see this!!"
    scene skatepark interior
    show inanna at center
    show javier happy at midright
    show parvez at farleft
    with wipeleft
    "Xe leads them to an area of the skatepark that was fenced off with chain link. Beyond, there was a dilapidated playground set, complete with rusty slide and a swing set where one of the swings was missing altogether and another's chain was broken."
    i "And you brought us here because ... ?"
    "Javier is worming xer way through a gap in the fence."
    "Xe turns to look at them."
    j "This old playground is sick!!"
    j "Can you imagine throwing a party in here?"
    show javier happy at farright
    show inanna at midright
    with MoveTransition(3)
    i "Babe this place is grimy (derogatory). Stay away from the slide or you'll get tetanus or some shit."
    j "Oh whatever."
    "Xe laughs."
    j "I'm vaccinated."
    j "Come on picture it! We could have a runway and performances down here--"
    "Xe gestures down a long straightaway between the skate ramps and where they are standing."
    j "-- we can have a DJ booth on top of the slide, and hang lights from all the playground stuff. It would be so sick!!"
    "Xe turns to Parvez."
    j "Maybe it can be a fundraiser to turn this place into like, something actually cool."
    show parvez:
        xalign 1.2
    with move
    p "Yeah, I don't know what I was planning on but like ..."
    p "I just love the greenery here."
    p "It feels kind of post apocalyptic ...{w} but in a good way?"
    p "Like what if we had a garden here? What if it was just a gay and weird place to be with plants."
    "Javier waggled xer eyebrows."
    j "Yeah bro we know you love to be with plants."
    show parvez worried with dissolve
    p "That wasn't what I meant!"
    j "Suuuure man, whatever you say."
    show parvez
    show inanna happy
    with dissolve
    i "Okay but like, why not?"
    i "All of the queer spaces we have in town are either centered around substance use and transphobic cis gays ... or like super sanitised."
    i "The judys and their allies are all constantly accusing us of being too sexual in public but like, we don't actually have a place to do that."
    i "Especially a space that is safe and beautiful, right??"
    p "I don't know I mean that sounds kind of--{nw}"
    show judys n kayden at furthestleft
    with moveinleft
    j "Bro who the fuck is that."
    "Parvez turns around to see the two judys he and Inanna had encountered at the bookstore, as well as a third one."
    i "Oh fuck, it's the judys."
    show inanna frightened:
        xalign 1.0
    with move
    show parvez worried
    show javier worried
    with dissolve
    "The judys hadn't seen them yet. Parvez watched them for a minute."
    "They were all wearing the same outfit but in different colors, like a cursed magical girl team."
    "The tallest one, Marianne, was talking to the others, and even though they were far away her voice echoed toward them along the concrete walls."
    "Marianne" "... certainly a safety hazard. We should let the counselor know immediately."
    "Marianne" "It's on county land as well, so I'm sure he'll be more than willing to donate it to the new police training and sex offender treatment facility."
    "Marianne turns to the new judy, who is dressed in pink."
    "Marianne" "How did you say you found out about this place, Kayla?"
    if met_kayden:
        "With a horrible start, Parvez realizes that it's Kayden."
        "They're not wearing a binder, and their face is washed clean of makeup."
        "They've dyed their hair blond again, and without its spikes it hangs almost down to their shoulders."
    else:
        "There's something off about the new judy ..."
        "She stands stiffly, apart from the rest of the group."
        "When she answers Marianne her voice is gravelly, too deep."
    "Kaye" "It's just Kaye, not Kayla."
    "Marianne" "Nonsense dear, we agreed that you were reclaiming your birth name, as God and your parents intended."
    "Marianne" "You {i}do{/i} want do get better, don't you?"
    "Kaye" "Yes, ma'am."
    "Marianne" "Good girl."
    show judys n chud:
        xalign 0.0
    with move
    "They move toward Parvez and he sees that they have a monstrous looking man with them, at the same time that the man sees him."
    "The man points them out to Marianne and her gaze snaps to them."
    j "Shit, what do we do?"
    j "We can't fight a chud. And there are four of them."
    if met_kayden:
        p "I think I know one of them ..."
        i "What??"
        p "The pink one ... I ... they used to be trans. We hooked up."
        p "They're the one who told me about this place."
        i "They used to be trans?? Jeez."
    j "We gotta run."
    i "I mean, if we want to make something of this place, we have to be willing to defend it ..."
    i "... but I've never seen anyone fight a chud and win ..."
    menu:
        "fight":
            show parvez with dissolve
            "Parvez steels himself."
            p "We have to stand our ground."
            p "If we show them that they can run us off just by bringing a scary dude around, they'll always be able to beat us."
            j "But he really is scary ..."
            show inanna worried with dissolve
            i "He's right. We had to stand up to them sometime."
            j "But Inanna--{nw}"
            i "It's okay babe, we can do this."
            show judys n chud at farleft
            with move
            "The judys are right in front of them now."
            if met_kayden:
                "Parvez can see clearly that the pink one is Kayden now."
                "He can't resist yelling at them."
                p "Hey what's wrong with you? You used to be one of us."
                "Kaye tries to speak but Marianne cuts them off--"
                "Marianne" "She is healed now from the depravity and violence that you people inflicted upon her."
                "Marianne" "Though her body bears indelible scars, she will be made whole again by the light of the Lord."
            else:
                "Marianne" "What are you freaks doing here?"
                "She turns toward Sarah and Kaye."
                "Marianne" "See, all the more reason why this place needs to be razed to the ground."
                "Marianne" "These fallen children need a place to be removed from soci--I mean healed."
                "She turns and addresses herself to Parvez and Inanna."
            "Marianne" "Prepare to be cleansed by the light of all that is natural and pure!"
            label inanna_n_javier_2_battle:
                call battle_2_def from _call_battle_def_2
                scene cardboard with dissolve
                "Transsexual battle mode activate"
                call battle_2_presetup from _call_battle_presetup_2
                call battle_2 from _call_battle_2
            label battle_2_end:
                $ battle_2_win = True
                "You won!!"
                scene skatepark interior
                show inanna excited at farright
                show javier happy at midright
                show parvez toppy at right
                show judys n chud:
                    xalign 0.0
                with irisin
                "Somehow Parvez and Javier and Inanna are able to defeat the judys and the chud!"
                "Their enemies stagger away miserably."
                show judys n chud at furthestleft
                with move
                p "This is our turf! You'd better stay away!"
                if met_kayden:
                    p "Great job picking the losing and miserable side, Kayden!"
                "Marianne turns to glare at them, and the chud growls. He is much less frightening with a kicked dog expression and a limp."
                hide judys n chud with moveoutleft
                show parvez toppy at left
                show javier happy at midright
                show inanna excited at center
                with move
                j "Holy shit we did it. I can't believe it."
                "Javi is shaking slightly."
                i "Honestly P I didn't think you had it in you. I'm really impressed."
                p "I didn't know if I had it in myself."
                if battle_1_win:
                    p "but after the last time you and I fought them, Inanna, I learned that I'm stronger than I think."
                    p "Now we know our enemies can always be beaten, no matter how frightened we are."
                else:
                    p "But honestly, being with you folks gave me courage."
                j "Damn that's kinda gay haha."
                i "It sure is."
                show inanna toppy at left
                with move
                "Inanna grabs Parvez by the shoulders and kisses him firmly."
                show inanna toppy at farright
                show javier happy at furthestright
                with move
                i "Alright cutie, unfortunately we have to run, but let's talk more about getting this place set up another time."
                p "Aww, we can't celebrate?"
                i "Sorry babe, we'll see you another time."
                hide inanna
                hide javier
                with easeoutright
                "Javier gives Parvez's butt a pinch as they leave."
                scene skatepark ramps
                with wipeleft
                "Parvez takes a moment to look around the park before going home."
                "He's proud of himself, which is kind of a strange feeling."
                "He's used to always thinking of himself as a loser, but maybe he could be a leader. Maybe he could be someone who does things in his community."
                if battle_1_win:
                    "After all, he has now defended himself and defeated the judys twice! Once with an honest to god monster with them!"
                else:
                    "Even though he didn't fight the judys last time, he found the courage and was able to defeat them this time."
                    "And even that weird man monster--what even was that??"
                "After completing his victory lap, Parvez decides to go leave."
                "He gets in his car with adrenaline still coursing through his veins, feeling thrilled and wound up."
                "Maybe Terry would be up for messing around when he gets back ..."
                call screen chapterselect
        "run":
            $ battle_2_ran = True
            "Parvez starts to panic."
            p "I don't think we can do this."
            p "W-we have to go."
            "Inanna looks at him for a moment, before glancing back at the chud and judys who are rapidly approaching."
            i "Okay, let's go."
            hide inanna
            hide parvez
            hide javier
            with moveoutright
            scene black with pushright
            "They get out of there as fast as they can, piling into Parvez's tiny car."
            "He drops Inanna and Javier off at their place. Inanna insists on him taking the remaining tea and summer rolls home."
            "Terry finds him a few hours later on the couch, baked out of his mind watching children's cartoons and surrounded by their plastic wrappings."
            scene couch
            show parvez bottomy at right
            with dissolve
            show terry worried at midleft
            with moveinleft
            t "Damn, it's a self-pity Parvez day. What happened? I thought you were going on a date?"
            show parvez worried at center
            with move
            "Parvez rushes over to Terry and buries his head in their belly. Terry smooths his hair."
            t "That bad, huh?"
            p "Mrghh ..."
            $ inanna_n_javier_2_complete = True
            call screen chapterselect
