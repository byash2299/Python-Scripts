import PyPDF2

watermark = PyPDF2.PdfFileReader(open('wtr.pdf','rb'))
inputfile = PyPDF2.PdfFileReader(open('output.pdf','rb'))
output = PyPDF2.PdfFileWriter()

def add_watermark(file):
    for i in range(inputfile.getNumPages()):
        page = inputfile.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)
    with open('wtrfile.pdf','wb') as file:
        output.write(file)

add_watermark(inputfile)
