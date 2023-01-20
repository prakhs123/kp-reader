import argparse

from pypdf import PdfReader

parser = argparse.ArgumentParser()
parser.add_argument('first_page', type=int, help='The first page number')
parser.add_argument('last_page', type=int, help='The last page number')
args = parser.parse_args()

first_page = args.first_page
last_page = args.last_page


pdf_path = "../pdf/Krishnamurti-Padhdhati-Vol-3 - English.pdf"
pdf_reader = PdfReader(pdf_path)
# pdf_page = pdf_reader.pages[1]
pages = []
for i in range(first_page-1, last_page):
    pdf_page = pdf_reader.pages[i]
    for image_file_object in pdf_page.images:
        with open(str(i)+image_file_object.name, 'wb') as f:
            f.write(image_file_object.data)
