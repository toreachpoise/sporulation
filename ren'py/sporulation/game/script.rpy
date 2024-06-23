# The script of the game goes in this file.

## DRAMATIS PERSONAE
# The color argument colorizes the name of the character.

define p = Character("Parvez", color="#b07030")
define t = Character("Terry", color="#ff33cc")
define a = Character("Ahmed", color="#43ab75")
define k = Character("Kayden", color="#cff450")
define i = Character("Inanna", color="#8f3ce9")
define j = Character("Javier", color="#cc0000")


## GAME START

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    "eventually there will be a menu screen for chapter navigation, but for now it's in order of me writing the scenes lol"
    jump plant_encounter_1
    return
