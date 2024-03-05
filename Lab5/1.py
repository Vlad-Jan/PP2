import re

def match(input_string):
    pattern = re.compile(r'ab*')
    match = pattern.fullmatch(input_string)
    
    if match:
        print(f'The string "{input_string}" matches the pattern.')
    else:
        print(f'The string "{input_string}" does not match the pattern.')

user_input = input("Enter a string: ")
match(user_input)
