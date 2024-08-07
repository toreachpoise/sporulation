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
    
label battle_4_def:#you usually call this in the very beginning of your game, it will set up all the variables being used for the battle system

####You can change everything below##################################################################################
#the base stats for the four characters
    #warrior type class
    $ player1_hp_max = 300
    $ player1_mp_max = 100    
    $ player1_attack = 25
    $ player1_defense = 40

    $ stun_dmg = False
    $ kaye_skipturn = False
    $ chud_skipturn = False
    $ chud2_skipturn = False
    $ check_win = False

####You can change everything above##################################################################################

    # default for message, leave it as is
    #check the battle_message screen to see how this is used
    $ message = "none"
    return
    
label battle_4_presetup: 
    
    #this all the variables needed before you call battle each time
####You can change everything below##################################################################################
    # right now, it is all in one set up but it can be seperated for more variety of monsters
    # your player names and the image being used for them, please take a look at how images are used in the battle folder so you understand the size of each image should be
    $ player1 = "Parvez" #names, set as none to not display image
    #$ player1_image_selected = "battle/player1_selected.png" #the images
    #$ player1_image_default = "battle/player1_default.png"
    # number of players, and the default is turn based so player goes first then monster afterwards and repeat
    $ player_numbers = 1
    $ turn = 1 #turn starts with player 1
    $ m_turn = 1 #starts with Marianne
    $ player_turn = "Parvez"
    $ monster_turn = "Kaye"
    $ check_win = False
    
    # if you want your player is start with full hp each battle, if not, you tinker around with this code
    # so maybe you might comment it out if you want the player's hp to remain what it was
    $ player1_hp = player1_hp_max
    $ player1_mp = player1_mp_max

    
    #the monster's graphics, hp points max and the range of their attack
    # example: monster 1 is a white sheep using sheep1.png for the image
    # it can attack between 10 to 30 damage on the player and has an hp of 100
    # you can get fancy with this but at the moment, you have a max of 3 monsters that can be on the battle field 
    $ chud = "Chud 1"
    $ chud2 = "Chud 2"
    $ kaye = "Kaye" #if you want only two monsters on the field, replace this with $ monster 3 = "none" and make $ chud_dead = True (see below)
    #$ kaye_image = "battle/sheep3.png"
    #$ chud_image = "battle/chest1.png"
    #$ chud2_image = "battle/chest1.png"
    $ kaye_hp_max = 100
    $ chud_hp_max = 400
    $ chud2_hp_max = 400
    $ kaye_hp = kaye_hp_max
    $ chud_hp = chud_hp_max
    $ chud2_hp = chud2_hp_max
    $ kaye_attack_min = 5
    $ kaye_attack_max = 20
    $ chud_attack_min = 20
    $ chud_attack_max = 50
    $ chud2_attack_min = 20
    $ chud2_attack_max = 50
    # the number of monsters, if you use less monster then you would need to change this number too
    $ monster_numbers = 3
    $ kaye_dead = False
    $ chud_dead = False
    $ chud2_dead = False # make this true if you don't want a third monster on the field, remember to set chud = "none" too
####You can change everything above##################################################################################
    
    #default values, leave it as is
    $ damage = 1
    $ m_damage = 1
    $ p_skill = "none" #player skill being used
    $ m_target = "none" #the player the monster is targetting
    $ monster_target = 0
    $ p_action = "none"
    $ player1_defend = False
    $ target = "none" #marianne,2,3

    return

#################################################################################################################
label battle_4: # the battle screen uses this general set up
    show bs
    show screen battle_4_overlay_monsters
    show screen battle_4_overlay_players
    show screen battle_4_message
    with blinds
    jump battling_4
label battling_4:
    #queue audio fightmusic
    call player_turn_4 from _call_player_turn_4
    $ turn = 0 #this is so that player 1 is not 'selected', that wouldn't make sense when it's not their turn
#    jump monster_dead_check
#    if check_win == True:
#        jump battle_win
    call monster_turn_4 from _call_monster_turn_4
    $ m_turn = 1
    $ turn = 1
    $ player1_defend = False
    jump battling_4
    
label battle_4_win: #the aftermath message
    "You somehow managed to defeat Kaye and the chuds"
    hide screen battle_4_overlay_players
    hide screen battle_4_overlay_monsters
    hide screen battle_4_message
    jump kayden_2_goodend
#################################################################################################################

label player_turn_4:
    call monster_dead_check_4 from _call_monster_dead_check_4
    if check_win:
        jump battle_4_win
    while player_numbers >= turn:
        if turn == 1:
            $ message = "player1_turn"
            $ player_turn = player1
        call screen player_actions_4
        $ p_action = _return
        call player_dealt_damage_4 from _call_player_dealt_damage_4
        call monster_dead_check_4 from _call_monster_dead_check_10
        if check_win:
            jump battle_4_win
        else:
            $ turn += 1
    return
    
