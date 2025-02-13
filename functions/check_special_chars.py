def check_special_chars(input_file, output_file):
    special_chars = ['[', ']', '{', '}', '(', ')', '/', '|', '#', '^', '*', '_', '<']
    found_chars = set()
    
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
            for char in special_chars:
                if char in content:
                    found_chars.add(char)
            
            if found_chars:
                chars_string = ", ".join(sorted(found_chars))
                print(f"Unwanted characters found: {chars_string}")
                
    except Exception as e:
        print(f"Error processing file: {str(e)}")