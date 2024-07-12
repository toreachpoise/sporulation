# there needs to be 4 players at the moment, I don't think the implementation is all there for players < 4 yet
# there can be 1, 2, 3 monsters, just make sure you define that
# player dead should work but there might be bugs that I haven't fixed yet
# look at how the script is set up in script.rpy and then go through it in battle.rpy to see how it works behind the scenes


init python:
    #custom bar HP
    style.bar_hp = Style(style.default)
    style.bar_hp.left_bar = Frame("battle/hp.png",20, 20)
    style.bar_hp.right_bar = Frame("battle/empty_bar.png", 20, 20)
    style.bar_hp.xmaximum = 181 # bar width
    style.bar_hp.ymaximum = 28 # bar height 
    #custom bar MP
    style.bar_mp = Style(style.default)
    style.bar_mp.left_bar = Frame("battle/mp.png",20, 20)
    style.bar_mp.right_bar = Frame("battle/empty_bar.png", 20, 20)
    style.bar_mp.xmaximum = 181 # bar width
    style.bar_mp.ymaximum = 28 # bar height 
    
    style.battlebutton = Style(style.button)
    style.battlebutton.xminimum = 150
    style.battlebutton.yminimum = 30
    style.battlebutton_text = Style(style.text)
    style.battlebutton_text.size = 31
    style.battlebutton_text.outlines = [(1, "#000000", 0, 0)]
    style.battlebutton_text.hover_size = 31
    style.battlebutton_text.hover_outlines = [(2, "#E28308", 0, 0)]
    
label battle_def:#you usually call this in the very beginning of your game, it will set up all the variables being used for the battle system

####You can change everything below##################################################################################
#the base stats for the four characters
    #warrior type class
    $ player1_hp_max = 300
    $ player1_mp_max = 100    
    $ player1_attack = 12
    $ player1_defense = 20


    #thief type class
    $ player2_hp_max = 400
    $ player2_mp_max = 70    
    $ player2_attack = 17
    $ player2_defense = 15

    $ stun_dmg = False
    $ marianne_skipturn = False
    $ sarah_skipturn = False

####You can change everything above##################################################################################

    # default for message, leave it as is
    #check the battle_message screen to see how this is used
    $ message = "none"
    return
    
label battle_presetup: 
    
    #this all the variables needed before you call battle each time
####You can change everything below##################################################################################
    # right now, it is all in one set up but it can be seperated for more variety of monsters
    # your player names and the image being used for them, please take a look at how images are used in the battle folder so you understand the size of each image should be
    $ player1 = "Parvez" #names, set as none to not display image
    $ player2 = "Inanna"
    #$ player3 = "Javier"
    #$ player4 = "Terry"
    $ player1_image_selected = "battle/player1_selected.png" #the images
    $ player1_image_default = "battle/player1_default.png"
    $ player2_image_selected = "battle/player2_selected.png" #the images
    $ player2_image_default = "battle/player2_default.png"
    #$ player3_image_selected = "battle/player3_selected.png" #the images
    #$ player3_image_default = "battle/player3_default.png"
    #$ player4_image_selected = "battle/player4_selected.png" #the images
    #$ player4_image_default = "battle/player4_default.png"
    # number of players, and the default is turn based so player goes first then monster afterwards and repeat
    $ player_numbers = 2
    $ turn = 1 #turn starts with player 1
    $ m_turn = 1 #starts with Marianne
    $ player_turn = "parvez"
    $ monster_turn = "Marianne"
    $ check_win = False
    
    # if you want your player is start with full hp each battle, if not, you tinker around with this code
    # so maybe you might comment it out if you want the player's hp to remain what it was
    $ player1_hp = player1_hp_max
    $ player2_hp = player2_hp_max
    #$ player3_hp = player3_hp_max
    #$ player4_hp = player4_hp_max
    $ player1_mp = player1_mp_max
    $ player2_mp = player2_mp_max
    #$ player3_mp = player3_mp_max
    #$ player4_mp = player4_mp_max
    
    #the monster's graphics, hp points max and the range of their attack
    # example: monster 1 is a white sheep using sheep1.png for the image
    # it can attack between 10 to 30 damage on the player and has an hp of 100
    # you can get fancy with this but at the moment, you have a max of 3 monsters that can be on the battle field 
    $ marianne = "Marianne"
    $ sarah = "Sarah"
    #$ chud = "Chud" #if you want only two monsters on the field, replace this with $ monster 3 = "none" and make $ chud_dead = True (see below)
    $ marianne_image = "battle/sheep1.png"
    $ sarah_image = "battle/sheep2.png"
    
    #$ chud_image = "battle/chest1.png"
    $ marianne_hp_max = 100
    $ sarah_hp_max = 100
    #$ chud_hp_max = 100
    $ marianne_hp = marianne_hp_max
    $ sarah_hp = sarah_hp_max
    #$ chud_hp = chud_hp_max
    $ marianne_attack_min = 10
    $ marianne_attack_max = 30
    $ sarah_attack_min = 15
    $ sarah_attack_max = 25
    #$ chud_attack_min = 5
    #$ chud_attack_max = 20
    # the number of monsters, if you use less monster then you would need to change this number too
    $ monster_numbers = 2
    $ marianne_dead = False
    $ sarah_dead = False
    # chud_dead = False # make this true if you don't want a third monster on the field, remember to set chud = "none" too
