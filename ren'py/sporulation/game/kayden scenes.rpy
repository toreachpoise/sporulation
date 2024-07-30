label kayden_1:
    #(unlocked by terry 2)
    $ didnt_fuck_kayden = False
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
    $ kayden_1_complete = True
    scene cardboard with fade
    call screen chapterselect
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
            $ didnt_fuck_kayden = True
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
            $ kayden_1_complete = True
            scene cardboard with fade
            call screen chapterselect
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
    $ kayden_1_complete = True
    scene cardboard with fade
    call screen chapterselect

label kayden_2:
    $ it_was_kayden = False
    $ kayden_2_badend = False
    scene bed
    show parvez worried at center
    with dissolve
    "NEONPUNKCUNTBOI has reappeared on the app."
    "It's Kayden's same profile, still, same pictures, same description:{w} 'nonbinary trans dude looking to get their holes stuffed'."
    "Parvez wonders what all that is about."
    menu:
        "Maybe it wasn't actually Kayden that Parvez saw with the judys ..."
        "it definitely was":
            $ it_was_kayden = True
            "Parvez would recognize them anywhere."
            "Even with their hair covered by the strange helmet, and the weird change of aesthetic into a powerpuff girls nurse."
            "That was definitely their voice, talking to Marianne."
            if (battle_2_ran == False) and (didnt_fuck_kayden == False):
                "And when Parvez hit them they had made the same sounds as when he was fucking them."
                "He feels an uncomfortable flush climb up his neck as he thinks about this."
            "It's wild to think about them jumping sides so fast, though."
            "Even if you realize that you're not really trans, why would you betray other trans people?"
            "After all, detransitioners have most of the same experiences as trans people and then some."
            "Trans people and detransitioners are the most alike out of any two groups."
            "Kayden was definitely always an unhinged weirdo, though. Parvez already knows that."
            "He decides to confront them."
            jump check_out_kaydens_pf
        "it probably wasn't":
            $ it_was_kayden = False
            "Kayden was definitely weird but they couldn't have gone down the detransitioner to full on transphobe pipeline that fast, right?"
            "Parvez can't imagine doing something like that. Even if you realize that you're not really trans, why would you betray other trans people?"
            "After all, detransitioners have most of the same experiences as trans people and then some."
            "Trans people and detransitioners are the most alike out of any two groups."
            "Parvez must have just been mistaken about what he saw."
            "He decides to message Kayden to see how they've been doing."
            jump check_out_kaydens_pf
label check_out_kaydens_pf:
    pdm "heyy"
    pdm "havent seen you on here in a while"
    pdm "it was kayden right?"
    npc "huh, fucking typical"
    npc "you don't even remember my name"
    npc "im sure you would remember my hole though, you freak"
    if it_was_kayden == False:
        "Why are they reacting like this? Parvez is just trying to be friendly."
    pdm "sorry, we just havent chatted in a bit"
    pdm "how have you been?"
    npc "i think you know how ive been"
    if didnt_fuck_kayden == True:
        npc "first your bitch ass was too cowardly to even fuck me"
        npc "and thank god for that"
        npc "i dont know what i would do if that unholy thing that grows out of you had defiled my body ..."
    else:
        npc "first you defiled me with your unholy ... thing ..."
    if battle_2_ran == True:
        npc "then you were too afraid to even face me"
        npc "as you should, we would have slaughtered you"
    elif battle_2_win == True:
        npc "then you crushed me into the dirt, as if i were nothing"
    else:
        npc "then we defeated you and your weak faggot friends"
    if it_was_kayden == False:
        "Holy shit ... it must really have been Kayden, or Kaye now, whatever they're called."
        "Parvez can't believe it."
    else:
        "Damn, that slimy weasel. It really was them that jumped ship. Parvez had kind of hoped they hadn't."
        "Well, there was no point in trying to be subtle any more."
    pdm "why would you join them in the first place?"
    pdm "aren't you trans like me?"
    npc "i was sick like you"
    npc "they showed me the light"
    npc "they brought me into their fold"
    npc "the women's space"
    npc "where i really belong"
    npc "and where you belong too"
    pdm "you're crazy"
    pdm "you think those people respect you?"
    pdm "i'm sure they still think of you as a freak"
    npc "they have accepted me as one of them now that i have healed myself"
    npc "my god has cleansed what was evil within me"
    npc "you could be healed too"
    npc "i can show you"
    menu:
        "meet them (kick their ass)":
            jump confront_kayden
        "sounds like a bad idea":
            pdm "you're out of your mind lmao"
            pdm "i just wanted to see if it was really you"
            pdm "guess you really are just a pathetic self-hating loser"
            npc "i hope that god will heal you"
            npc "you are deeply sick"
            npc "that you would mutilate your body and spread the cancer to others"
            npc "is a true tragedy and a sickness"
            "They're still typing when Parvez mashes the block button."
            "He's shaking, full of rage."
            "He throws his phone across the bed."
            "It hits right on the edge and slides off, thunking dully on the floor."
            p "Ugh, fuck this shit ..."
            p "... I wanna have a wank ..."
            $ kayden_2_complete = True
            scene cardboard with fade
            call screen chapterselect
