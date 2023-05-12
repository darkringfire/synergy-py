import re

string = input("Enter a string: ")
new_string = re.sub(" +", " ", string)
print(f'"{new_string}"')
