"""
Abstraction is also a common feature in real life applications. For example,
-> When we log in to an online account, we enter user ID and password and click login button. The process of how input
data is sent to the server and verified is abstracted from us.
-> When type on computer, we press key to produce results on the screen. Here we don't need to know the mechanism behind
how output is produced.
-> In Hashmap, class provides methods for storing and retrieving key-value pairs. All we need to know the cases of
Hashmap in our application. The implementation details are abstracted from us.


But, Python doesn't support abstraction directly.

OOP uses 'Abstraction' to separate interface of an object from its implementation. It defines external behaviour of
an object and encapsulates its internal working. This allows the developer to interact with objects based on intended
behaviour, without understanding the details of how the behaviour is achieved

In other words, abstraction in OOP enables hiding internal details of an object from the outside world, so that focus
is on what the object does rather than how does it

Advantages of abstraction in OOPS:
1) Simplifies Code and reduce complexity: Abstraction is used to create a boundary between application and client code,
which can help reduce implementation complexity of software.
2) Facilitates modular and flexible design: Abstraction help us divide responsibilities into software entities (classes
and methods etc..,) where user only necessary functionalities , but not how functionality is implemented.
3) Improves code re-usability, readability and maintainability -> in other words code with proper abstraction helps
programmers quickly understand what the code does and how it is meant to be used.
4) Allows programmers simplify programming and shifts focus from implementation details and avoid writing low-level
code. On the other hand, it allows programmers to change internal implementation of methods or concrete classes without
affecting the interface.
5) Enhances code security by hiding internal implementation details and enables encapsulation od data and behaviour
within objects.
6) Supports extensibility, scalability and evolutionary development of code.
"""
# To create abstract class we have to import ABC module to use it
import abc


# To inherit abstract class for Human class
class Human(abc.ABC):
    def __init__(self, name: str):
        self.name = name

    def report(self):
        print(f"I'm Human and my name is {self.name}")

    @abc.abstractmethod
    def who_am_i(self):
        pass

    @abc.abstractmethod
    def provide_thumb_print(self):
        pass


class Teacher(Human):
    """
    If an abstract method is declared in a superclass, subclasses that inherit from the superclass must have their
    own implementation of the method.
    """
    def provide_thumb_print(self):
        return 'Teacher Thumb'

    def who_am_i(self):
        print("I'm a Teacher..!")

    def __init__(self, name: str, department: str):
        super().__init__(name)
        self.department = department

    def report(self):
        print(f"I'm Teacher {self.name} in department {self.department})")


class Student(Human):
    def provide_thumb_print(self):
        return 'Student Thumb'

    def __init__(self, name: str, standard: str):
        super().__init__(name)
        self.standard = standard

    def report(self):
        print(f"I'm student {self.name} studying standard {self.standard}")

    def who_am_i(self):
        print("I'm a student.!")


class AttendanceMachine:
    def in_entry(self, human: Human):
        print(f"Entry for IN added for {human.__class__} with Thumb:", human.provide_thumb_print())

    def exit_entry(self, human: Human):
        print(f"Entry for EXIT added for for {human.__class__} with Thumb:", human.provide_thumb_print())


studentRam = Student('Ram', 'V')
teacherSaku: Teacher = Teacher('Saku', "CSE")

attendanceMachine = AttendanceMachine()

attendanceMachine.in_entry(studentRam)
attendanceMachine.in_entry(teacherSaku)

attendanceMachine.exit_entry(studentRam)
attendanceMachine.exit_entry(teacherSaku)