label confront_kayden:
    "Parvez feels like he might regret this, but he has to know what has gone wrong with Kayden."
    scene cardboard with pushleft
    #replace with laundromat bg
    show parvez at midright
    with moveinright
    "The place where they want to meet him this time is even sketchier than last time."
    "It appears to be an abandoned laundromat."
    "There's a dripping noise that echoes throughout the space."
    "This really was a bad idea ...{w} Parvez moves to leave.{nw}"
    k "Damn, you really did come."
    show kayden threatening at furthestleft
    with moveinleft
    "Kaye emerges from the shadow of a doorway on the other side of the room."
    k "You're even dumber than I thought."
    k "Either that or you really must want salvation."
    show kayden threatening at midleft
    with move
    "They keep moving toward Parvez."
    show parvez worried with dissolve
    p "S-Stay back!!"
    show kayden threatening at center
    with move
    k "You want to see what true healing looks like."
    k "Secretly you want to be saved."
    "Parvez is certain he shouldn't have come here."
    if didnt_fuck_kayden == False:
        k "Even though you planted the seeds of vileness inside me, I have been restored."
        "They lift their skirt. They're still not wearing any panties, just like before, and this gives Parvez a moment of brief relief before he sees what's underneath."
        #cg
        "Their pussy lips are spread wide open, but no dick emerges from it. Instead there is a circular, glassy surface."
        "Or, more like gooey, actually. Like a leaf of aloe vera chopped in half."
        "The cut looks scabbed around the edges, but still fresh in the middle. Something clear oozes from it. Parvez feels sick."
        p "Holy shit."
        show parvez worried at furthestright
        with move
        "Parvez backpedals away from them."
        p "W--why would you do that?"
        p "Holy fuck."
        p "Y-you mutilated yourself."
        k "No, it was you who mutilated me. I am healed now. My body is restored."
        p "But it's not--look! It's still alive and trying to grow."
        "Kaye's expression falters but then they cover it up."
        k "The cancer must be burned several times to be fully removed, yes."
        k "But this is proof of my healing journey."
        k "And it is what you must also do to be restored."
        p "You're out of your fucking mind."
        p "Get away from me!"
    else:
        k "We must cleanse the vileness that has grown inside you."
        k "We must restore your body to its proper state so you can be healed."
        p "Damn bitch you really are crazy."
        p "Get the fuck away from me!"
    show chud at furthestleft
    show chud2 at farleft
    with moveinleft
    "Two chuds appear in the shadows behind Kaye."
    p "Oh fuck."
    show chud at farleft
    show chud2 at midleft
    "They close in quickly on Parvez."
label kayden_2_battle:
            call battle_4_def from _call_battle_def_4
            scene cardboard with dissolve
            "Transsexual battle mode activate"
            call battle_4_presetup from _call_battle_presetup_4
            call battle_4 from _call_battle_4
