# The script of the game goes in this file.

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
# 6 forthcoming tentacles
# 7 forthcoming preg
image cg S2A8 = "/cgs/S2A/8 alien.png"
image cg S2B = "/cgs/S2B.png"
image cg T1A = "/cgs/T1A.png"
image cg T1B = "/cgs/T1B.png"
image cg T2 = "/cgs/T2.png"
image cg T3 = "/cgs/T3.png"
image cg T4A = "/cgs/T4A.png"
image cg T4B = "/cgs/T4B.png"

## GAME START / NAVIGATION MENU

label start:
    $ strokerattempt = 1
    $ strokerused = False
    $ met_kayden = False
    $ tried_to_leave = False
    $ plantasy = False
    $ battle_1_win = False
    $ battle_2_ran = False
    $ battle_2_win = False
    $ made_ahmed_smile = False
    $ bullied_ahmed = False
    $ kayden_2_badend = False

    $ plant_encounter_1_complete = False
    $ plant_encounter_2_complete = False
    # plant encounter 3--extra skatepark scene

    $ terry_1_complete = False
    $ terry_2_complete = False
    $ terry_3_complete = False
    $ terry_4_complete = False

    $ ahmed_1_complete = False
    $ ahmed_2_complete = False

    $ kayden_1_complete = False
    $ kayden_2_complete = False

    $ solo_1_complete = False
    $ solo_2_complete = False

    $ inanna_1_complete = False
    $ inanna_2_complete = False

    $ inanna_n_javier_1_complete = False
    $ inanna_n_javier_2_complete = False
    # inanna n javier 3

    $ javier_1_complete = False

    $ chud_1_complete = False
    # chud 2

    call screen chapterselect
    return
