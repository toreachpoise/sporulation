label plant_encounter_1:
    # BG WOODS
    "Parvez hopes he hasn't locked himself out of his car."
    "When he'd got to the trail, he'd decided it would be easier to leave his keys in the car than to try and wedge them into his running shorts pocket--"
    "--seriously, what are those things supposed to hold?--"
    "Now he's starting to worry if he's locked his keys in his car though."
    "He thinks he may have pushed the lock down on the door instinctively on his way out."
    "He can't afford another $200 call to the only locksmith that is both unlikely to murder him and willing to drive up a dirt road to find him."
    "He shakes his head like a tetra pak of soup, as if that will clear it."
    "The violets have started to come up on the side of the trail, little spiral leaves scything out of the ground."
    "There are bluebells up, too. He wonders if he'd know what any of the plants along a trail in Rajasthan were called. Probably not."
    "Parvez stops for a drink of water."
    "The trail slopes down into a swamp. In among the skunk cabbages, there's a plant he's never seen before."
    "He pulls out his vape and takes a hit. The plant looks like a fern--no, like seaweed almost. Slimy and wavy around the edges."
    "The plant is standing in a dry area that Parvez could probably get to from the other side of the swamp."
    menu:
        "check out the plant":
            pass
    "He squelches his way around the harder ground at the edge of the swamp. It's still muddy enough that his feet get stuck in it a couple of times."
    # PLANT CG/SPRITE
    "The plant is bigger than it looked from far away."
    "Up close, Parvez can see it looks more like some kind of succulent; thicker than seaweed."
    "He wishes he had his phone. Too bad it wouldn't fit in his running shorts."
    menu:
        "should I touch it?"
        "touch it":
            "He runs his fingers over the top of one of the fronds. It's squishier than he expected it to be, firm but still soft somehow."
            jump plant_touches_you
        "don't touch it":
            p "Fuck no I'm not touching that shit."
            p "What even is this thing?"
            "Something is really off about this plant ... Parvez isn't superstitious or anything but a really strange energy seems to be radiating off it."
            jump plant_touches_you
label plant_touches_you:
    "... Also, some of the fronds on the other side appear to be moving slightly."
    p "Bro what the hell??"
    "He must have smoked too much again."
    "Actually, no, this thing is definitely moving. A couple of the fronds brush his legs, then his arms, like it's testing him out."
    "Then it starts to slither around his arms, around his ankles."
    "At this point it's too late, of course. Parvez is trapped."
    # PLANTFUCKING CG
    p "This is some sick hentai shit."
    "Oddly, he's not panicking."
    "One of the fronds is trailing up his inner thigh, into his shorts."
    p "Back hole only, please."
    "Now maybe he's panicking."
    menu:
        "struggle":
            $ struggled = True
            "Parvez fights against the frond of the plant--"
            p "--don't say tentacle."
            "--he's kicking with all his might, even as the plant snakes around his body, squishy but strong."
            "There's no point in fighting back. The thing has him firmly around the shoulders and chest. He can't wriggle out."
            jump it_has_you
        "it won't work":
            "There's no point in fighting back."
            "There never is."
            "Parvez feels a familiar horrible dread. He remembers all the moments his body wasn't his, was something for others to use."
            "They wash over him all at once, not as images but as a dull sensation of powerlessness."
            jump it_has_you
