import re
text =  str(input("Enter a string:"))
print(re.findall('[A-Z][^A-Z]*', text))
