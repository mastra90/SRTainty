from functions.remove_square_bracketed_text import remove_square_bracketed_text
from functions.remove_bracketed_text import remove_bracketed_text
from functions.remove_uppercase_colon import remove_uppercase_colon
from functions.remove_words_ending_with_colon import remove_words_ending_with_colon
from functions.delay_subtitles import delay_subtitles
from functions.spelling_corrections import spelling_corrections
from functions.remove_empty_entries import remove_empty_entries
from functions.renumber_subtitles import renumber_subtitles
from functions.remove_lines_with_music_char import remove_lines_with_music_char
from functions.syntax_corrections import syntax_corrections
from functions.double_dashes import double_dashes
from functions.check_special_chars import check_special_chars


def process_subtitles(input_file, output_file, actions, delay_ms=0):
    temp_file = 'temp.srt'
    current_file = input_file

    action_map = {
        'remove_square_bracketed_text': remove_square_bracketed_text,
        'remove_bracketed_text': remove_bracketed_text,
        'remove_uppercase_colon': remove_uppercase_colon,
        'remove_words_ending_with_colon': remove_words_ending_with_colon,
        'remove_lines_with_music_char': remove_lines_with_music_char,
        'delay_subtitles': lambda infile, outfile: delay_subtitles(infile, outfile, delay_ms),
        'remove_empty_entries': remove_empty_entries,
        'spelling_corrections': spelling_corrections,
        'syntax_corrections': syntax_corrections,
        'double_dashes': double_dashes,
        'check_special_chars': check_special_chars,
    }

    for action in actions:
        func = action_map.get(action)
        if func:
            func(current_file, temp_file)
            current_file = temp_file
        else:
            print(f"Unknown action: {action}")
    
    # Renumber subtitles after all other actions
    renumber_subtitles(current_file, output_file)

if __name__ == "__main__":
    input_file_name = 'test'

    extension = '.srt'
    output_file_name = f'{input_file_name}'
    input_file = f'srt_files/input/{input_file_name}{extension}'
    output_file = f'srt_files/output/{output_file_name}_processed{extension}'

    actions = [
        'remove_square_bracketed_text',
        'remove_bracketed_text',
        'remove_uppercase_colon',
        'remove_words_ending_with_colon',
        'remove_lines_with_music_char',
        'remove_empty_entries',
        'double_dashes',
        'spelling_corrections',
        'syntax_corrections',
        'check_special_chars',
        'delay_subtitles'
    ]

    delay_ms = 200 # Delay in milliseconds

    process_subtitles(input_file, output_file, actions, delay_ms)
    print('Your subtitles have been processed.')

    #testing git