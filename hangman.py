# KC, hangman
import random

Wguesses = 0
guess_letters = []
text = ""
words = []
word = ""
guess = ""
win = 0
lost = 0
display = ""
text1


with open("words.txt", "r") as file:
    text = file.read()
words = (text.split())
with open("stats.txt", "r") as file:
    text = file.read()
words = (text.split())



def display_word(word, guess_letters):
    display = ""
    for letter in word:
        if letter in guess_letters:
            display += letter
        else:
            display += "_ "
    return display





def hangman(word, Wguesses, guess):
    word = random.choice(words)
    while True:
        if Wguesses == 0:
            print("""
        _____________
        |            |
        |            |
        |  
        |
        |
        |
        |_________________
""")
        elif Wguesses == 1:
            print("""
        _____________
        |            |
        |            |
        |            O
        |            
        |           
        |
        |_________________
""")
        elif Wguesses == 2:
            print("""
        _____________
        |            |
        |            |
        |            O
        |            |
        |           
        |
        |_________________
""")
        elif Wguesses == 3:
            print("""
        _____________
        |            |
        |            |
        |            O
        |           /|
        |          
        |
        |_________________
""")
        elif Wguesses == 4:
            print("""
        _____________
        |            |
        |            |
        |            O
        |           /|\\
        |          
        |
        |_________________
""")
        elif Wguesses == 5:
            print("""
        _____________
        |            |
        |            |
        |            O
        |           /|\\
        |           /
        |
        |_________________
""")
        elif Wguesses == 6:
            print("""
        _____________
        |            |
        |            |
        |            O
        |           /|\\
        |           / \\
        |
        |_________________
""")

        print(display_word(word, guess_letters))

        guess = input("guess a letter. ")
        if guess in guess_letters:
            print("you already guessed that")
        else:
            guess_letters.append(guess)
            if guess not in word:
                Wguesses += 1

            
        




hangman(word, Wguesses, guess)






# create a list of 10 words on a seperate txt file
# create another file that hols win/loss counts
# use split(",") on the content of the word txt doc to create your list of words
# pull win and loste otals from the other txt file and save them as seperate variables
# build hang man (ez)
# save the correct word as a variable random.choice(name of the list)
# number of wrong guesses
# what letter have been guessed