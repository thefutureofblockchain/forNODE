from fpdf import FPDF
pdf = FPDF()
def pdf_ize(format= "a", description="b"):
    pdf.add_page()
    pdf.set_font("helvetica", "B", 30)
    pdf.cell(0, 0, "Your Analysis:", align="C")
    pdf.image("debate_analysis.png", x=-75, y=60)
    c = "hello world"
    pdf.set_font("helvetica", "B", 16)
    pdf.cell(99,50, "")
    pdf.image("bp.png", x=-60, y=50)
    pdf.set_font("helvetica", "B", 30)
    pdf.cell(-375,550,format,align="C")
    pdf.output("pdf-with-image.pdf")
pdf_ize(format = "British Parliamentary")
