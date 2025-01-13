def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    power = len(str(num))
    sum_of_powers = sum(d**power for d in digits)
    return sum_of_powers == num
user_input = int(input("Enter a number greater than 10: "))
if user_input <= 10:
    print("Please enter a number greater than 10.")
else:
    if is_armstrong(user_input):
        print("Number is armstrong")
    else:
        print("Number is not armstrong")
