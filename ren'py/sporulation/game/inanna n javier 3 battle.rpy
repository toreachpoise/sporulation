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
    
label battle_5_def:#you usually call this in the very beginning of your game, it will set up all the variables being used for the battle system

####You can change everything below##################################################################################
#the base stats for the four characters
    $ player1_hp_max = 300
    $ player1_mp_max = 100    
    $ player1_attack = 25
    $ player1_defense = 40

    $ player2_hp_max = 400
    $ player2_mp_max = 70    
    $ player2_attack = 35
    $ player2_defense = 15

    $ player3_hp_max = 250
    $ player3_mp_max = 150
    $ player3_attack = 17
    $ player3_defense = 10

    $ player4_hp_max = 350
    $ player4_mp_max = 150
    $ player4_attack = 30
    $ player4_defense = 30

    $ stun_dmg = False
    $ marianne_skipturn = False
    $ sarah_skipturn = False
    $ kaye_skipturn = False
    $ chud_skipturn = False
    $ chud2_skipturn = False
    $ check_win = False

####You can change everything above##################################################################################

    # default for message, leave it as is
    #check the battle_message screen to see how this is used
    $ message = "none"
    return
    
label battle_5_presetup: 
    
    #this all the variables needed before you call battle each time
####You can change everything below##################################################################################
    # right now, it is all in one set up but it can be seperated for more variety of monsters
    # your player names and the image being used for them, please take a look at how images are used in the battle folder so you understand the size of each image should be
    $ player1 = "Parvez" #names, set as none to not display image
    $ player2 = "Inanna"
    $ player3 = "Javier"
    $ player4 = "Terry"

    # number of players, and the default is turn based so player goes first then monster afterwards and repeat
    $ player_numbers = 4
    $ turn = 1 #turn starts with player 1
    $ m_turn = 1 #starts with Marianne
    $ player_turn = "Parvez"
    $ monster_turn = "Marianne"
    $ check_win = False
    
    # if you want your player is start with full hp each battle, if not, you tinker around with this code
    # so maybe you might comment it out if you want the player's hp to remain what it was
    $ player1_hp = player1_hp_max
    $ player2_hp = player2_hp_max
    $ player3_hp = player3_hp_max
    $ player4_hp = player4_hp_max
    $ player1_mp = player1_mp_max
    $ player2_mp = player2_mp_max
    $ player3_mp = player3_mp_max
    $ player4_mp = player4_mp_max
    
    #the monster's graphics, hp points max and the range of their attack
    # example: monster 1 is a white sheep using sheep1.png for the image
    # it can attack between 10 to 30 damage on the player and has an hp of 100
    # you can get fancy with this but at the moment, you have a max of 3 monsters that can be on the battle field 
    $ marianne = "Marianne"
    $ sarah = "Sarah"
    $ chud = "Chud"
    $ chud2 = "Chud 2"
    $ kaye = "Kaye" #if you want only two monsters on the field, replace this with $ monster 3 = "none" and make $ chud_dead = True (see below)

    $ marianne_hp_max = 100
    $ sarah_hp_max = 100
    $ kaye_hp_max = 100
    $ chud_hp_max = 350
    $ chud2_hp_max = 350
    $ marianne_hp = marianne_hp_max
    $ sarah_hp = sarah_hp_max
    $ kaye_hp = kaye_hp_max
    $ chud_hp = chud_hp_max
    $ chud2_hp = chud2_hp_max
    $ marianne_attack_min = 10
    $ marianne_attack_max = 75
    $ sarah_attack_min = 15
    $ sarah_attack_max = 45
    $ kaye_attack_min = 5
    $ kaye_attack_max = 50
    $ chud_attack_min = 30
    $ chud_attack_max = 75
    $ chud2_attack_min = 35
    $ chud2_attack_max = 80
    # the number of monsters, if you use less monster then you would need to change this number too
    $ monster_numbers = 5
    $ marianne_dead = False
    $ sarah_dead = False
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
    $ player2_defend = False
    $ player3_defend = False
    $ player4_defend = False
    $ target = "none" #marianne,2,3

    return

#################################################################################################################
label battle_5: # the battle screen uses this general set up
    show bs
    show screen battle_5_overlay_monsters
    show screen battle_5_overlay_players
    show screen battle_5_message
    with blinds
    jump battling_5
