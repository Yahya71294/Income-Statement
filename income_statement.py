


# To collect all the totaling
def calculate_totals(income,expense,taxes):
    total_income = sum(income.values())
    total_expense = sum(expense.values())
    net_income = total_income-total_expense
    # Calculate tax
    net_tax = 0
    for rate in taxes.values():
        net_tax =net_tax + net_income * (rate / 100)

    after_tax = net_income - net_tax

    return total_income,total_expense,net_income,net_tax,after_tax
# Display Income Statement
def display_statement(date,company_name,income,expense,total_income,total_expense,net_income,year):
    width = 60
    print(f"Date: {date}")
    print( company_name.center(width))
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
# DIsplay Tax Statement
def tax_display(taxes, net_tax, after_tax):
    print("Taxes:")
    print(f"{'Category':<20}:| {'Rate (%)':<10}")
    print("-"*33)
    for category, rate in taxes.items():
        print(f"{category:<20}:| {rate:>10.2f}")
    print("-"*33)
    print(f"{'Net Tax Amount':<20}:| {after_tax:>10.2f}")
    print("-"*33)
    print(f"{'Net Income After Tax':<20}:| {net_tax:>10.2f}")
    print("-"*34)
