﻿# The script of the game goes in this file.

## DRAMATIS PERSONAE
# The color argument colorizes the name of the character.

define p = Character("Parvez", color="#85511d")
define t = Character("Terry", color="#7d282f")
define a = Character("Ahmed", color="#258654")
define k = Character("Kayden", color="#617b0a")
define i = Character("Inanna", color="#8f3ce9")
define j = Character("Javier", color="#cc0000")

define npc = Character("neonpunkcuntboi", color="#617b0a")
define pdm = Character("plantdickman", color="#b07030")
define lj = Character("snakewoman", color="#8f3ce9")
define mm = Character("mathlord", color="#258654")
define cg = Character("clowngender", color="#cc0000")

## BGS

image alley = "/bgs/alley.png"
image ahmedbed = "/bgs/ahmed-bed.png"
image ahmedshelves = "/bgs/ahmed-shelves.png"
image balcony = "/bgs/ahmed-balcony.png"
image bed = "/bgs/p&t-bed.png"
image cardboard = "/bgs/cardboard.png"
image chudhideout = "/bgs/chud-hideout.png"
image coffeeshop1 = "/bgs/coffeeshop-1.png"
image coffeeshop2 = "/bgs/coffeeshop-2.png"
image couch = "/bgs/couch.png"
image inannabed = "/bgs/i&j-bed.png"
image kitchen = "/bgs/kitchen.png"
image plant far = "/bgs/woods-2.png"
image plant midway = "/bgs/woods-3.png"
image plant closeup = "/bgs/woods-1.png"
image skatepark interior = "/bgs/skatepark-int.png"
image skatepark ramps = "/bgs/skatepark-ramps.png"
image skatepark hill = "/bgs/skatepark-up-high.png"
image skatepark bonus = "/bgs/skatepark-bonus.png"
image spiral:
    "/bgs/spiral/00001.png"
    pause 0.1
    "/bgs/spiral/00002.png"
    pause 0.1
    "/bgs/spiral/00003.png"
    pause 0.1
    "/bgs/spiral/00004.png"
    pause 0.1
    "/bgs/spiral/00005.png"
    pause 0.1
    "/bgs/spiral/00006.png"
    pause 0.1
    "/bgs/spiral/00007.png"
    pause 0.1
    "/bgs/spiral/00008.png"
    repeat #In case you want it looping, might want to add another pause

## CHARACTER SPRITES

image ahmed = "/character sprites/ahmed.png"
image ahmed bottomy = "/character sprites/ahmed bottomy.png"
image ahmed crying = "/character sprites/ahmed crying.png"
image ahmed overwhelmed = "/character sprites/ahmed overwhelmed.png"
image ahmed speaking = "/character sprites/ahmed speaking.png"
image ahmed flip = im.Flip("/character sprites/ahmed.png", horizontal=True)
image ahmed flip bottomy = im.Flip("/character sprites/ahmed bottomy.png", horizontal=True)
image ahmed flip crying = im.Flip("/character sprites/ahmed crying.png", horizontal=True)
image ahmed flip overwhelmed = im.Flip("/character sprites/ahmed overwhelmed.png", horizontal=True)
image ahmed flip speaking = im.Flip("/character sprites/ahmed speaking.png", horizontal=True)

image inanna = "/character sprites/inanna.png"
image inanna even more toppy = "/character sprites/inanna even more toppy.png"
image inanna excited = "/character sprites/inanna excited.png"
image inanna frightened = "/character sprites/inanna frightened.png"
image inanna happy = "/character sprites/inanna happy.png"
image inanna toppy = "/character sprites/inanna toppy.png"
image inanna worried = "/character sprites/inanna worried.png"

image javier = "/character sprites/javier.png"
image javier crying = "/character sprites/javier crying.png"
image javier happy = "/character sprites/javier happy.png"
image javier worried = "/character sprites/javier worried.png"

image inanna n javier = "/character sprites/inanna n javier.png"

