# keegan carter, text based adventure game
import random



######################## step 1: variables #######################
player = {   # <==== dictonary (key & value pair to give details about an item)
    "hp": 20,
    "L_attack": 6,
    "H_attack": 10,
    "defense": 5,
    "inventory": []
}

enemy = {
    "hp": 8,
    "L_attack": 4,
    "H_attack": 7,
    "defense": 2,
}

boss = {
    "hp": 200,
    "L_attack": 30,
    "H_attack": 40,
    "defense": 5,

}

sword = 0
while True:
    if player["hp"] > 0:
        break
# varible for the current room
current_room = 1
coin_amount = 0
turn = ""
turn2 = ""
enemy_attack = ""

#### step 2: functions ########################################################
# combat function
def combat(player, enemy, turn, turn2, enemy_attack, sword):
    while True:
            # give player 3 or more options
        enemy_attack = random.choice(["light", "heavy", "defend"])
        print("you have ", player["hp"], " hp")
        print("the enemy has ", enemy["hp"], " hp")
        turn = input("would you like to attack, defend, use item, (attack, defend, item) ")
        if sword == 0:
            if turn == "attack":
                turn2 = input("would you like to light attack, heavy attack, attack with item or attack secondary. (light, heavy or item) ")
                if turn2 == "light":
                    if enemy_attack == "light":
                        print("you hit with a light attack and so does the enemy. nothing happens")
                    elif enemy_attack == "heavy":
                        enemy["hp"] -= player["L_attack"]
                        print("your enemy tried to hit you with a heavy attack but you quickly hit them with a light attack.")
                    elif enemy_attack == "defend":
                        enemy["hp"] += 2
                        print("the enemy defended and gained more hp")
                elif turn2 == "heavy":
                    if enemy_attack == "light":
                        player["hp"] -= enemy["L_attack"]
                        print("as you try to attack the enemy with a heavy attack, they quickly attack you with a light attck. you take damage...")
                    elif enemy_attack == "heavy":
                        print("the enemy did a heavy attack, you did as well. nothing happened")
                    elif enemy_attack == "defend":
                        enemy["hp"] -= player["H_attack"]
                        print("they defended and you hit them with a heavy attack! you damaged them.")
                if turn2 == "item":
                    print(player["inventory"])
            elif turn == "defend":
                if enemy_attack == "light":
                    print("as you defended, they try to hit you with a light attack!, you healed.")
                    player["hp"] += 2
                elif enemy_attack == "heavy":
                    print("as you defended, they hit you with a heavy attack... you take damage,")
                    player["hp"] -= enemy["H_attack"]
                elif enemy_attack == "defend":
                    print("as you defended, they did too. nothing happend")
            elif turn == "kill thy enemy":
                enemy["hp"] -= 327892387923 
                print("you kinda uh cheated...")         
            else:
                print("please select one of the moves")
            #check to see if died, break out of the loop
            if player["hp"] <= 0:
                print("you died to the enemy. try again loser")
                break
            if enemy["hp"] <= 0: 
                print("you have killed the enemy!")
                break
        elif sword == 1:
            if turn == "attack":
                turn2 = input("you have thy sword, strike them down... (light, heavy, defend, item)")
                if turn2 == "light":
                    if enemy_attack == "light":
                        print("the enemy tried to hit you with a light attack, doesnt matter...")
                        enemy["hp"] -= player["L_attack"]
                    elif enemy_attack == "heavy":
                        enemy["hp"] -= player["L_attack"]
                        print("they tried to hit you with a heavy attack. but doesnt matter")
                    elif enemy_attack == "defend":
                        enemy["hp"] -= player["L_attack"]
                        print("the enemy defended yet you broke their defense")
                elif turn2 == "heavy":
                    if enemy_attack == "light":
                        enemy["hp"] -= player["L_attack"]
                        print("they tried to be fast at hitting yet failed...")
                    elif enemy_attack == "heavy":
                        print("they tried to copy you, failed in doing so")
                        enemy["hp"] -= player["h_attack"]
                    elif enemy_attack == "defend":
                        enemy["hp"] -= player["H_attack"]
                        print("they defended... bad mistake")
                if turn2 == "item":
                    print(player["inventory"])
            elif turn == "defend":
                if enemy_attack == "light":
                    print("you defended and they lightly hit you... healed.")
                    player["hp"] += 2478423043
                elif enemy_attack == "heavy":
                    print("you defended, they hit heavy... reflected")
                    enemy["hp"] -= enemy["H_attack"]
                elif enemy_attack == "defend":
                    print("you defended, they did too.")
            elif turn == "kill thy enemy":
                enemy["hp"] -= 327892387923 
                print("even with thy power, you result to this..?")         
            else:
                print("kill them NOW")
            #check to see if died, break out of the loop
            if player["hp"] <= 0:
                print("you died to the enemy. try again loser")
                break
            if enemy["hp"] <= 0: 
                print("death")
                break
    return player, enemy, turn, turn2, enemy_attack, sword



