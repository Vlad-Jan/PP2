def replace(input_string):
    replacement_chars = [' ', ',', '.']
    
    for char in replacement_chars:
        input_string = input_string.replace(char, ':')
    
    return input_string

user_input = input("Enter a string: ")
result = replace(user_input)
print(f"The modified string is: {result}")