label it_has_you:
    "It's inside his shirt, checking him out with one frond--"
    if struggled:
        p "Don't say tentacle, don't say tentacle."
    else:
        p "--don't say tentacle."
    "It seems to be listening to his request, though, staying away from his front hole."
    "It pokes his clit, cautiously at first but then settling into a rhythm."
    "Parvez gasps. It feels ... good?"
    "He starts to moan, and hopes no one can hear him out there in the woods."
    "One of the fronds is playing around his ass now."
    "He can feel it circling and dipping in. It's big."
    "Parvez is no slouch in the taking-it-up-the-ass department, but this thing is almost three inches thick."
    "Again, as soon as the panic starts to well up in his mind it disappears."
    "He feels secure, held and safe."
    "Once inside, the frond feels incredible."
    "The wavy shape feels like it's actually rippling inside of him."
    "Parvez is dimly aware that he's moaning really loudly, screaming even."
    "He should be embarrassed and probably frightened too. He's being fucked by a plant for god's sake."
    "But all he feels is good, a feeling of warmth filling him, and rightness. Even though it's strange it feels like a kind of homecoming."
    "When he cums he starts crying, shaking and wailing uncontrollably."
    "He's not sure where such strong emotion is even coming from inside him. It's like a well flooding, overflowing and pouring out of him."
    "The plant just holds him in place while he cries a moment."
    "As Parvez calms down he notices that the plant has flowers. One in particular on the end of a long thin frond is coming toward him."
    "The flower looks a bit like birds of paradise. Kind of like a speculum."
    "Parvez starts to become nervous again. The plant is still holding his legs open, his whole body splayed three feet off the ground."
    p "No, no. Please don't do that! Please don't do that! Please!"
    "Parvez is begging, wiggling as if he could get out of this thing's grasp even though he knows he can't."
    if struggled:
        "A familiar feeling of terrified resignation comes over him."
        "He's being held down and there's nothing he can do about it."
    "As soon as the flower touches him, he's engulfed by a strange calm feeling once more."
    "Parvez looks down and sees that it has pushed the flower and part of its long stem deep inside his vagina."
    "It feels like there's a small balloon inflating inside of him."
    "It doesn't hurt, he's not actually feeling any discomfort, but it doesn't feel good either."
    "After a few moments the balloon inside him seems to burst. The flower pulls out, with a deflated bulb near the bottom."
    "This is the last thing Parvez registers before he passes out."
    ".........."
    "When he wakes up it's almost dark. He's wet, freezing, and covered in mud."
    "He gets to his shaky feet and starts to walk back to his car."
    "The moon is already high in the gray late afternoon sky."
    "Even though Parvez felt cold the entire way, when he arrives at his car he is drenched in sweat."
    "He downs the rest of his water. His car, mercifully, is unlocked."
    # APARTMENT BG
    "Terry is waiting for him on the couch with a glass of wine."
    # SHOW TERRY
    t "Where were you? I was really worried."
    p "I think my vape oil is laced or something."
    p "I passed out in the mud and had a really weird nightmare."
    t "What??"
    p "I dreamt I had sex with this weird plant. It was like, big and fleshy."
    p "It was good at first but then it was kind of rapey ..."
    p "... but I was okay with it? Somehow??"
    t "Damn sweetie, are you okay? Are you sure you don't have a fever or something??"
    "Terry comes up to Parvez, reaching for his forehead like they're gonna check his temperature."
    menu:
        "let them comfort you":
            "Parvez leans into Terry's hand when they place it on his head. It's cool and soft."
            t "You don't feel feverish."
            "They pet Parvez's head for a moment before withdrawing. His hair feels sticky and gross on his head. He needs a shower, bad."
            jump temp_check
        "you don't want to be touched right now":
            "Parvez swats Terry's hand away."
            "He doesn't know how to say it but the idea of being touched, even by Terry, feels bad right now."
            "He's disgusting, covered in mud. He doesn't know what just happened, if it even did happen. But either way his whole body feels gross and wrong."
            jump temp_check
label temp_check:
    p "I'm fine. It was just a weird dream. I must have gotten too stoned in the woods."
    "Terry rolls his eyes."
    t "You're so weird."
    "They lean in to kiss Parvez's cheek."
    t "I'm just glad you're okay babe."
    # UNLOCKS TERRY 1
    # UNLOCKS SOLO 1
    jump nav_menu

