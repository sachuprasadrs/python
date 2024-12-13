n = int(input("Enter the number of names: "))
names = [input("Enter name: ") for _ in range(n)]
count_a = sum(name.lower().count('a') for name in names)
print("Total occurrences of 'a':", count_a)
