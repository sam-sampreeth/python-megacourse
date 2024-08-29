from fpdf import FPDF
import glob
from pathlib import Path

pdf = FPDF("p", "mm", "A4")
files = glob.glob('txtFiles/*.txt')
for file in files:
    headName = Path(file).stem.title()
    pdf.add_page()
    pdf.set_font("helvetica", size=18, style="B")
    pdf.cell(50, 8, txt=headName, ln=1)
    with open(file, 'r') as f:
        content = f.read()
    pdf.set_font("helvetica", size=14)
    pdf.multi_cell(0, 6, txt=content)
pdf.output("Animals.pdf")