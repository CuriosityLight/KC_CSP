# KC 7th, your budget.
while True:
    try:
        income = float(input("what is your monthly income? "))
        break
    except:
        print("type a dang number")
    
while True:
    try:
        rent = float(input("what is your monthly rent/mortgage price? "))
        break
    except:
        print("please just type a number")
    
while True:
    try:
        utilities = float(input("what is your monthy utilities price? "))
        break
    except:
        print("number please")

while True:
    try:
        groceries = float(input("what is your monthly price of grocceries? "))
        break
    except:
        print("number?")

while True:
    try:
        transportation = float(input("what yur monlthy price on transportation? "))
        break
    except:
        print("number...")




rent_percent = (rent/income) * 100
util_percent = (utilities/income) * 100
groc_percent = (groceries/income) * 100
transp_precent = (transportation/income) * 100

print(f"your rent is $ {rent} and that is {rent_percent:.2f} % of your income")
print(f"your utilities is $ {utilities} and that is {util_percent:.2f}% of your income")
print(f"your groceries is $ {groceries} and that is {groc_percent:.2f}% of your income")
print(f"your transportation is ${transportation} and that is, {transp_precent:.2f}% of your income")

total = income - (rent + utilities + groceries + transportation)
print("you hvae $", total, "left to spend on anything each month. ")