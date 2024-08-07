label inanna_1:
    #unlocked by ahmed 1 or kayden 1
    scene bed with fade
    play music planty if_changed
    $ inanna_points = 5
    $ asked_about_judys = 0
    "Even though the app is mostly dudes, every once in a while a woman will show up."
    "Parvez starts talking to Inanna at first because of a picture she had posted of her with her dog."
    "He's an ugly little pit bull, and Parvez is obsessed with him."
    "Inanna is really cool, too. She seems actually smart in a way that Parvez always pretends to be."
    "She's a PhD student and using her education to actually help people, building a community that is really radical."
    "Parvez just kind of lays around and jerks off most of the time, after getting half of three degrees."
    "Inanna is {i}hot{/i}, too."
    "Parvez isn't usually into women, but she has this tightly coiled ferocity to her that is mindmelting to have turned on you."
    # chat
    lj "... I just couldn't believe they sold out to the gas company, after Ginger got faer arm broken being pulled down from a tree sit by the pigs."
    lj "Sorry, what were we talking about?"
    pdm "I think your tree hugging interlude was a way of telling me how much you want this green dick."
    lj "Hah. As if. If you really did just grow that thing then I'm sure you have no idea how to use it yet."
    lj "You need a lady to show you how."
    "She has a boyfriend, Javier, who is also trans. She says she's told xem about Parvez's profile."
    "Javier is skeptical though. Inanna tells Parvez xe thinks it's fake."
    pdm "I promise you it's all real."
    "He sends her a video of him bouncing his cock around."
    lj "I mean shit, I'm definitely intrigued enough to see it in person, even if xe isn't."
    menu:
        "'wanna meet up, cutie?'"
        "hell yeah":
            jump meet_inanna
        "nah actually, sorry":
            "Parvez isn't actually that into Inanna sexually, is the thing."
            "Maybe he's not really into women after all ..."
            scene cardboard with fade
            call screen chapterselect
label meet_inanna:
    scene coffeeshop2
    show inanna excited:
        zoom 1.75
        yalign 0.0
        xalign 2.0
    with dissolve
    "Inanna gets Parvez to meet her at a big queer bookstore downtown."
    i "It's the oldest still-running queer bookstore in the world."
    "It had taken Parvez an hour on the train to get there from where he lived, but it's pretty cool."
    "He isn't sure if he's ever been in a specifically queer bookstore before."
    "The person working the cashier has their hair dyed in trans flag colors."
    "There's a cafe with coffee and milkshakes as well as alcohol drinks. It's all so ... perfect, and wholesome."
    "Kind of obnoxiously so to Parvez."
    "He slurps his milkshake grumpily."
    i "Bro, why do you look like that? Is it just this much of a struggle for you to go outside?"
    "She's grinning widely as she bugs him."
    i "Or are you just this intimidated by the sight of a real woman instead of one of your little anime pornos?"
    "She is stunningly hot in person, thick and brash and brightly colored."
    "Her energy takes up the entire room, but in a way that makes you grateful for it."
    p "I've seen women before ..."
    i "Where, at your mama's house?"
    "Parvez scowls. {w}Inanna softens slightly."
    i "Sorry, I forgot transsexuals like us don't often get to have parents."
    p "It's okay, I was just being a brat."
    "She pushes his knee gently under the wobbly little table with hers."
    i "I kind of like that."
    scene alley
    show parvez happy at left
    show inanna happy at midleft
    with fade
    play music maintheme
    "Parvez finds himself actually smiling as they step out of the book store into the late afternoon sunshine."
    "As soon as they do so, however, Inanna's expression turns into a frown."
    i "Shit, what are they doing here?"
    show judys flip at right
    with moveinright
    "There is a group of women standing across the street from the bookstore."
    "They look like strange nurses, like someone from the 1950s' idea of what a nurse would look like in the year 2000."
    "For some reason they seem to be wearing bike helmets with reflective plates on the forehead."
    "They have placards with them that say things like FEMINISM NEEDS WOMEN and SEX IS SCIENCE."
    i "Why don't you go preach your bullshit in your own neighborhoods you freaks?"
    "The tallest woman looks right at Inanna and gestures for another, shorter woman to look at her."
