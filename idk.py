import random
from random import SystemRandom
import time





ball_choice = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, -5]
# Red: 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36
# black: 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 31, 33, 35
# green: 0,
red = False
black = False
green = False
blue = False
coins = 50
choice_player = ""
choice = ""
bet_amount = 0
rand = SystemRandom()
fun_again = ""

def roulette(choice_player, choice, coins, bet_amount, fun_again, black, red, green, blue):
    while True:
        while True:
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
        if choice == 1 or choice == 3 or choice == 5 or choice == 7 or choice == 9 or choice == 12 or choice == 14 or choice == 16 or choice == 18 or choice == 19 or choice == 21 or choice == 23 or choice == 25 or choice == 27 or choice == 30 or choice == 32 or choice == 34 or choice == 36 :
            red = True
        elif choice == 2 or choice == 4 or choice == 6 or choice == 8 or choice == 10 or choice == 11 or choice == 13 or choice == 15 or choice == 17 or choice == 20 or choice == 22 or choice == 24 or choice == 26 or choice == 28 or choice == 31 or choice == 33 or choice == 35:
            black = True
        elif choice == -5:
            blue = True
        else:
            green = True
        print(red, black, green, blue)
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
            elif blue == True:
                if choice_player == "blue":
                    print("you..won?")
                    coins += bet_amount*100
                elif choice_player == "-5":
                    print("you..won?")
                    coins += bet_amount*100
                else:
                    print("you lost???")

slot_choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "B"]
slot1 = ""
slot2 = ""
slot3 = ""
slot4 = ""
slot5 = ""
slot6 = ""
slot7 = ""
slot8 = ""
slot9 = ""

def slots(slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, coins, bet_amount, fun_again):
    coins -= bet_amount
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
            if slot4 == "B":
                print("YOU LOST")
                bet_amount = 0
            else:
                print("you win the jackpot!")
                bet_amount *= 100
        elif slot4 == slot5 or slot4 == slot6 or slot5 == slot6:
            if slot4 == "B" or slot5 == "B":
                print("YOU LOST:")
                bet_amount = 0
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
card_type = ""
player_cards = []
dealer_cards = []
player_type = []
dealer_type = []
cards = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "king", "queen", "king"]
type_cards = ["of spades", "of hearts", "of clovers", "of diamonds"]
move = ""
total_player = 0
total_dealer = 0
cards_full = []
new_card = ""
new_type = ""
#"Ace of Spades", "2 of Spades", "3 of Spades", "4 of Spades", "5 of Spades", "6 of Spades", "7 of Spades", "8 of Spades", "9 of Spades", "10 of Spades", "Jack of Spades", "Queen of Spades", "King of Spades", "Ace of Hearts", "2 of Hearts", "3 of Hearts", "4 of Hearts", "5 of Hearts", "6 of Hearts", "7 of Hearts", "8 of Hearts", "9 of Hearts", "10 of Hearts", "Jack of Hearts", "Queen of Hearts", "King of Hearts", "Ace of Diamonds", "2 of Diamonds", "3 of Diamonds", "4 of Diamonds", "5 of Diamonds", "6 of Diamonds", "7 of Diamonds", "8 of Diamonds", "9 of Diamonds", "10 of Diamonds", "Jack of Diamonds", "Queen of Diamonds", "King of Diamonds", "Ace of Clubs", "2 of Clubs", "3 of Clubs", "4 of Clubs", "5 of Clubs", "6 of Clubs", "7 of Clubs", "8 of Clubs", "9 of Clubs", "10 of Clubs", "Jack of Clubs", "Queen of Clubs", "King of Clubs"

