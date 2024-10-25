n = int(input("Enter the number of words: "))

words = []
for i in range(n):
     word = input("Enter a word: ")
     words.append(word)

longest_word = words[0]

for word in words:
     if len(word) > len(longest_word):
         longest_word = word

print("The word with the longest length is:", longest_word)