label judys_conversation_with_inanna:
    menu:
        "who are these people?":
            $ asked_about_judys += 1
            p "Who are these people?"
            i "They call themselves the Judys."
            i "They pretend to be feminists but really they just hate trans people."
            i "They say they defend women but they're just a block of cis women who stand in front of the real transphobes--powerful men, and hide them."
            i "If they're the loudest opposition to trans people, and they say they're feminists, it confuses the public."
            i "Cuz feminism is supposed to be good, right?"
            i "But these bitches are just the wives and daughters of rich men who want to control all our bodies, including theirs."
            jump judys_conversation_with_inanna
        "why are they dressed like that?":
            $ asked_about_judys += 1
            p "What's with the weird retro space nurse outfits?"
            i "I think it started out as ironic or something."
            i "People kept calling them backwards and they decided they liked it."
            i "Now they think of themselves as going back to traditional values to lead us into a purer whiter future."
            jump judys_conversation_with_inanna
        "why did you shout at them?":
            $ asked_about_judys += 1
            p "Why did you yell at them? That just made them notice us."
            i "People shouldn't feel safe to come to our places and harass us."
            i "They should be ashamed to show their hatred in public, and be afraid."
            menu:
                "you shouldn't have yelled at them":
                    p "You shouldn't have yelled at them, {fast} all that did was draw their attention to us."
                    p "Look, that lady is coming over now."
                    $ inanna_points -= 2
                    "Inanna glares at him."
                    i "Fuck that, you think it's more important to be polite, to keep your head down and stay quiet, than to defend yourself?"
                    i "At best that's how you end up getting stepped on, at worse you end up getting killed or selling out everyone else."
                    jump judys_conversation_with_inanna
                "that was really brave of you to do":
                    p "That was really brave of you ... {fast} I would never have the courage to do something like that."
                    i "Sure you do. Courage is a muscle, you just have to build it."
                    "She flexes her rather large bicep at him and winked."
                    i "You might get a chance right now, looks like they're coming over."
                    jump judys_conversation_with_inanna
        "what should we do?" if asked_about_judys > 1:
            "The tall woman is striding toward them across the street, heedless of an oncoming car that screeches to stop before hitting her."
            show judys flip at midright
            with move
            "JUDY" "Watch where you're going!"
            "She keeps walking right toward Parvez and Inanna, her gaze fixed on them."
            "The shorter woman is trailing behind her, looking a bit nervous."
            show judys flip at center
            hide inanna
            show inanna worried:
                xalign 0.2
            show parvez worried:
                xalign -0.2
            with hpunch
            "The tall woman gets right in Inanna's face and puffs out her chest."
            "JUDY" "What did you say to me, transvestite?"
            "Inanna doesn't look phased, looking serenely down at the woman."
            i "Damn, bitch. Did you bring your insults with you from the 1950s along with your outfit?"
            "The woman turns to her recently-arrived companion, speaking to her as if Inanna and Parvez don't understand."
            "JUDY" "You see, Sarah? He called me a bitch right away. The TIM cannot disguise his disgust for women even for a few moments."
            "Sarah" "Yes, Marianne."
            i "It's not women that I hate, lady. It's just your stale bitch ass. I'm not even fully sure you are human. You might be a robot under that weird nun's habit."
            if inanna_points < 5:
                menu:
                    "damn Inanna, calm down":
                        p "Damn Inanna, calm down. {fast}People are staring .... you're causing a scene."
                        i "{i}I'm{/i} causing a scene? {w}Not these bitches when they posted up outside a queer bookstore with their hateful ass signs?"
                        "Inanna turns back to the woman, no longer addressing Parvez."
                        i "When are you and your daddies going to learn that you're not welcome here?"
                        i "This is our turf, the place where we get to feel safe."
                        "Inanna spits on the woman's shoes and strides off."
                        hide inanna with moveoutleft
                        "Parvez runs to follow her, the two women speaking in agitated tones behind him."
                        hide parvez with moveoutleft
                        play music cutesad volume 2.0
                        scene alley
                        show inanna frightened at center
                        with wipeleft
                        show parvez worried at right with moveinright
                        p "Inanna!"
                        "She rounds on him."
                        show inanna even more toppy at midright
                        with hpunch
                        i "What?"
                        i "You wanna lecture me more about how to lick boots?"
                        i "I thought you were cool under your lil tuff guy grumpyboy exterior."
                        i "But you ain't shit."
                        i "I don't care if your little plant dick is real. Cuz it's clear you don't have any balls."
                        show inanna worried at center
                        with move
                        "She turns away from him."
                        i "Don't follow me this time."
                        hide inanna with moveoutleft
                        scene cardboard with fade
                        call screen chapterselect
                    "nah, fuck them":
                        "Parvez realizes in a flash that Inanna was right."
                        "These people hate them, but in a quiet way, a way that is designed to frame them as innocent even though they were the aggressors."
                        "The woman came over to Inanna, she could have ignored her."
                        pass
label judys_fight_1:
    "Marianne" "You freaks are just jealous. You use your size and natural masculinity to intimidate real women because you know you'll never become like us."
    i "Who the fuck would want to be like--{nw}"
    hide parvez
    show parvez flip:
        xalign 0.15
    show inanna happy:
        xalign -0.2
    with move
    "Parvez steps in front of Inanna, getting between her and the woman even though he's shorter than both of them."
    "He tries to steady his shaking voice as he speaks."
    p "You shouldn't be here. Leave us alone."
    "The woman looks down at Parvez and her voice drips with condescension."
    "Marianne" "Oh honey, I don't know what sick things this monster has done to you to make you like this, but you belong with us. With other real women."
    show parvez flip:
        xalign 0.25
    show judys flip:
        xalign 0.55
    with hpunch
    "Parvez shoves her, his fear evaporating into anger."
    p "Fuck you, you don't know what I am."
    scene black with fade
    "It's time to fight for your right to be who you are!!"
label inanna_1_battle:
    call battle_def from _call_battle_def
    $ renpy.music.set_pause(True, channel='music')
    play audio battlestart
    scene cardboard with dissolve
    "Transsexual battle mode activate"
    play sound fightmusic loop
    call battle_presetup from _call_battle_presetup
    call battle from _call_battle
label battle_end:
    $ renpy.music.set_pause(False, channel='music')
    $ battle_1_win = True
    scene alley
    show judys flip at center
    show inanna toppy:
        xalign 0.2
    show parvez toppy:
        xalign -0.2
    with irisin
    "Parvez and Inanna defeated the Judys!!"
    "The two women run off, abandoning all their shitty signs on the ground."
    hide judys with moveoutright
    show inanna at center
    with move
    "Inanna begins to gather them and throw them away."
    i "Hey, good job kid."
    i "For a second I wasn't sure if you had it in you."
    "Parvez bends down to help her."
    p "I've never really done anything like that before ..."
    menu:
        "it was scary":
            pass
        "it felt good":
            pass
    "Inanna chuckles."
    i "Yeah, it's scary, and it kind of does feel good."
    show inanna toppy with dissolve
    i "Speaking of things that feel good, did you wanna go back to my place?"
    menu:
        "fuck yeah":
            jump fuck_inanna
        "actually no thanks":
            show parvez worried with dissolve
            p "I feel a bit shaken up after all that, honestly."
            show inanna worried with dissolve
            i "Hey man, that's fair, totally understandable."
            i "I still had a really great time with you today."
            i "If you ever wanted to hook up, I think my partner would probably be into it. You seem like a great guy."
            p "Thanks ...{w} I had a really nice time with you too."
            i "Are you gonna be okay getting home?"
            p "Yeah, thanks. I'll see you around, Inanna."
            $ inanna_1_complete = True
            scene cardboard with fade
            call screen chapterselect