####You can change everything above##################################################################################
    
    #default values, leave it as is
    $ damage = 1
    $ m_damage = 1
    $ p_skill = "none" #player skill being used
    $ m_target = "none" #the player the monster is targetting
    $ monster_target = 0
    $ p_action = "none"
    $ player1_defend = False
    $ player2_defend = False
    #$ player3_defend = False
    #$ player4_defend = False
    $ target = "none" #marianne,2,3

    return

#################################################################################################################
label battle: # the battle screen uses this general set up
    show bs
    show screen battle_overlay_players
    show screen battle_overlay_monsters
    show screen battle_message
    with blinds
    jump battling
label battling:
    call player_turn from _call_player_turn
    $ turn = 0 #this is so that player 1 is not 'selected', that wouldn't make sense when it's not their turn
#    jump monster_dead_check
#    if check_win == True:
#        jump battle_win
    call monster_turn from _call_monster_turn
    $ m_turn = 1
    $ turn = 1
    $ player1_defend = False
    $ player2_defend = False
    #$ player3_defend = False
    #$ player4_defend = False
    jump battling
    
label battle_win: #the aftermath message
    "You've won the battle!"
    hide screen battle_overlay_players
    hide screen battle_overlay_monsters
    hide screen battle_message
    jump battle_end
#################################################################################################################

label player_turn:
    call monster_dead_check from _call_monster_dead_check
    if check_win:
        jump battle_win
    while player_numbers >= turn:
        if turn == 1:
            $ message = "player1_turn"
            $ player_turn = player1
        elif turn == 2:
            $ message = "player2_turn"
            $ player_turn = player2
        #elif turn == 3:
#            $ message = "player3_turn"
#            $ player_turn = player3
        #elif turn == 4:
#            $ message = "player4_turn"
#            $ player_turn = player4
        call screen player_actions
        $ p_action = _return
        call player_dealt_damage from _call_player_dealt_damage
        call monster_dead_check from _call_monster_dead_check_1
        if check_win:
            jump battle_win
        else:
            $ turn += 1
    return
    
label player_dealt_damage:
    $ target = "none"
    if player_turn == player1:
        if p_action == "attack":
            $ damage = player1_attack
        elif p_action == "skills":
            call player1_skills from _call_player1_skills
        elif p_action == "defend":
            $ damage = -1
            $ player1_defend = True
        
    elif player_turn == player2:
        if p_action == "attack":
            $ damage = player2_attack
        elif p_action == "skills":
            call player2_skills from _call_player2_skills
        elif p_action == "defend":
            $ damage = -1
            $ player2_defend = True