label player_dealt_damage_4:
    $ target = "none"
    if player_turn == player1:
        if p_action == "attack":
            $ damage = player1_attack
            if player1_mp < 90:
                $ player1_mp += 10
        elif p_action == "skills":
            call player1_skills_4 from _call_player1_skills_4
        elif p_action == "defend":
            $ damage = -1
            $ player1_defend = True
            if player1_mp < 95:
                $ player1_mp += 5

    if damage < 0:
        return
    else:
        call screen player_target_4
        $ target = _return
        if target == "kaye":
            if stun_dmg:
                $ kaye_skipturn = True
                "[target] was stunned by Inanna's studied materialist application of theory and may not attack!"
                $ stun_dmg = False
            else:
                $ kaye_hp = kaye_hp - damage
        elif target == "chud":
            if stun_dmg:
                $ chud_skipturn = True
                $ stun_dmg = False
                "[target] was stunned by Inanna's studied materialist application of theory and may not attack!"
            else:
                $ chud_hp = chud_hp - damage
        elif target == "chud2":
            if stun_dmg:
                $ chud2_skipturn = True
                $ stun_dmg = False
                "[target] was stunned by Inanna's studied materialist application of theory and may not attack!"
            else:
                $ chud2_hp = chud2_hp - damage
        elif target == "all":
            if stun_dmg:
                $ chud_skipturn = True
                $ kaye_skipturn = True
                $ chud2_skipturn = True
                "All enemies were stunned by Javier's dazzling show!"
                $ stun_dmg = False
            else: 
                $ chud_hp = chud_hp - damage
                $ kaye_hp = kaye_hp - damage
                $ chud2_hp = chud2_hp - damage
        if p_action == "attack":
            $ message = "player_attack"
        elif p_action == "skills":
            $ message = "player_skill"
        $ renpy.pause(1.0)
        return

label player1_skills_4:
    hide screen battle_4_overlay_players
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
        $ player1_hp += 10
    show screen battle_4_overlay_players

    return

label monster_turn_4:
    while monster_numbers >= m_turn:
        if m_turn == 1:
            if kaye_dead:
                pass
            elif kaye_skipturn:
                "Kaye was stunned and couldn't attack!"
                $ kaye_skipturn = False
                return
            else:
                $ monster_turn = "marianne"
                call monster_dealt_damage_4 from _call_monster_dealt_damage_10
                $ message = "marianne_attack"
                call player_dead_check_4 from _call_player_dead_check_11
        elif m_turn == 2:
            if chud_dead:
                pass
            elif chud_skipturn:
                "The chud was stunned and couldn't attack!"
                $ chud_skipturn = False
                return
            else:
                $ monster_turn = "chud"
                call monster_dealt_damage_4 from _call_monster_dealt_damage_4_1
                $ message = "chud_attack"
                call player_dead_check_4 from _call_player_dead_check_12
        elif m_turn == 3:
            if chud2_dead:
                pass
            elif chud2_skipturn:
                "The chud was stunned and couldn't attack!"
                $ chud2_skipturn = False
                return
            else:
                $ monster_turn = "chud2"
                call monster_dealt_damage_4 from _call_monster_dealt_damage_4_2
                $ message = "chud2_attack"
                call player_dead_check_4 from _call_player_dead_check_13
        $ renpy.pause(1.5)
        $ m_turn += 1
    return

label monster_dealt_damage_4:
    if monster_turn == "kaye":
        $ m_damage = renpy.random.randint(kaye_attack_min,kaye_attack_max)
    elif monster_turn == "chud":
        $ m_damage = renpy.random.randint(chud_attack_min,chud_attack_max)
    elif monster_turn == "chud2":
        $ m_damage = renpy.random.randint(chud2_attack_min,chud2_attack_max)
    $ monster_target = renpy.random.randint(1,player_numbers)
    if monster_target == 1:
        if player1_defend:
            $ m_damage = m_damage - player1_defense
            if m_damage < 0: #so there's no negative values
                $ m_damage = 0
        $ player1_hp = player1_hp - m_damage
        $ m_target = player1
    return
    
label monster_dead_check_4:
    if kaye_hp <=0:
        $ kaye_dead = True
        $ kaye = "none"
    if chud_hp <=0:
        $ chud_dead = True
        $ chud = "none"
    if chud2_hp <= 0:
        $ chud2_dead = True
        $ chud2 = "none"
    if kaye_dead == chud_dead == chud2_dead == True: # chud_dead == True:
        $ check_win = True
        $ chud2 = "none"
        $ chud = "none"
        $ kaye = "none"
    return 

