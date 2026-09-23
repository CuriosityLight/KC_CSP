import random

ball_choice = ["0 green", "1 black"]
coins = 10
choice_player = ""
choice = ""
bet_amount = 0


def funny(choice_player, choice, coins, bet_amount):
    choice_player = str(input("place a bet on black, red, green or a specific number. ")) .lower()
    choice = random.choice(ball_choice)
    print("rolling...")
    if choice == "0 green":
        print("0 green")
        if choice_player == "0" or "green":
            coins += bet_amount
            print("you won")
            return choice_player, choice, coins, bet_amount
        else:
            print("you lost")
            coins /= 2
            return choice_player, choice, coins, bet_amount
    elif choice == "1 black":
        if choice_player == "1":
            coins *= 4
            return
        elif choice_player == "black":
            coins *= 2
            return
        else:
            coins /= 2


while True:
    print("you have ", coins, " coins")
    fun_again = input("bet again? ") .lower()
    if fun_again == "yes":
        bet_amount = float(input("how much would you like to bet. "))
        funny(choice_player, choice, coins, bet_amount)
    elif fun_again == "no":
        break