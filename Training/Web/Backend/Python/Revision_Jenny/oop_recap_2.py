import math
import random

# ------> Q1
class Circle:
    '''
    It calculate the area and circumference of a circle
    :param radius: int
    '''

    PI = math.pi  # Class attr
    def __init__(self, radius):
        self._radius = radius  # Obj protected attr

    def area(self):
        return round(Circle.PI * (self._radius**2), 2)

    def circumference(self):
        return round(Circle.PI * (2 * self._radius), 2)


# c1 = Circle(9)
# c2 = Circle(10)

# print(c1.area())
# print(c2.area())


# ------> Inheritance intro
class Pets:
    _data = []
    def __init__(self, name, age, breed, diet):
        self.name = name
        self.age = age
        self.breed = breed
        self.diet = diet
        self._id = self.id_generator()
        self._owner = None

        Pets._data.append(self)

    def __repr__(self):
        return f'{self.breed}'

    def __str__(self):
        owner_info = f", owned by {self._owner.name}" if self._owner else ", --No owner--"
        return f"{self.breed} (ID: {self._id}){owner_info}"


    def id_generator(self):
        ''' Generate a unique ID for each pet '''
        while True:
            new_id = random.randint(1, 100)
            if not any(pet._id == new_id for pet in Pets._data):
                return new_id

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, details):
        '''
        Set the owner details - (name, phone, and address)
        :param details: tuple
        '''
        if isinstance(details, tuple) and len(details) == 3:
            self._owner = Owner(details[0], details[1], details[2])
            return

        print('Must be a tuple of of owner\'s name, phone, and address')



class Owner():
    def __init__(self, name, phone, address):
        '''
        :param name: str
        :param phone: str
        :param address: str
        '''

        self.name = name
        self.contact = (phone, address)

    def __repr__(self):
        return f'Owner(Name: {self.name}, Contact: {self.contact})'

class Dog(Pets):
    pass

class Cat(Pets):
    pass


# d1 = Dog('Jerry', 5, 'Golden Retriever', 'beef')
# d1.owner = ('Tope', '+2348146257816', '2 Div, Nigerian Army Barracks')
#
# d2 = Dog('Tom', 7, 'Bulldog','beef')
#
# c1 = Cat('Bunny', 3, 'persian', 'fish')
# c1.owner = ('Hamzy', '+2349031740783', 'UI second gate')
#
#
# print(Pets._data)
# print(d1)
# print(d1.owner)
# print(d2)
# print(c1)

# -------> Single inheritance - One child from a parent
class Human:
    def __init__(self, name, age, gender, department, courses):
        self.name = name
        self.age = age
        self.gender = gender
        self.department = department
        self.courses = courses
        self.in_class = False
        self.current_lecture = None

    def __repr__(self):
        return self.name

    def having_lecture(self, course):
        self.in_class = True
        self.current_lecture = course
        return

class Student(Human):
    def __init__(self, name, age, gender, dep, courses):
        super().__init__(name, age, gender, dep, courses)
        self._has_paid = False


s1 = Student('Lanx', 50, 'M', 'TAE', ['TAE701', 'TAE751', 'TAE722'])

# print(s1)


# -------> Multiple inheritance - One child from multiple parents
# The MRO started from the "first parent (param)"

# class A:
#     def __init__(self, name):
#         self.name = name
#
#     def shout(self):
#         print('I am MR. A')
#         return
#
#
# class B:
#     def __init__(self, gender):
#         self.gender = gender
#
#     def shout(self):
#         print('I am MR. B')
#         return
#
#
# class C(A, B):
#     # The effect of MRO
#     def __init__(self, name, gender):
#         A.__init__(self, name)
#         B.__init__(self, gender)
#
#
# c1 = C('Lanx', 'Male')
# print(c1.name)
# print(c1.gender)


# -------> Multilevel inheritance - One child from multiple parents
# The MRO started from the immediate/first parent (param) to the base parent
# class A:
#     def __init__(self, name):
#         print('This is from class A')
#         self.name = name
#
#     def shout(self):
#         print('I am MR. A')
#         return
#
#
# class B(A):
#     def __init__(self, gender):
#         print('This is from class B')
#         self.gender = gender
#
#     def shout(self):
#         print('I am MR. B')
#         return
#
#
# class C(B):
#     # The effect of MRO
#     # def __init__(self, name, gender):
#     #     A.__init__(self, name)
#     #     B.__init__(self, gender)
#     pass
#
#
# c1 = C('Male')
# print(c1.gender)
#

# -------> Hierarchical inheritance - Multiple children from one parent
# The MRO started from the immediate/first parent (param) to the base parent
class User:
    def __init__(self, name):
        print('This is from class A')
        self.name = name

    def shout(self):
        print('I am MR. A')
        return


class Teacher(User):
    def __init__(self):
        print('This is from class Teacher')
    def shout(self):
        print('I am MR. B')
        return


class Student(User):
    # The effect of MRO
    # def __init__(self, name, gender):
    #     A.__init__(self, name)
    #     B.__init__(self, gender)
    pass


# -------> Hybrid inheritance - Mixing of two or more inheritance methods
# The MRO is same as multiple's (L -> R) but also extend to the base of the
# current class being searched at that time
class A:
    # def __init__(self, name):
    #     self.name = name

    def shout(self):
        print('Shouting from A')
        return


class B(A):
    def walk(self):
        print('Walking from B')
        return

    def shout(self):
        print('Shouting from B')
        return


class C:
    # The effect of MRO
    def run(self):
        print('Run from C')
        return
    def shout(self):
        print('Shouting from C')
        return

class D(B, C):
    pass


d1 = D()
d1.shout()







