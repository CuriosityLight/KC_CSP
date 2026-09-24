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
people = ["king george the III", "george washington", "curious george", "george the pig", "george w bush", "other george bush"]
print(people[4])