label fuck_inanna:
    scene balcony
    show inanna excited at midright
    show parvez at midleft
    with fade
    "Inanna's house is as beautiful and put together as she is."
    "There's actually framed art on the walls, prints and even a few original canvas paintings--"
    i "--all by local queer artists, of course."
    "She offers Parvez tea, grown by a comrade from a land defense camp, sits him down on her balcony, and immediately starts asking him about his dick."
    "Their conversation at the book store was pretty chill and nonsexual but she's clearly super interested in him."
    "Parvez isn't sure if it's from a scientific or sexual standpoint just yet."
    i "So it just?? Grew out of you? Wild!"
    "As soon as Parvez is done drinking his tea, she gets up and goes into the bedroom."
    "Parvez follows her, not sure what to do."
    scene inannabed with dissolve
    show inanna toppy at right
    show parvez flip at midleft
    with moveinleft
    i "The fuck you waiting for, boy? Take your pants off."
    i "I wanna see that weird green thing."
    show parvez flip bottomy at center
    with move
    "Parvez has no choice but to comply. He drops his shorts and reveals his hard dick."
    "Inanna immediately drops to her knees, poking at the place where it comes out of him. Parvez is wet there."
    i "Holy shit, huh. It really is coming out of there."
    "She looks up at him."
    i "Wait, is this okay?"
    p "Y-yeah."
    "She closes her hand around his dick."
    i "Can I pull on it?"
    p "Yeah."
    "When she gives it a tug, Parvez can feel how deeply rooted it is inside him."
    "For a second he has to marvel again about how weird this whole situation is."
    "Inanna is staring at him like he's a specimen on a microscope slide--but not in a creepy or objectifying way.{w} It's kind of hot actually."
    "She's pulling on his cock with an intent look on her face."
    i "So you can feel this??"
    p "Ah! mm-hmm"
    i "Fascinating. And this top part here--"
    "She squeezes the bulb at the end of his cock, making Parvez gasp."
    p "Ah!!"
    "Inanna acts as if she didn't notice his reaction, continuing on."
    i "This is where the seeds come out of, you say?"
    "She leans forward and licks his slit, where a little juice is coming out."
    i "Weird ... vegetal."
    "Parvez kind of expects her to suck on it more, but she gets up and pulls him to his feet, before shoving him onto the bed."
    scene cg I1 with hpunch
    pause
    "Inanna sheds her leotard and climbs on top of Parvez."
    "She's so beautiful, the mass of her on him kind of overwhelming."
    "Her thighs are huge, spanning his torso easily."
    "Her breasts wiggle as she leans back on him, revealing her hard cock."
    i "I don't usually need a lot of prep and can take way bigger than you so we might as well go for it."
    "She reaches to the bedside drawer and pulls out a bottle of lube, slathering it (cold!!) all over Parvez's cock."
    p "(squeak!)"
    i "Oh don't whine little guy."
    i "It'll be warm in just a second."
    "With that she lifted herself, lined his cock up, and slid down, almost halfway on the first try."
    p "H--ghhrk!!"
    i "Oh my! That certainly is a unique texture."
    "She lifted herself back up, squeezing tightly on him as she did so."
    p "Ah-hahh"
    "She dropped herself down with full force, beginning to pound down on him mercilessly."
    i "Is that too much for you, little boy?"
    i "I kinda thought you were a little bitch."
    menu:
        "n-no, I--":
            pass
    i "Shh, it's okay."
    i "Let mommy rock you to sleep."
    "She drives herself onto him with a punishing rhythm. It's all Parvez can do to cling to her legs as they flex and stretch above him."
    "She's bouncing on him so lightly and effortlessly, a grin fixed on her face, teasing him without breaking a sweat."
    i "You think you're a man now just cuz you got this little thing?"
    "She squeezes down on him to punctuate her sentence."
    i "I've had one of these since before you were born, and let me tell you baby."
    i "I'm 100 percent woman and I'm still more of a man than you'll ever be."
    menu:
        "wait, this is too much actually":
            stop music
            scene inannabed
            show parvez flip worried
            with dissolve
            i "Oh jeez I'm sorry."
            "Inanna gets up immediately, with a wet plop."
            show inanna worried at midright
            with move
            i "I should have asked, I thought we had a vibe going."
            i "My bad."
            "Parvez gets up too and awkwardly starts pulling his pants up."
            p "N-no, it's okay, I just --"
            "He's too embarrassed to finish."
            "She offers him tea again but he just excuses himself and leaves."
            scene cardboard with fade
            call screen chapterselect
        "ahh ... yes mommy":
            pass
    i "That's right, baby boy, I am your mommy."
    i "Now are you gonna show me that you wanna grow up to be a big man?"
    "Parvez grabs her by the hips and starts fucking up into her in earnest."
    i "Ahh! Yes! That's good baby.{w} Give it to me."
    i "Show mommy how much of a big boy you are."
    "It's actually pretty difficult. She's bigger than Parvez and heavy on top of him."
    "Even when he matches her pace, the force of her down thrusts drives him into the mattress each time."
    "Within a few minutes Parvez is drenched in sweat, her legs sliding along his sides with every push."
    "He reaches for her cock to hasten her orgasm, but she bats him away."
    i "Don't worry about me, baby. Mama can take care of herself."
    i "Just keep giving it to me good."
    "Parvez isn't sure if he can do that, his legs are burning, his head is starting to spin."
    "He feels like he's losing consciousness, focusing on nothing but the next time she's going to crush him into the bedding, trying to spring back in time."
    "Again, and again."
    "He feels like she's pounding the air out of him."
    "Like he's a piece of raw metal and she's a blacksmith, forging him, shaping him into something useful."
    "Even though he's inside her she's the one fucking him."
    "As soon as this thought hits him so does the orgasm he didn't realize he'd been building up to."
    "He feels the gush come from deep in his belly, a huge volume of gel coursing through his cock and up into Inanna's ass."
    i "Ahhhhh!"
    i "Shit, that's the good stuff."
    "She keeps riding him, slower but just as hard, squeezing him for every drop, palming her own cock."
    "Parvez is gasping and twitching, overstimulated by the tightness inside her and the gloopy feeling of the seeds."
    "She's so hot riding against herself, making slick noises on his softening cock."
    "The sensation and the sight together become overwhelming for Parvez as her ass tightens more and more on him."
    "Just in time, she cums, not really shooting much, but Parvez can feel her cum through her ass, the rhythmic twitching of it pushing his now fully soft cock out."
    "She pushes off his chest and slides down onto the bed."
    i "Shit, that was wild."
    "She's barely out of breath."
    "She reaches back behind her to gather some of his goopy and seedy cum from her hole."
    "She looks at it in her hand."
    i "Very interesting, young man."
    "She winks."
    i "I'll have to collect more samples from you again sometime."
    $ inanna_1_complete = True
    scene cardboard with Fade(0.5,1.0,0.5)
    call screen chapterselect

