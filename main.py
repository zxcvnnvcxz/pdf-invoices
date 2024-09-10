import pandas as pd
import fpdf
import glob

filepaths = glob.glob("invoices/*")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    print(df)

