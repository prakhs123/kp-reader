import os
import sys
import logging
import time

import openai
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('log_file_path', type=str, help='The path to the log file')
parser.add_argument('txt_file_path', type=str, help='The path to the text file')
parser.add_argument('md_file_path', type=str, help='The path to the Markdown file')

args = parser.parse_args()

log_file_path = args.log_file_path
txt_file_path = args.txt_file_path
md_file_path = args.md_file_path

logging.basicConfig(filename=log_file_path,
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

with open(txt_file_path, "r+") as f:
    text = f.read()

chunks = text.split('\n\n')


def join_chunks(string_list, X):
    i = 0
    while i < len(string_list) - 1:
        if len(string_list[i])/4 < X and len(string_list[i+1])/4 < X:
            string_list[i] = string_list[i] + '\n' + string_list[i+1]
            string_list.pop(i+1)
        else:
            i += 1
    return string_list


# new_chunks = join_chunks(chunks, 400)
for chunk in chunks:
    print(len(chunk)/4)
    if len(chunk)/4 > 1800:
        print('ALERT')
        print(chunk)
    print('-'*100)


def make_request(chunk):
    # Make request to API
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Correct this to standard English, fix OCR errors, correct numbering and "
               "output in markdown format"
               f"\n\nINPUT: \n\n {chunk}\n OUTPUT:\n",
        temperature=0,
        max_tokens=(int(len(chunk)/4) + 300) if (int(len(chunk)/4) < 1500) else 2096,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response


with open(md_file_path, "a") as fout:
    for chunk in chunks:
        max_retries = 5
        retry_delay = 2

        for i in range(max_retries):
            try:
                response = make_request(chunk)
                # Request succeeded, break out of loop
                break
            except Exception as e:
                if i == max_retries - 1:
                    # Last retry, raise exception
                    raise e
                else:
                    # Calculate delay for next retry
                    retry_delay *= 2
                    time.sleep(retry_delay)
        ans = response["choices"][0]
        if ans["finish_reason"] == "stop":
            logger.info("INPUT:\n %s", chunk)
            logger.info("OUTPUT:\n %s", ans['text'])
            fout.write(ans['text'])
        else:
            print(response)
            sys.exit(1)
        time.sleep(3)