def combat_boss(player, boss, boss_attack, turn_boss, turn2_boss):
    while True:
        boss_attack = random.choice(["light", "heavy", "defend"])
        print("you have ", player["hp"], " hp")
        print("the enemy has ", boss["hp"], " hp")
        turn_boss = input("would you like to attack, defend, use item, (attack, defend, item) ")
        if turn_boss == "attack":
            turn2_boss = input("would you like to light attack, heavy attack, attack with item or attack secondary. (light, heavy or item) ")
            if turn2_boss == "light":
                if boss_attack == "light":
                    print("you hit with a light attack and so does the enemy. nothing happens")
                elif boss_attack == "heavy":
                    boss["hp"] -= player["L_attack"]
                    print("your enemy tried to hit you with a heavy attack but you quickly hit them with a light attack.")
                elif boss_attack == "defend":
                    boss["hp"] += 10
                    print("the enemy defended and gained more hp")
            elif turn2_boss == "heavy":
                if boss_attack == "light":
                    player["hp"] -= boss["L_attack"]
                    print("as you try to attack the enemy with a heavy attack, they quickly attack you with a light attck. you take damage...")
                elif boss_attack == "heavy":
                    print("the enemy did a heavy attack, you did as well. nothing happened")
                elif boss_attack == "defend":
                    boss["hp"] -= player["H_attack"]
                    print("they defended and you hit them with a heavy attack! you damaged them.")
            if turn2_boss == "item":
                print(player["inventory"])
        elif turn_boss == "defend":
            if boss_attack == "light":
                print("as you defended, they try to hit you with a light attack!, you healed.")
                player["hp"] += 2
            elif boss_attack == "heavy":
                print("as you defended, they hit you with a heavy attack... you take damage,")
                player["hp"] -= boss["H_attack"]
            elif boss_attack == "defend":
                print("as you defended, they did too. nothing happend")          
        else:
            print("please select one of the moves")
         #check to see if died, break out of the loop
        if player["hp"] <= 0:
            print("you died to the enemy. try again loser")
            break
        if boss["hp"] <= 0: 
            print("you have killed the enemy!")
            break
    return player, boss

# in combat, the user can either attack (it has its sub categories), defend, use item,
    # attack sub categories: light attack, heavy attack, attack with item.
        # light attack is where you usse the primary weapon you have but its fast but not strong.
        # heavy attack is where you use the primary weapon you have but its slow but fast
            # speed of an attack is that fast beats slow.
        # attack with item is self explanatory, you use an item you have to attack with.
    # if you do a fast attack when they do a slow, you do double the damage.
    # when you defend, you regen but you still get some damge from the enemy.

room1_coin = 0


# room 1 (start room)
    # give the description of situation
        # you're alone, you are broke, you have nothing but the only thing in mind is to... get stronger.
# if you search here you find a coin.
    # give options of where to go/things to do
    # return what room they are going to next
# a door goes to only room 2
action = ""
print("             You dont know how you got here. but all you have in mind is to get stronger")
print("remember to get the coin in each room, you might not be able to go back")

def room(action, room1_coin, coin_amount, current_room):
    print("This is the first room, you cant see much but theres only 1 door...")
    action = input("you can either search or go to the next room which is room 2. (next or search) ")
    if action == "next":
            current_room += 1
            return 2, room1_coin, coin_amount
    if action == "search":
        if room1_coin == 0:
            coin_amount += 1
            print("you found a coin, ", coin_amount, "/7")
            room1_coin = 1
            return 1, room1_coin, coin_amount
        elif room1_coin == 1:
            print("you already searched, you found nothing.")
            return 1, room1_coin, coin_amount