image kayden = "character sprites/kayden.png"
image kayden bottomy = "character sprites/kayden bottomy.png"
image kayden threatening = "character sprites/kayden threatening.png"

image parvez = "/character sprites/parvez.png"
image parvez bottomy = "/character sprites/parvez bottomy.png"
image parvez crying = "/character sprites/parvez crying.png"
image parvez happy = "/character sprites/parvez happy.png"
image parvez toppy = "/character sprites/parvez toppy.png"
image parvez worried = "/character sprites/parvez worried.png"
image parvez flip = im.Flip("/character sprites/parvez.png", horizontal=True)
image parvez flip bottomy = im.Flip("/character sprites/parvez bottomy.png", horizontal=True)
image parvez flip crying = im.Flip("/character sprites/parvez crying.png", horizontal=True)
image parvez flip happy = im.Flip("/character sprites/parvez happy.png", horizontal=True)
image parvez flip toppy = im.Flip("/character sprites/parvez toppy.png", horizontal=True)
image parvez flip worried = im.Flip("/character sprites/parvez worried.png", horizontal=True)

image terry = "/character sprites/terry.png"
image terry angry = "/character sprites/terry angry.png"
image terry embarrassed = "/character sprites/terry embarrassed.png"
image terry toppy = "/character sprites/terry toppy.png"
image terry worried = "/character sprites/terry worried.png"
image terry worried flip = im.Flip("/character sprites/terry worried.png", horizontal=True)

image parvez n terry = "/character sprites/parvez n terry.png"

image judys = "/character sprites/judys without kayden.png"
image judys flip = im.Flip("/character sprites/judys without kayden.png", horizontal=True)

image judys n kayden = "/character sprites/judys with kayden.png"

image chud = "/character sprites/chud.png"
image chud flip = im.Flip("/character sprites/chud.png", horizontal=True)
image chud2 = im.Flip("/character sprites/chud.png", horizontal=True)

image judys n chud = "/character sprites/judys n chud.png"

image bs = im.FactorScale("battle/battlescene.png", 1.5)

## battle animations
image inanna_sprite:
    "battle/ina_0000.png"
    pause 0.2
    "battle/ina_0001.png"
    pause 0.2
    "battle/ina_0002.png"
    pause 0.2
    "battle/ina_0003.png"
    pause 0.2
    repeat
image inanna_sprite_idle:
    "battle/ina_0000_idle.png"
    pause 0.2
    "battle/ina_0001_idle.png"
    pause 0.2
    "battle/ina_0002_idle.png"
    pause 0.2
    "battle/ina_0003_idle.png"
    pause 0.2
    repeat
image parvez_sprite:
    "battle/parv_0000.png"
    pause 0.3
    "battle/parv_0001.png"
    pause 0.3
    repeat
image parvez_sprite_idle:
    "battle/parv_0000_idle.png"
    pause 0.3
    "battle/parv_0001_idle.png"
    pause 0.3
    repeat
image chud_sprite:
    "battle/chud_idle_0000.png"
    pause 0.5
    "battle/chud_idle_0001.png"
    pause 0.5
    repeat
image chud2_sprite:
    "battle/chud2_idle_0000.png"
    pause 0.5
    "battle/chud2_idle_0001.png"
    pause 0.5
    repeat
image kaye_sprite:
    "battle/dekayden_idle_0000.png"
    pause 0.5
    "battle/dekayden_idle_0001.png"
    pause 0.5
    repeat
image marianne_sprite:
    "battle/marianne_idle_0000.png"
    pause 0.5
    "battle/marianne_idle_0001.png"
    pause 0.5
    repeat
image sarah_sprite:
    "battle/sarah_idle_0000.png"
    pause 0.5
    "battle/sarah_idle_0001.png"
    pause 0.5
    repeat
image javier_sprite:
    "/battle/javier_0000.png"
    pause 0.33
    "/battle/javier_0001.png"
    pause 0.33
    repeat
