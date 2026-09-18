# KC, strings

# string => any saved data inside of qutotaion marks "" '


name = input("what is your name? ") .strip() .title()

age = input("how old are you? ")
print(type(age))

# concatenation => puts two strings directly next to eachother
print(age+age)

print(name + " " + "#2")

sentence = "the quick brown fox jumped over the lazy dog"
print(sentence)
print(sentence.replace("dog", "monkey"))
print(len(name)) #<= gets the length of a string
print("your name is ", name, "that is ", len(name), "letters long. your first initial is", name[0] )
print(f"your name is {name} that is {len(name)} letter long. your first initial is {name[0]}, i think i will call you {name[0:3]}")

# f strings


