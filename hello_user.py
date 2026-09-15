#  KC,  hello user

while True:
    user = input("Whats your name? ") .strip() .title()
    if user.isnumeric():
        print("I'm pretty sure numbers arent in names.")
    else:
        break
print("Hello,", user)