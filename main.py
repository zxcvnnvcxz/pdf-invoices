from pathlib import Path
import pandas as pd
from fpdf import FPDF
import glob

filepaths = glob.glob("invoices/*")

for filepath in filepaths:

    # Extract names
    filename = Path(filepath).stem
    invoice_nr, date = filename.split("-")

    # Create title and date
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_nr}", ln=1)
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date {date}", ln=1)

    # Import data file
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    columns = df.columns
    columns = [item.replace("_", ' ').title() for item in columns] # Important List Comprehension

    # Header
    pdf.set_font(family="Times", size=10, style="B")
    pdf.cell(w=30, h=8, txt=str(columns[0]), border=1)
    pdf.cell(w=70, h=8, txt=str(columns[1]), border=1)
    pdf.cell(w=30, h=8, txt=str(columns[2]), border=1)
    pdf.cell(w=30, h=8, txt=str(columns[3]), border=1)
    pdf.cell(w=30, h=8, txt=str(columns[4]), border=1, ln=1)

    # Cell Body
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=70, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)

    # Total Sum Cell
    total_sum = df["total_price"].sum()

    pdf.set_font(family="Times", size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=70, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)

    # Add total sum sentence
    pdf.set_font(family="Times", size=10)
    pdf.set_text_color(0,0,0)
    pdf.cell(w=30, h=11, txt=f"The total price is {total_sum}.", ln=1)

    # Add company name and logo
    pdf.set_font(family="Times", size=14, style="B")
    pdf.set_text_color(0,0,0)
    pdf.image("image.png", h=8)


    pdf.output(f"PDFs/{filename}.pdf")
