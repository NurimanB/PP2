class MyClass():
    def __init__(self):
        self.str = ""

    def getString(self):
        self.str = input("Enter a string: ")

    def printString(self):
        print(self.str.upper()) 
a = MyClass()

a.getString()

a.printString()

