print("Hello World!")

if 5>2:
    print("YES")

#This is a comment
"""
This is a comment
written in 
more than just one line
"""

carname = "Volvo"
x = 50

x=5
y=10
print(x+y)

x=5
y=10
z=x+y
print(z)

x, y, z = "Orange", "Banana", "Cherry"
x=y=z="Orange"

def myFunc():
    global x
    x = "fantastic"

x = 5
print(type(x)) #type - int

x = "Hello World"
print(type(x)) #type - str

x = 20.5
print(type(x)) #type - float

x = ["apple", "banana", "cherry"]
print(type(x)) #type - list

x = ("apple", "banana", "cherry")
print(type(x)) #type - tuple

x = {"name" : "John", "age" : 36}
print(type(x)) #type - dict

x = True
print(type(x)) #type - bool

x = 5
x = float(x)

x = 5.5
x = int(x)

x = 5
x = complex(x)

x = "Hello World"
print(len(x))

txt = "Hello World"
x = txt[0]

txt = "Hello World"
x = txt[2:5]

txt = " Hello World "
x = txt.strip()

txt = "Hello World"
txt = txt.upper()

txt = "Hello World"
txt = txt.lower()

txt = "Hello World"
txt = txt.replace("H", "J")

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))