search_2 = 0
# room 2 (4 way hallway)
    # nothing happens only a way to go to room
        # go to either start, room 3, room 4, room 5
    # return what room they are going to next
# you can search but you find a mice and it bites you, -10 hp
action2 = ""
def room2(action2, current_room, search_2, coin_amount, castle_diamond):
    print("this is the second room, its a four way hallway.")
    action2 = input("you can go left, forward, right, or back, or instead of moving you can search (left, right, forward ,back or search) ")
    if action2 == "left":
        current_room += 1
        return action2, current_room, search_2, coin_amount, castle_diamond
    elif action2 == "right":
        current_room += 2
        return action2, current_room, search_2, coin_amount, castle_diamond
    elif action2 == "forward":
        current_room += 3
        return action2, current_room, search_2, coin_amount, castle_diamond
    elif action2 == "back":
        current_room -= 1
        return action2, current_room, search_2, coin_amount, castle_diamond
    elif action2 == "search":
        if search_2 == 0:
            print("you searched and found a rat! it bit you but it was a small rat, so nothings. maybe try searching again? ")
            search_2 += 1
            return action2, current_room, search_2, coin_amount
        elif search_2 == 1:
            print("you searched again and found a coin!")
            coin_amount += 1
            print(coin_amount, "/7")
            return action2, current_room, search_2, coin_amount
    else:
        print("pick one of the objects")

 
coin_gambled = ""
manuel_read = 0
gamba_again = ""

def gambling(manuel_read, coin_amount, gamba, player, search_amount3, castle_diamond, current_room, gamba_again, coin_gambled):
        gamba = random.choice(["gain", "little gain", "nothing", "little lose", "lose", "gain", "little gain", "coin",  "nothing", "little lose", "lose", "all", "coin", "double", "gain", "little gain", "nothing", "gain", "little gain", "nothing", "coin", "double"])
        if gamba == "gain":
            player["hp"] += 10
            print("you gambled and gain a lot of hp, you now have ", player["hp"], " hp.")
        elif gamba == "little gain":
            player["hp"] += 5
            print("you gambled and gain some hp, you now have ", player["hp"], " hp.")
        elif gamba == "nothing":
            print("you gambled yet nothing happend")
        elif gamba == "little lose":
            player["hp"] -= 5
        elif gamba == "lose":
            player["hp"] -= 10
            print("you gambled and lose a lot of hp, you now have ", player["hp"], " hp.")
        elif gamba == "all":
            player["hp"] = 1
            print("oh no... you lossed all your hp, you only have 1 hp left.")
        elif gamba == "coin":
            if coin_gambled == 0:
                coin_amount += 1
                print("you gambled and got a coin!")
                coin_gambled += 1
            elif coin_gambled == 1:
                print("you gambled and got nothing, you wouldve gotton a coing but you already got it")
        elif gamba == "double":
            player["hp"] + player["hp"]
        if player["hp"] <= 0:
            print("you gambled your life away...")
            exit()
        else:
            while True:
                gamba_again = input("do you want to gamble again? (yes or no)")
                if gamba_again == "yes":
                    gambling(manuel_read, coin_amount, gamba, player, search_amount3, castle_diamond, current_room, gamba_again, coin_gambled)
                elif gamba_again == "no":
                    return coin_amount, manuel_read, gamba, player, search_amount3, castle_diamond, current_room, gamba_again, coin_gambled    
                else:
                    print("yes or no")    
gamba = ""
action3 = ""
search_amount3 = 0
castle_diamond = 0
# room 3 (open space with nothing but 1 door, and a slot machine)
    # the lone slot machine is used to gamble your health
        # gain alot of health, gain some health, break even, lose some health, lose alot of health, set hp to 1. or gain the coin (guarenteed on the third spin)
    # only way is to go back to the 4 way hallway
