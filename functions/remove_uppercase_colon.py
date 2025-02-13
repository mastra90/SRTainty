import pysrt
import re

def remove_uppercase_colon(input_file, output_file):
    subs = pysrt.open(input_file)
    
    # Updated pattern to match uppercase words followed by a colon
    # It matches uppercase words, optionally followed by a space and/or a number
    pattern = re.compile(r'\b[A-Z]+\s*\d*:\s*')
    
    for sub in subs:
        sub.text = pattern.sub('', sub.text).strip()
    
    subs.save(output_file, encoding='utf-8')