label inanna_2:
    scene bed with fade
    play music maintheme
    "Parvez has been feeling weird for a while."
    "He's been through a lot lately."
    $ fucked_by_a_plant = 0
    if plant_encounter_1_complete == True:
        $ fucked_by_a_plant += 1
    if plant_encounter_2_complete == True:
        $ fucked_by_a_plant += 1
    if solo_2_complete == True:
        $ fucked_by_a_plant += 1
    if terry_4_complete == True:
        $ fucked_by_a_plant += 1
    if fucked_by_a_plant == 1:
        "He's been fucked by a plant ..."
    elif fucked_by_a_plant == 2:
        "He's been fucked by a plant ... twice!"
    else:
        "He's been fucked by a plant--{w}[fucked_by_a_plant] times!"
    if chud_1_complete:
        "... He's been raped ..."
    $ passed_on_to = 0
    if ahmed_1_complete:
        $ passed_on_to += 1
    if kayden_1_complete:
        $ passed_on_to += 1
    if inanna_n_javier_1_complete:
        $ passed_on_to += 1
    if (kayden_2_badend == True):
        if (badend_skipped == False):
            "He's grown a plant dick, just to have it chopped off and have to regrow it again."
            "But he at least managed to pass it on to [passed_on_to] cuties in the process."
        else:
            "He's grown a plant dick ... and passed it on to [passed_on_to] cuties!"
    else:
        "He's grown a plant dick ... and passed it on to [passed_on_to] cuties!"
    if didnt_fuck_kayden == False:
        "... even though one of them was Kayden ..."
        if inanna_n_javier_2_complete:
            "... or Kaye or whatever ..."
    "It's all really started to take a toll on Parvez."
    "He feels like he needs some motherly love ..."
    lj "sounds like my boy has been corrupted and filled with sin and needs to be set straight"
    "That's not what Parvez meant at all."
    $ obedience_points = 0
label obedience_check_1:
    menu:
        "yes mommy":
            $ obedience_points += 1
            lj "good boy"
            lj "mommy will cleanse you and put you on the path of light again"
            "Parvez feels a rush of heat down to his cunt."
            pdm "i think i might need to be punished mommy"
            lj "i know you do"
            lj "you've been a nasty boy"
            jump obedience_check_2
        "fukc u im not full of sin":
            $ obedience_points -= 3
            pdm "wtf"
            pdm "literally none of this has been my fault"
            pdm "are you even listening"
            lj "you ungrateful brat"
            lj "how dare you defy me"
            lj "i'm trying to set you on the right path"
            lj "after you went and degraded yourself"
            lj "like a nasty little slut"
            lj "now, as i was saying:"
            pass
label obedience_check_2:
    lj "come and see me on saturday"
    if obedience_points < 0:
        menu:
            "do I even want to see her??"
            "no, fuck that":
                stop music
                pdm "you no what no, fuck you"
                pdm "you hurt my feelings"
                pdm "i don't want to see you saturday"
                lj "shit, fine bro, I was just playing with you"
                "Parvez is kind of upset by how callous Inanna was.{w} He's moody for the rest of the day."
                $ inanna_2_complete = True
                scene cardboard with fade
                call screen chapterselect
            "i kinda really do tho ...":
                pass
    lj "and don't touch yourself or let anyone make you cum until then"
    menu:
        "It's only Monday ... Saturday is four days away ..."
        "whine about it":
            $ obedience_points -= 1
            pdm "but mooom"
            pdm "saturday is so long from now"
            pdm "i gotta touch myself like twice a day"
            pdm "it's like"
            pdm "biology"
            pdm "or hormones or something"
            lj "goddamn you are such a horny little freak ahaha"
            lj "you really do need to be punished"
            jump obedience_check_3_preset
        "yes mommy":
            $ obedience_points += 1
            lj "good boy.{w} maybe you can be redeemed afterall"
label obedience_check_3_preset:
    lj "and remember ! mommy will know if you touch yourself !"
    $ obedience_days = 0
    $ ignored_ahmed = False
    $ ignored_kayden = False
    $ ignored_javier = False
    $ ignored_terry = False
    $ ignored_chud = False
    $ controlled_self = False
