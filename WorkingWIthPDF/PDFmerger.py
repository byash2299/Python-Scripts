import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdfs):
    merger = PyPDF2.PdfFileMerger()
    for file in pdfs:
        merger.append(file)
    merger.write('output.pdf')
    merger.close()

pdf_combiner(inputs)