word = input("Enter a word: ")
ordinal_values = []
for char in word:
    ordinal_values.append(ord(char))
print("Ordinal values of each element in the word:", ordinal_values)
