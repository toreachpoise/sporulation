label nav_menu:
    scene cardboard with fade
    menu:
        "plant encounters":
            jump plant_encounter_list
        "terry encounters":
            jump terry_encounter_list
        "ahmed encounters":
            jump ahmed_encounter_list
        "kayden encounters":
            jump kayden_encounter_list
        "solo scenes":
            jump solo_encounter_list
        "inanna encounters":
            jump inanna_encounter_list
        "inanna and javier encounters":
            jump inanna_n_javier_encounter_list
        "battles":
            jump battles_list

label plant_encounter_list:
    menu:
        "plant encounter 1":
            jump plant_encounter_1
        "plant encounter 2":
            jump plant_encounter_2

label terry_encounter_list:
    menu:
        "terry 1":
            jump terry_1
        "terry 2":
            jump terry_2

label ahmed_encounter_list:
    menu:
        "ahmed 1":
            jump ahmed_1
        "ahmed 2":
            jump ahmed_2

label kayden_encounter_list:
    menu:
        "kayden 1":
            jump kayden_1

label solo_encounter_list:
    menu:
        "solo 1": ##if strokerused == False
            jump solo_1

label inanna_encounter_list:
    menu:
        "inanna 1":
            jump inanna_1

label inanna_n_javier_encounter_list:
    menu:
        "inanna and javier 1":
            jump inanna_n_javier_1

label javier_encounter_list:

label battles_list:
    menu:
        "inanna 1 battle":
            jump inanna_1_battle