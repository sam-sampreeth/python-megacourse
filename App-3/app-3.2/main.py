import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob('invoices/*.xlsx')

for filepath in filepaths:
    df = pd.read_excel(filepath, "Sheet 1")
    pdf = FPDF("p", "mm", "A4")
    pdf.add_page()
    invNum = Path(filepath).stem.split("-")[0]
    pdf.set_font("helvetica", size=17, style="B")
    pdf.cell(50, 8, f"Invoice #{invNum}")
    pdf.output(f"PDFs/{invNum}.pdf")