# if you search, you find nothing. seems like the only thing you can do here is to gamble.
# if you search TWICE, it says the same thing
# if you search THRICE, it says the same thing
# IF YOU SEARCH FOR THE FOURTH TIIIMMEEE, you get castle's diamond might uss for a quest that rewards you with nothing.
def room3(action3, manuel_read, coin_amount, gamba, player, search_amount3, castle_diamond, current_room, gamba_again, coin_gambled):
    print("this room is very dark, only with one lightbulb lighting a single slot machine, it has a manuel on it")
    action3 = input("would you like to leave back to the hallways, read the manuel, or start the slot machine. (leave, read, start, or search)")
    if action3 == "leave":
        current_room -= 1
        return action3, manuel_read, coin_amount, gamba, player, search_amount3, castle_diamond, current_room, gamba_again, coin_gambled
    elif action3 == "read":
        if manuel_read == 0:
            print("""you read the manuel:
               READ BEFORE USING THE SLOT MACHINE
                  step 1: turn on the slot machine, press the switch on the back.
                  step 2: insert your hp!
                  step 3: GAMBlING!!!!!!""")
            manuel_read += 1
            return action3, manuel_read, coin_amount, gamba, player, search_amount3, castle_diamond, current_room, gamba_again, coin_gambled
        elif manuel_read == 1:
            print("you already read it")
            return action3, manuel_read, coin_amount, gamba, player, search_amount3, castle_diamond, current_room, gamba_again, coin_gambled
    elif action3 == "start":
        if manuel_read == 0:
            print("you dont know how to turn the slots machine on, maybe try reading the manuel")
            return action3, manuel_read, coin_amount, gamba, player, search_amount3, castle_diamond, current_room, gamba_again, coin_gambled 
        elif manuel_read == 1:
            print("gambling time!!")
            print("you can gain health, gain some health, break even, lose some health, lose a lot of health, or lose ALL your health (very rare), and a some secrets too!!!")
            gambling(manuel_read, coin_amount, gamba, player, search_amount3, castle_diamond, current_room, gamba_again, coin_gambled)
            return action3, manuel_read, coin_amount, gamba, player, search_amount3, castle_diamond, current_room, gamba_again, coin_gambled
    elif action3 == "search":
        if search_amount3 == 0:
            print("you searched and found nothing")
            search_amount3 += 1
            return action3, manuel_read, coin_amount, gamba, player, search_amount3, castle_diamond, current_room, gamba_again, coin_gambled
        elif search_amount3 == 1:
            print("you searched and found nothing")
            search_amount3 += 1
            return action3, manuel_read, coin_amount, gamba, player, search_amount3, castle_diamond, current_room, gamba_again, coin_gambled
        elif search_amount3 == 2:
            print("you searched and found nothing")
            search_amount3 += 1
            return action3, manuel_read, coin_amount, gamba, player, search_amount3, castle_diamond, current_room, gamba_again, coin_gambled
        elif search_amount3 == 3:
            print("you searched and found nothing")
            search_amount3 += 1
            return action3, manuel_read, coin_amount, gamba, player, search_amount3, castle_diamond, current_room, gamba_again, coin_gambled
        elif search_amount3 == 4:
            print("you searched and found nothing")
            search_amount3 += 1
            return action3, manuel_read, coin_amount, gamba, player, search_amount3, castle_diamond, current_room, gamba_again, coin_gambled
        elif search_amount3 == 5:
            print("you search one more time, and found castles diamond!!!!!!")
            search_amount3 +=1
            castle_diamond +=1
            return action3, manuel_read, coin_amount, gamba, player, search_amount3, castle_diamond, current_room, gamba_again, coin_gambled
        else:
            print("why search anymore?")
            return action3, manuel_read, coin_amount, gamba, player, search_amount3, castle_diamond, current_room, gamba_again, coin_gambled
    else:
        action3 = input("leave, read, start, or search")
        
            
action4 = ""
enemy_killed = 0
# room 4 (the outside)
    # some monster attack you
    # a door back to hallway, a door to  room 5, a door to room 6
