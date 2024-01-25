#PYTHON Booleans
#exercise 1
print(10 > 9)

True

#exercise 2
print(10 == 9)

False
 
#exercise 3
print(10 < 9)

False

#exercise 4
print(bool("abc"))

True

#exercise 5
print(bool(0))

False

#PYTHON Operators
#exercise 1
print(10*5)

#exercise 2
print(10/2)

#exercise 3
fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Yes, apple is a fruit!")

#exercise 4
if 5 != 10:
    print("5 and 10 is not equal")

#exercise 5
if 5 == 10 or 4 == 4:
    print("At least one of the statements is true")

#PYTHON Lists
#exercise 1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#exercise 2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

#exercise 3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#exercise 4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

#exercise 5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#exercise 6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#exercise 7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#exercise 8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

#PYTHON Tuples
#exercise 1
fruits = ("apple", "banana", "cherry")
print(fruits[0])

#exercise 2
fruits = ("apple", "banana", "cherry")
print(len(fruits))

#exercise 3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

#exercise 4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

#PYTHON Sets
#exercise 1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:  
    print("Yes, apple is a fruit!")

#exercise 2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#exercise 3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#exercise 4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#exercise 5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

#PYTHON Dictionaries
#exercise 1
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

#exercise 2
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020
