d1 = {}
d2 = {}
n = int(input("Enter number of elements in dict 1:\n"))
for i in range(n):
	key = int(input("Enter the key:"))
	value = input("Enter the value:")
	d1[key] = value
m = int(input("Enter number of elements in dict 2:\n"))
for i in range(m):
	key = int(input("Enter the key:"))
	value = input("Enter the value:")
	d2[key] = value
d1.update(d2)

print("Dictionary after merge:")
print(d1)

