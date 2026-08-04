from income_statement import calculate_totals,display_statement, tax_display
from data_collect import income_collect, expense_collect, taxes_collect


print("Welcome to the Income Statement Generator")
date =input("\nEnter Date:\n")
company_name = input("\nEnter your Company name:\n")
year = int(input("\nEnter the year (e.g., 2026):\n"))
income = income_collect()
expense = expense_collect()
taxes = taxes_collect()
total_income, total_expense, net_income,after_tax,net_tax = calculate_totals(income, expense,taxes)
display_statement(date,company_name, income, expense, total_income, total_expense, net_income, year)
tax_display(taxes, net_tax, after_tax)