label obedience_check_3:
    scene bed
    if obedience_days < 1:
        $ obedience_days += 1
        if ahmed_2_complete == False and ignored_ahmed == False:
            "Parvez switches over to the other message window ...there's a message from Ahmed on the app ..."
            menu:
                "read the message":
                    p "What could it hurt, right?"
                    $ inanna_sent_me = True
                    jump ahmed_2
                "ignore it":
                    $ ignored_ahmed = True
                    jump obedience_check_3
        elif ((kayden_1_complete == False) or ((kayden_2_complete == False) and (inanna_n_javier_2_complete == True))) and (ignored_kayden == False):
            "Parvez switches over to the other message window ...there's a message from Kayden on the app ..."
            menu:
                "read the message":
                    p "What could it hurt, right?"
                    $ inanna_sent_me = True
                    if (kayden_1_complete == False) and (inanna_n_javier_2_complete == False):
                        jump kayden_1
                    else:
                        jump kayden_2
                "ignore it":
                    $ ignored_kayden = True
                    jump obedience_check_3
        elif (inanna_n_javier_1_complete == False) and (javier_1_complete == False) and (ignored_javier == False):
            "Parvez switches over to the other message window ...there's a message from Javier on the app ..."
            menu:
                "read the message":
                    p "What could it hurt, right?"
                    $ inanna_sent_me = True
                    $ javier_tells = True
                    jump javier_1
                "ignore it":
                    $ ignored_javier = True
                    jump obedience_check_3
        elif terry_3_complete == False and ignored_terry == False:
            "Terry brushes up against Parvez a couple hours later while they're making lunch together."
            "Their hands snake around Parvez's waist and dip into his pants, almost surreptitiously except for how they honk his dick with their hand."
            "Parvez is hard already."
            menu:
                "try to fuck terry":
                    $ inanna_sent_me = True
                    jump terry_3
                "control yourself":
                    $ ignored_terry = True
                    jump obedience_check_3
        elif chud_1_complete == False and ignored_chud == False:
            "Parvez switches over to the other message window ... he has no interesting messages ..."
            "... he's really scraping the bottom of the barrel here ..."
            "... some chaser has been messaging him ..."
            "... maybe he should see what they have to say ..."
            menu:
                "read the message":
                    p "What could it hurt, right?"
                    $ inanna_sent_me = True
                    jump chud_1
                "ignore it":
                    $ ignored_chud == True
                    jump obedience_check_3
        elif ((solo_1_complete == False) or (solo_2_complete == False)) and controlled_self == False:
            "Barely a few hours later and Parvez is already so horny he can't take it."
            "He has no self control."
            "No one is around for him to fuck, so he supposes he'll just have to take matters into his own hands."
            menu:
                "jerk off?"
                "... yeah ...":
                    $ inanna_sent_me = True
                    if solo_1_complete == False:
                        jump solo_1
                    else:
                        jump solo_2
                "no, goddamn it":
                    $ controlled_self = True
                    jump obedience_check_3
        else:
            $ obedience_points += 5
            "Parvez has honestly been so busy these days that he has no one left to fuck and no time to jerk off."
            "He easily waits the few days until he sees Inanna."
            jump see_inanna
    elif obedience_days < 4:
        $ obedience_days += 1
        if ahmed_2_complete == False and ignored_ahmed == False:
            "The next day there's a message from Ahmed on the app ..."
            menu:
                "read the message":
                    p "What could it hurt, right?"
                    $ inanna_sent_me = True
                    jump ahmed_2
                "ignore it":
                    $ ignored_ahmed = True
                    jump obedience_check_3
        elif ((kayden_1_complete == False) or ((kayden_2_complete == False) and (inanna_n_javier_2_complete == True))) and ignored_kayden == False:
            "The next day there's a message from Kayden on the app ..."
            menu:
                "read the message":
                    p "What could it hurt, right?"
                    $ inanna_sent_me = True
                    if (kayden_1_complete == False) and (inanna_n_javier_2_complete == False):
                        jump kayden_1
                    else:
                        jump kayden_2
                "ignore it":
                    $ ignored_kayden = True
                    jump obedience_check_3
        elif (inanna_n_javier_1_complete == False) and (javier_1_complete == False) and (ignored_javier == False):
            "The next day there's a message from Javier on the app ..."
            menu:
                "read the message":
                    p "What could it hurt, right?"
                    $ inanna_sent_me = True
                    $ javier_tells = True
                    jump javier_1
                "ignore it":
                    $ ignored_javier = True
                    jump obedience_check_3
        elif terry_3_complete == False and ignored_terry == False:
            "Terry brushes up against Parvez the next day while they're making lunch together."
            "Their hands snake around Parvez's waist and dip into his pants, almost surreptitiously except for how they honked his dick with their hand."
            "Parvez is hard already."
            menu:
                "try to fuck terry":
                    $ inanna_sent_me = True
                    jump terry_3
                "control yourself":
                    $ ignored_terry = True
                    jump obedience_check_3
        elif chud_1_complete == False and ignored_chud == False:
            "The next day Parvez finds himself scrolling the app ... he has no interesting messages ..."
            "... he's really scraping the bottom of the barrel here ..."
            "... some chaser has been messaging him ..."
            "... maybe he should see what they have to say ..."
            menu:
                "read the message":
                    p "What could it hurt, right?"
                    $ inanna_sent_me = True
                    jump chud_1
                "ignore it":
                    $ ignored_chud = True
                    jump obedience_check_3
        elif ((solo_1_complete == False) or (solo_2_complete == False)) and controlled_self == False:
            "By the next day, Parvez is so horny he can't take it."
            "No one is around for him to fuck, so he supposes he'll just have to take matters into his own hands."
            menu:
                "jerk off?"
                "... yeah ...":
                    $ inanna_sent_me = True
                    if solo_1_complete == False:
                        jump solo_1
                    else:
                        jump solo_2
                "no, goddamn it":
                    $ controlled_self = True
                    jump obedience_check_3
        else:
            if obdience_days < 3:
                "From that point on in the week, Parvez has no one left to fuck and no time to jerk off."
                "He's honestly been kind of busy lately, he realizes with a shock."
                "He easily waits the few remaining days until he sees Inanna."
                jump see_inanna
            else:
                "Finally, on the last day, there's no one left for Parvez to fuck."
                "He feels like he's attained a glorious kind of clarity."
                "He's really proud of himself as he goes to Inanna's house the next day."
                jump see_inanna
    else:
        pass
