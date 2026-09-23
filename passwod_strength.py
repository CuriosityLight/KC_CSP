# KC, password strength checker

length = False
upper = False
lower = False
number = False
symbol = False
strength = 5

password = input("what is your password")

password

if len(password) >= 8:
    length = True

for letter in password:
    if letter.isupper():
        upper = True
    if letter.islower():
        lower = True
    if letter.isnumeric():
        number = True
    if letter in "~!@#$%^&*()_+`-=|[];':<>?,./":
        symbol = True
print("at least 8 letters:" + length)
print("has an uppercase letter:" + upper)
print("has a lowercase letter:" + lower)
print("has a number:" + number)
print("has a symbol:" + symbol)


if length == False:
    print("you need to make your password longer")
    strength -= 1
if upper == False:
    print("you need at least 1 uppercase letter")
    strength -= 1
if lower == False:
    print("you need at least 1 lowercase letter")
    strength -= 1
if number == False:
    print("you need at least 1 number")
    strength -= 1
if symbol == False:
    print("you need at least 1 symbol")
    strength -= 1

if strength == 1:
    print("your password is weak")
if strength == 2:
    print("your password is weak")
if strength == 3:
    print("your password is medium")
if strength == 4:
    print("your password is medium")
if strength == 5:
    print("your password is strong")