# lamda, filter, map, reduce

# => 1. lamda (anonymous function)
# It is defined in this format, "lamda param : xpression"
# a value is return and save in a variable
# Usually, lamda is used in a function such as "map"
'''
square = lambda a: a * a
print(square(6))
print(square(30))
print(square(10))

# => 2. Filter function works with true or false and returns a list
data = list(range(1, 50))

# normal func
def is_even(n):
  return n % 2 == 0


even_nums = list(filter(is_even, data))
print(even_nums)
odd_nums = list(filter(lambda el: el % 2 == 1, data))
print(odd_nums)


data = list(range(1, 50))
even_nums = list(filter((lambda n: n % 2 == 0), data))
print(even_nums)

# => 3. Map is used to perform operation on each element of a list and returns new list
square_even = list(map(lambda el: el * el, even_nums))
print(square_even)

# => 4. Reduce all the elements of a list to a certain value based on the operation performed
from functools import reduce
sum_square_even = reduce(lambda a, b: a + b, square_even)
print(f"The sum is: {sum_square_even}")

# ===> Higher order function
# Higher-Order Functions: These are functions that take other functions as arguments or return functions.
# Decorators: A specific type of higher-order function used to modify the behavior of another function.
# In Python, decorators are often used with the @decorator syntax for simplicity and readability.

# ===> Decorator
# A function decorator in Python is a higher-order function that takes another function
# as an argument and returns a new function. Decorators are a powerful feature of Python
# that allows you to modify or extend the behavior of functions or methods without directly
# modifying their source code. They are commonly used for tasks such as logging, caching,
# authentication, and more.
# For example, imagine we have an existing function or module and there's to be some modifications
# before final result and there's no way to modify the module or decided to leave the original code
# as it is, then we can make use of decorator.

data = list(range(-5, 10))

# we can use the existing "sum" function
print(sum(range(10)))
print(sum(data))

def non_neg_sum(func):
    def sum_wrapper(data):
        positive_data = list(filter(lambda el: el > 0, data))
        return func(positive_data)

    return sum_wrapper


# summation = non_neg_sum(sum)
# print(summation(data))
@non_neg_sum
def miniSum(li):
    return sum(li)

# ---------------- NB: "@non_neg_sum" is a shorthand for "miniSum = non_neg_sum(miniSum)"
# "miniSum = non_neg_sum(miniSum)" is equivalent to "summation = non_neg_sum(sum)"
# where the variable "minSum" stores the returned function "sum_wrapper" of the higher order function

miniSum(data)


# Instead of calling the decorator "non_neg_sum" function, we can call the function name directly
def greetings_decorator(func):
    def wrapper():
        print('Before greetings')
        result = func()
        print('After greetings')

        return result
    return wrapper


@greetings_decorator
def greetings():
    print("Hey there!!!")


greetings()


# ===> Modules (custom modules or external files in the main code)
import test_modules

# from test_modules import add, subtract, divide, multiply
# from test_modules import *  # To import all functions in the module


# ==> Special variable (__name__) and methods (__init__)
# In C programming for example, "main" function is the starting point of execution or entry point
# And same goes for python as well where we have the main module or file that interact with other modules
# E.g. this file is the main module or file because it is not used in another program
print(__name__)
if __name__ == "__main__":
    print('Hey there')
    print(test_modules.add(2,3))


# =====> Python OOP
# Class is the design of an object
# Class -> Design/Blueprint
# Object -> Instance of the class; Object created from a class is called an instance of a class
# So we can use the term object/instance to mean the same thing.
# A class object has two types of information termed as "Attributes" of the obj.
# Data attr (also known as obj ppties) defines the state of an obj
# Function attr (also known as methods) defines the behaviour of an obj

# I. ----> Class and Object
class Person:
    def walk(self):
        print('I am walking')


person1 = Person()
person2 = Person()

# To access the object methods, we call the method on the class... OR
Person.walk(person1)  # Pass the obj as args to rep the "self" param
Person.walk(person2)

# Call the methods on the object itself (which is the conventional way)
# but under the hood, the first method is what is happening
person1.walk()
person2.walk()


# ===> Types of attributes/variables in oop realm
# Two types -> Instance attributes and class (static) attributes
# variable outside the constructor "__init__" is a class variable and it is the same for all objects of the class
class Car:
    # Class attr
    # It can be access directly through the class name or instance but
    # modification must be from class itself except if an obj wants to override it
    car_wheel = 4
    def __init__(self, model, colour, milage):
        # Object attributes
        self.model = model
        self.colour = colour
        self.milage = milage

    def update(self, colour):
        self.colour = colour


car1 = Car('BMW', 'Black', 20)
car2 = Car('Lexus', 'Pink', 10)

# car1.car_wheel = 6  # New attr has been added to this obj and overriding the class attr
# print(car1.model, car1.car_wheel)
# print(car2.model, car2.car_wheel)
# print(Car.car_wheel)

#----------------
# Car.car_wheel = 6
# print(car1.model, car1.car_wheel)
# print(car2.model, car2.car_wheel)
# print(Car.car_wheel)




# ===> Types of methods
# Instance, class, and static methods
# a. Instance method -> It is used to work with instance attr and it can be either
# Accessor/getter (to fetch attr value) and Mutator/setter (to modify attr value) methods

# b. Class method is used for class attributes and/or to manipulate the whole class
# c. Static methods are utility methods for miscellaneous purposes and it is called on class name
# we use the decorator "@staticmethod" for such... it is just there as usual function for some operation
class Student:
    department = 'Agricultural and Environmental Engineering'
    no_of_student = 0

    def __init__(self, name, age, level, course_unit):
        self.name = name
        self.age = age
        self.level = level
        self.course_unit = course_unit
        self._carryover = 0  # private attr and only access directly within the class

        Student.count_student()

    # ->  Instance methods
    def greetings(self):
        print(f'Hey {self.name.capitalize()}! Welcome on board👋')

    # Instead of using regular instance var, we'll use getter and setter methods
    # since this method is being treated as attr
    @property
    def carryover(self):
        return self._carryover

    @carryover.setter
    def carryover(self, courses):
        if courses:
            self._carryover = courses

    @classmethod  # decorator
    def count_student(cls):
        cls.no_of_student += 1


user1 = Student("ibrahim", 25, 300, 43)
user2 = Student("sikiru", 29, 400, 27)

user1.greetings()
user2.greetings()

print()

print(f'{user1.name} has {user1.carryover} carryovers')
print(f'{user2.name} has {user2.carryover} carryovers')
print()

user2.carryover = 2

print(f'{user1.name} has {user1.carryover} carryovers')
print(f'{user2.name} has {user2.carryover} carryovers')


print(Student.department)


# ===> Inheritance
# This is a concept that allows a class
# (called a subclass or derived class) to
# inherit attributes and methods from another
# class (called a superclass or base class)
# Diff methods of inheritance:
# Single inheritance -> A subclass inherits from a single superclass
# Multilevel inheritance -> A subclass inherits from another subclass, creating a chain of inheritance.
# Multiple inheritance -> A subclass can inherit from more than one superclass
# Hierarchical inheritance -> Multiple subclasses inherit from a single superclass.


# 1. Single inheritance
class A:
    def method1(self):
        print('method1 -> in class A')

    def method2(self):
        print('method2 -> in class A')
class B(A):
    def method3(self):
        print('method3 -> in class A')

    def method4(self):
        print('method4 -> in class A')



# 2. Multilevel inheritance
class A:
    def method1(self):
        print('method1 -> in class A')

    def method2(self):
        print('method2 -> in class A')
class B(A):
    def method1(self):
        print('method1 -> in class B')
    def method3(self):
        print('method3 -> in class B')

    def method4(self):
        print('method4 -> in class B')
class C(B):
    def method5(self):
        print('method5 -> in class C')


a = A()
b = B()
c = C()

a.method1()
b.method1()
b.method4()
c.method5()

'''