label plant_encounter_2:
    $ tried_to_take_plant = False
    "Even though this whole having a plant dick thing has been cool, it still kind of freaks Parvez out not knowing how it happened."
    "He just can't shake the feeling that the whole thing was a weird dream, even in the face of the physical evidence."
    "One morning he wakes up and realizes that the only way to set his doubts to rest is to just go and try to find the plant again."
    "He gets up early on a Friday morning while the city is still steamy outside."
    "Terry shuffles blearily out of the bathroom in his bathrobe while Parvez is tying his shoes."
    t "Where ya going baby?"
    p "For a run."
    t "Don't get fucked by any more supernatural entities. Or do, I guess. Whichever you want."
    "Parvez parks his beat up hatchback down the side of the logging road."
    "As soon as he steps outside he's assaulted by the forest air, which is hot and steamy like a giant's breath."
    "He has brought a bag this time, stowing his keys securely and locking his car."
    "He runs down the same route he took last time, an overgrown deer trail that had newly forked away from his usual track."
    "The atmosphere is oppressive. His nostrils feel full of air and gnats with each inhalation."
    "He keeps running though, and sure enough after a couple of kilometers he sees the trail give way down into a swamp."
    "He realizes he had convinced himself the plant wouldn't still be there when he sees it, oil slick iridescent in the low light of the wetlands."
    "Now that he's expecting it, it's visibly moving from far away."
    "He approaches, fear and anticipation building in his gut."
    "Parvez didn't really have a plan beyond seeing if the plant was still there."
    "But now that he's here ..."
    "But now that he's here ... what?"
    "The plant seems docile today. It's not reacting directly to Parvez's presence."
    menu:
        "what should I do?"
        "taste it":
            jump plant_blowjob
        "take a piece with me and go home":
            $ tried_to_take_plant = True
            "Parvez comes up near the plant and finds that there are smaller ones growing near it."
            "He kneels down to take a closer look."
            "They're like weird tiny succulents. Parvez and Terry had had one kind of similar before, he remembers."
            "Terry was the main one who was good at houseplants, but for some reason not succulents. It had rotted and died."
            "Parvez grabs one of the small plants with his palm and twists it clear of the ground, its roots hanging free."
            "He could swear he saw the main plant recoil when he did that."
            "He wishes he had something to leave as an offering, but he doesn't."
            "He stuffs the small plant in his pocket and goes home."
            "He transplants his cutting into a little cup and puts it on the windowsill, but it withers and dies within two weeks."
            jump nav_menu
label plant_blowjob:
    "He finds himself standing right beside it, reaching out a finger to touch a pulsing arm of the plant."
    "It's slick, a clear film coats his hand."
    "He rubs his fingers together, and then, unthinkingly, puts them to his lips."
    "It tastes good. A little sweet and just ... fresh, vegetal."
    "He leans forward and kisses one of the fronds of the plant, sticking his tongue out to taste it directly."
    "He kisses along the length of it as it wiggles. Then he kisses the tip."
    "The tentacle--he's willing to call it that now--presses against his mouth."
    p "Fuck it."
    "Parvez parts his lips."
    "The tentacle enters his mouth, feeling around cautiously at first."
    "It flicks the sides of his cheeks exploratorily, then wraps around his tongue and squeezes, pulling a couple of times."
    p "W-ghugh--"
    "It feels kind of good, tugging firmly but not too hard on his tongue. Parvez feels his dick getting hard, pressing against the waistband of his shorts."
    "Then the plant seemingly loses interest in his tongue, delving deep into the back of his mouth."
    "Parvez chokes. His hands go to the tentacle, trying to pull it out,"
    "but by now it's fully awake, grasping him by the shoulders and the back of his head and forcing the tentacle in."
    if struggled:
        "Parvez tries to fight against the tentacles holding him off the ground, in part by the one down his throat."
        "He chokes and sputters, tears coming to his eyes, snot pouring from his nose."
    "He's gasping, he can't breathe, gagging continually on the tentacle as it fucks his throat."
    menu:
        "I've got to get out of here!":
            $ struggled_again = True
            "Parvez keeps fighting, sweating and choking."
            "He's starting to get lightheaded. Black spots flutter at the edges of his vision."
            "The more he wriggles the more the plant's grip tightens on him."
            "One of the tentacles is around his throat."
            "He can feel the delicate skin and blood vessels of his neck being squeezed between the tentacle inside his throat and the one around it."
            "His eyes roll back in his head."
            "The black spots fill Parvez's vision until he can't see or feel anything any more."
            "................."
            "Parvez wakes up to a squelching noise."
            "He looks down and it's him, both his holes being spread open by the plant."
            jump gag_and_pass_out
        "stop fighting":
            pass
    "He gives up and tries to let his throat go slack."
    "He swallows around the tentacle, trying to time his breaths with when it pulls out,"
    "breathing steadily through his nose and getting the air rhythmically punched out by the long tentacle."
    "His cock is rock hard, and he can feel himself dripping around the base of it where it joins his pussy."
    "He can also feel two more tentacles circling his two holes."
    "One plays around where the fluid is coming out of his cunt, around back of where his cock comes out."
    "Parvez didn't even know that he could still put things in there, not that he had wanted to before."
    "Now it seemed he had no choice but to learn."
    "The tentacle pressed into his pussy, bulging it around the two objects shoved inside."
    "Parvez had hardly ever had anything put in there before--and never consensually--and here this plant was fucking him again. And he liked it."
    "As soon as the thought came to him the plant pulled out, leaving him oddly empty feeling."
    "His disappointment had barely registered before the plant, slick with his cunt juice, dove into his ass, another tentacle coming to his cunt again to replace it."
    p "Sh--shit, wait--"
    p "I don't know if I can handle--three--"
    "He didn't have a choice."
