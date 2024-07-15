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

## BGS
# these are just placeholder thumbnails for now

image ahmed balcony = "/bgs/ahmed-balcony.png"
image ahmedbed = "/bgs/ahmed-bed.png"
image ahmedshelves = "/bgs/ahmed-shelves.png"
image cardboard = "/bgs/cardboard.png"
image couch = "/bgs/couch.png"
image bed = "/bgs/p&t-bed.png"
image kitchen = "/bgs/kitchen.png"
image inannabed = "/bgs/i&j-bed.png"
image skatepark interior = "/bgs/skatepark-int.png"
image skatepark ramps = "/bgs/skatepark-ramps.png"
image skatepark hill = "/bgs/skatepark-up-high.png"
image plant far = "/bgs/woods-2.png"
image plant midway = "/bgs/woods-3.png"
image plant closeup = "/bgs/woods-1.png"

## CHARACTER SPRITES
# these are just placeholder sprites for now, they need expressions

image ahmed = "/character sprites/ahmed.png"
image ahmed bottomy = "/character sprites/ahmed bottomy.png"
image ahmed crying = "/character sprites/ahmed crying.png"
image ahmed overwhelmed = "/character sprites/ahmed overwhelmed.png"
image ahmed speaking = "/character sprites/ahmed speaking.png"

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

image terry = "/character sprites/terry.png"
image terry angry = "/character sprites/terry angry.png"
image terry embarrassed = "/character sprites/terry embarrassed.png"
image terry toppy = "/character sprites/terry toppy.png"
image terry worried = "/character sprites/terry worried.png"

image parvez n terry = "/character sprites/parvez n terry.png"

image judys = "/character sprites/judys without kayden.png"

image judys n kayden = "/character sprites/judys with kayden.png"

image chud = "/character sprites/chud.png"

image judys n chud = "/character sprites/judys n chud.png"

image bs = im.FactorScale("battle/battlescene.png", 1.5)

## CGs
# these will be artworks depicting certain scenes, we'll see how many of them get made lol

image plant_encounter_1_cg1 = "/cgs/plants concept.png"


## GAME START / NAVIGATION MENU

label start:
    $ strokerattempt = 1
    $ strokerused = False
    "this is a placeholder for the app navigation screen"
    jump nav_menu
    return