label battling_5:
    call player_turn_5 from _call_player_turn_5
    $ turn = 0 #this is so that player 1 is not 'selected', that wouldn't make sense when it's not their turn
    call monster_turn_5 from _call_monster_turn_5
    $ m_turn = 1
    $ turn = 1
    $ player1_defend = False
    $ player2_defend = False
    $ player3_defend = False
    $ player4_defend = False
    jump battling_5
    
label battle_5_win: #the aftermath message
    stop sound
    play audio fanfare
    "You've won the battle!"
    hide screen battle_5_overlay_players
    hide screen battle_5_overlay_monsters
    hide screen battle_5_message
    jump battle_5_end
#################################################################################################################

label player_turn_5:
    call monster_dead_check_5 from _call_monster_dead_check_5
    if check_win:
        jump battle_5_win
    while player_numbers >= turn:
        if turn == 1 and player1_hp > 0:
            $ message = "player1_turn"
            $ player_turn = player1
        elif turn == 2 and player2_hp > 0:
            $ message = "player2_turn"
            $ player_turn = player2
        elif turn == 3 and player3_hp > 0:
            $ message = "player3_turn"
            $ player_turn = player3
        elif turn == 4 and player4_hp > 0:
            $ message = "player4_turn"
            $ player_turn = player4
        call screen player_actions_5
        $ p_action = _return
        call player_dealt_damage_5 from _call_player_dealt_damage_5
        call monster_dead_check_5 from _call_monster_dead_check_15
        if check_win:
            jump battle_5_win
        else:
            $ turn += 1
    return
    
label player_dealt_damage_5:
    $ target = "none"
    if player_turn == player1:
        if p_action == "attack":
            $ damage = player1_attack
            if player1_mp < 90:
                $ player1_mp += 10
        elif p_action == "skills":
            call player1_skills_5 from _call_player1_skills_5
        elif p_action == "defend":
            $ damage = -1
            $ player1_defend = True
            if player1_mp < 95:
                $ player1_mp += 25
        
    elif player_turn == player2:
        if p_action == "attack":
            $ damage = player2_attack
            if player2_mp < 90:
                $ player2_mp += 10
        elif p_action == "skills":
            call player2_skills_5 from _call_player2_skills_5
        elif p_action == "defend":
            $ damage = -1
            $ player2_defend = True
            if player2_mp < 95:
                $ player2_mp += 25
    elif player_turn == player3:
        if p_action == "attack":
            $ damage = player3_attack
            if player3_mp < 90:
                $ player3_mp += 10
        elif p_action == "skills":
            call player3_skills_2 from _call_player3_skills_2
        elif p_action == "defend":
            $ damage = -1
            $ player3_defend = True
            if player3_mp < 95:
                $ player3_mp += 25
    elif player_turn == player4:
        if p_action == "attack":
            $ damage = player4_attack
            $ player4_mp += 10
        elif p_action == "skills":
            call player4_skills from _call_player4_skills_1
        elif p_action == "defend":
            $ damage = -1
            $ player4_defend = True
            $ player4_mp += 25
    if damage < 0:
        return
    else:
        call screen player_target_5
        $ target = _return
        if target == "marianne":
            if stun_dmg:
                $ marianne_skipturn = True
                $ marianne_hp = marianne_hp - damage
                "[target] was stunned by Inanna's studied materialist application of theory and may not attack!"
                $ stun_dmg = False
            else:
                $ marianne_hp = marianne_hp - damage
        elif target == "sarah":
            if stun_dmg:
                $ sarah_skipturn = True
                $ sarah_hp = sarah_hp - damage
                "[target] was stunned by Inanna's studied materialist application of theory and may not attack!"
                $ stun_dmg = False
            else:
                $ sarah_hp = sarah_hp - damage
        elif target == "kaye":
            if stun_dmg:
                $ kaye_skipturn = True
                $ kaye_hp = kaye_hp - damage
                "[target] was stunned by Inanna's studied materialist application of theory and may not attack!"
                $ stun_dmg = False
            else:
                $ kaye_hp = kaye_hp - damage
        elif target == "chud":
            if stun_dmg:
                $ chud_skipturn = True
                $ chud_hp = chud_hp - damage
                $ stun_dmg = False
                "[target] was stunned by Inanna's studied materialist application of theory and may not attack!"
            else:
                $ chud_hp = chud_hp - damage
        elif target == "chud2":
            if stun_dmg:
                $ chud2_skipturn = True
                $ chud2_hp = chud2_hp - damage
                $ stun_dmg = False
                "[target] was stunned by Inanna's studied materialist application of theory and may not attack!"
            else:
                $ chud2_hp = chud2_hp - damage
        elif target == "all":
            if stun_dmg:
                $ chud_skipturn = True
                $ chud2_skipturn = True
                $ marianne_skipturn = True
                $ kaye_skipturn = True
                $ sarah_skipturn = True
                "All enemies were stunned by Javier's dazzling show!"
                $ stun_dmg = False
            else: 
                $ marianne_hp = marianne_hp - damage
                $ sarah_hp = sarah_hp - damage
                $ chud_hp = chud_hp - damage
                $ kaye_hp = kaye_hp - damage
                $ chud2_hp = chud2_hp - damage
        if p_action == "attack":
            $ message = "player_attack"
        elif p_action == "skills":
            $ message = "player_skill"
        $ renpy.pause(1.0)
        return

