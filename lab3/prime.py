def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

numbers_string = input("Enter numbers separated by spaces: ")
numbers_list = list(map(int, numbers_string.split()))

prime_numbers = filter_prime(numbers_list)
print("Prime numbers in the list:", prime_numbers)
