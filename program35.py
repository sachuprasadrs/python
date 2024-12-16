text = input("Enter a line of text: ")
words = text.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Occurrences of each word:")
for word, count in word_count.items():
    print(word, ":", count)
