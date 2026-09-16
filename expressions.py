# KC 7th, intege, floats, and expressions notes


######## integer => a whole number
students = 23
cars = 50
computers = 29
awareness = -12

###### float 

pi = 3.14159
temp = -95.6
cost = 1.99
rain = 2.17


#### arithemtic operators
# + addition
# - subtraction
# * multiplication
# / divide
# % mod
# // interger division
# ** exponetd

print("18/4 is", 18/4, "or", 18//4, "the remainer of 18%4 is", 18%4)
print("18/5 is", 18/5, "or", 18//5, "the remainer of 18%5 is", 18%5)

# order of operation

grades = [85, 94, 94, 72, 932998322987643298743298743287043287432870]
students = len(grades)
average = sum(grades)/students

print("the average is ", int(average))


# convert the data types
price = input("how much did the item cost")
tax = 0.0485
sales_tax = price * tax
total = price + sales_tax
print(total)