#    elif player_turn == player3:
#        if p_action == "attack":
#            $ damage = player3_attack
#        elif p_action == "skills":
#            call player3_skills 
#        elif p_action == "defend":
#            $ damage = -1
#            $ player3_defend = True
#    elif player_turn == player4:
#        if p_action == "attack":
#            $ damage = player4_attack
#        elif p_action == "skills":
#            call player4_skills
#        elif p_action == "defend":
#            $ damage = -1
#            $ player4_defend = True
    if damage < 0:
        return
    else:
        call screen player_target
        $ target = _return
        if target == "marianne":
            if stun_dmg:
                $ marianne_skipturn = True
                "[target] was stunned by Inanna's studied materialist application of theory and may not attack!"
                $ stun_dmg = False
            else:
                $ marianne_hp = marianne_hp - damage
        elif target == "sarah":
            if stun_dmg:
                $ sarah_skipturn = True
                "[target] was stunned by Inanna's studied materialist application of theory and may not attack!"
                $ stun_dmg = False
            else:
                $ sarah_hp = sarah_hp - damage
#        elif target == "chud":
#            if stun_dmg:
#                $ chud_skipturn = True
#                $ stun_dmg = False
#                "[target] was stunned by Inanna's studied materialist application of theory and may not attack!"
#            else:
#               $ chud_hp = chud_hp - damage
        elif target == "all":
            $ marianne_hp = marianne_hp - damage
            $ sarah_hp = sarah_hp - damage
#            $ chud_hp = chud_hp - damage
        if p_action == "attack":
            $ message = "player_attack"
        elif p_action == "skills":
            $ message = "player_skill"
        $ renpy.pause(1.0)
        return

label player1_skills:
    hide screen battle_overlay_players
    call screen parvez_skills
    $ p_skill = _return
    if p_skill == "Tboy Swag":
        $ damage = player1_attack * 2
        $ player1_mp -= 25
    elif p_skill == "Plantboy Dickslap":
        $ damage = player1_attack*3
        $ player1_mp -= 50
    elif p_skill == "Panic Attack":
        $ damage = player1_attack * 0.75
        $ target = "all"
        $ player1_mp -= 33
    show screen battle_overlay_players

    return
label player2_skills:
    hide screen battle_overlay_players
    call screen inanna_skills
    $ p_skill = _return
    if p_skill == "Rigorous Discourse":
        $ damage = player2_attack * 1.5
        $ player2_mp -= 33
        $ stun_dmg = True
    elif p_skill == "Double Mommy Smack":
        $ damage = player2_attack
        $ target = "all"
        $ player2_mp -= 45
    elif p_skill == "Righteous Smiting":
        $ damage = player2_attack * 2.5
        $ player2_mp -= 66
    show screen battle_overlay_players
    return
#label player3_skills:
#    hide screen battle_overlay_players
#    call screen javier_skills
#    $ p_skill = _return
#    if p_skill == "Bow Attack 1":
#        $ damage = player3_attack * 2
#    elif p_skill == "Bow Attack 2":
#        $ damage = player3_attack*4
#    elif p_skill == "Bow Attack 3":
#        $ damage = player3_attack * 6
#    show screen battle_overlay_players
#    return    
#label player4_skills:
#    hide screen battle_overlay_players
#    call screen terry_skills
#    if p_skill == "Magic Attack 1":
#        $ damage = player4_attack * 2
#    elif p_skill == "Magic Attack 2":
##        $ damage = player4_attack*4
#    elif p_skill == "Magic Attack 3":
#        $ damage = player4_attack * 6
#    show screen battle_overlay_players
#    return
screen parvez_skills:
    add "battle/battlebox2.png" xalign 0.2 yalign .95
    if player1_mp > 25:
        textbutton "Tboy Swag" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.15 yalign 0.87 action Return("Tboy Swag")  
    if player1_mp > 50:
        textbutton "Plantboy Dickslap" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.35 yalign 0.87 action Return("Plantboy Dickslap") 
    if player1_mp > 33:
        textbutton "Panic Attack" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.15 yalign 0.92 action Return("Panic Attack") 