label see_inanna:
    play music planty if_changed
    "Parvez feels nervous as he approaches Inanna's apartment."
    if obedience_points <= 0:
        "He knows he's been bad ..."
        if obedience_points <= -5:
            "He's slipped up and done sexy stuff ..."
        if obedience_points <= -20:
            "... four times."
        elif obedience_points <= -15:
            "... three times."
        elif obedience_points <= -10:
            "... twice."
        "Inanna is sure to punish him."
    else:
        "Even though he's done his best to be good, Inanna can be unpredictable ..."
        "... he kind of liked it that way, though."
        "Why would he be here if he doesn't want to be punished, after all?"
    "He knocks on her door."
    scene balcony
    show inanna toppy with hpunch
    "Inanna pulls the door open."
    "She's already undressed, wearing only a skimpy bikini top with slatted cutouts, and a thong. with a sheer robe over top."
    i "I bet you've been a bad boy, haven't you?"
    menu:
        "I tried to be good!":
            $ obedience_points += 1
            i "uh huh, sure you did son."
        "how would you even know?":
            $ obedience_points -= 1
            "Inanna squints at him."
            i "I have my ways."
            i "But a good boy would tell me anyway ..."
            i "Did you do something bad?"
            if obedience_points > -5:
                p "no, I was good!"
                "She scrutinizes him."
                i "Alright ... if you say so ..."
                i "But I'm sure you deserve to be punished nonetheless ..."
                jump spanking_time
            else:
                menu:
                    "no i didn't":
                        $ obedience_points -= 3
                        "Inanna's frown deepens."
                        i "I don't know if I believe you ..."
                        menu:
                            i "Are you sure about that?"
                            "yeah":
                                if javier_tells == False:
                                    $ obedience_points -= 10
                                    i "Well I happen to know that's a lie, because Javi told me otherwise."
                                    i "Are you so brazen as to lie to me when you know I know the truth?"
                                    i "You really are a twisted brat."
                                    i "I'll leave your ass tanned red for this."
                                    jump spanking_time
                                else:
                                    $ obedience_points -= 3
                                    i "Hmm ... interesting ... if that's what you're going with."
                                    i "I suppose I'll have to punish you extra hard ..."
                                    jump spanking_time
                            "no, I'm sorry ...":
                                p "I'm sorry I lied ..."
                                p "and I fucked up ..."
                                p "I couldn't help myself."
                                i "You're such a filthy boy with no self control."
                                i "I'm going to punish you severely."
                                i "But I am merciful, and I will always reward honesty."
                                i "So I won't punish you quite as much as I would have if you had lied to me a second time."
                                jump spanking_time
                    "I fucked up":
                        $ obedience_points += 3
                        p "I'm sorry mommy ..."
                        p "I couldn't help myself."
                        i "You're such a filthy boy with no self control."
                        i "I'm going to punish you severely."
                        i "But I am merciful, and I will always reward honesty."
                        i "So I won't punish you quite as much as I would have if you had lied."
                        jump spanking_time
label spanking_time:
    "Inanna leads Parvez over to the large daybed that functions as their second living room couch."
    i "Strip."
    menu:
        "be a brat":
            $ obedience_points -= 2
            p "What if I don't want to?"
            i "You'll just get punished more."
            "Parvez takes his pants off nonetheless."
            jump how_many_spanks
        "do it":
            "Parvez strips down immediately."
            i "There you go, maybe you can be a good boy ..."
            $ obedience_points += 2
label how_many_spanks:
    scene cg I2A with dissolve
    "Inanna bends Parvez over her knee and raises her hand."
    $ begged_for_more = False
    if obedience_points > 0:
        $ spanks_left = 25 ## up to 50 if you beg for more
    elif obedience_points == 0:
        $ spanks_left = 40 ## up to  65 if you beg for more
    elif obedience_points > -5:
        $ spanks_left = 50 ## up to 75 if you beg for more
    elif obedience_points > -10:
        $ spanks_left = 70
    elif obedience_points > -15:
        $ spanks_left = 80
    elif obedience_points > -20:
        $ spanks_left = 90
    else:
        $ spanks_left = 100
    if obedience_points <= -4:
        i "You've been such a bad boy, I'm going to have to spank you so many times."
        "Parvez feels his cheeks flush in anticipation."
        p "How many times mommy?"
        i "I'm going to spank you [spanks_left] times."
        "Parvez gasps."
        i "Now be a good brat and count them out loud for mommy."
        p "Yes mommy."
        $ spanks_set = spanks_left
    else:
        i "You've honestly been a good boy, I don't know if it's even right to punish you."
        p "Please mommy ... I want to ..."
        i "Okay fine, I'll spank you [spanks_left] times."
        menu:
            "beg for more like a freak":
                $ begged_for_more = True
                p "Please mommy I want more."
                p "I'm so bad, I need to be punished."
                i "Damn what a pathetic little brat."
                i "Begging to be punished, like a sick little pervert."
                i "That deserves to be punished unto itself ..."
                $ spanks_left += 25
                i "I'll spank you [spanks_left] times ...{w} try not to enjoy it too much ..."
                i "And make sure you count them out or I'll start over ..."
                $ spanks_set = spanks_left
                jump get_spanked
            "thank her":
                p "Thank you mommy for setting me straight."
                p "I'm a bad boy and I deserve to be punished."
                i "Ugh, what a pathetic little bootlicking freak."
                i "And make sure you count them out like a good brat ..."
                $ spanks_set = spanks_left
                jump get_spanked
label get_spanked:
    $ spank_count = 0
    "Inanna lifts her hand up and lets it fall on Parvez's ass cheek with a mighty thwack!"
    $ spank_count += 1
    $ spanks_left -= 1
    p "Ah!!"
    i "You better count, bitch."
    p "[spank_count]!"
    i "That's right, keep counting ..."
    i "If you lose track I'll start over ..."
