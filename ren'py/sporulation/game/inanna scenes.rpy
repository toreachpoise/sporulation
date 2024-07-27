label inanna_1:
    #unlocked by ahmed 1 or kayden 1
    $ inanna_points = 5
    $ asked_about_judys = 0
    "Even though the app is mostly dudes, every once in a while a woman will show up."
    "Parvez started talking to Inanna at first because of a picture she had posted of her with her dog."
    "He was an ugly little pit bull, and Parvez was obsessed with him."
    "Inanna was really cool, too. She seemed actually smart in a way that Parvez always pretended to be."
    "She was a PhD student and using her education to actually help people, building a community that was really radical."
    "Parvez just kind of laid around and jerked off most of the time, after getting half of three degrees."
    "Inanna was {i}hot{/i}, too."
    "Parvez wasn't usually into women, but she had this tightly coiled ferocity to her that was mindmelting to have turned on you."
    # chat
    lj "... I just couldn't believe they sold out to the gas company, after Ginger got faer arm broken being pulled down from a tree sit by the pigs."
    lj "Sorry, what were we talking about?"
    pdm "I think your tree hugging interlude was a way of telling me how much you want this green dick."
    lj "Hah. As if. If you really did just grow that thing then I'm sure you have no idea how to use it yet."
    lj "You need a lady to show you how."
    "She had a boyfriend, Javier, who was also trans. She said she had told xem about Parvez's profile."
    "Javier was skeptical though. Inanna told Parvez xe thought it was fake."
    pdm "I promise you it's all real."
    "He sent her a video of him bouncing his cock around."
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
    #needs bg (maybe same as ahmed coffee shop lol)
    show inanna excited at midleft
    show parvez at midright
    with dissolve
    "Inanna gets Parvez to meet her at a big queer bookstore downtown."
    i "It's the oldest still-running queer bookstore in the world."
    "It had taken Parvez an hour on the train to get there from where he lived, but it was pretty cool."
    "He wasn't sure if he'd ever been in a specifically queer bookstore before."
    "The person working the cashier had their hair dyed in trans flag colors."
    "There was a cafe with coffee and milkshakes as well as alcohol drinks. It was all so ... perfect, and wholesome."
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
    # new bg--outside
    show parvez happy at left
    show inanna happy at midleft
    with fade
    "Parvez found himself actually smiling as they stepped out of the book store into the late afternoon sunshine."
    "As soon as they do so, however, Inanna's expression turns into a frown."
    i "Shit, what are they doing here?"
    show judys at right
    with moveinright
    "There is  a group of women standing across the street from the bookstore."
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
            show judys at midright
            with move
            "JUDY" "Watch where you're going!"
            "She keeps walking right toward Parvez and Inanna, her gaze fixed on them."
            "The shorter woman is trailing behind her, looking a bit nervous."
            show judys at center
            show inanna worried:
                xalign 0.2
            show parvez worried:
                xalign -0.2
            with hpunch
            "The tall woman gets right in Inanna's face and puffs out her chest."
            "JUDY" "What did you say to me, transvestite?"
            "Inanna doesn't look phased, looking serenely down at the woman."
            i "Damn, bitch. Did you bring your insults with you from the 1950s along with your outfit?"
            "The woman turns to her recently-arrived companion, speaking to her as if Inanna and Parvez didn't understand."
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
                        "Inanna spit on the woman's shoes and strode off."
                        hide inanna with moveoutleft
                        "Parvez ran to follow her, the two women speaking in agitated tones behind him."
                        hide parvez with moveoutleft
                        # new bg or something
                        scene cardboard
                        show inanna frightened at center
                        with wipeleft
                        show parvez worried at right with moveinright
                        p "Inanna!"
                        "She rounded on him."
                        show inanna even more toppy at midright
                        with hpunch
                        i "What?"
                        i "You wanna lecture me more about how to lick boots?"
                        i "I thought you were cool under your lil tuff guy grumpyboy exterior."
                        i "But you ain't shit."
                        i "I don't care if your little plant dick is real. Cuz it's clear you don't have any balls."
                        show inanna worried at center
                        with move
                        "She turned away from him."
                        i "Don't follow me this time."
                        hide inanna with moveoutleft
                        scene cardboard with fade
                        call screen chapterselect
                    "nah, fuck them":
                        "Parvez realized in a flash that Inanna was right."
                        "These people hated them, but in a quiet way, a way that was designed to frame them as innocent even though they were the aggressors."
                        "The woman came over to Inanna, she could have ignored her."
                        pass
label judys_fight_1:
    "Marianne" "You freaks are just jealous. You use your size and natural masculinity to intimidate real women because you know you'll never become like us."
    i "Who the fuck would want to be like--{nw}"
    show parvez:
        xalign 0.15
    show inanna happy:
        xalign -0.2
    with move
    "Parvez stepped in front of Inanna, getting between her and the woman even though he was shorter than both of them."
    "He tried to steady his shaking voice as he spoke."
    p "You shouldn't be here. Leave us alone."
    "The woman looked down at Parvez and her voice dripped with condescension."
    "Marianne" "Oh honey, I don't know what sick things this monster has done to you to make you like this, but you belong with us. With other real women."
    "Parvez shoved her, his fear evaporating into anger."
    p "Fuck you, you don't know what I am."
    scene black with fade
    "It's time to fight for your right to be who you are!!"
label inanna_1_battle:
    call battle_def from _call_battle_def
    scene cardboard with dissolve
    "Transsexual battle mode activate"
    call battle_presetup from _call_battle_presetup
    call battle from _call_battle
label battle_end:
    $ battle_1_win = True
    scene cardboard
    show judys at center
    show inanna toppy:
        xalign 0.2
    show parvez toppy:
        xalign -0.2
    with dissolve
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
    show parvez at midleft
    with moveinleft
    i "The fuck you waiting for, boy? Take your pants off."
    i "I wanna see that weird green thing."
    show parvez bottomy at center
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
    # CG GOES HERE
    show inanna even more toppy at center
    show parvez bottomy at midleft
    with hpunch
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
    "She squeezed down on him to punctuate her sentence."
    i "I've had one of these since before you were born, and let me tell you baby."
    i "I'm 100 percent woman and I'm still more of a man than you'll ever be."
    menu:
        "wait, this is too much actually":
            show parvez worried with dissolve
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
    scene cardboard with fade
    call screen chapterselect