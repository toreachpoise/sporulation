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
    # UNLOCKS PLANT ENCOUNTER 2
    jump nav_menu

