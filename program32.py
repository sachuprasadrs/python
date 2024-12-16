word = input("Enter a word: ")
vowels = ['a', 'e', 'i', 'o', 'u']
vowels_in_word = []
for char in word.lower():
    if char in vowels:
        vowels_in_word.append(char)
print("Vowels in the word:", vowels_in_word)