label player1_skills_5:
    hide screen battle_5_overlay_players
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
    show screen battle_5_overlay_players

    return
label player2_skills_5:
    hide screen battle_5_overlay_players
    call screen inanna_skills
    $ p_skill = _return
    if p_skill == "Rigorous Discourse":
        $ damage = player2_attack * 0.75
        $ player2_mp -= 33
        $ stun_dmg = True
    elif p_skill == "Double Mommy Smack":
        $ damage = player2_attack
        $ target = "all"
        $ player2_mp -= 45
    elif p_skill == "Righteous Smiting":
        $ damage = player2_attack * 2.5
        $ player2_mp -= 66
    show screen battle_5_overlay_players
    return
label player3_skills_2:
    hide screen battle_5_overlay_players
    call screen javier_skills
    $ p_skill = _return
    if p_skill == "Razzle Dazzle":
        $ target = "all"
        $ stun_dmg = True
        $ player3_mp -= 60
    elif p_skill == "Femboi Magic":
        $ damage = player3_attack*4
        $ player3_mp -= 25
    elif p_skill == "Eyeliner Slash":
        $ damage = player3_attack * 6
        $ player3_mp -= 30
    elif p_skill == "Healing Gay Vibes":
        $ player3_mp -= 20
        menu:
            "Who should Javier heal?"
            "Parvez":
                $ damage = -1
                $ player1_hp += 40
                "Javier healed Parvez by 40 points!"
            "Inanna":
                $ damage = -1
                $ player2_hp += 40
                "Javier healed Inanna by 40 points!"
            "Javier":
                $ damage = -1
                $ player3_hp += 40
                "Javier healed xemself by 40 points!"
            "Terry":
                $ damage = -1
                $ player4_hp += 40
                "Javier healed Terry by 40 points!"
    show screen battle_5_overlay_players
    return    
label player4_skills:
    hide screen battle_overlay_players
    call screen terry_skills
    $ p_skill = _return
    if p_skill == "Bisexual Disaster":
        $ damage = player4_attack * 2
        $ target = "all"
        $ player4_mp -= 33
    elif p_skill == "Restoring Hug":
        $ player4_mp -= 55
        menu:
            "Who should Terry heal?"
            "Parvez":
                $ damage = -1
                $ player1_hp += 55
                "Terry healed Parvez by 55 points!"
            "Inanna":
                $ damage = -1
                $ player2_hp += 55
                "Terry healed Inanna by 55 points!"
            "Javier":
                $ damage = -1
                $ player3_hp += 55
                "Terry healed Javier by 55 points!"
            "Terry":
                $ damage = -1
                $ player4_hp += 55
                "Terry healed themself by 55 points!"
    elif p_skill == "Good Vibration":
        $ player4_mp -= 20
        "Terry's good energy healed all party members by 20 points."
        $ player1_hp += 20
        $ player2_hp += 20
        $ player3_hp += 20
        $ player4_hp += 20
        $ damage = -1
    elif p_skill == "Protective Instinct":
        $ player4_mp -= 40
        $ damage = player4_attack * 4
    show screen battle_5_overlay_players
    return

