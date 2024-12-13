
numbers = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
positive_numbers = [num for num in numbers if num > 0]
print("Positive numbers:", positive_numbers)
