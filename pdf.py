from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def save_statement(filename, company_name, year, date,
                   income_dict, expense_dict, taxes_dict,
                   total_income, total_expense, net_income, net_tax, after_tax):

    c = canvas.Canvas(filename, pagesize=letter)
    c.setFont("Courier", 12)  # Courier keeps spacing consistent like console

    y = 750  # start position

    # Header
    c.drawString(100, y, f"Date: {date}")
    y -= 20
    c.drawString(100, y, f"{company_name}")
    y -= 20
    c.drawString(100, y, f"Yearly Income Statement for Year Ended {year}")
    y -= 30

    # Income Section
    c.drawString(100, y, "Income:")
    y -= 20
    c.drawString(100, y, "category            :| amount")
    y -= 20
    c.drawString(100, y, "---------------------------------")
    y -= 20
    for category, amount in income_dict.items():
        c.drawString(100, y, f"{category:<20}:| {amount:>10.2f}")
        y -= 20
    c.drawString(100, y, "---------------------------------")
    y -= 20
    c.drawString(100, y, f"Total Income        :| {total_income:>10.2f}")
    y -= 20
    c.drawString(100, y, "---------------------------------")
    y -= 30

    # Expense Section
    c.drawString(100, y, "Expense:")
    y -= 20
    c.drawString(100, y, "category            :| amount")
    y -= 20
    c.drawString(100, y, "---------------------------------")
    y -= 20
    for category, amount in expense_dict.items():
        c.drawString(100, y, f"{category:<20}:| {amount:>10.2f}")
        y -= 20
    c.drawString(100, y, "---------------------------------")
    y -= 20
    c.drawString(100, y, f"Total Expense       :| {total_expense:>10.2f}")
    y -= 20
    c.drawString(100, y, "---------------------------------")
    y -= 30

    # Net Income
    c.drawString(100, y, f"Net Income          :| {net_income:>10.2f}")
    y -= 20
    c.drawString(100, y, "---------------------------------")
    y -= 30

    # Taxes Section
    c.drawString(100, y, "Taxes:")
    y -= 20
    c.drawString(100, y, "Category            :| Rate (%)")
    y -= 20
    c.drawString(100, y, "---------------------------------")
    y -= 20
    for category, rate in taxes_dict.items():
        c.drawString(100, y, f"{category:<20}:| {rate:>10.2f}")
        y -= 20
    c.drawString(100, y, "---------------------------------")
    y -= 20
    c.drawString(100, y, f"Net Tax Amount      :| {net_tax:>10.2f}")
    y -= 20
    c.drawString(100, y, "---------------------------------")
    y -= 20
    c.drawString(100, y, f"Net Income After Tax:| {after_tax:>10.2f}")
    y -= 20
    c.drawString(100, y, "----------------------------------")

    c.save()
