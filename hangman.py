# KC, hangman
import random

Wguesses = 0
guess_letters = []
text = ""
words = []
word = ""
guess = ""
display = ""
text1 =  ""
stat = []
win = 0
lost = 0
w_l = ""

def stats_update(win, lost):
    win = str(win)
    lost = str(lost)
    with open("stats.txt", "w") as file2:
        file2.write(win)
    with open("stats.txt", "a") as file2:
        file2.write(",")
        file2.write(lost)
    return win, lost




def display_word(word, guess_letters):
    display = ""
    for letter in word:
        if letter in guess_letters:
            display += letter
        else:
            display += "_ "
    print(display)
    return display

def hangman(word, Wguesses, guess, stat, win, lost):

    with open("stats.txt", "r") as file1:
        statistic = file1.read()
    stat = (statistic.split(","))
    win = int(stat[0])
    lost = int(stat[1])
    print("won:", win)
    print("lost:", lost)
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
            print("you were out of guesses, the word was,", word)
            lost += 1
            stats_update(win, lost)
            return word, Wguesses, guess, stat, win
        if display_word(word, guess_letters) == word:
            print("you won!")
            win += 1
            stats_update(win, lost)
            return word, Wguesses, guess, stat, win

        if guess_letters != []:
            print("your guessed letters is:")
            print(str(guess_letters).replace("[", " ").replace("]", "").replace("'", "").strip())
        while True:
            guess = input("guess a letter. ")
            if guess in guess_letters:
                print("you already guessed that")
            else:
                guess_letters.append(guess)
                if guess not in word:
                    Wguesses += 1
                    break
                else:
                    print(guess, "was in the word")
                    break

again = ""
again_again = 0
while True:
    guess_letters = []
    with open("words.txt", "r") as file:
        text = file.read()
    words = (text.split())
    if again_again >= 1:
        again = input("do you want to play again? ")
    else:
        again = input("do you want to play hangman? ")
    if again == "yes":
        again_again += 1
        hangman(word, Wguesses, guess, stat, win, lost)
    elif again == "no":
        print("bye bye")
        break
    else:
        print("yes or no")
            
        











# create a list of 10 words on a seperate txt file
# create another file that hols win/loss counts
# use split(",") on the content of the word txt doc to create your list of words
# pull win and loste otals from the other txt file and save them as seperate variables
# build hang man (ez)
# save the correct word as a variable random.choice(name of the list)
# number of wrong guesses
# what letter have been guessed