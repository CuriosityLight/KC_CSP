import random
from random import SystemRandom
ball_choice = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
# Red: 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36
# black: 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 31, 33, 35
# green: 0,
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
        if choice % 2 == 0:
            if choice_player == "even":
                print(choice)
                coins += bet_amount
            elif choice_player == "odd":
                coins -= bet_amount
                print(choice)
        elif choice %2 != 0:
            if choice_player == "odd":
                coins += bet_amount
                print(choice)
            elif choice_player == "even":
                coins -= bet_amount
                print(choice)
        else:
            if choice == 0:
                print("0 green")
                if choice_player == "0":
                    coins += (bet_amount * 35)
                    print("you won")
                elif choice_player == "green":
                    coins += (bet_amount * 35)
                    print("you won")
                else:
                    print("you lost")
                    coins -= bet_amount
            elif choice == 1:
                print("1 red")
                if choice_player == "1":
                    print("you win")
                    coins += (bet_amount * 2)
                elif choice_player == "red":
                    coins += bet_amount
                    print("you win")
                else:
                    coins -= bet_amount
                    print("you lost")
            elif choice == 2:
                print("2 black")
                if choice_player == "2":
                    coins += (bet_amount *  2)
                elif choice_player == "black":
                    coins += bet_amount
            elif choice == 3:
                print("3 red")
                if choice_player == "3":
                    print("you won")
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



