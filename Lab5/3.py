import re

def seq(input_string):
    pattern = re.compile(r'[a-z]+_[a-z]+')
    matches = pattern.findall(input_string)

    if matches:
        print(f'Sequences found: {", ".join(matches)}')
    else:
        print('No sequences found.')

user_input = input("Enter a string: ")
seq(user_input)
