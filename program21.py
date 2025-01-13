string = input("Enter a string: ")
count = 0
for char in string:
	if char != ' ':
		count += 1
print(f"The number of characters in the string (excluding spaces) is: {count}")
