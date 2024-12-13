n = int(input("Enter the number of names: "))
names = []
for _ in range(n):
    name = input("Enter name: ")
    names.append(name)
count_a = 0
for name in names:
    count_a += name.lower().count('a')
print("Total occurrences of 'a':", count_a)
