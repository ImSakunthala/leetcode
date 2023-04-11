"""
Inheritance is a core principle of OOP that allow us to derive a class from another class hierarchy of that share
set of attributes and methods. A class's ability to inherit methods and/or characteristics from another class is known
as inheritance.

It is a relationship between a superclass (Parent class or generalized class) and a subclass (child or specialized
class) . That is, the subclass or child class is the class that inherits and the superclass or parent class is the
class from which methods and/or attributes are inherited.

Advantages of Inheritance:
-> Code re-usability: Primary purpose of inheritance is code reuse. If we have an existing class A and we want to
create another class B with common data and methods as class A, we can derive class B from class A and reuse it.

-> Avoiding code duplication: Inheritance helps reduce amount of duplicate code by sharing common code among multiple
subclasses. If similar code exists, in two related classes, we can move common code to a shared superclass.

-> Improving code extensibility and flexibility: Any changes applied to the attributes and methods of superclass will
automatically apply to derived class. The subclasses can also add new attributes or methods if needed.

-> Provide better code structure and management: Inheritance also makes the subclasses follow a standard interface. It
provides a clear code structure that is easy to understand because class becomes grouped together in hierarchical tree
structure

-> Help to achieve runtime polymorphism: Inheritance provide the capability of subclass to override superclass method
by providing a new implementation

-> Avoid possible code errors: Error change applied in super class will automatically apply to subclass, without
inheritance it is difficult.

-> Preserves integrity of super class: Declaring subclass does not affect its superclass source code. So inheritance
preserves integrity of super class

-> Data hiding: The base class can be set to keep some data private so it cannot be altered by derived class.

Types of Inheritance:

1) Simple Inheritance: Subclass inherit characteristic from a single super class.

2) Multilevel Inheritance: A subclass may have its own subclasses. That is, A subclass of a superclass itself a
superclass to another subclass

3) Hierarchical Inheritance: A base class acts a parent class to multiple levels of subclasses.

4) Multiple Inheritance: A subclass may have more than one superclass and inherits characteristics from all of them.

5) Hybrid inheritance: A combination of one or more inheritance type.
"""


class Human(object):
    def __init__(self, name: str):
        self.name = name

    def report(self):
        print(f"I'm Human and my name is {self.name}")


class Teacher(Human):
    def __init__(self, name: str, department: str):
        super().__init__(name)
        self.department = department

    def report(self):
        print(f"I'm Teacher {self.name} in department {self.department})")


class Student(Human):
    def __init__(self, name: str, standard: str):
        super().__init__(name)
        self.standard = standard

    def report(self):
        print(f"I'm student {self.name} studying standard {self.standard}")


studentRam = Student('Ram', 'V')
teacherSaku: Teacher = Teacher('Saku', "CSE")