def jack(bet_amount, player_cards, cards, move, dealer_cards, player_type, dealer_type, coins, total_dealer, total_player, cards_full, new_card, new_type):
    while True:
        try:
            bet_amount = int(input("how much would you like to bet"))
            break
        except:
            print("number please")
    print("disclaimer, aces = 1 not 1 and 11 sorry!")
    player_cards.append(rand.choice(cards))
    player_cards.append(rand.choice(cards))
    dealer_cards.append(rand.choice(cards))
    dealer_cards.append(rand.choice(cards))
    player_type.append(rand.choice(type_cards))
    player_type.append(rand.choice(type_cards))
    dealer_type.append(rand.choice(type_cards))
    dealer_type.append(rand.choice(type_cards))
    print("the dealer shows they have ", dealer_cards[0], "of", dealer_type[0])
    time.sleep(1)
    print("you have", player_cards[0], player_type[0], "and", player_cards[1], player_type[1])
    while True:
        total_player = 0
        total_dealer = 0
        for player_card in player_cards:
            try:
                total_player += player_card
            except:
                if player_card == "ace":
                    total_player += 1
                else:
                    total_player += 10
        for dealer_card in dealer_cards:
            try:
                total_dealer += dealer_card
            except:
                if dealer_card != "ace":
                    total_dealer += 10
                else:
                    total_dealer + 1
        if total_player > 21:
            print("you went over!")
            return coins - bet_amount
        elif total_player == 21:
            if total_dealer == 21:
                print("there was a push!")
                return coins
            else:
                print("you win!")
                return coins + round(bet_amount*2.5)

        time.sleep(1)
        move = input("would you like to stay or hit: ")
        if move == "stay":
            print("you stay")
            while True:
                time.sleep(1)
                print("the dealer has:")
                cards_full = [f"{x} {y}" for x, y in (zip(dealer_cards, dealer_type))]
                print (str(cards_full).replace("[", "").replace("'", "").replace("]", ""))
                total_dealer = 0
                for dealer_card in dealer_cards:
                    try:
                        total_dealer += dealer_card
                    except:
                        if dealer_card != "ace":
                            total_dealer += 10
                        else:
                            total_dealer + 1
                time.sleep(1)
                if total_dealer == 21:
                    if total_player == 21:
                        print("there was a push")
                        return coins
                    else:
                        print("you lost")
                        return coins - bet_amount
                elif total_dealer <= 18:
                    new_card = rand.choice(cards)
                    dealer_cards.append(new_card)
                    new_type = rand.choice(type_cards)
                    dealer_type.append(new_type)
                    time.sleep(2)
                    print(f"the dealers new card is {new_card, new_type}".replace(",", "").replace("(", "").replace(")", "").replace("'", ""))
                elif total_dealer > 18:
                    print("the dealer stayed")
                    time.sleep(1)
                    break
            if total_dealer > 21:
                print("dealer went over")
                print("you win")
                return coins + round(bet_amount*2.5)
            if total_player > total_dealer:
                print("you win!")
                return coins + round(bet_amount*2.5)
            elif total_player < total_dealer:
                print("you lost")
                return coins - bet_amount
            else:
                print("there was a push")
                return coins

                
    
        elif move == "hit":
            print("you grab another card")
            time.sleep(1)
            new_card = rand.choice(cards)
            player_cards.append(new_card)
            new_type = rand.choice(type_cards)
            player_type.append(new_type)
            print(f"your new card is {new_card, new_type}".replace(",", "").replace("(", "").replace(")", "").replace("'", ""))
            time.sleep(1)
            print("your cards are: ")
            cards_full = [f"{x} {y}" for x, y in (zip(player_cards, player_type))]
            print (str(cards_full).replace("[", "").replace("'", "").replace("]", ""))



while True:
    if coins <= 0:
        print("well you gambled all your money and died")
    print("you have ", coins, "coins")
    game = input("what game would you like to player (roulette, or slots or black jack )")
    if game == "roulette":
        roulette(choice_player, choice, coins, bet_amount, fun_again, black, red, green, blue)
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
    elif game == "black jack":
        coins = jack(bet_amount, player_cards, cards, move, dealer_cards, player_type, dealer_type, coins, total_dealer, total_player, cards_full, new_card, new_type)



