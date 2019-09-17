from fpdf import FPDF

pdf=FPDF()
pdf.add_page()

# Font size
pdf.set_font("Arial",size=12)

# line 1, align center
pdf.cell(200,10,txt="hello",ln=1,align="C")

# line 2, align center
pdf.cell(200,10,txt="This is my data",ln=2,align="C")

#  path of file
pdf.output("C:\\Users\\Tayyab\\Desktop\\name.pdf")