# if you search, you find another monster that attacks you.
def room4(player, enemy, enemy_killed, action4, current_room, coin_amount, turn, turn2, enemy_attack, sword):
    if enemy_killed == 0:
        print("uh oh, theres an enemy outside!")
        combat(player, enemy, turn, turn2, enemy_attack, sword)
        enemy_killed += 1
        print("luckily the enemy dropped a coin!")
        coin_amount += 1
        print("you now have ", coin_amount, "/6")
        return player, enemy, enemy_killed, action4, current_room, coin_amount, turn, turn2, enemy_attack
    elif enemy_killed == 1:
        print("the monsters corpse lays in front of you")
        action4 = input("do you want to go to room 5 or room 6, search, or back to room 2? (5 or 6 or 2 or search)")
        if action4 == "5":
            current_room += 1
            return player, enemy, enemy_killed, action4, current_room, coin_amount, turn, turn2, enemy_attack
        elif action4 == "6":
            current_room += 2
            return player, enemy, enemy_killed, action4, current_room, coin_amount, turn, turn2, enemy_attack
        elif action4 == "2":
            current_room -= 2
            return player, enemy, enemy_killed, action4, current_room, coin_amount, turn, turn2, enemy_attack
        elif action4 == "search":
            print("you found nothing")
            return player, enemy, enemy_killed, action4, current_room, coin_amount, turn, turn2, enemy_attack



    
    
action5 = ""
weapon_grabbed = ""
coinfound5 = 0
# room 5 (weaponary where if you grab a weapon, room 6 will be WAY more dangerous)
    # weapons contain: subspace tripmine, command block, super star, the master emerald, zentith, pure nail, the real knife, the thornring, and the gifted vicious bee.   
    # a door to room 2, room 4, and room 6
def room5(weapon_grabbed, coinfound5, current_room, action5, coin_amount):
    if weapon_grabbed == "":
        print("theres many weapons that you can grab in this room, but grabbing one could cause the next room to be bad")
        weapon_grabbed = input("the weapons you could grab is subspace tripmine, or the gifted viscious bee. (subspace, or gifted)")
    elif weapon_grabbed != "":
        print("you have already picked up an item, youre cooked")
    action5 = input("would you like to go back to room 4 or foward to room 6 or search? (4, 6 or search)")
    if action5 == "4":
        current_room -= 1
        return weapon_grabbed, coinfound5, current_room, action5, coin_amount
    elif action5 == "6":
        current_room += 1
        return weapon_grabbed, coinfound5, current_room, action5, coin_amount
    elif action5 == "search":
        if coinfound5 == 0:
            print("you found a coin or whatever")
            coin_amount += 1
            print("you now have ", coin_amount, "/6")
            coinfound5 +=1
            return weapon_grabbed, coinfound5, current_room, action5, coin_amount
        elif coinfound5 == 1:
            print("you searched again and found nothing")
            return weapon_grabbed, coinfound5, current_room, action5, coin_amount
    elif action5 == "glass door":
                current_room += 3
                return weapon_grabbed, coinfound5, current_room, action5, coin_amount

search6 = 0
action6 = ""
enemy_killed2 = 0
# room 6 (the dangerous room)
    # 3 moster in a row to kill, but if you grabbed a weapon from room 5 you have 20 monster fight.
# the monsters will gain upgraded armor and weapons if you grabbed a weapon from room 5
# if you search, you find a potion. the user wont know what it does, but it does -25 hp. you can drink it or throw it onto enemies.
# a door to room 5, room 7
def room6(enemy_killed2, weapon_grabbed, enemy, player, search6, action6, current_room,):
    print("room 6, which is very dangerous, watch out a lot of enemies are here")
    if enemy_killed2 == 0:
        if weapon_grabbed == "gifted":
            print("because you grabbed the gifted vicious bee, theres 3 more enemy than usualy but the bee lowered the health of all the enemy")
            enemy["hp"] -= 12
            combat(player, enemy)
            combat(player, enemy)
            combat(player, enemy)
            combat(player, enemy)
            combat(player, enemy)
            enemy_killed2 += 1
            return enemy_killed2, weapon_grabbed, enemy, player, search6
        elif weapon_grabbed == "subspace":
            print("because you grabbed the subspace tripmine, theres 2 more enemy than usual, but the subspace tripmine insta killed 3 of them")
            combat(player, enemy)
            combat(player, enemy)
            enemy_killed2 += 1
        else:
            print("because you didnt grab anything theres only 3 enemys instead of 5")
            combat(player, enemy)
            combat(player, enemy)
            combat(player, enemy)
            enemy_killed2 += 1
    else:
        action6 = input("would you like to go back to room 5 or try to go foward to room 7 or search (7 or 5 or search) ")
        if action6 == "5":
            current_room -= 1
            return enemy_killed2, weapon_grabbed, enemy, player, search6, action6, current_room
        elif action6 == "7":
            current_room += 1
            return enemy_killed2, weapon_grabbed, enemy, player, search6, action6, current_room
        elif action6 == "search":
            if search6 == 0:
                print("you found a potion")
                return enemy_killed2, weapon_grabbed, enemy, player, search6, action6, current_room
            else:
                print("theres nothing left")
                return enemy_killed2, weapon_grabbed, enemy, player, search6, action6, current_room
        else:
            action6 = input("5, 7 or search")
            return enemy_killed2, weapon_grabbed, enemy, player, search6, action6, current_room


