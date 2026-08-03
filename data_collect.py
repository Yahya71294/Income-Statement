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
def taxes_collect():
    taxes = {}
    while True:
        option = input("Type 'Taxes' to add taxes and 'done' to be finished:\n").lower()
        if option == "taxes":
            category = input("Enter Taxes Category:\n").lower()
            rate = float(input("Enter an Rate(in decimals e.g:10:\n"))
            taxes[category] = rate
        elif option == "done":
         break
        else:
         print("Invalid Option")
    return taxes
