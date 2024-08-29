import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob('invoices/*.xlsx')

for filepath in filepaths:
    pdf = FPDF("p", "mm", "A4")
    pdf.add_page()
    invNum, invDate = Path(filepath).stem.split("-")

    pdf.set_font("helvetica", size=17, style="B")
    pdf.cell(50, 8, f"Invoice #{invNum}", ln=1)

    pdf.set_font("helvetica", size=16, style="B")
    pdf.cell(50, 8, f"Date: {invDate}", ln=1)

    df = pd.read_excel(filepath, "Sheet 1")
    columns = list(df.columns)
    columns = [item.replace("_", " ").title() for item in columns]

    pdf.set_font("helvetica", size=10, style="B")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(30, 8, columns[0], border=1)
    pdf.cell(70, 8, columns[1], border=1)
    pdf.cell(35, 8, columns[2], border=1)
    pdf.cell(30, 8, columns[3], border=1)
    pdf.cell(30, 8, columns[4], border=1, ln=1)

    for index, row in df.iterrows():
        pdf.set_font("helvetica", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(30, 8, str(row["product_id"]), border=1)
        pdf.cell(70, 8, str(row["product_name"]), border=1)
        pdf.cell(35, 8, str(row["amount_purchased"]), border=1)
        pdf.cell(30, 8, str(row["price_per_unit"]), border=1)
        pdf.cell(30, 8, str(row["total_price"]), border=1, ln=1)

    pdf.output(f"PDFs/{invNum}.pdf")
