# Data_collect.py
# To collect all the data related to income
def income_collect():
    income ={}

    while True:
        option = input("Type 'Income' to add an income or 'Done' to Finish:\n").lower()
        if option == "income":
            category = input("Enter Income Category:\n").lower()
            amount = float(input("Enter an Amount\n"))
            income[category] = amount
        elif option == "done":
            break
        else:
            print("Invalid Option")
    return income
# To collect all the data related to expenses
def expense_collect():
    expense = {}
    while True:
        option = input("Type 'Expense' to add expenses or 'Done' to Finish:\n").lower()
        if option == "expense":
           category = input("Enter Expense Category:\n").lower()
           amount = float(input("Enter an Amount:\n"))
           expense[category] = amount
        elif option =="done":
            break
        else:
            print("Invalid Option")
    return expense
# To Collect all  the related to tax
def taxes_collect():
    taxes = {}
    while True:
        option = input("Type 'tax' to add a tax rate or 'done' to finish:\n").lower()
        if option == "tax":
            category = input("Enter Tax Category:\n")
            rate = float(input("Enter Tax Rate (e.g., 10 for 10%):\n"))
            taxes[category] = rate  # always store as rate (%)
        elif option == "done":
            break
        else:
            print("Invalid Option. Please type 'tax' or 'done'.")
    return taxes
