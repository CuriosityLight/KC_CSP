import random
from random import SystemRandom
ball_choice = [0, 1, 2, 3, 17]
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
        if choice_player == "odd" or "even":
            if choice % 2 == 0:
                if choice_player == "even":
                    print(choice)
                    coins += bet_amount
                elif choice_player == "odd":
                    coins -= bet_amount
                    print(choice)
            else:
                if choice_player == "odd":
                    coins += bet_amount
                    print(choice)
                elif choice_player == "even":
                    coins -= bet_amount
                    print(choice)
        elif choice == 0:
            print("0 green")
            if choice_player == "0" or "green":
                coins += (bet_amount * 10)
                print("you won, you now have", coins, "coins")
            else:
                print("you lost")
                coins -= bet_amount
        elif choice == 1:
            if choice_player == "1":
                coins += (bet_amount * 2)
            elif choice_player == "red":
                coins += bet_amount
            else:
                coins -= bet_amount
        elif choice == 2:
            print("2 black")
            if choice_player == "2":
                coins += (bet_amount *  2)
            elif choice_player == "black":
                coins += bet_amount
        elif choice == 17:
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



