from fpdf import FPDF
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("helvetica", "B", 16)
pdf.cell(60,10,"CS50 SHIRTIFICATE", align="C")
pdf.output("new-tuto2.pdf")