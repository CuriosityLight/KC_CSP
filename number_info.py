# KC, number information

number = 1

while True:
    if number == 20:
        break
    if number %2 == 0:
        if number %5 == 0:
            print(number, "is even, and divisible by 5")
            number += 1
        elif number %5 != 0:
            print(number, "is even, and not divisible by 5")
            number += 1
    elif number %2 != 0:
        if number %5 == 0:
            print(number, "is odd, and divisible by 5")
            number += 1
        elif number %5 != 0:
            print(number, "is odd, and not divisible by 5")
            number += 1