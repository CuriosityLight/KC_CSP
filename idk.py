import random

ball_choice = ["0 green", "1 black" "2 red", "3 black", "4 red", "5 black", "6 red", "7 black", "8 red", "9 black", "10 red", "11 black", "12 red" "13 black", "14 red", "15 black", "16 red", "17 black", "18 red", "19 black", "20 red", "21 black"]
coins = 10
choice_player = ""
bet_amount = int
choice = ""



def funny(choice_player, bet_amount, choice):
    choice_player = input("place a bet on black, red, green or a specific number")
    bet_amount = input("how much would you like to bet")
    choice = random.choice(ball_choice)
    print("rolling...")
    if choice == "0 green":
        print("0 green")
        if choice_player == "green" or "0":
            bet_amount * 27
            bet_amount + coins
            return
        else:
            print("you lost")
            coins - bet_amount
            return
    elif choice == "1 black":
        if choice_player == "1":
            bet_amount * 2
            coins + bet_amount
            return
            
        







while True:
    print("you have ", coins, " coins")
    fun_again = input("bet again?") .lower()
    if fun_again == "yes":
        funny(choice_player, bet_amount, choice)
    elif fun_again == "no":
        break