# KC, 7th, Number Guessing Game
import random
tries = 0
number = random.randint(1,100)
guess = ""
while tries > 10:
    guess = int(input("guess the number. "))
    if guess == number:
        print("you won, it only took you", tries, "tries")
    elif guess > number:
        tries += 1
        print("wrong, too high")
    elif guess < number:
        tries += 1
        print("wrong, too low")

print("out of guesses, the number was", number)