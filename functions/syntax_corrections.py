import pysrt

syntax_corrections_dict = {
    '  ':' ',
    ' .':'.',
    '...':'…',
    '....':'…',
    '. . .':'…',
    '. . . .':'…',
    '–': '-',
    ' ?': '?',
    ' !': '!',
    '«': '',
    '»': '',
    '<b>': '',
    '</b>': '',
    '<i>': '',
    '</i>': '',
}

def syntax_corrections(input_file, output_file):
    subs = pysrt.open(input_file)
    
    for sub in subs:
        for incorrect, correct in syntax_corrections_dict.items():
            # Use word boundaries to ensure we're replacing whole words
            sub.text = sub.text.replace(f" {incorrect} ", f" {correct} ")
            # Check for word at the beginning of the line
            sub.text = sub.text.replace(f"{incorrect} ", f"{correct} ")
            # Check for word at the end of the line
            sub.text = sub.text.replace(f" {incorrect}", f" {correct}")
            # Check for word on its own line
            sub.text = sub.text.replace(f"{incorrect}", f"{correct}")
    
    subs.save(output_file, encoding='utf-8')