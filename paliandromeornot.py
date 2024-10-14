def is_palindrome(n):
     n_str = str(n)
     n_rev = n_str[::-1]
     if n_str == n_rev:
         return True
     else:
         return False

n = int(input("Enter a number to check if it's a palindrome: "))

result = is_palindrome(n)

if result:
     print("The number is a palindrome.")
else:
     print("The number is not a palindrome.")
