"""Method Overloading -> to the use of many methods with the same name that take various numbers of arguments within a
single class

But in python, Python doesn't support Method Overloading by default.

Because Python only remembers the most recent definition of method(self, name:str), which takes one parameter in
addition to self. As a result, one argument must be passed to the add() method when it is called. To put it
another way, it disregards the prior definition of method(self). """


class MethodOverloading:
    def method(self):
        print('No argument method')

    def method(self, name: str):
        print(f"Method with one argument: {name}")