image javier_sprite_idle:
    "/battle/javier_idle_0000.png"
    pause 0.33
    "/battle/javier_idle_0001.png"
    pause 0.33
    repeat
image terry_sprite:
    "/battle/terry_0000.png"
    pause 0.26
    "/battle/terry_0001.png"
    pause 0.26
    repeat
image terry_sprite_idle:
    "/battle/terry_idle_0000.png"
    pause 0.26
    "/battle/terry_idle_0001.png"
    pause 0.26
    repeat

## CGs
# these will be artworks depicting certain scenes, we'll see how many of them get made lol

image cg A1A = "/cgs/A1A.png"
image cg A1B = "/cgs/A1B.png"
image cg A1C = "/cgs/A1C.png"
image cg A2A = "/cgs/A2A.png"
image cg A2B = "/cgs/A2B.png"
image cg C1A = "/cgs/C1A.png"
image cg C1B = "/cgs/C1B.png"
image cg I1 = "/cgs/I1.png"
image cg I2A = "/cgs/I2A.png"
image cg I2B = "/cgs/I2B.png"
image cg InJ1A = "/cgs/InJ1A.png"
image cg InJ1B = "/cgs/InJ1B.png"
image cg J1A = "/cgs/J1A.png"
image cg J1B :
    "/cgs/J1B1.png"
    pause 0.3
    "/cgs/J1B2.png"
    pause 0.3
    "/cgs/J1B3.png"
    pause 0.3
    "/cgs/J1B4.png"
    pause 0.3
    "/cgs/J1B5.png"
image cg J1C = "/cgs/J1C.png"
image cg K1 = "/cgs/K1.png"
image cg K2A = "/cgs/K2A.png"
image cg K2B = "/cgs/K2B.png"
image cg K2C = "/cgs/K2C.png"
image cg PE1 = "/cgs/PE1.png"
image cg PE2 = "/cgs/PE2.png"
image cg S1 = "/cgs/S1.png"
image cg S2A1 = "/cgs/S2A/1 abduction.png"
image cg S2A2 = "/cgs/S2A/2 abduction.png"
image cg S2A3 = "/cgs/S2A/3 aliens.png"
image cg S2A4 = "/cgs/S2A/4 space.png"
image cg S2A5 = "/cgs/S2A/5 cry.png"
image cg S2A6 = "/cgs/S2A/6 tentacles.png"
image cg S2A7 = "/cgs/S2A/7 alien.png"
image cg S2A8 = "/cgs/S2A/8 preg.png"
image cg S2B = "/cgs/S2B.png"
image cg T1A = "/cgs/T1A.png"
image cg T1B = "/cgs/T1B.png"
image cg T2 = "/cgs/T2.png"
image cg T3 = "/cgs/T3.png"
image cg T4A = "/cgs/T4A.png"
image cg T4B = "/cgs/T4B.png"

image purple = "/bgs/purple.png"
image splash:
    "/splashscreen/0.png"
    pause 0.2
    "/splashscreen/1.png"
    pause 0.2
    "/splashscreen/2.png"
    pause 0.2
    "/splashscreen/3.png"
    pause 0.2
    "/splashscreen/4.png"
    pause 0.2
    "/splashscreen/5.png"
    pause 0.2
    "/splashscreen/6.png"
    pause 0.2
    "/splashscreen/7.png"
    pause 0.2
    "/splashscreen/8.png"
    pause 0.2
    "/splashscreen/9.png"
    pause 0.2
    "/splashscreen/10.png"
    pause 0.2
    "/splashscreen/11.png"
    pause 0.2
    "/splashscreen/12.png"
    pause 0.2
    "/splashscreen/13.png"
    pause 0.2
    "/splashscreen/14.png"
    pause 0.2
    "/splashscreen/15.png"
    pause 0.2
    "/splashscreen/16.png"
    pause 0.2
    "/splashscreen/17.png"
    pause 0.2
    "/splashscreen/18.png"
    pause 0.2
    repeat
