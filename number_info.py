# KC, number information

number = 1

while number <= 20:
    if number %2 == 0:
        if number %5 == 0:
            print(number, "is even, and divisible by 5")
            number += 1
        else:
            print(number, "is even, and not divisible by 5")
            number += 1
    else:
        if number %5 == 0:
            print(number, "is odd, and divisible by 5")
            number += 1
        else:
            print(number, "is odd, and not divisible by 5")
            number += 1