screen javier_skills:
    add "battle/battlebox2.png" xalign 0.375 yalign .95
    if player3_mp >= 60:
        textbutton "Razzle Dazzle" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.3 yalign 0.855 action Return("Razzle Dazzle")  
    if player3_mp >= 25:
        textbutton "Femboi Magic" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.525 yalign 0.855 action Return("Femboi Magic") 
    if player3_mp >= 30:
        textbutton "Eyeliner Slash" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.3 yalign 0.92 action Return("Eyeliner Slash")
    if player3_mp >= 20:
        textbutton "Healing Gay Vibes" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.525 yalign 0.92 action Return("Healing Gay Vibes") 
screen terry_skills:
    add "battle/battlebox2.png" xalign 0.375 yalign .95
    if player4_mp >= 33:
        textbutton "Bisexual Disaster" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.3 yalign 0.855 action Return("Bixsexual Disaster")  
    if player4_mp >= 55:
        textbutton "Restoring Hug" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.525 yalign 0.855 action Return("Restoring Hug") 
    if player4_mp >= 40:
        textbutton "Protective Instinct" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.3 yalign 0.92 action Return("Protective Instinct")
    if player4_mp >= 20:
        textbutton "Good Vibration" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.525 yalign 0.92 action Return("Good Vibration")
label monster_turn_5:
    while monster_numbers >= m_turn:
        if m_turn == 1:
            if marianne_dead:
                pass
            elif marianne_skipturn:
                "Marianne was stunned and couldn't attack!"
                $ marianne_skipturn = False
                return
            else:
                $ monster_turn = "marianne"
                call monster_dealt_damage_5 from _call_monster_dealt_damage_5
                $ message = "marianne_attack"
                call player_dead_check_5 from _call_player_dead_check_15
        elif m_turn == 2:
            if sarah_dead:
                pass
            elif sarah_skipturn:
                "Sarah was stunned and couldn't attack!"
                $ sarah_skipturn = False
                return
            else:
                $ monster_turn = "sarah"
                call monster_dealt_damage_5 from _call_monster_dealt_damage_15
                $ message = "sarah_attack"
                call player_dead_check_5 from _call_player_dead_check_16
        elif m_turn == 3:
            if kaye_dead:
                pass
            elif kaye_skipturn:
                "Kaye was stunned and couldn't attack!"
                $ kaye_skipturn = False
                return
            else:
                $ monster_turn = "kaye"
                call monster_dealt_damage_5 from _call_monster_dealt_damage_16
                $ message = "kaye_attack"
                call player_dead_check_5 from _call_player_dead_check_17
        elif m_turn == 4:
            if chud_dead:
                pass
            elif chud_skipturn:
                "The chud was stunned and couldn't attack!"
                $ chud_skipturn = False
                return
            else:
                $ monster_turn = "chud"
                call monster_dealt_damage_5 from _call_monster_dealt_damage_5_1
                $ message = "chud_attack"
                call player_dead_check_5 from _call_player_dead_check_18
        elif m_turn == 5:
            if chud2_dead:
                pass
            elif chud2_skipturn:
                "The chud was stunned and couldn't attack!"
                $ chud2_skipturn = False
                return
            else:
                $ monster_turn = "chud2"
                call monster_dealt_damage_5 from _call_monster_dealt_damage_5_2
                $ message = "chud2_attack"
                call player_dead_check_5 from _call_player_dead_check_19        
        
        $ renpy.pause(1.5)
        $ m_turn += 1
    return

label monster_dealt_damage_5:
    if monster_turn == "marianne":
        $ m_damage = renpy.random.randint(marianne_attack_min,marianne_attack_max)
    elif monster_turn == "sarah":
        $ m_damage = renpy.random.randint(sarah_attack_min,sarah_attack_max)
    elif monster_turn == "kaye":
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
    elif monster_target == 2:
        if player2_defend:
            $ m_damage = m_damage - player2_defense
            if m_damage < 0:
                $ m_damage = 0
        $ player2_hp = player2_hp - m_damage
        $ m_target = player2
    elif monster_target == 3:
        if player3_defend:
            $ m_damage = m_damage - player3_defense
            if m_damage < 0:
                $ m_damage = 0
        $ player3_hp = player3_hp - m_damage
        $ m_target = player3
    elif monster_target == 4:
        if player4_defend:
            $ m_damage = m_damage - player4_defense
            if m_damage < 0:
                $ m_damage = 0
        $ player4_hp = player4_hp - m_damage
        $ m_target = player4
    return
    
