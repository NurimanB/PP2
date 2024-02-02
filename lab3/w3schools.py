#PYTHON Functions
#exercise 1
def my_function():
    print("Hello from a function")

#exercise 2
def my_function():
  print("Hello from a function")

my_function()

#exercise 3
def my_function(fname, lname):
    print(fname)

#exercise 4
def my_function(x):
   return x+5

#exercise 5
def my_function(*kids):
    print("The youngest child is " + kids[2])

#exercise 6
def my_function(**kid):
    print("His last name is " + kid["lname"])


#PYTHON Lambda
#exercise 1
x = lambda a : a


#PYTHON Classes
#exercise 1
class MyClass:
    x = 5

#exercise 2
class MyClass:
    x = 5

p1 = MyClass()

#exercise 3
class MyClass:
  x = 5

p1 = MyClass()

print(p1.x)

#exercise 4
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age


#PYTHON Inheritance
#exercise 2
class Person:
  def __init__(self, fname):
    self.firstname = fname

  def printname(self):
    print(self.firstname)

class Student(Person):
  pass

x = Student("Mike")
x.printname()

#exercise 1
class Student(Person):
    x = 5 #It's not related to task. Just for code to not show error

#PYTHON Modules
#exercise 1
import mymodule

#exercise 2
import mymodule as mx

#exercise 3
import mymodule

print(dir(mymodule))

#exercise 4
from mymodule import person1