screen inanna_skills:
    add "battle/battlebox2.png" xalign 0.2 yalign .99
    if player2_mp > 33:
        textbutton "Rigorous Discourse" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.15 yalign 0.87 action Return("Rigorous Discourse")  
    if player2_mp > 45:
        textbutton "Mommy Smack" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.35 yalign 0.87 action Return("Mommy Smack") 
    if player2_mp > 66:
        textbutton "Righteous Smiting" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.15 yalign 0.92 action Return("Righteous Smiting") 
#screen javier_skills:
#    add "battle/battlebox2.png" xalign 0.2 yalign .99
#    textbutton "Bow Attack 1" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.1 yalign 0.8 action Return("Bow Attack 1")  
#    textbutton "Bow Attack 2" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.7 yalign 0.8 action Return("Bow Attack 2") 
#    textbutton "Bow Attack 3" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.1 yalign 0.85 action Return("Bow Attack 3") 
#screen terry_skills:
#    add "battle/battlebox2.png" xalign 0.2 yalign .99
#    textbutton "Magic Attack 1" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.1 yalign 0.8 action Return("Magic Attack 1")  
#    textbutton "Magic Attack 2" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.7 yalign 0.8 action Return("Magic Attack 2") 
#    textbutton "Magic Attack 3" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.1 yalign 0.85 action Return("Magic Attack 3") 
label monster_turn:
    while monster_numbers >= m_turn:
        if m_turn == 1:
            if marianne_dead:
                pass
            elif marianne_skipturn:
                "Marianne was stunned by Inanna's intellect and couldn't attack!"
                $ marianne_skipturn = False
                return
            else:
                $ monster_turn = "marianne"
                call monster_dealt_damage from _call_monster_dealt_damage
                $ message = "marianne_attack"
                call player_dead_check from _call_player_dead_check
        elif m_turn == 2:
            if sarah_dead:
                pass
            elif sarah_skipturn:
                "Sarah was stunned by Inanna's intellect and couldn't attack!"
                $ sarah_skipturn = False
                return
            else:
                $ monster_turn = "sarah"
                call monster_dealt_damage from _call_monster_dealt_damage_1
                $ message = "sarah_attack"
                call player_dead_check from _call_player_dead_check_1
#        elif m_turn == 3:
#            if chud_dead:
#                pass
#           elif chud_skipturn:
#               "The chud was stunned by Inanna's intellect and couldn't attack!"
#               $ chud_skipturn = False
#               return
#            else:
#                $ monster_turn = "chud"
#                call monster_dealt_damage
#                $ message = "chud_attack"
#                call player_dead_check
#        
        $ renpy.pause(1.5)
        $ m_turn += 1
    return

label monster_dealt_damage:
    if monster_turn == "marianne":
        $ m_damage = renpy.random.randint(marianne_attack_min,marianne_attack_max)
    elif monster_turn == "sarah":
        $ m_damage = renpy.random.randint(marianne_attack_min,marianne_attack_max)
#    elif monster_turn == "chud":
#        $ m_damage = renpy.random.randint(marianne_attack_min,marianne_attack_max)
    $ monster_target = renpy.random.randint(1,player_numbers)
    if monster_target == 1:
        if player1_defend:
            $ m_damage = m_damage - player1_defense
            if m_damage < 0: #so there's no negative values
                $ m_damage = 0
        $ player1_hp = player1_hp - m_damage
        $ m_target = player1
    elif monster_target == 2:
        if player2_defend:
            $ m_damage = m_damage - player2_defense
            if m_damage < 0:
                $ m_damage = 0
        $ player2_hp = player2_hp - m_damage
        $ m_target = player2
