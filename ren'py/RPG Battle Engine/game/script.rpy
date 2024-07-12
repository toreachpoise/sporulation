# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")


# The game starts here.
label start:
    call battle_def
    
    scene black with fade
    e"This is your normal game"
    scene bb with dissolve
    "battle system on"
    call battle_presetup
    call battle
label battle_end:
    "congratulations you won the battle!"
    scene black with fade
    "and another scene...."
    return
