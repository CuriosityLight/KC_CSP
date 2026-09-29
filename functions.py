# KC, functiond notes


def stupid_proof(money):
    while True:
        try:
            amount = float(input(f"what is your monthly {money}"))
            return amount
        except:
            print("NUMBER PlESASEESESSESESESESES")

    
# write all your variables
income = stupid_proof("income")
rent = stupid_proof("rent")
utilit = stupid_proof("utilites")
groceries = stupid_proof("groceries")
transportation = stupid_proof("transportation")
savings = income * 0.1


# write any functions you are using
def calc_percent(income, bill):
    return round(bill/income *100)


# outputs for the user
print(f"your rent is ${rent:.2f} that is {calc_percent(income, rent)}% of your income")
print(f"your utilites is ${utilit:.2f} that is {calc_percent(income, utilit)}% of your income")
print(f"your groceries is ${groceries:.2f} that is {calc_percent(income, groceries)}% of your income")
print(f"your transportation is ${transportation:.2f} that is {calc_percent(income, transportation)}% of your income")
print(f"you should save ${savings:.2f} that is {calc_percent(income, savings)}% of your income")

print(f"you have ${income - rent - utilit - groceries - transportation - savings:.2f} left to spend")


