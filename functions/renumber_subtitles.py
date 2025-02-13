import pysrt

def renumber_subtitles(input_file, output_file):
    subs = pysrt.open(input_file)
    
    # Iterate through the subtitles and update the index
    for i, sub in enumerate(subs):
        sub.index = i + 1  # Renumber starting from 1
    
    # Save the renumbered subtitle file
    subs.save(output_file, encoding='utf-8')
