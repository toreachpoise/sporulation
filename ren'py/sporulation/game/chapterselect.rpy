screen chapterselect():
    add "/bgs/purple.png"
    imagemap:
        ground "/gui/chapter_select_ground.png"
        idle "/gui/chapter_select_idle.png"
        hover "/gui/chapter_select_hover.png"
        xalign 0.5

        hotspot (0, 217, 242, 238) action Call("plant_encounter_list")
        if plant_encounter_1_complete == True:
            hotspot (241, 217, 239, 240) action Call("terry_encounter_list")
        if terry_1_complete == True:
            hotspot (482, 218, 238, 241) action Call("solo_encounter_list")
        if terry_2_complete == True:
            hotspot (0, 457, 239, 236) action Call("ahmed_encounter_list")
            if (kayden_1_complete == False) or (inanna_n_javier_2_complete == True):
                hotspot (239, 458, 241, 237) action Call("kayden_encounter_list")
        if (ahmed_1_complete == True) or (kayden_1_complete == True):  
            hotspot (477, 458, 244, 238) action Call("inanna_encounter_list")
        if inanna_1_complete == True:
            hotspot (0, 693, 242, 239) action Call("inanna_n_javier_encounter_list")
        if inanna_n_javier_1_complete == True:
            hotspot (242, 693, 240, 239) action Call("javier_encounter_list")
        if inanna_n_javier_2_complete == True:
            hotspot (482, 695, 239, 236) action Call("chud_encounter_list")
        

label plant_encounter_list:
    menu:
        "plant encounter 1" if (plant_encounter_1_complete == False):
            jump plant_encounter_1
        "plant encounter 2" if (terry_1_complete == True) and (plant_encounter_2_complete == False):
            jump plant_encounter_2
        "return":
            call screen chapterselect

label terry_encounter_list:
    if kayden_2_badend:
        menu:
            "terry 4":
                jump terry_4
            "return":
                call screen chapterselect
    else:
        menu:
            "terry 1" if (plant_encounter_1_complete == True) and (terry_1_complete == False):
                jump terry_1
            "terry 2" if (terry_1_complete == True) and (terry_2_complete == False):
                jump terry_2
            "terry 3" if (terry_2_complete == True) and (terry_3_complete == False):
                jump terry_3
            "return":
                call screen chapterselect

label ahmed_encounter_list:
    if kayden_2_badend:
        "These encounters have been locked by the events of Kayden 2. Please complete Terry 4 to continue."
        call screen chapterselect
    else:
        menu:
            "ahmed 1" if (terry_2_complete == True) and (ahmed_1_complete == False):
                jump ahmed_1
            "ahmed 2" if (ahmed_1_complete == True) and (ahmed_2_complete == False):
                jump ahmed_2
            "return":
                call screen chapterselect

label kayden_encounter_list:
    menu:
        "kayden 1" if (terry_1_complete == True) and (kayden_1_complete == False):
            jump kayden_1
        "kayden 2" if (inanna_n_javier_2_complete == True) and (kayden_2_complete == False):
            jump kayden_2
        "return":
            call screen chapterselect

label solo_encounter_list:
    if kayden_2_badend:
        "These encounters have been locked by the events of Kayden 2. Please complete Terry 4 to continue."
        call screen chapterselect
    else:
        menu:
            "solo 1" if (terry_1_complete == True) and (strokerused == False): ##if strokerused == False
                jump solo_1
            "solo 2" if (ahmed_2_complete == True) and (solo_2_complete == False):
                jump solo_2
            "return":
                call screen chapterselect

label inanna_encounter_list:
    if kayden_2_badend:
        "These encounters have been locked by the events of Kayden 2. Please complete Terry 4 to continue."
        call screen chapterselect
    else:
        menu:
            "inanna 1" if ((ahmed_1_complete == True) or (kayden_1_complete == True)) and (inanna_1_complete == False):
                jump inanna_1
            "inanna 2" if ((inanna_1_complete == True) and (inanna_2_complete == False)):
                jump inanna_2
            "return":
                call screen chapterselect

label inanna_n_javier_encounter_list:
    if kayden_2_badend:
        "These encounters have been locked by the events of Kayden 2. Please complete Terry 4 to continue."
        call screen chapterselect
    else:
        menu:
            "inanna and javier 1" if (inanna_1_complete == True) and (inanna_n_javier_1_complete == False):
                jump inanna_n_javier_1
            "inanna and javier 2" if (inanna_n_javier_1_complete == True) and (inanna_n_javier_2_complete == False):
                jump inanna_n_javier_2
            "return":
                call screen chapterselect

label javier_encounter_list:
    if kayden_2_badend:
        "These encounters have been locked by the events of Kayden 2. Please complete Terry 4 to continue."
        call screen chapterselect
    else:
        menu:
            "javier 1" if (inanna_n_javier_1_complete == True) and (ahmed_2_complete == True) and (javier_1_complete == False):
                jump javier_1
            "return":
                call screen chapterselect

label chud_encounter_list:
    if kayden_2_badend:
        "These encounters have been locked by the events of Kayden 2. Please complete Terry 4 to continue."
        call screen chapterselect
    else:
        menu:
            "cw: sexual assault and severe transphobia for all chud scenes"
            "chud 1" if (inanna_n_javier_2_complete == True) and (chud_1_complete == False):
                jump chud_1
            "return":
                call screen chapterselect