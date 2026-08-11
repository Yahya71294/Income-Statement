# Data_collect.py
# To collect all the data related to income
def income_collect():
    income ={}
    income_category =["1. Sales Revenue","2. Service Revenue","3. Rental Income","4. Interest Income","5. Commission Income","6. Other Income"]

    while True:
        option = input("\nType 'i' to add an income or 'd' to Finish as an option:\n").lower()
        if option == "i":
            print("These are your choices for  Income Category:\n")
            for cat in income_category:
                print(cat)
            while True:
                cat_input = int(input("\nEnter your choice from (1 - 6):\n"))
                if cat_input == 1:
                    category = "Sales Revenue"
                    break
                elif cat_input == 2:
                    category = "Service Revenue"
                    break
                elif cat_input == 3:
                    category = "Rental Income"
                    break
                elif cat_input == 4:
                    category = "Interest Income"
                    break
                elif cat_input == 5:
                    category = "Commission Income"
                    break
                elif cat_input == 6:
                    other = input("Enter your other income category:\n")
                    category = other
                    break
                else:
                    print("Invalid option. Please enter number from '1 - 6'.")
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
            print("These are your choices for Expense Category:\n")
            for cat in expense_category:
                print(cat)
            while True:
                category_input = int(input("\nEnter your choice from (1 - 6):\n"))
                if category_input == 1:
                    category = "Rent"
                    break
                elif category_input == 2:
                    category = "Salaries"
                    break
                elif category_input == 3:
                    category = "Maintenance"
                    break
                elif category_input == 4:
                    category = "Loan Payment"
                    break
                elif category_input == 5:
                    category = "Utilities Expense"
                    break
                elif category_input == 6:
                    other = input("Enter your other expense category:\n")
                    category = other
                    break
                else:
                    print("Invalid option. Please enter number from '1 - 6'.")
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
            print("These are your tax category:\n")
            for cat in tax_category:
                print(cat)
            while True:
                tax_input = int(input("\nEnter your choice from (1 - 6):\n"))
                if tax_input == 1:
                    category = "Individual Income Tax"
                    break
                elif tax_input == 2:
                    category = "Corporate Tax"
                    break
                elif tax_input == 3:
                    category = "Capital Gain Tax"
                    break
                elif tax_input == 4:
                    category = "Import Duties"
                    break
                elif tax_input == 5:
                    category = "Sales Tax"
                    break
                elif tax_input == 6:
                    other= input("Enter your other tax category")
                    category = other
                    break
                else:
                    print("Invalid option. Please enter number from '1 - 6'.")
            rate = float(input("\nEnter Tax Rate (e.g., 10 for 10%):\n"))
            taxes[category] = rate  # always store as rate (%)
        elif option == "d":
            break
        else:
            print("Invalid Option. Please type 'tax' or 'done'.")
    return taxes



