#PYTHON Syntax
#exercise 1
print("Hello World!")

#exercise 2
if 5>2:
    print("YES")


#PYTHON Comments
#exercise 1
#This is a comment
    
#exercise 2
"""
This is a comment
written in 
more than just one line
"""


#PYTHON Variables
#exercise 1
carname = "Volvo"

#exercise 2
x = 50

#exercise 3
x=5
y=10
print(x+y)

#exercise 4
x=5
y=10
z=x+y
print(z)

#exercise 5
x, y, z = "Orange", "Banana", "Cherry"

#exercise 6
x=y=z="Orange" 

#exercise 7
def myFunc():
    global x
    x = "fantastic"


#PYTHON Data Types
#exercise 1
x = 5
print(type(x)) #type - int

#exercise 2
x = "Hello World"
print(type(x)) #type - str

#exercise 3
x = 20.5
print(type(x)) #type - float

#exercise 4
x = ["apple", "banana", "cherry"]
print(type(x)) #type - list

#exercise 5
x = ("apple", "banana", "cherry")
print(type(x)) #type - tuple

#exercise 6
x = {"name" : "John", "age" : 36}
print(type(x)) #type - dict

#exercise 7
x = True
print(type(x)) #type - bool


#PYTHON Numbers
#exercise 1
x= 5
x = float(x)

#exercise 2
x = 5.5
x = int(x)

#exercise 3
x = 5
x = complex(x)


#PYTHON Strings
#exercise 1
x = "Hello World"
print(len(x))

#exercise 2
txt = "Hello World"
x = txt[0]

#exercise 3
txt = "Hello World"
x = txt[2:5]

#exercise 4
txt = " Hello World "
x = txt.strip()

#exercise 5
txt = "Hello World"
txt = txt.upper()

#exercise 6
txt = "Hello World"
txt = txt.lower()

#exercise 7
txt = "Hello World"
txt = txt.replace("H", "J")

#exercise 8
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))