# add spank sfx??
label spank_loop:
    while spanks_left > 0:
        $ spanks_left = spanks_set - spank_count
        if spank_count < 5:
            "Inanna thwacks him four more times in rapid succession."
            p "Ah ! 2! 3! Ah! 4! 5!"
            $ spank_count = 5
        elif spank_count < 10:
            "His ass is starting to feel warm."
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            "Each successive hit feels more painful on his ass cheeks."
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
        elif spanks_set == 25:
            "Inanna is spreading the hits around Parvez's ass but it still hurts, each whack landing somewhere she's already hit."
            $ spank_count += 1
            p "Uuungh ... [spank_count]"
            i "Oh, quit whining, this is nothing."
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "Ahh ... hahh ... [spank_count]"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "Ah! [spank_count]!"
            $ spank_count += 1
            p "[spank_count]! Hahhhhhh !!"
            i "See, you got off easy ... there's only a few left so count them out nice and loud."
            i "And no whining."
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]! Wah!"
            $ spank_count += 1
            p "[spank_count]!"
            jump end_spanking
        elif spank_count < 25:
            "Inanna is spreading the hits around Parvez's ass but it still hurts, each whack landing somewhere she's already hit."
            $ spank_count += 1
            p "Uuungh ... [spank_count]"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "Ahh ... hahh ... [spank_count]"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]! Hahhhhhh !!"
            $ spank_count += 1
            p "Ah! [spank_count]"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
        elif spank_count == 25:
            "After 25 spanks, Inanna asks if Parvez would like a break"
            i "We have [spanks_left] more ..."
            if spank_count < spanks_left:
                i "You still have a long way to go, you nasty boy."
            elif spank_count == spanks_left:
                i "You're halfway there."
            elif spank_count > spanks_left:
                i "You're more than halfway there!"
            $ spank_count += 1
            menu:
                "I need a break":
                    if spank_count > spanks_left:
                        i "I mean you're almost there, but alright ..."
                    scene couch
                    show inanna even more toppy at center
                    show parvez bottomy at left
                    with dissolve
                    "Inanna helps Parvez up and gives him a glass of water, which he gratefully drinks."
                    "His ass and his cheeks are both burning."
                    "Inanna is watching him with focused eyes, despite her flush and wild grin."
                    "Parvez hands her back the glass of water."
                    menu:
                        i "Are you ready to keep going?"
                        "Yeah":
                            i "That's a good boy, you're doing so well."
                            scene cg I2A with dissolve
                            "She strokes Parvez's arm before bending him back over her lap."
                            "He can feel that she's hard underneath him, just like he is."
                            "Then she smacks him hard enough that he doesn't think of anything."
                            jump spank_loop
                        "I think I need the bathroom":
                            i "Okay baby, you know where it is?"
                            p "Yeah."
                            show black with moveinleft
                            "Parvez goes to the bathroom and struggles to pee because he's rock hard."
                            hide black with moveoutleft
                            "He returns to find Inanna sprawled out on the daybed, legs wide open, stroking herself through her skimpy panties."
                            p "Damn, that's hot."
                            "She stops touching herself and immediately glares at him."
                            i "Mind your own business you little squirt."
                            scene cg I2A with hpunch
                            "She roughly grabs his arm and bends him back over her lap."
                            "He can feel that she's hard underneath him, just like he is."
                            "Then she smacks him hard enough that he doesn't think of anything."
                            jump spank_loop
                        "Actually, I kind of want to be done":
                            show inanna worried
                            show parvez
                            with dissolve
                            "Inanna snaps out of play mode right away."
                            i "Sure, of course babe."
                            i "Do you still wanna fuck or should we just chill instead?"
                            menu:
                                "fuck":
                                    p "I still wanna mess around, if you do too."
                                    i "Yeah baby, definitely."
                                    jump fingering
                                "chill":
                                    p "I think I'm good actually."
                                    i "Sure babe of course."
                                    jump aftercare
                "let's keep going":
                    i "That's my good boy!"
                    i "She rubs her hand on Parvez's warm ass cheek, which intensifies the next smack."
                    jump spank_loop
        elif spanks_set == 40:
            p "Uuungh ... [spank_count]"
            i "Oh, quit whining, this is nothing."
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "Ahh ... hahh ... [spank_count]"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "Ah! [spank_count]!"
            $ spank_count += 1
            p "[spank_count]! Hahhhhhh !!"
            i "See, you got off easy ... there's only a few left so count them out nice and loud."
            i "And no whining."
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]! Wah!"
            $ spank_count += 1
            p "[spank_count]!"
            jump end_spanking
        elif spank_count < 45:
            i "Remember to keep counting nice and loud for me."
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "Wah !! [spank_count]!"
            $ spank_count += 1
            "Parvez's ass is burning."
            p "[spank_count]!"
            $ spank_count += 1
            p "Ah! [spank_count]!"
            $ spank_count += 1
            p "Ah ! [spank_count]!"
            $ spank_count += 1
            "Tears are streaming freely from his eyes."
            i "Such a good boy for me, crying but still taking his punishment like a champ."
            "She smacks him extra hard on the next one."
            p "Ah!! [spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]! Wah!"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
            p "Ahh ... hah--hahh."
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
        elif spanks_set == 50:
            i "There's only a few left so count them out nice and loud for me like a good boy."
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]! Wah!"
            $ spank_count += 1
            p "[spank_count]!"
            jump end_spanking
        elif spank_count < 60:
            play music forest
            "After 50 spanks, Parvez starts to lose focus on the proceedings."
            $ spank_count += 5
            p "[spank_count]"
            "He's still counting, but he's not really there. He's somewhere above the scene, watching."
            $ spank_count += 1
            p "[spank_count]"
            $ spank_count += 1
            p "[spank_count]"
            "Parvez isn't frightened, though. If anything, he feels warm, safe, and protected."
            "... Even though he's being hit."
            $ spank_count += 1
            p "[spank_count]"
            $ spank_count += 1
            p "[spank_count]"
            $ spank_count += 1
            p "[spank_count]"
            "Time starts to speed up."
            $ spank_count += 2
            p "[spank_count]"
            $ spank_count += 3
            p "Ah! [spank_count]!"
        elif spanks_set == 65:
            "Inanna's voice breaks through Parvez's fugue state."
            i "There's only a few left so count them out nice and loud for me like a good boy."
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]!"
            $ spank_count += 1
            p "[spank_count]! Wah!"
            $ spank_count += 1
            p "[spank_count]!"
            jump end_spanking
        elif spank_count < 70:
            $ spank_count += 1
            p "Wahh! [spank_count]!"
            $ spank_count += 4
            p "[spank_count]!"
            if spanks_set == 70:
                jump last_few
            $ spank_count += 3
            p "[spank_count]"
            $ spank_count += 1
            p "Ah! [spank_count]"
            $ spank_count += 1
            p "[spank_count] ahh--hahh-hahh--"
            "Parvez is gasping for breath."
            if spanks_set == 75:
                jump last_few
            elif spanks_set == 80:
                i "Good boy, come on, you've just got 10 left."
                $ spank_count += 1
                p "[spank_count]!"
                $ spank_count += 1
                p "[spank_count]!"
                $ spank_count += 1
                p "[spank_count]!"
                $ spank_count += 1
                p "[spank_count]! Wah!"
                $ spank_count += 1
                p "[spank_count]!"
                i "That's it, last 5 ..."
                $ spank_count += 1
                p "Waugh !! [spank_count]!"
                $ spank_count += 1
                p "[spank_count]!"
                $ spank_count += 1
                p "[spank_count]!"
                $ spank_count += 1
                p "[spank_count]! Ahh"
                $ spank_count += 1
                p "[spank_count]!"
                jump end_spanking
            else:
                menu:
                    i "Do you need a break baby?"
                    "yeah":
                        i "Alright baby, let's take a sec."
                        "She blows cool air over Parvez's ass but it just makes it burn more."
                        jump spank_loop
                    "no":
                        "Parvez grits his teeth."
                        p "Let's just keep going."
                        i "What a brave boy!"
                        i "Don't worry sweetie, we're almost there."
                        jump spank_loop
        else:
            i "You're so close now ..."
            "She smacks him again."
            $ spank_count += 6
            p "... [spank_count]"
            i "What was that? Keep counting loud enough."
            $ spank_count += 1
            p "Ah! [spank_count]!"
            i "Good boy ..."
            $ spank_count += 5
            p "[spank_count]"
            $ spank_count += 1
            p "[spank_count]"
            $ spank_count += 1
            p "[spank_count]"
            $ spank_count += 1
            p "[spank_count]"
            if spanks_set == 90:
                jump last_few
            else:
                i "Come on, last 15, and then you'll be at 100."
                $ spank_count += 1
                p "[spank_count]"
                i "Did you even think you would make it this far?"
                $ spank_count += 1
                p "[spank_count]"
                "She whaps him extra hard."
                $ spank_count += 1
                p "Ah ! [spank_count] !"
                i "Answer me."
                menu:
                    "y-yes mommy ...":
                        pass
                    "n-no...":
                        pass
                i "I knew you could do it."
                $ spank_count += 1
                p "[spank_count]"
                $ spank_count += 1
                p "Ah ! [spank_count] !"
                i "Last 10 ..."
                $ spank_count += 1
                p "[spank_count]"
                $ spank_count += 1
                p "[spank_count]"
                $ spank_count += 1
                p "[spank_count]"
                $ spank_count += 1
                p "[spank_count]"
                $ spank_count += 1
                p "[spank_count]!! Aaaagh !!!!"
                i "Oh, hush. Five more ..."
                $ spank_count += 1
                p "[spank_count]"
                $ spank_count += 1
                p "[spank_count]"
                $ spank_count += 1
                p "[spank_count]"
                $ spank_count += 1
                p "[spank_count]"
                $ spank_count += 1
                p "[spank_count]"
                jump end_spanking
    return
