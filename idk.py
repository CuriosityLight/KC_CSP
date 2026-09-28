import random
from random import SystemRandom
ball_choice = ["0 green", "1 black", "17 black"]
coins = 50
choice_player = ""
choice = ""
bet_amount = 0
rand = SystemRandom()
fun_again = ""
def funny(choice_player, choice, coins, bet_amount, fun_again):
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
        choice_player = str(input("place a bet on black, red, green or a specific number. ")) .lower()
        choice = rand.choice(ball_choice)
        print("rolling...")
        if choice == "0 green":
            print("0 green")
            if choice_player == "0" or "green":
                coins += (bet_amount * 10)
                print("you won, you now have", coins, "coins")
            else:
                print("you lost")
                coins -= bet_amount
        elif choice == "1 black":
            if choice_player == "1":
                coins += bet_amount
            elif choice_player == "black":
                coins += bet_amount
            else:
                coins -= bet_amount
        elif choice == "17 black":
            print("17 black")
            print("let it ride")
            if choice_player == "17":
                coins += bet_amount
            elif choice_player == "black":
                coins += bet_amount
            else:
                print("you lose")
                coins -= bet_amount
funny(choice_player, choice, coins, bet_amount, fun_again)



