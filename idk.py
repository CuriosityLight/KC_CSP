import random
from random import SystemRandom
ball_choice = ["0 green", "1 black"]
coins = 10
choice_player = ""
choice = ""
bet_amount = 0
rand = SystemRandom()

def funny(choice_player, choice, coins, bet_amount):
    while True:
        while True:
            print("you have", coins, "coins")
            fun_again = input("bet again? ") .lower()
            if fun_again == "yes":
                bet_amount = int(input("how much would you like to bet. "))
                if bet_amount <= coins:
                    break
                else:
                    
            elif fun_again == "no":
                return
        choice_player = str(input("place a bet on black, red, green or a specific number. ")) .lower()
        choice = rand.choice(ball_choice)
        print("rolling...")
        if choice == "0 green":
            print("0 green")
            if choice_player == "0" or "green":
                coins += bet_amount
                print("you won, you now have", coins, "coins")
            else:
                print("you lost")
                coins /= 2
        elif choice == "1 black":
            if choice_player == "1":
                coins *= 4
                return
            elif choice_player == "black":
                coins *= 2
                return
            else:
                coins /= 2
funny(choice_player, choice, coins, bet_amount)



