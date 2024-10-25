string = input("Enter a string: ")

start = string[0]
end = string[-1]

new_string = end + string[1:-1] + start

print("String with first and last characters exchanged:", new_string)
