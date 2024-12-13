n = int(input("Enter the number of integers: "))
numbers = []
for _ in range(n):
    num = int(input("Enter an integer: "))
    if num > 100:
        numbers.append('over')
    else:
        numbers.append(num)
print("Filtered list:", numbers)