label monster_dead_check_5:
    if marianne_hp <=0:
        $ marianne_dead = True
        $ marianne = "none"
    if sarah_hp <=0:
        $ sarah_dead = True
        $ sarah = "none"
    if kaye_hp <=0:
        $ kaye_dead = True
        $ kaye = "none"
    if chud_hp <=0:
        $ chud_dead = True
        $ chud = "none"
    if chud2_hp <=0:
        $ chud2_dead = True
        $ chud2 = "none"
    if marianne_dead == sarah_dead == kaye_dead == chud_dead == chud2_dead == True: # chud_dead == True:
        $ check_win = True
        $ marianne = "none"
        $ sarah = "none"
        $ chud = "none"
        $ kaye = "none"
        $ chud2 = "none"
    return 

label player_dead_check_5:
    if player1_hp <= 0 and player2_hp <= 0 and player3_hp <= 0 and player4_hp <= 0: # or player3_hp <= 0 or player4_hp <= 0:
        stop sound
        play audio defeated
        $ renpy.music.set_pause(False, channel='music')
        "You got bashed!"
        "The crew were barely able to escape to safety."
        call screen chapterselect
        #$ renpy.full_restart() # returns to main menu, game over 
    else:
        return
screen battle_5_overlay_players:
    add "battle/battlebox2.png" xalign 0.375 yalign .95
    add "battle/battlebox1.png" xalign .75 yalign .95
    #player 1 is assume to always exist
    if turn == 1:
        add "parvez_icon" xalign 0.25 yalign .94   # player icon in hp area
        add "parvez_sprite" xalign 0.3 yalign 0.25       #player chara above 
    else:
        add "parvez_icon_idle" xalign 0.25 yalign .94
        add "parvez_sprite_idle" xalign 0.3 yalign 0.25
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
    
    if player2 != "none":
        
        if turn == 2:
            add "inanna_icon" xalign 0.36 yalign .94     # player icon in hp area
            add "inanna_sprite" xalign 0.3 yalign 0.66     # player chara above   
        else:
            add "inanna_icon_idle" xalign 0.36 yalign .94
            add "inanna_sprite_idle" xalign 0.3 yalign 0.66
        bar:
            xalign .36
            yalign .9
            style "bar_hp"
            value player2_hp xmaximum 181
            range player2_hp_max
        bar:
            xalign .36
            yalign .94
            style "bar_mp"
            value player2_mp xmaximum 181
            range player2_mp_max
        text"[player2_hp]/[player2_hp_max]" xalign 0.36 yalign 0.904
        text"[player2_mp]/[player2_mp_max]" xalign 0.36 yalign 0.944   
        
    if player3 != "none":
        
        if turn==3:
            add "javier_icon" xalign 0.47 yalign .94
            add "javier_sprite" xalign 0.15 yalign 0.25
        else:
            add "javier_icon_idle" xalign 0.47 yalign .94
            add "javier_sprite_idle" xalign 0.15 yalign 0.25
        bar:
            xalign .47
            yalign .9
            style "bar_hp"
            value player3_hp xmaximum 181
            range player3_hp_max
        bar:
            xalign .47
            yalign .94
            style "bar_mp"
            value player3_mp xmaximum 181
            range player3_mp_max
        text"[player3_hp]/[player3_hp_max]" xalign 0.47 yalign 0.904
        text"[player3_mp]/[player3_mp_max]" xalign 0.47 yalign 0.944 
        
    if player4 != "none":
        if turn == 4:
            add "terry_icon" xalign 0.58 yalign .94
            add "terry_sprite" xalign 0.15 yalign 0.7
        else:
            add "terry_icon_idle" xalign 0.58 yalign .94
            add "terry_sprite_idle" xalign 0.15 yalign 0.7
        bar:
            xalign .58
            yalign .90
            style "bar_hp"
            value player4_hp xmaximum 181
            range player4_hp_max
        bar:
            xalign .58
            yalign .94
            style "bar_mp"
            value player4_mp xmaximum 181
            range player4_mp_max
        text"[player4_hp]/[player4_hp_max]" xalign 0.58 yalign 0.904
        text"[player4_mp]/[player4_mp_max]" xalign 0.58 yalign 0.944  

