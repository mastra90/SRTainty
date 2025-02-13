import re
import pysrt

def double_dashes(input_file, output_file):
    subs = pysrt.open(input_file)
    pattern = re.compile(r'(?<!-)--((?!>))')
    
    for sub in subs:
        sub.text = pattern.sub('-', sub.text)
    
    subs.save(output_file, encoding='utf-8')