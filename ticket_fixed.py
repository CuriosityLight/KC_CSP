# KC, vibe debugging


while True:
    try:
        age = int(input("Enter your age: ").strip())
        if age < 0:
            print("Invalid age")
        elif age == 0:
            print("Invalid age")
        else:
            break
    except:
        print("Invalid age")
while True:
    try:
        matinee = str(input("Is this a matinee? (yes/no): ")).lower().strip()
        if matinee == "yes":
            break
        elif matinee == "no":
            break
        else:
            BrokenPipeError
    except:
        print("Yes or No")

if age < 5:
    price = 0
elif age < 12:
    price = 8
elif age < 65:
    price = 12
else:
    price = 9

if matinee == "yes":
    if price != 0:
        price -= 3

print(f"Ticket price: ${price}.00")