label player_dead_check_4:
    if player1_hp <= 0 : # or player3_hp <= 0 or player4_hp <= 0:
        "The chuds and Kaye easily defeat you."
        menu:
            "try again":
                "Maybe you'll have better luck next time ..."
                scene cardboard
                hide screen battle_4_message
                hide screen battle_4_overlay_monsters
                hide screen battle_4_overlay_players
                jump kayden_2_battle
            "give up":
                hide screen battle_4_overlay_players
                hide screen battle_4_overlay_monsters
                hide screen battle_4_message
                jump kayden_2_badend
        #$ renpy.full_restart() # returns to main menu, game over 
    else:
        return

screen battle_4_overlay_players:
    add "battle/battlebox2.png" xalign 0.375 yalign .95
    add "battle/battlebox1.png" xalign .75 yalign .95
    #player 1 is assume to always exist
    if turn == 1:
        add "parvez_icon" xalign 0.25 yalign .94   # player icon in hp area
        add "parvez_sprite" xalign 0.25 yalign 0.5       #player chara above 
    else:
        add "parvez_icon_idle" xalign 0.25 yalign .94
        add "parvez_sprite_idle" xalign 0.25 yalign 0.5
    bar:
        xalign .25
        yalign .90
        style "bar_hp"
        value player1_hp xmaximum 181
        range player1_hp_max
    bar:
        xalign .25
        yalign .94
        style "bar_mp"
        value player1_mp xmaximum 181
        range player1_mp_max
    text"[player1_hp]/[player1_hp_max]" xalign 0.25 yalign 0.904
    text"[player1_mp]/[player1_mp_max]" xalign 0.25 yalign 0.944
    

screen battle_4_overlay_monsters:
    if kaye != "none":
        add "kaye_sprite" xalign 0.66 yalign 0.5
        bar:
            xalign .63
            yalign .47
            style "bar_hp"
            value kaye_hp xmaximum 181
            range kaye_hp_max
        text "[kaye_hp]/[kaye_hp_max]" xalign 0.63 yalign 0.47

    if chud != "none":
        add "chud_sprite" xalign 0.9 yalign 0.25
        bar:
            xalign .8
            yalign .35
            style "bar_hp"
            value chud_hp xmaximum 181
            range chud_hp_max
        text "[chud_hp]/[chud_hp_max]" xalign 0.8 yalign 0.35

    if chud2 != "none":
        add "chud2_sprite" xalign 0.9 yalign 0.7
        bar:
            xalign .8
            yalign .6
            style "bar_hp"
            value chud2_hp xmaximum 181
            range chud2_hp_max
        text "[chud2_hp]/[chud2_hp_max]" xalign 0.8 yalign 0.6



screen battle_4_message:
    add "battle/messagebox.png" xalign 0.5 yalign 0.025
    if message == "player1_turn":
        text "What will [player1] do?" xalign 0.5 yalign 0.05
        
    if message == "player_attack":
        text "[player_turn] attacks! Dealt [damage] damage!" xalign 0.5 yalign 0.05
    if message == "player_skill":
        text "[player_turn] used [p_skill]! Dealt [damage] damage!" xalign 0.5 yalign 0.05


    elif message == "kaye_attack":
        text "[kaye] attacks! [m_target] took [m_damage] damage!" xalign 0.5 yalign 0.05
    elif message == "chud_attack":
        text "[chud] attacks! [m_target] took [m_damage] damage!" xalign 0.5 yalign 0.05
    elif message == "chud2_attack":
        text "[chud2] attacks! [m_target] took [m_damage] damage!" xalign 0.5 yalign 0.05

screen player_actions_4: #returns for player action
    textbutton "Attack" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.75 yalign 0.84 action Return("attack") 
    textbutton "Skills" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.75 yalign 0.89 action Return("skills") 
    textbutton "Defend" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.75 yalign 0.94 action Return("defend") #damage from monster is lowered depending on player's defense
    #textbutton "Items" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.75 yalign 0.98 action Return("items") #not implemented yet

screen player_target_4: #returns monster player wants to attack
    if target == "all":
        textbutton "All Enemies" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.45 yalign 0.48 action Return("all")
    else:
        if kaye != "none":
            textbutton "[kaye]" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.63 yalign 0.44 action Return("kaye") 
        if chud != "none":
            textbutton "[chud]" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.79 yalign 0.315 action Return("chud") 
        if chud2 != "none":
            textbutton "[chud2]" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.79 yalign 0.57 action Return("chud2") 