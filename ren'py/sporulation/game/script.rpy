# The script of the game goes in this file.

## DRAMATIS PERSONAE
# The color argument colorizes the name of the character.

define p = Character("Parvez", color="#85511d")
define t = Character("Terry", color="#7d282f")
define a = Character("Ahmed", color="#258654")
define k = Character("Kayden", color="#617b0a")
define i = Character("Inanna", color="#8f3ce9")
define j = Character("Javier", color="#cc0000")

define npc = Character("cuntboi", color="#617b0a")
define pdm = Character("plantman", color="#b07030")

## BGS
# these are just placeholder thumbnails for now

image ahmed balcony = "/bgs/ahmed-balcony.png"
image ahmed bed = "/bgs/ahmed-bed.png"
image ahmed shelves = "/bgs/ahmed-shelves.png"
image cardboard = "/bgs/cardboard.png"
image couch = "/bgs/couch.png"
image bed = "/bgs/p&t-bed.png"
image kitchen = "/bgs/kitchen.png"
image inanna bed = "/bgs/i&j-bed.png"
image skatepark interior = "/bgs/skatepark-int.png"
image skatepark ramps = "/bgs/skatepark-ramps.png"
image skatepark hill = "/bgs/skatepark-up-high.png"
image plant far = "/bgs/woods-2.png"
image plant midway = "/bgs/woods-3.png"
image plant closeup = "/bgs/woods-1.png"

## CHARACTER SPRITES
# these are just placeholder sprites for now, they need expressions

image ahmed = "/character sprites/ahmed.png"
image inanna = "/character sprites/inanna n javier.png"
image javier = "/character sprites/inanna n javier.png"
image kayden = "character sprites/kayden.png"
image parvez = "/character sprites/parvez.png"
image terry = "/character sprites/terry.png"
image parvez n terry = "/character sprites/parvez n terry.png"

## CGs
# these will be artworks depicting certain scenes, we'll see how many of them get made lol

image plant_encounter_1_cg1 = "/cgs/plants concept.png"


## GAME START / NAVIGATION MENU

label start:
    $ strokerattempt = 1
    $ strokerused = False
    "this is a placeholder for the app navigation screen"
label nav_menu:
    scene cardboard with fade
    menu:
        "plant encounter 1":
            jump plant_encounter_1
        "terry 1":
            jump terry_1
        "terry 2":
            jump terry_2
        "ahmed 1":
            jump ahmed_1
        "kayden 1":
            jump kayden_1
        "plant encounter 2":
            jump plant_encounter_2
        "solo 1" if strokerused == False:
            jump solo_1
    return
