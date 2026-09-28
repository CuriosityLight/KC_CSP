# KC, nesting notes



#number = 0

#while number <= 20:
#    print(number)
#    number += 2

#for count in range(2, 21, 2):
#    print(count)


for number in range(1, 21):
    if number %15 == 0:
        print("fizzbuzz")
    elif number %3 == 0:
        print("fizz")
    elif number %5 == 0:
        print("buzz")
    else:
        print(number)


georges = ["george washington", "king george the III", "curious george", "george bush", "other george bush", "george the pig", "gorg", "georgy"]
count = 1
if len(georges) > 0:
    while count <= len(georges):
        print(f"{count}. {georges[count-1]}")
        count += 1
else:
    print("there are no georges")


