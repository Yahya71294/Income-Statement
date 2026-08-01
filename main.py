from income_statement import calculate_totals,display_statement
from data_collect import income_collect, expense_collect


print("Welcome to the Income Statement Generator")
company_name = input("\nEnter your Company name:\n")
year = int(input("\nEnter the year (e.g., 2026):\n"))
income = income_collect()
expense = expense_collect()
total_income, total_expense, net_income = calculate_totals(income, expense)
display_statement(company_name, income, expense, total_income, total_expense, net_income, year)
