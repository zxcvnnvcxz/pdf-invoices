from pathlib import Path
import pandas as pd
from fpdf import FPDF
import glob

filepaths = glob.glob("invoices/*")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    filename = Path(filepath).stem
    invoice_nr = filename.split("-")[0]

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_nr}")
    pdf.output(f"PDFs/{filename}.pdf")