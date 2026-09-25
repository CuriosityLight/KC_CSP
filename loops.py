# KC, 7th, loops notes
import random
# start pont
count = 1

#      v v v v v v stop point, it is boolean
while count <= 10:
    print(count)
    count += 1 # <-=-=-=--=-=-=- increase the iterater


ducks = 1
goose = random.randint(1, 10000)

while True:
    if ducks == goose:
        break
    print("duck")
    ducks += 1
print("goose")

# complex data = holds other data in it
georges = ["king george the III", "george washington", "curious george", "george the pig", "george w bush", "other george bush"]
print(georges[4])
georges.append("gregory") #< adds the item to the end of the list
name = input("george")
georges.append(name)
georges.insert(3, "i dont know anymore george")
print(georges)
#remove from a list
georges.pop(3) # <---- if no number given pop removes the last item
print(georges)

# print each item in a list
for george in georges:
    print(george)

# for loops
for num in range(1, 26):
    if num %15 == 0:
        print("fizzBuzz")
    elif num %3 == 0:
        print("fizz")
    elif num %5 == 0:
        print("buzz")
    else:
        print(num)