def square(a, b):
    for i in range(a, b+1):
        yield i**2

a = int(input("a: "))
b = int(input("b: "))
for i in square(a, b):
    print(i)