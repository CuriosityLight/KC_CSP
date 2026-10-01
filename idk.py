import random
from random import SystemRandom
import time





ball_choice = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
# Red: 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36
# black: 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 31, 33, 35
# green: 0,
red = False
black = False
green = False
coins = 50
choice_player = ""
choice = ""
bet_amount = 0
rand = SystemRandom()
fun_again = ""

def roulette(choice_player, choice, coins, bet_amount, fun_again, black, red, green):
    while True:
        while True:
            if coins <= 0:
                print("well you gambled all your money and died")
                return choice_player, choice, coins, bet_amount, fun_again
            print("you have", coins, "coins")
            fun_again = input("bet again? ") .lower()
            while True:
                if fun_again == "yes":
                    bet_amount = int(input("how much would you like to bet. "))
                    if bet_amount <= coins:
                        break
                    else:
                        print("you dont have enough to do that bet")
            if fun_again == "yes":
                break
            elif fun_again == "no":
                return
        choice_player = input("place a bet on black, red, green, even or odds, or a specific number. ") .lower()
        try:
            choice_player = int(choice_player)
        except:
            choice_player = str(choice_player)
        choice = rand.choice(ball_choice)
        if choice == 1 or 3 or 5 or 7 or 9 or 12 or 14 or 16 or 18 or 19 or 21 or 23 or 25 or 27 or 30 or 32 or 34 or 36:
            red = True
        elif choice == 2 or 4 or 6 or 8 or 10 or 11 or 13 or 15 or 17 or 20 or 22 or 24 or 26 or 28 or 31 or 33 or 35:
            black = True
        else:
            green = True
        print("rolling...")
        if choice_player == "even":
            if choice %2 == 0:
                print(choice)
                coins += bet_amount
            elif choice %2 != 0:
                coins -= bet_amount
                print(choice)
        elif choice_player == "odd":
            if choice %2 != 0:
                coins += bet_amount
                print(choice)
            elif choice %2 == 0:
                coins -= bet_amount
                print(choice)
        else:
            if black == True:
                print(choice, "black")
                if choice_player == "black":
                    coins += bet_amount
                    print("you won")
                elif choice_player == choice:
                    coins += bet_amount*36
                    print("you won")
                else:
                    print("you lost")
                    coins -= bet_amount
            elif red == True:
                print(choice, "red")
                if choice_player == "red":
                    coins += bet_amount
                    print("you won")
                elif choice_player == choice:
                    coins += (bet_amount*36)
                    print("you won")
                else:
                    print("you lost")
                    coins -= bet_amount
            elif green == True:
                print(choice, "green")
                if choice_player == "green":
                    coins += bet_amount
                    print("you won")
                elif choice_player == choice:
                    coins += bet_amount*35
                    print("you won")
                else:
                    print("you lost")
                    coins -= bet_amount

slot_choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
slot1 = ""
slot2 = ""
slot3 = ""
slot4 = ""
slot5 = ""
slot6 = ""
slot7 = ""
slot8 = ""
slot9 = ""
coins = 50

def slots(slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, coins, bet_amount, fun_again):
    while True:
        slot1 = rand.choice(slot_choices)
        slot2 = rand.choice(slot_choices)
        slot3 = rand.choice(slot_choices)
        slot4 = rand.choice(slot_choices)
        slot5 = rand.choice(slot_choices)
        slot6 = rand.choice(slot_choices)
        slot7 = rand.choice(slot_choices)
        slot8 = rand.choice(slot_choices)
        slot9 = rand.choice(slot_choices)
        print(f"""
         ___________________
        |                   |
        |    {slot1}    {slot2}    {slot3}    |
        |  \x1b[3m\033[1m  {slot4}    {slot5}    {slot6}\x1b[0m\033[0m    |
        |    {slot7}    {slot8}    {slot9}    |
        |___________________|

        """)
        if slot4 == slot5 and slot5 == slot6:
            print("you win the jackpot!")
            bet_amount *= 100
        elif slot4 == slot5 or slot4 == slot6 or slot5 == slot6:
            print("you win!")
            bet_amount *= 10
        else:
            print("you lost")
            bet_amount *= 0.5
            bet_amount = int(round(bet_amount))
        print(bet_amount, "coins is in the machine")
        while True:
            fun_again = input("would you like to let it ride: ")
            if fun_again == "yes":
                slots(slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, coins, bet_amount, fun_again)
            elif fun_again == "no":
                coins += bet_amount
                return slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, coins, bet_amount, fun_again
            else:
                print("yes or no")
            


def plinko():
    fun_again = input("drop a ball: ")
    if fun_again == "yes":
        print("unfinished")










while True:
    print("you have ", coins, "coins")
    game = input("what game would you like to player (roulette, or slots or plinko)")
    if game == "roulette":
        roulette(choice_player, choice, coins, bet_amount, fun_again, black, red, green)
    elif game == "slots":
        while True:
            try:
                while True:
                    bet_amount = int(input("how much would you like to bet: "))
                    if bet_amount > coins:
                        print("you dont have enough money to do that")
                    else:
                        break
                break
            except:
                print("number please")
        slots(slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, coins, bet_amount, fun_again)





