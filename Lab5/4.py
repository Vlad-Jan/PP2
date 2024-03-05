import re

def find_sequences(input_string):
    pattern = re.compile(r'[A-Z][a-z]+')
    matches = pattern.findall(input_string)

    if matches:
        print(f'Sequences found: {", ".join(matches)}')
    else:
        print('No sequences found.')

user_input = input("Enter a string: ")
find_sequences(user_input)
