# The script of the game goes in this file.

## DRAMATIS PERSONAE
# The color argument colorizes the name of the character.

define p = Character("Parvez", color="#b07030")
define t = Character("Terry", color="#ff33cc")
define a = Character("Ahmed", color="#43ab75")
define k = Character("Kayden", color="#cff450")
define i = Character("Inanna", color="#8f3ce9")
define j = Character("Javier", color="#cc0000")

## VARIABLES
$ struggled = False
$ doubted = False


## GAME START

label start:

    "this is a placeholder for the app navigation screen"
label nav_menu:
    menu:
        "plant_encounter 1":
            jump plant_encounter_1
        "terry 1":
            jump terry_1
        "terry 2":
            jump terry_2
        "ahmed 1":
            jump ahmed_1
        "kayden 1":
            jump kayden_1
    return
