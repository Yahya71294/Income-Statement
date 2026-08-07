from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def save_statement(filename, company_name, year, date,
                   income_dict, expense_dict, taxes_dict,
                   total_income, total_expense, net_income, net_tax, after_tax):
    c = canvas.Canvas(filename, pagesize=letter)
    c.setFont("Helvetica", 12)

    # Title
    c.drawString(100, 750, f"{company_name} - Income Statement {year} ({date})")

    # Income
    c.drawString(100, 720, "Income:")
    y = 700
    for category, amount in income_dict.items():
        c.drawString(100, y, f"{category:<20}: {amount:>10.2f}")
        y -= 20
    c.drawString(100, y, f"{'Total Income':<20}: {total_income:>10.2f}")
    y -= 40

    # Expense
    c.drawString(100, y, "Expense:")
    y -= 20
    for category, amount in expense_dict.items():
        c.drawString(100, y, f"{category:<20}: {amount:>10.2f}")
        y -= 20
    c.drawString(100, y, f"{'Total Expense':<20}: {total_expense:>10.2f}")
    y -= 40
    # Net Income
    c.drawString(100, y, f"{'Net Income':<20}: {net_income:>10.2f}")
    y -= 20

    # Taxes
    c.drawString(100, y, "Taxes:")
    y -= 20
    for category, amount in taxes_dict.items():
        c.drawString(100, y, f"{category:<20}: {amount:>10.2f}")
        y -= 20
    c.drawString(100, y, f"{'Net Tax Amount':<20}: {net_tax:>10.2f}")
    y -= 40

    c.drawString(100, y, f"{'Net Income After Tax':<20}: {after_tax:>10.2f}")

    c.save()
