import pdf2image
import pytesseract
from pytesseract import Output
import argparse
import re

pdf_path = "../pdf/Krishnamurti-Padhdhati-Vol-3 - English.pdf"

parser = argparse.ArgumentParser()
parser.add_argument('first_page', type=int, help='The first page number')
parser.add_argument('last_page', type=int, help='The last page number')
parser.add_argument('destination_txt_path', type=str, help='The path to the destination text file')

args = parser.parse_args()

first_page = args.first_page
last_page = args.last_page
destination_txt_path = args.destination_txt_path

images = pdf2image.convert_from_path(pdf_path, first_page=first_page, last_page=last_page)


def split_list_by_pattern(string_list, pattern):
    split_list = []
    current_group = []
    for i in range(len(string_list)):
        if i + len(pattern) <= len(string_list) and string_list[i:i+len(pattern)] == pattern:
            split_list.append(current_group)
            current_group = []
        else:
            current_group.append(string_list[i])
    split_list.append(current_group)
    return split_list


def consolidate_page(list_of_lines):
    final_lines = []
    for line in list_of_lines:
        raw_line = ' '.join(line)
        final_lines.append(raw_line)
    return '\n'.join(final_lines)


def remove_first_two_empty_strings(alist):
    return alist[2:]


def add_newline_where_necessary(alist):
    for j in range(len(alist)):
        if alist[j] == '' and j != len(alist)-1 and alist[j+1] and alist[j+1][0].isupper():
            alist[j] = '\n'
    return alist


def run():
    pages = []
    for image in images:
        ocr_dict = pytesseract.image_to_data(image, lang='eng', output_type=Output.DICT)
        # ocr_dict now holds all the OCR info including text and location on the image
        texts = [c.strip() for c in ocr_dict['text']]
        # strip texts after line
        found_index = -1
        for index, s in enumerate(texts):
            if s and re.match(r'[a-z.,0-9]', s[-1]):
                if len(texts) > index + 3 and texts[index+1:index+4] == ['', '', '']:
                    found_index = index
        filtered_texts = texts
        if found_index != -1 and found_index > 20:
            filtered_texts = texts[:found_index+1]
        pattern = ['', '', '']
        chunks = split_list_by_pattern(texts, pattern)
        final_chunks = []
        # print(chunks)
        for chunk in chunks:
            filtered_chunk = remove_first_two_empty_strings(chunk)
            filtered_chunk_2 = add_newline_where_necessary(filtered_chunk)
            filtered_chunk_3 = [c for c in filtered_chunk_2 if c != '']
            if filtered_chunk_3 and not filtered_chunk_3[0].isnumeric():
                final_chunks.append(filtered_chunk_3)
        # print(final_chunks)
        if final_chunks[-1] and final_chunks[-1][-1].isnumeric():
            final_chunks = final_chunks[:-1]
        pages.append(final_chunks)

    final_chunks_across_pages = []
    current_text = ''
    for i, page in enumerate(pages):
        if i != 0 and page[0][0][0].isupper():
            final_chunks_across_pages.append(current_text)
            current_text = ''
        raw_page_text = consolidate_page(page)
        current_text += '\n' + raw_page_text

    if current_text:
        final_chunks_across_pages.append(current_text)
    for chunk in final_chunks_across_pages:
        with open(destination_txt_path, "a") as f:
            f.write(chunk)


if __name__ == '__main__':
    run()