from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.image("debate_analysis.png", x=20, y=60)
pdf.output("pdf-with-image.pdf")