from data_collect import income_collect, expense_collect, taxes_collect
from income_statement import calculate_totals, display_statement, tax_display
from pdf import save_statement

# Collect basic info
company_name = input("Enter your Company name:\n")
year = input("Enter the year:\n")
date = input("Enter the date (e.g., 07-Aug-2026):\n")

# Collect data
income = income_collect()          # dictionary
expense = expense_collect()        # dictionary
taxes = taxes_collect()            # dictionary

# Calculate totals
total_income, total_expense, net_income, net_tax, after_tax = calculate_totals(income, expense, taxes)

# Show on console
display_statement(date ,company_name,income,expense,total_income,total_expense,net_income,year)
tax_display(taxes,net_tax, after_tax)

# Ask user if they want a PDF
choice = input("Do you want to save this statement as PDF? (yes/no): ").lower()
if choice == "yes":
    filename = f"{company_name}_{year}_{date}_statement.pdf"
    save_statement(filename, company_name, year, date,
                   income, expense, taxes,
                   total_income, total_expense, net_income, net_tax, after_tax)
    print(f"PDF saved as {filename}")
