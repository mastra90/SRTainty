import pysrt

def delay_subtitles(input_file, output_file, delay_ms):
    subs = pysrt.open(input_file)
    delay = pysrt.SubRipTime(milliseconds=delay_ms)
    
    for sub in subs:
        sub.start += delay
        sub.end += delay
    
    subs.save(output_file, encoding='utf-8')