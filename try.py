from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 30)
pdf.cell(0, 0, "Your Analysis:", align="C")
pdf.image("debate_analysis.png", x=-75, y=60)
pdf.output("pdf-with-image.pdf")
