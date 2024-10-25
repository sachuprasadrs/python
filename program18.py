string = input("Enter a string: ")
first_char = string[0]
modified_string = first_char + string[1:].replace(first_char, '$')
print("Modified string:", modified_string)
