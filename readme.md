# Subtitle Processing Application

A Python application for cleaning and processing .srt subtitle files. This tool provides various functions to improve subtitle readability and timing, making it easier to prepare subtitles for viewing.

## Features

The application includes the following processing options:

- **Remove Square Bracketed Text**: Eliminates text within square brackets (e.g., [applause])
- **Remove Bracketed Text**: Removes text within regular brackets
- **Remove Uppercase Colon**: Cleans up speaker labels in uppercase followed by colons
- **Remove Words Ending with Colon**: Removes speaker labels or descriptive text ending with colons
- **Remove Lines with Music Characters**: Eliminates lines containing music notation
- **Delay Subtitles**: Adjusts subtitle timing (delay in milliseconds)
- **Remove Empty Entries**: Cleans up blank subtitle entries
- **Spelling Corrections**: Applies common spelling fixes
- **Syntax Corrections**: Fixes common syntax issues
- **Double Dashes**: Standardizes dialogue dashes
- **Check Special Characters**: Validates and processes special characters
- **Automatic Renumbering**: Ensures correct subtitle sequence numbering

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install pysrt
```

## Directory Structure

```
your-app-directory/
├── app.py
├── functions/
│   ├── remove_square_bracketed_text.py
│   ├── remove_bracketed_text.py
│   └── ... (other function files)
├── srt_files/
│   ├── input/
│   └── output/
```

## Usage

1. Place your .srt file in the `srt_files/input/` directory
2. Open `app.py` and modify the following variables as needed:
   - `input_file_name`: Name of your input subtitle file (without extension)
   - `actions`: List of processing functions to apply
   - `delay_ms`: Delay time in milliseconds (if using delay_subtitles)

3. Run the application:
```bash
python app.py
```

4. Find your processed subtitle file in `srt_files/output/` with "_processed" appended to the filename

## Customizing Processing

You can customize which processing functions are applied by modifying the `actions` list in `app.py`. For example:

```python
actions = [
    'remove_square_bracketed_text',
    'remove_bracketed_text',
    'delay_subtitles'
]
```

## Available Processing Functions

| Function Name | Description |
|--------------|-------------|
| `remove_square_bracketed_text` | Removes text within square brackets like [applause] or [laughter] |
| `remove_bracketed_text` | Removes text within regular brackets (text) |
| `remove_uppercase_colon` | Removes speaker names in uppercase followed by colons |
| `remove_words_ending_with_colon` | Removes any word or phrase that ends with a colon |
| `remove_lines_with_music_char` | Removes lines containing music notation |
| `delay_subtitles` | Adds a specified delay to all subtitle timings |
| `remove_empty_entries` | Removes subtitle entries that contain no text |
| `spelling_corrections` | Applies common spelling corrections |
| `syntax_corrections` | Fixes common syntax issues |
| `double_dashes` | Standardizes dialogue dashes |
| `check_special_chars` | Validates and processes special characters |

## Example

Input subtitle:
```
1
00:00:01,000 --> 00:00:04,000
[Background music]
JOHN: Hey, what's up?

2
00:00:04,500 --> 00:00:06,500
MARY: Not much--how are you?
```

After processing with appropriate functions:
```
1
00:00:01,800 --> 00:00:04,800
Hey, what's up?

2
00:00:05,300 --> 00:00:07,300
Not much — how are you?
```

## Notes

- The application processes files sequentially, applying each selected function in order
- All processed files are automatically renumbered to ensure correct sequence
- Original files remain unchanged in the input directory
- Processed files are saved with "_processed" suffix in the output directory

## Error Handling

If a processing function isn't found, the application will print "Unknown action: [action_name]" and continue with the remaining functions.

## Post-Processing and Quality Control

### Working with MKV Files

- To extract subtitles from MKV files: Use **Shutter Encoder** to extract the existing subtitles
- To add processed subtitles to MKV files: Use **MKVToolNix** to merge the processed subtitles with your video

### Quality Control Checks

After processing, it's recommended to perform these additional checks using the serach function (Ctrl + F) in VS Code to catch any remaining issues. Use these regular expressions with the following search options enabled:
- "Match case"
- "Use regular expression"

1. Find uppercase words (2 or more letters):
```regex
\b[A-Z]{2,}\b
```

2. Find words ending with colon (any case, 2 or more letters):
```regex
\b[A-Za-z]{2,}:
```

3. Find standalone hyphens with no following content:
```regex
(?<=^\s*)-\s*$
```

These patterns will help you identify:
- Remaining speaker labels in uppercase
- Unconverted character names or descriptive text
- Improper line endings or dialogue marks