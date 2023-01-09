from fpdf import FPDF
name = input(": ")
name = f"{name} took CS50"
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("helvetica", "B", 16)
pdf.cell(0, 0, 'CS50 SHIRTIFICATE', align='C')
pdf.image("shirtificate.png", x=0, y = 50)
pdf.set_text_color(0)
pdf.cell(-23,112,name,align="C")
pdf.output("new-tuto2.pdf")
