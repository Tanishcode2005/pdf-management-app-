from PyPDF2 import PdfWriter

merger = PdfWriter()
pdfs =[]
n = int(input("How maniy pdf to merge ?\n"))

for i in range (0,n):
    print(f"enter the name of the {i +1}:")
    name = input("")
    pdfs.append(name)
for pdf in pdfs:
    merger.append(pdf)
merger.write("merged-pdf.pdf")
merger.close()
