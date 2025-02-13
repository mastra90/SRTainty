import pysrt
import re

def remove_words_ending_with_colon(input_file, output_file):
    subs = pysrt.open(input_file)
    
    # Pattern to match any number of words followed by a colon at the start of the line
    pattern = re.compile(r'^\s*(?:\w+(?:\s+\w+)*)?:\s*', re.MULTILINE | re.IGNORECASE)
    
    for sub in subs:
        # Remove the matched words from the beginning of subtitle text
        sub.text = pattern.sub('', sub.text).strip()
    
    subs.save(output_file, encoding='utf-8')