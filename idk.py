import random

ball_choice = ["0 green", "1 black"]
coins = 10 
choice_player = ""
choice = ""
bet_amount = 0


def funny(choice_player, choice, coins):
    choice_player = input("place a bet on black, red, green or a specific number. ")
    choice = random.choice(ball_choice)
    print("rolling...")
    if choice == "0 green":
        print("0 green")
        if choice_player == "green" or "0":
            coins += bet_amount
            return choice_player, choice, coins
        else:
            print("you lost")
            coins / 2
            return
    elif choice == "1 black":
        if choice_player == "1":
            coins * 4
            return
        elif choice_player == "black":
            coins * 2
            return
        


while True:
    print("you have ", coins, " coins")
    fun_again = input("bet again?") .lower()
    if fun_again == "yes":
        while True:
            bet_amount = input("how much would you like to bet")
            if bet_amount.isnumeric:
                break
            else:
                print("yo we fr?")
        funny(choice_player, choice, coins)
    elif fun_again == "no":
        break