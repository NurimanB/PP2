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

#exercise 3
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"

#exercise 4
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

#exercise 5
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

#PYTHON if...else
#exercise 1
a = 50
b = 10
if a > b:
    print("Hello World")

#exercise 2
a = 50
b = 10
if a != b:
    print("Hello World")

#exercise 3
a=50
b=10
if a==b:
    print("Yes")
else:
    print("No")

#exercise 4
a=50
b=10
if a==b:
    print("1")
elif a>b:
    print("2")
else:
    print("3")

c=10
d=10
#exercise 5
if a == b and c == d:
    print("Hello")

#exercise 6
if a == b or c == d:
    print("Hello")

#exercise 7
if 5>2:
    print("YES")

#exercise 8
a = 2
b = 5
print("YES") if a == b else  print("NO")

#exercise 9
a = 2
b = 50
c = 2
if a == c or b == c:
    print("YES")

#PYTHON While loops
#exercise 1
i = 1
while i < 6:
    print(i)
    i += 1

#exercise 2
i = 1
while i < 6:
    if i == 3:
        break
    i += 1

#exercise 3
i=0
while i<6:
    i+=1
    if i==3:
        continue
    print(i)

#exercise 4
i=1
while i<6:
    print(i)
    i+=1
else:
    print("i is no longer less than 6")

#PYTHON For loops
#exercise 1
fruits=["apple", "banana", "cherry"]
for x in fruits:
    print(x)

#exercise 2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

#exercise 3
for x in range(6):
    print(x)

#exercise 4
fruits=["apple", "banana", "cherry"]
for x in fruits:
    if x=="banana":
        break
    print(x)