label last_few:
    "Inanna's voice breaks through Parvez's fugue state."
    i "There's only a few left so count them out nice and loud for me like a good boy."
    $ spank_count += 1
    p "[spank_count]!"
    $ spank_count += 1
    p "[spank_count]!"
    $ spank_count += 1
    p "[spank_count]!"
    $ spank_count += 1
    p "[spank_count]! Wah!"
    $ spank_count += 1
    p "[spank_count]!"
label end_spanking:
    i "Good boy!!"
    "Her voice sounds genuinely pleased. Her hand comes down to rub Parvez's raw ass cheek."
    i "See, that wasn't so bad, was it?"
    i "You've been so good for me, look how nice and red your ass is now."
    "She dips her finger down to feel his pussy."
    i "And you're so wet ... and hard ..."
    i "Do you want mommy to help you with that?"
    menu:
        "yes please ...":
            jump fingering
        "I think I want to be done":
            p "I don't think I can take any more, I feel like I want to collapse."
            i "Yeah, baby, you've already been through a lot."
            i "Let's call that our scene."
            jump aftercare
label fingering:
    scene cg I2B with dissolve
    "Inanna circles the opening of Parvez's wet pussy, tracing around where his cock comes out."
    i "You're so tight here."
    "She dips her finger in, the stretch is intense for Parvez after all he's been feeling."
    i "Maybe I'll just borrow some lube and visit my other friend."
    "She scoops out a bit of lube and begins poking his asshole."
    "The sensation of her arm rubbing against his raw ass is intense, bringing his attention to her every movement."
    "She pushes her fingertip inside."
    p "Ahh!!"
    i "Damn, you screamed louder for that than me beating your ass."
    "Parvez feels embarrassed."
    p "It's tight ..."
    i "Oh don't worry baby, I know."
    "She works one finger into him and then a second one in quick succession."
    p "Wahh."
    i "Such a good boy for me, just let me in."
    p "Ahhh ..."
    "She strokes his insides."
    "Parvez can feel her rubbing in against where his cock is on the other side of his rectum, pressing against where his prostate would be."
    "It feels so good."
    p "Shit Inanna, that's amazing."
    i "I know. I know what I'm doing."
    p "Mmmmh."
    "Parvez can't cum right now so he just rides the waves of pulsing sensation from Inanna gently probing him."
    "Her touch is so much kinder and softer now, her hands that were causing him pain before are filling him with glowy pleasure."
    p "Shit, please, more ..."
    i "Damn, alright bro."
    "She works a third finger in."
    p "F-fuck!!"
    "He feels so stretched out, between the cock growing out of his pussy and her three fingers in his ass."
    "Still, he rides back on it, wanting more."
    i "Fuck, maybe next time I'll have to try and fist you."
    "Parvez gasps."
    p "P-please ..."
    i "Please what?"
    menu:
        "Please, mommy ...":
            pass
    i "Good boy ..."
    "She fucks his ass with her fingers for a while before pulling them out with a slick pop!"
    "Parvez feels his hole pulsing, with some disappointment."
    i "Sorry bro, my hand is killing me, we gotta be done."
    "Parvez sits up."
    p "Oh, yeah, of course."
    "He kisses her cheek."
    p "Thank you mommy."
    i "You're welcome baby."
label aftercare:
    scene couch
    show inanna happy at midleft
    show parvez happy at midright
    with dissolve
    play music cutesad volume 3.0
    "Parvez sits on the day bed beside Inanna."
    "She snuggles up against him, smooshing him into the pillows."
    "He feels warm and soft and tingly all over."
    "Even in his stinging butt--maybe especially so."
    "After a while Inanna gets up and goes to the kitchen, bringing over a pitcher of iced tea and some cookies."
    "They munch on the cookies and chat about Inanna's organizing, and Parvez's plans for the plants."
    "Eventually Terry texts Parvez 'wer r u' and Parvez decides to go."
    "He kisses Inanna on the cheek before he leaves."
    p "Thanks for a lovely time mama."
    i "Anytime, baby."
    $ inanna_2_complete = True
    scene cardboard with fade
    call screen chapterselect