#    elif monster_target == 3:
#        if player3_defend:
#            $ m_damage = m_damage - player3_defense
#            if m_damage < 0:
#                $ m_damage = 0
#        $ player3_hp = player3_hp - m_damage
#        $ m_target = player3
#    elif monster_target == 4:
#        if player4_defend:
#            $ m_damage = m_damage - player4_defense
#            if m_damage < 0:
#                $ m_damage = 0
#        $ player4_hp = player4_hp - m_damage
#        $ m_target = player4
    return
    
label monster_dead_check:
    if marianne_dead == sarah_dead == True: # chud_dead == True:
        $ check_win = True
        $ marianne = "none"
        $ sarah = "none"
#        $ chud = "none"
        return 
    if marianne_hp <=0:
        $ marianne_dead = True
        $ marianne = "none"
    if sarah_hp <=0:
        $ sarah_dead = True
        $ sarah = "none"
#    if chud_hp <=0:
#        $ chud_dead = True
#        $ chud = "none"
    return 

label player_dead_check:
    if player1_hp <= 0 or player2_hp <= 0: # or player3_hp <= 0 or player4_hp <= 0:
        "One of the players died"
        $ renpy.full_restart() # returns to main menu, game over 
    else:
        return
screen battle_overlay_players:
    add "battle/battlebox2.png" xalign 0.375 yalign .95
    add "battle/battlebox1.png" xalign .75 yalign .95
    #player 1 is assume to always exist
    if turn == 1:
        add player1_image_selected xalign 0.26 yalign .93   # player icon in hp area
        add player1_image_selected xalign 0.2 yalign 0.33       #player chara above 
    else:
        add player1_image_default xalign 0.26 yalign .93
        add player1_image_default xalign 0.2 yalign 0.33
    bar:
        xalign .26
        yalign .84
        style "bar_hp"
        value player1_hp xmaximum 181
        range player1_hp_max
    bar:
        xalign .26
        yalign .88
        style "bar_mp"
        value player1_mp xmaximum 181
        range player1_mp_max
    text"[player1_hp]/[player1_hp_max]" xalign 0.26 yalign 0.844
    text"[player1_mp]/[player1_mp_max]" xalign 0.26 yalign 0.884
    
    if player2 != "none":
        
        if turn == 2:
            add player2_image_selected xalign 0.4 yalign .93     # player icon in hp area
            add player2_image_selected xalign 0.2 yalign 0.5     # player chara above   
        else:
            add player2_image_default xalign 0.4 yalign .93
            add player2_image_default xalign 0.2 yalign 0.66
        bar:
            xalign .4
            yalign .84
            style "bar_hp"
            value player2_hp xmaximum 181
            range player2_hp_max
        bar:
            xalign .4
            yalign .88
            style "bar_mp"
            value player2_mp xmaximum 181
            range player2_mp_max
        text"[player2_hp]/[player2_hp_max]" xalign 0.4 yalign 0.844
        text"[player2_mp]/[player2_mp_max]" xalign 0.4 yalign 0.884   
        
