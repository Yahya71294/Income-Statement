# Data_collect.py
# To collect all the data related to income
def income_collect():
    income ={}
    income_category =["1. Sales Revenue","2. Service Revenue","3. Rental Income","4. Interest Income","5. Commission Income","6. Other Income"]

    while True:
        option = input("\nType 'i' to add an income or 'd' to Finish as an option:\n").lower()
        if option == "i":
            print("Select an Income Category:\n")
            for cat in income_category:
                print(cat)
            while True:
                income_input = input("\nEnter Income Category:\n")
                if income_input.replace(" ","").isalpha():
                    category = income_input
                    break
                elif income_input != income_input.isalpha():
                    print("Invalid Option")
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
    expense_category =['1. Rent','2. Salaries','3. Maintenance','4. Loan Payment','5. Utilities Expense','6. Other Expense']
    while True:
        option = input("\nType 'e' to add expenses or 'd' to Finish as an option:\n").lower()
        if option == "e":
            print("Select an Expense Category:\n")
            for cat in expense_category:
                print(cat)
            while True:

                category_input = input("\nEnter Expense Category:\n").lower()
                if category_input.replace(" ","").isalpha():
                    category = category_input
                    break

                elif category_input != category_input.isalpha():
                     print("Invalid Option")

            amount = float(input("\nEnter an Amount:\n"))
            expense[category] = amount
        elif option =="d":
            break
        else:
            print("Invalid Option")
    return expense
# Tax calculator
def taxes_collect():
    taxes = {}
    tax_category =['1. Individual Income Tax','2. Corporate Tax','3. Capital Gain Tax','4. Import Duties','5. Sales Tax','6. Other Tax']
    while True:
        option = input("\nType 't' to add a tax rate or 'd' to finish:\n").lower()
        if option == "t":
            print("Select a Tax Category:\n")
            for cat in tax_category:
                print(cat)
            category = input("\nEnter Tax Category:\n")
            rate = float(input("\nEnter Tax Rate (e.g., 10 for 10%):\n"))
            taxes[category] = rate  # always store as rate (%)
        elif option == "d":
            break
        else:
            print("Invalid Option. Please type 'tax' or 'done'.")
    return taxes