label kayden_2_badend:
    $ kayden_2_badend = True
    show chud at farleft
    show chud2 at midleft
    show kayden threatening at center
    with irisin
    "Parvez is no match for Kaye and two chuds."
    "Parvez can hardly stand. His head rings from where one of the chuds had bashed it into the concrete."
    "One of them slides behind him and secures his arms, frogmarching him over to a low table."
    "The other chud pulls his shorts down."
    "Chud 2" "Damn, look at this bitch's weird fake dick."
    "Chud 1" "Shit's freaky, huh?"
    "Kaye" "Don't worry, it won't be there for long."
    # cg2
    "Kaye produces a heavy cleaver."
    "Kaye" "Hold her steady."
    p "No, no wait, no. Don't do this."
    p "Look I know you're really messed up in the head, and I'm sorry for what I did to you, if you really didn't want it."
    p "But you can't do this. This is a part of my body. Please. Please!!!"
    "Kaye ignores him."
    "The chud not holding Parvez's arms pulls his dick up and lays it on the table."
    "Kaye raises the blade."
    "Parvez closes his eyes."
    "There's a schwing and then a loud thud."
    "He hears the knife hit the table, and for a moment feels nothing."
    "Then his whole body is suffused with a burning agony."
    p "Agh!! fuck!!!!!"
    "He opens his eyes even as they are filling with tears."
    "Kayden has cut his dick off."
    "The little green tube sits uselessly on the table, oozing from the cut and already wilting now that it's detached from its life source."
    "The end inside of Parvez is gushing clear green goo."
    "He can hear himself screaming but the pain has consumed all his awareness."
    "Dimly he can hear the chuds and Kaye speaking but he's not really listening."
    "Kaye" "Well, that takes care of that."
    "Chud 2" "I mean, not really. There's still some inside. That's not a normal pussy if I've ever seen one."
    "Kaye" "Indeed. Who knows if you have, other than that of some child you've molested."
    "Chud 2" "Hey!"
    "Chud 1" "Don't worry, I can fix that."
    "Parvez feels himself being hauled up by the two arms pinned behind his back."
    "He's not sure what's about to happen until the burning where his cock used to be is replaced with a brutal, stabbing pain."
    "He looks down."
    # cg3
    "The chud's huge cock is inside him."
    "Parvez can feel it churning around in his pussy, pulverizing what remains of his cock."
    "He's biting his lip to stifle the groans of agony that the chud is pounding out of him."
    "Chud 1" "Damn this pussy is tight."
    "Chud 1" "Good thing this weird goo makes good lube."
    "Chud 1" "... Wait, I'm not gonna catch mutant AIDS off this freak, right?"
    "Kaye" "No, it's harmless."
    "Parvez looks at Kaye but they aren't looking at him."
    "They're facing away, deliberately avoiding his gaze, no doubt grateful they managed to avoid this fate."
    "Blood is running down Parvez's chin from his bitten lip. He keeps his focus on that pain, ignoring the jostling that is consuming his whole body, the squelching and mashing sounds coming from inside him."
    "Chud 2" "Hey, quit hogging the slut, I want a turn!"
    "Chud 1" "Hold on bro I'm almost done."
    "The chud grunts loudly and finishes inside Parvez, before passing him on to the other one like a rag doll."
    "Parvez is limp, dimly aware, oozing from his hole."
    "A moment of relief passes through him when the first chud pulls out of him, leaving only the throbbing of his mashed insides."
    "Then the other chud thrusts into him brutally deep and resumes raping him."
    "When they're finally finished with him, they leave Parvez on the table, numb and battered, oozing chud cum and the remains of his dick out of his raw pussy."
    "Kaye stands over him and looks down, finally catching his gaze. They look ... sad."
    "Kaye" "This didn't have to happen ... if you'd just ... not gone down this path..."
    "Parvez doesn't have the energy to speak, but he musters his last reserves to spit at Kaye."
    "They don't react, his saliva trickles down their cheek for a moment before they turn and walk away."
    "Parvez blacks out."
    scene black with dissolve
    "He wakes up cold and in pain all over. Most intensely, his pussy throbs, the remnants of his cock screaming in pain all the way up into his womb."
    "His head is still ringing from the concussion he must have sustained during the battle, too."
    "He pulls out his phone and calls Inanna, his eyes burning from the brightness."
    p "Inanna I ... something bad happened ... I need help."
    "She comes to get him."
    "Once she sees the state of him, she doesn't bother asking what happened."
    scene kitchen
    show terry worried at midright
    with wipeleft
    show inanna worried at farleft
    show parvez crying at furthestleft
    with moveinleft
    t "Where have you been babe?? I've been so worried."
    "Parvez doesn't say anything."
    i "He was attacked."
    show terry worried at farleft
    show inanna worried at center
    with move
    "Terry pushes in front of her to see Parvez."
    t "Holy fuck, baby, what happened???"
    p "Terry ... please ... I can't ..."
    "Inanna had dressed him again, but Parvez is oozing through his shorts, the whole bottom of them wet, his own dick remains running down his leg, mixed with fascist jizz."
    "Parvez starts crying at the worried look on Terry's face."
    "Terry embraces him."
    t "Shh, it's okay baby. It's okay."
    "Terry takes him to the bathroom and undresses him."
    "Parvez moves to cover himself but Terry sees, with a horrified gasp."
    t "Baby ... what?"
    p "Please ... I don't ..."
    "Parvez is sobbing."
    t "Shh ... it's okay, you're okay."
    "They don't look like they believe that. Parvez certainly doesn't."
    "They wash him with a tenderness that hurts almost as much as being raped by the chuds."
    "Then they put him to bed."
    scene bed with wipeleft
    "Parvez doesn't sleep, but his head is still ringing and he's grateful to at least be somewhere still and dark."
    "He can hear Terry and Inanna arguing in the kitchen."
    t "We have to find who did this to him!"
    i "I know who did this."
    t "Then we have to call the police!"
    "Inanna's voice is grim, monotone."
    i "They probably are the police."
    i "When we saw those bitches last time they said they knew the city council."
    i "You know the pigs won't protect people like us."
    t "We have to do something! Look what they did to him!"
    "Inanna's voice softens."
    i "Honey, I know. But what can we do?"
    i "All we can do is take care of each other, and make sure it doesn't happen again."
    "Inanna leaves a while later and Terry comes to bed."
    "Parvez pretends to be asleep."
    "He can hear them crying beside him. He feels like he should comfort them, but he doesn't have the energy, or even know how."
    "Over the next few days, the rest of Parvez's cock falls out in green slimy chunks."
    "In a perverse way, it reminds him of having a period: the stabbing pain in his belly, the soreness, the messy underwear."
    "This doesn't bring him any humor, though."
    "Mostly Parvez feels empty."
    "He feels like whatever was growing inside him has been replaced by a nothingness, a black hole that sucks all feeling into it."
    "Terry tries to touch him, to comfort him and cheer him up, but he wants nothing to do with them."
    "He can't find the enthusiasm for anything. All he can manage is to wallow, to lay down and wait to die."
    $ kayden_2_complete = True
    scene cardboard with fade
    call screen chapterselect
label kayden_2_goodend:
    "Parvez can't believe he's actually defeated Kaye and the two chuds."
    "He runs home as fast as he can, calling Inanna on the way to report what had happened."
    i "Damn, you're amazing, I can't believe you got away."
    i "We can't let anything like that happen again, though."
    i "From now on we have to travel in pairs, at least. Full buddy system mode."
    "Parvez chuckles."
    p "Yes mommy."
    i "Now don't go taking that tone with me young man. I just want you to be safe."
    "He finds himself playing the role of a child, taking a petulant tone."
    p "I knowww ..."
    $ kayden_2_complete = True
    scene cardboard with fade
    call screen chapterselect