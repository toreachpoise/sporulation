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
            jump nav_menu
label meet_inanna:
    #needs bg (maybe same as ahmed coffee shop lol)
    show inanna at midleft
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
    show parvez at left
    show inanna at midleft
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
            with move
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
                        show inanna at center
                        with wipeleft
                        show parvez at right with moveinright
                        p "Inanna!"
                        "She rounded on him."
                        show inanna at midright
                        with hpunch
                        i "What?"
                        i "You wanna lecture me more about how to lick boots?"
                        i "I thought you were cool under your lil tuff guy grumpyboy exterior."
                        i "But you ain't shit."
                        i "I don't care if your little plant dick is real. Cuz it's clear you don't have any balls."
                        show inanna at center
                        with move
                        "She turned away from him."
                        i "Don't follow me this time."
                        hide inanna with moveoutleft
                        jump nav_menu
                    "nah, fuck them":
                        "Parvez realized in a flash that Inanna was right."
                        "These people hated them, but in a cool way."
                        "The woman came over to Inanna, she could have ignored her."
                        pass
label judys_fight_1:
    "Marianne" "You freaks are just jealous. You use your size and natural masculinity to intimidate real women because you know you'll never become like us."
    i "Who the fuck would want to be like--{nw}"
    show parvez at midleft
    show inanna at left
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
    "You defeated the Judys!!"
    "Oh got there's a chud, run!"
    "Sex Scene!!!"
    jump nav_menu