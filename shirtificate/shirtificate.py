from fpdf import FPDF
class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 15)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "CS50 SHIRTIFICATE", border=1, align="C")
        # Performing a line break:
        self.ln(20)
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
