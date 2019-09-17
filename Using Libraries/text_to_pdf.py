from fpdf import FPDF

pdf=FPDF()
pdf.add_page()
pdf.set_font("Arial",size=12)
pdf.cell(200,10,txt="hello",ln=1,align="C")
pdf.cell(200,10,txt="hello",ln=2,align="C")

#  path of file
pdf.output("C:\\Users\\Tayyab\\Desktop\\I.T E-Books\\iot.pdf")