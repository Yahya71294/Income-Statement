


# To collect all the totaling
def calculate_totals(income,expense):
    total_income = sum(income.values())
    total_expense = sum(expense.values())
    net_income = total_income-total_expense
    return total_income,total_expense,net_income
# Display Income Statement
def display_statement(company_name,income,expense,total_income,total_expense,net_income,year):
    width = 60
    print("\n" + company_name.center(width))
    print((f"Yearly Income Statement for Year Ended {year}").center(width))
    print("Income:")
    print(f"{'category':<20}:| {'amount':<10}")
    print("-"*33)
    for category, amount in income.items():
        print(f"{category:<20}:| {amount:>10.2f}   ")
    print("-"*33)
    print(f"{'Total Income':<20}:|{total_income:>10.2f}")
    print("-"*33)
    print("Expense:")
    print(f"{'category':<20}:| {'amount':<10}")
    print("-"*33)
    for category,amount in expense.items():
        print(f"{category:<20}:| {amount:>10.2f}   ")
    print("-"*33)
    print(f"{'Total Expense':<20}:|{total_expense:>10.2f}")
    print("-"*33)
    print(f"{'Net Income':<20}:|{net_income:10.2f}")
    print("-"*33)