image cover img = "cover img.png"
image barrowboy = "/splashscreen/barrow boy.png"
image titletext = ParameterizedText(xalign=0.25, yalign=0.5, size=72)

# music
define audio.maintheme = "/sounds/game theme draft.mp3" ## close, atmospheric, rhythmic
define audio.forest = "/sounds/game draft again.mp3" ##creepy, eerie, kinda sanctified vibes, also rain/wet noises lol
define audio.friendcore = "/sounds/Friendcore.wav" # fun n cute
define audio.fightmusic = "/sounds/Sporulation Fight.wav" # action babeyy
define audio.planty = "/sounds/planty ambient.mp3" # upbeat, creepy but in a fun way
define audio.badvibes = "/sounds/sporulation draft.mp3" # grimy, crackly, pushy beat
define audio.cutesad = "/sounds/cute and sad.wav"
define audio.floaty = "/sounds/game draft drumless.mp3" # string instruments, breathy, floaty

#sfx
define audio.fanfare = "/sounds/Fanfare2.mp3"
define audio.battlestart = "/sounds/Start_Press.wav"
define audio.defeated = "/sounds/Menu_Error_1.wav"
define audio.heal = "/sounds/heal.wav"
define audio.beam = "/sounds/beam.wav"
define audio.dazzle = "/sounds/dazzle.wav"
define audio.hit = "/sounds/Hit.wav"
define audio.heal = "/sounds/heal.wav"


## setting up variables

default strokerattempt = 1
default strokerused = False
default met_kayden = False
default tried_to_leave = False
default plantasy = False
default battle_1_win = False
default battle_2_ran = False
default battle_2_win = False
default made_ahmed_smile = False
default bullied_ahmed = False
default didnt_fuck_kayden = False
default kayden_2_badend = False
default inanna_sent_me = False
default javier_tells = False
default had_threeway = False
default panicked = False

default plant_encounter_1_complete = False
default plant_encounter_2_complete = False
# plant encounter 3--extra skatepark scene

default terry_1_complete = False
default terry_2_complete = False
default terry_3_complete = False
default terry_4_complete = False

default ahmed_1_complete = False
default ahmed_2_complete = False

default kayden_1_complete = False
default kayden_2_complete = False

default solo_1_complete = False
default solo_2_complete = False

default inanna_1_complete = False
default inanna_2_complete = False

default inanna_n_javier_1_complete = False
default inanna_n_javier_2_complete = False
default inanna_n_javier_3_complete = False

default javier_1_complete = False

default chud_1_complete = False

## LOADING/SPLASHSCREEN
label splashscreen:
    play music forest
    scene black
    pause 1
    show barrowboy at sizedown
    with dissolve
    show titletext "Toreachpoise presents ...":
        yalign 0.2
    pause 3
    scene purple with None
    show splash at sizeup
    with dissolve
    pause 10
    hide splash
    show cover img
    with dissolve
    pause 5
    scene black with dissolve
    return


## GAME START

label start:
    "This story contains numerous depictions of sex, kink, and sexual violence, as well as transphobia. It's recommended for adult audiences."
    menu:
        "This story contains numerous depictions of sex, kink, and sexual violence, as well as transphobia. It's recommended for adult audiences.{fast}.. Continue?"
        "yes":
            call screen chapterselect
        "no":
            $ renpy.quit()

    return

label endcredits:
    play music maintheme
    "Thank you for playing Sporulation!"
    "We hope you enjoyed it half as much as we enjoyed making it."
    "Sporulation was mostly made by Aaron El Sabrout. The music is by Nephenee Rose and Cartoon Wetwork, with SFX by Cartoon Wetwork. Battle sprite animations by Galateas Grievance. Solo 2 illustrations by Breezy."
    "Additional credit information and links can be found in the about section."
    menu:
        "continue game":
            call screen chapterselect
        "start over":
            $ renpy.full_restart(transition=fade)
        "save and quit":
            $ renpy.quit(save=True)