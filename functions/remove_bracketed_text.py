import pysrt
import re

def remove_bracketed_text(input_file, output_file):
    subs = pysrt.open(input_file)
    bracket_pattern = re.compile(r'\(.*?\)')
    for sub in subs:
        sub.text = bracket_pattern.sub('', sub.text).strip()
    subs.save(output_file, encoding='utf-8')