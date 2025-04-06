import pysrt
import re

def remove_italics_tags_and_text(input_file, output_file):
    subs = pysrt.open(input_file)
    italics_pattern = re.compile(r'<i>.*?</i>')
    for sub in subs:
        sub.text = italics_pattern.sub('', sub.text).strip()
    subs.save(output_file, encoding='utf-8')