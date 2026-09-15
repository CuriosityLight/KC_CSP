# KC, ficxing users inputs

while True:
    color = input("Give me a color: ") .strip() .lower()
    if color.isnumeric():
        print("that is a number br, are we fr?")
    elif " " in color:
        print("i said one word")
    else:
        break

print("We painted the walls", color + "!")