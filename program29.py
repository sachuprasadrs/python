numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
squares = [num ** 2 for num in numbers]
print("Squares of the numbers:", squares)
