import os
import sys
import logging
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

for chunk in chunks:
    print(len(chunk)/4)
    # if len(chunk)/4 > 1000:
        # print(chunk)
    print('-'*100)

with open(md_file_path, "a") as fout:
    for chunk in chunks:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Correct this to standard English with the heading if present:\n"+chunk,
            temperature=0,
            max_tokens=2000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        ans = response["choices"][0]
        logger.info(chunk)
        if ans["finish_reason"] == "stop":
            logger.info(ans['text'])
            fout.write(ans['text'])
        else:
            sys.exit(1)