screen battle_5_overlay_monsters:
    if marianne != "none":
        add "marianne_sprite" xalign 0.66 yalign 0.2
        bar:
            xalign .6
            yalign .305
            style "bar_hp"
            value marianne_hp xmaximum 181
            range marianne_hp_max
        text "[marianne_hp]/[marianne_hp_max]" xalign 0.6 yalign 0.305
    if sarah != "none":
        add "sarah_sprite" xalign 0.9 yalign 0.0
        bar:
            xalign .8
            yalign .23
            style "bar_hp"
            value sarah_hp xmaximum 181
            range sarah_hp_max
        text "[sarah_hp]/[sarah_hp_max]" xalign 0.8 yalign 0.23

    if kaye != "none":
        add "kaye_sprite" xalign 0.9 yalign 0.5
        bar:
            xalign .8
            yalign .5
            style "bar_hp"
            value kaye_hp xmaximum 181
            range kaye_hp_max
        text "[kaye_hp]/[kaye_hp_max]" xalign 0.8 yalign 0.5
    
    if chud != "none":
        add "chud_sprite" xalign 0.66 yalign 0.6
        bar:
            xalign .6
            yalign .55
            style "bar_hp"
            value chud_hp xmaximum 181
            range chud_hp_max
        text "[chud_hp]/[chud_hp_max]" xalign 0.6 yalign 0.55

    if chud2 != "none":
        add "chud2_sprite" xalign 0.9 yalign 1.0
        bar:
            xalign .8
            yalign .75
            style "bar_hp"
            value chud2_hp xmaximum 181
            range chud2_hp_max
        text "[chud2_hp]/[chud2_hp_max]" xalign 0.8 yalign 0.75


screen battle_5_message:
    add "battle/messagebox.png" xalign 0.5 yalign 0.025
    if message == "player1_turn":
        text "What will [player1] do?" xalign 0.5 yalign 0.05
    elif message == "player2_turn":
        text "What will [player2] do?" xalign 0.5 yalign 0.05
    elif message == "player3_turn":
        text "What will [player3] do?" xalign 0.5 yalign 0.05
    elif message == "player4_turn":
        text "What will [player4] do?" xalign 0.5 yalign 0.05
        
    if message == "player_attack":
        text "[player_turn] attacks! Dealt [damage] damage!" xalign 0.5 yalign 0.05
    if message == "player_skill":
        text "[player_turn] used [p_skill]! Dealt [damage] damage!" xalign 0.5 yalign 0.05

        
    elif message == "marianne_attack":
        text "[marianne] attacks! [m_target] took [m_damage] damage!" xalign 0.5 yalign 0.05
    elif message == "sarah_attack":
        text "[sarah] attacks! [m_target] took [m_damage] damage!" xalign 0.5 yalign 0.05
    elif message == "kaye_attack":
        text "[kaye] attacks! [m_target] took [m_damage] damage!" xalign 0.5 yalign 0.05
    elif message == "chud_attack":
        text "[chud] attacks! [m_target] took [m_damage] damage!" xalign 0.5 yalign 0.05
    elif message == "chud2_attack":
        text "[chud2] attacks! [m_target] took [m_damage] damage!" xalign 0.5 yalign 0.05

screen player_actions_5: #returns for player action
    textbutton "Attack" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.75 yalign 0.84 action Return("attack") 
    textbutton "Skills" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.75 yalign 0.89 action Return("skills") 
    textbutton "Defend" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.75 yalign 0.94 action Return("defend") #damage from monster is lowered depending on player's defense
    #textbutton "Items" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.75 yalign 0.98 action Return("items") #not implemented yet

screen player_target_5: #returns monster player wants to attack
    if target == "all":
        textbutton "All Enemies" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.48 yalign 0.48 action Return("all")
    else:
        if marianne != "none":
            textbutton "[marianne]" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.6 yalign 0.27 action Return("marianne") 
        if sarah != "none":
            textbutton "[sarah]" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.79 yalign 0.195 action Return("sarah") 
        if kaye != "none":
            textbutton "[kaye]" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.79 yalign 0.47 action Return("kaye") 
        if chud != "none":
            textbutton "[chud]" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.59 yalign 0.52 action Return("chud") 
        if chud2 != "none":
            textbutton "[chud2]" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.79 yalign 0.72 action Return("chud2")