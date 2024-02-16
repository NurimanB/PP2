def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)

number = int(input("Enter a positive integer: "))
if number < 0:
    print("Please enter a positive integer.")
else:
    result = calculate_factorial(number)
    print(f"The factorial of {number} is: {result}")
