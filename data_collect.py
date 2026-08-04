# Data_collect.py
# To collect all the data related to income
def income_collect():
    income ={}

    while True:
        option = input("Type 'I' to add an income or 'D' to Finish:\n").lower()
        if option == "i":
            category = input("Enter Income Category:\n").lower()
            amount = float(input("Enter an Amount\n"))
            income[category] = amount
        elif option == "d":
            break
        else:
            print("Invalid Option")
    return income
# To collect all the data related to expenses
def expense_collect():
    expense = {}
    while True:
        option = input("Type 'E' to add expenses or 'D' to Finish:\n").lower()
        if option == "e":
           category = input("Enter Expense Category:\n").lower()
           amount = float(input("Enter an Amount:\n"))
           expense[category] = amount
        elif option =="d":
            break
        else:
            print("Invalid Option")
    return expense
# To Collect all  the related to tax
def taxes_collect():
    taxes = {}
    while True:
        option = input("Type 't' to add a tax rate or 'd' to finish:\n").lower()
        if option == "t":
            category = input("Enter Tax Category:\n")
            rate = float(input("Enter Tax Rate (e.g., 10 for 10%):\n"))
            taxes[category] = rate  # always store as rate (%)
        elif option == "d":
            break
        else:
            print("Invalid Option.")
    return taxes