def roomCastle(current_room, player, castle_diamond, sword):
    if sword == 0:
        print("how did you even get here?")
        print("a kid awaits your presence here")
        if castle_diamond == 1:
            print("the kid takes the diamond out of thy hands, you wonder why must he want it so bad?")
            print("he gives you something... a sword of somesorts")
            print("anti-mafia sword equipped")
            player["L_attack"] += 3943782378234782347823
            player["H_attack"] += 3474378348972347892347
            sword += 1
            current_room -= 3
            return
        else:
            print("the kid gets angry that you dont have thy jewl or diamond")
            print("he smites you down, youre dead.")
            exit()
    else:
        print("hes gone, so you go back to whatever you were")
        current_room -= 3



# room 7 (the exit)
    # when you have went to every room and grabbed the coin from each, you win. if not then the room will stay locked untill then.
    # also theres a boss too.
# a door back to room 6
final_choice = ""
def room7(coin_amount, final_choice, current_room, player, boss):
    if coin_amount == 7:
        final_choice = input("the door opens, youre about to fight the final boss, are you sure you want to enter?")
        if final_choice == "yes":
            combat_boss(player, boss)
            print("you have won the game congrats!!!")
        elif final_choice == "no":
            current_room -= 1
    else:
        print("door has not opened yet, go find the rest. you have ", coin_amount-7, "left")
        current_room -= 1


# to win you have to explore every room, you have to find a coin from each room (via searching or from a drop from enemies) and go to room 7 where you then have to defeat a boss.
# to lose, you have to either lose all your health, or you give up.

################### step 3L loop to run the game ##

# Make a while true loop
    #build condtional that checks the room ad calls the coreect function
## example
#if current_room == "start":
#    current_room = start()
#elif current_room = "2nd":
#    current_room, player, monster = 2nd(player, monster)

# check if user died, loser
# check if user won
while True:
    if current_room == 1:
        current_room, room1_coin, coin_amount = room(action, room1_coin, coin_amount, current_room)
    elif current_room == 2:
        action2, current_room, search_2, coin_amount, castle_diamond = room2(action2, current_room, search_2, coin_amount, castle_diamond)
    elif current_room == 3:
        action3, manuel_read, coin_amount, gamba, player, search_amount3, castle_diamond, current_room, gamba_again, coin_gambled = room3(action3, manuel_read, coin_amount, gamba, player, search_amount3, castle_diamond, current_room, gamba_again, coin_gambled)
    elif current_room == 4:
        player, enemy, enemy_killed, action4, current_room, coin_amount, turn, turn2, enemy_attack, sword = room4(player, enemy, enemy_killed, action4, current_room, coin_amount, turn, turn2, enemy_attack, sword)
    elif current_room == 5:
        weapon_grabbed, coinfound5, current_room, action5, coin_amount = room5(weapon_grabbed, coinfound5, current_room, action5, coin_amount)
    elif current_room == 6:
        enemy_killed2, weapon_grabbed, enemy, player, search6, action6, current_room = room6(enemy_killed2, weapon_grabbed, enemy, player, search6, action6, current_room)
    elif current_room == 7:
        coin_amount, final_choice, current_room, player, boss = room7(coin_amount, final_choice, current_room, player, boss)
    elif current_room == 8:
        roomCastle()

