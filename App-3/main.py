from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')

pdf.add_page()
pdf.set_font('Times', 'B', 12)
pdf.cell(w=0, h=12, txt="Hello World", align='L', ln=1, border=1)

pdf.add_page()
pdf.set_font('Times', 'B', 12)
pdf.cell(w=0, h=12, txt="Hello World", align='L', ln=1, border=1)

pdf.output('output.pdf',)