#    if player3 != "none":
#        
#        if turn==3:
#            add player3_image_selected xalign 0.49 yalign .97
#        else:
#            add player3_image_default xalign 0.49 yalign .97
#        bar:
#            xalign .49
#            yalign .92
#            style "bar_hp"
#            value player3_hp xmaximum 181
#            range player3_hp_max
#        bar:
#            xalign .49
#            yalign .96
#            style "bar_mp"
#            value player3_mp xmaximum 181
#            range player3_mp_max
#        text"[player3_hp]/[player3_hp_max]" xalign 0.47 yalign 0.92
#        text"[player3_mp]/[player3_mp_max]" xalign 0.47 yalign 0.96  
#        
#    if player4 != "none":
#        if turn == 4:
###            add player4_image_selected xalign 0.73 yalign .97
#        else:
#            add player4_image_default xalign 0.73 yalign .97
#        bar:
##            xalign .73
#            yalign .92
#            style "bar_hp"
#            value player4_hp xmaximum 181
#            range player4_hp_max
#        bar:
##            xalign .73
#            yalign .96
#            style "bar_mp"
#            value player4_mp xmaximum 181
#            range player4_mp_max
#        text"[player4_hp]/[player4_hp_max]" xalign 0.68 yalign 0.92
#        text"[player4_mp]/[player4_mp_max]" xalign 0.68 yalign 0.96  

screen battle_overlay_monsters:
    if marianne != "none":
        add marianne_image xalign 0.8 yalign 0.3
        bar:
            xalign .8
            yalign .27
            style "bar_hp"
            value marianne_hp xmaximum 181
            range marianne_hp_max
        text "[marianne_hp]/[marianne_hp_max]" xalign 0.8 yalign 0.2725
    if sarah != "none":
        add sarah_image xalign 0.8 yalign 0.6
        bar:
            xalign .8
            yalign .52
            style "bar_hp"
            value sarah_hp xmaximum 181
            range sarah_hp_max
        text "[sarah_hp]/[sarah_hp_max]" xalign 0.8 yalign 0.5225
    
#    if chud != "none":
#        add chud_image xalign 0.8 yalign 0.6
###        bar:
#            xalign .8
#            yalign .5
#            style "bar_hp"
##            value chud_hp xmaximum 181
#            range chud_hp_max
#        text "[chud_hp]/[chud_hp_max]" xalign 0.75 yalign 0.5


screen battle_message:
    add "battle/messagebox.png" xalign 0.5 yalign 0.025
    if message == "player1_turn":
        text "What will [player1] do?" xalign 0.5 yalign 0.05
    elif message == "player2_turn":
        text "What will [player2] do?" xalign 0.5 yalign 0.05
#    elif message == "player3_turn":
#        text "What will [player3] do?" xalign 0.17 yalign 0.05
#    elif message == "player4_turn":
#        text "What will [player4] do?" xalign 0.17 yalign 0.05
        
    if message == "player_attack":
        text "[player_turn] attacks! Dealt [damage] damage!" xalign 0.5 yalign 0.05
    if message == "player_skill":
        text "[player_turn] used [p_skill]! Dealt [damage] damage!" xalign 0.5 yalign 0.05

        
    elif message == "marianne_attack":
        text "[marianne] attacks! [m_target] took [m_damage] damage!" xalign 0.5 yalign 0.05
    elif message == "sarah_attack":
        text "[sarah] attacks! [m_target] took [m_damage] damage!" xalign 0.5 yalign 0.05
#    elif message == "chud_attack":
#        text "[chud] attacks! [m_target] took [m_damage] damage!" xalign 0.5 yalign 0.05

screen player_actions: #returns for player action
    textbutton "Attack" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.75 yalign 0.84 action Return("attack") 
    textbutton "Skills" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.75 yalign 0.89 action Return("skills") 
    textbutton "Defend" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.75 yalign 0.94 action Return("defend") #damage from monster is lowered depending on player's defense
    #textbutton "Items" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.75 yalign 0.98 action Return("items") #not implemented yet

screen player_target: #returns monster player wants to attack
    if target == "all":
        textbutton "All Enemies" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.75 yalign 0.4 action Return("all")
    else:
        if marianne != "none":
            textbutton "[marianne]" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.8 yalign 0.23 action Return("marianne") 
        if sarah != "none":
            textbutton "[sarah]" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.8 yalign 0.49 action Return("sarah") 
#        if chud != "none":
#            textbutton "[chud]" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.8 yalign 0.4 action Return("chud") 