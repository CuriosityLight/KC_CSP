# KC, 7th, Number Guessing Game
import random
tries = 0
number = random.randint(1,100)
guess = ""
print("im thinking of a number between 1 and 100, guess it")
while True:
    if tries >= 6:
        print("out of guesses, the number was", number)
        break
    guess = int(input("guess the number. "))
    if guess == number:
        print("you won, it only took you", tries, "tries")
    elif guess > number:
        tries += 1
        print("wrong, lower")
    elif guess < number:
        tries += 1
        print("wrong, higher")

