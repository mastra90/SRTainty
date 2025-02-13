import pysrt

def remove_empty_entries(input_file, output_file):
    subs = pysrt.open(input_file)
    
    # Filter out subtitle entries where text is empty
    non_empty_subs = [sub for sub in subs if sub.text.strip()]
    
    # Save the cleaned subtitle file
    subs.clear()  # Clear the existing subs
    subs.extend(non_empty_subs)  # Add only non-empty subs
    subs.save(output_file, encoding='utf-8')
