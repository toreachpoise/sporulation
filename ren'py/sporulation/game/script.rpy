﻿# The script of the game goes in this file.

## DRAMATIS PERSONAE
# The color argument colorizes the name of the character.

define p = Character("Parvez", color="#b07030")
define t = Character("Terry", color="#ff33cc")
define a = Character("Ahmed", color="#43ab75")
define k = Character("Kayden", color="#cff450")
define i = Character("Inanna", color="#8f3ce9")
define j = Character("Javier", color="#cc0000")

define npc = Character("NEON PUNK CUNTBOY", color="#cff450")
define pdm = Character("PLANT DICK MAN", color="#b07030")

## VARIABLES
$ struggled = False
$ doubted = False
$ struggled_again = False
$ plantflation = False
$ met_kayden = False
$ tried_to_leave = False


## GAME START

label start:

    "this is a placeholder for the app navigation screen"
label nav_menu:
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
    return