label gag_and_pass_out:
    "The two tentacles inside his cunt and ass were punishing the membrane between them."
    if struggled_again:
        "The sight paired with the sound of his gooshy holes getting stretched open brings Parvez fully to consciousness."
    "The pounding is overwhelming. Parvez wails. It hurts but he can't stop cumming, this strange pulsing overwhelming feeling that's still unsatisfying."
    "His cock throbs with pleasure, unable to shoot and tortured by it."
    "The plant fucks him relentlessly for what feels like hours. His holes are raw."
    "Riding the wave of his orgasm for all this time has made Parvez lose his mind."
    "All he knows is the rhythm of the two tentacles pressing together inside him."
    menu:
        "should I let the plant cum inside me?"
        "yes (cumflation)":
            $ plantflation = True
            "After millenia, after an eternity, Parvez feels the tentacles bulge and get even fuller inside him."
            "His holes are being stretched to their absolute limit. It feels like his ass might rip."
            "Then the tentacles begin to throb."
            "Parvez feels them pulsing and shooting inside him."
            "The juice is oddly cool, he feels it coating the inside of the holes."
            "And it keeps coming, the tentacles pumping him."
            "He can feel its cum filling his womb, gushing further and further into his ass."
            "He looks down to find his belly swollen and distended."
            "It keeps growing. It feels so tight, painful even, but the plant keeps squishing more cum into him."
            "It's pushing into his holes even deeper, squeezing more into him."
            "Just when he feels like his belly is about to burst, the tentacles withdraw."
            "Clear, seedy goo gushes out of his holes."
            jump end_plant_encounter_2
        "no thanks":
            jump end_plant_encounter_2
label end_plant_encounter_2:
    "The plant is no longer restraining him."
    "Parvez gets down shakily, his legs barely able to support him."
    if plantflation:
        "Plant goop oozes down his legs as he struggles to pull his shorts back on."
        "The seat quickly becomes wet as it keeps squishing out of him."
    "He has to find a walking stick to help him get back to his car,"
    if plantflation:
        "dripping plant cum from his gaped ass and cunt the whole way,"
    "and when he gets there he sits in the driver's seat, still shaky and out of breath,"
    if plantflation:
        "soaking the seat with the seedy gel."
    p "Well, I guess it really was real."
    "Then he drives home to tell Terry about it."
    jump nav_menu