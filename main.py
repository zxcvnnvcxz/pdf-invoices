from pathlib import Path
import pandas as pd
from fpdf import FPDF
import glob

filepaths = glob.glob("invoices/*")

for filepath in filepaths:
    # Import data file
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    # Extract names
    filename = Path(filepath).stem
    invoice_nr, date = filename.split("-")

    # Create title and date
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_nr}", ln=1)
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date {date}")


    pdf.output(f"PDFs/{filename}.pdf")
