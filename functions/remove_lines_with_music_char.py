import pysrt

def remove_lines_with_music_char(input_file, output_file, special_char='♪'):
    subs = pysrt.open(input_file)
    
    # Filter out subtitle entries containing the special character
    filtered_subs = [sub for sub in subs if special_char not in sub.text]
    
    # Save the cleaned subtitle file
    subs.clear()  # Clear the existing subs
    subs.extend(filtered_subs)  # Add only the filtered subs
    subs.save(output_file, encoding='utf-8')