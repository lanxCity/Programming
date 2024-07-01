# import math
# from random import random
#
# # ===========> Intro
# class User():
#     #==> Attributes or properties of the object goes inside the "__init__" function which is the
#     # object constructor.
#     def __init__(self, name, birth_year, username, is_active=False):
#         '''
#         :param str name: str,
#         :param int birth_year:int,
#         :param str username:str
#         :param bool is_active:bool
#         '''
#         if not name or not username:
#             name = username = 'User'
#
#         self.name = name
#         self.birth_year = birth_year
#         self.id = self.generate_id()
#         self.username = str(username) + self.id
#         self.is_active = is_active
#
#     #==> The "class obj attribute" or "class variable" is an attribute or any variable of the
#     class itself. And called as normal attr or ppty
#     is_new_member = True
#
#     #==> The following are methods of the objects created. And also called "instance method",
#     which only used on any instance or new object created from the class.
#     def generate_id(self):
#         '''
#         This returns three (3) digits random number,
#
#         :return str:
#         '''
#         random_num = ''
#         for _ in range(3):
#             random_num += str(math.floor(random() * 10))
#         return random_num
#
#     def greetings(self):
#         '''
#         This function greets the user with their first name
#
#         :return: str,
#         '''
#         msg = f'Hi {self.name}! You are welcome to my website.'
#         return msg
#
#
# user_1 = User('', 1997, 'lanx', True)
# user_2 = User('Adigun', 1997, 'lanx')
# user_3 = User('kareem', 1997, 'Lanx')
# user_4 = User('kareemah', 1997, 'Lanx')
#
# user_1.is_new_member = False   # It over-written the default class (or prototype) attribute and
# # created new property inside the object directly
#
# user_1.__dict__.pop('is_new_member')
#
#
# print(user_1.__dict__)
# print(user_1.is_new_member)
# print(user_2.__dict__)
# print(user_3.__dict__)
# print(user_4.__dict__)


# =====> @classmethod and @staticmethod
# => The "@classmethod" method is a method used with the class itself. And its main advantage is
# that we can use the class method without instantiation. And can also be used for "factory"
# object; when the class needs modification before instantiation.
# It is used when the 'cls' param is to be used inside the method.

# => The "@staticmethod" method is a method neither used with class nor instances, but has their
# use for conversion.
# ===> They can both be called using either the "className" or class object (instance)


# class User():
#     is_new_user = True
#
#     def __init__(self, name, birth_year, username, is_active=False):
#         if User.is_new_user or not User.is_new_user:
#             self.name = name
#             self.birth_year = birth_year
#             self.username = username
#             self.is_active = is_active
#
#     def greetings(self):
#         msg = f'Hey there! I\'m {self.name}'
#         return msg
#
#     # defining a class method using the decorator "@classmethod"
#     @classmethod
#     def change_membership_status(cls, membership_status):
#         cls.is_new_user = membership_status
#
#     # defining a static method using the decorator "@staticmethod"
#     @staticmethod
#     def subscription(member_sub):
#         member_list = ['REGULAR', 'VIP', 'VVIP']
#         if member_sub.upper() in member_list:
#             return f'Welcome! You are now a {member_sub.upper()} member on this platform'
#         else:
#             return 'Invalid!!!'
#
#
# user1 = User('Sodiq', 1948, 'lanx', True)
# user2 = User('Sekinat', 1942, 'Becky')
#
# # **They both change the original value of the class variable
# # User.change_membership_status(False)
# # user1.change_membership_status(False)
#
#
# print(user1.subscription('regular'))
#
# print(user1.is_new_user)
# print(user2.is_new_user)
#
# print(user1.__dict__)
# print(user2.__dict__)

# ==> Ex.2
# class User():
#     def __init__(self, name, gender, age, campus_status):
#         self.name = name
#         self.gender = gender
#         self.age = age
#         self.campus_status = campus_status
#
#     def greetings(self):
#         if self.campus_status.lower() is 'student':
#             msg = f'{self.name.capitalize()} says good day!'
#             return msg
#         else:
#             msg = f'{self.campus_status} {self.name.capitalize()} says good day to you all! You
#             ' \
#                   f'are all welcome to my class'
#             return msg
#
#     @classmethod
#     def do_math(cls, n1, n2):
#         return n1 + n2
#
#     @classmethod
#     def lecturer(cls, title):
#         if title.isalpha() or title[:-1].isalpha() and title[-1] is '.':
#             return cls('Oyefeso', 'Female', 1998, title)  # Creating a factory class
#         else:
#             return cls('Oyefeso', 'Female', 1998, 'Instructor')
#
#
# # print(User.do_math(5,6))
#
# user1 = User('Sodiq', 'Male', 1888, 'student')
# user2 = User.lecturer('Prof.')
#
# print(user1.__dict__)
# print(user2.__dict__)


# ===>Ex.3
# class User():
#     def __init__(self, name, gender, dep, campus_status=None, active=False):
#         self._name = name  # to show it's private.
#         self.gender = gender
#         self.dep = dep
#         self.campus_status = campus_status
#         self.active = active
#
#     def greetings(self):
#         return f'{self._name} says Hello!!!'
#
#
# user1 = User('lanx', 'male', 39, 'Student')
#
# print(user1.__dict__)
# print(user1.greetings())
# print(user1.greetings() is user1)   #True


# ==> Pillars of OOP
# 1. Encapsulation
# 2. Abstraction: This means hiding or abstracting away info, and giving access to what is
# necessary. That is, those info that only need to perform some actions and give out the result.
# e.g. "greet()". In abstraction, when it comes overwritten a certain attr or method inside object
# created there is this idea of "public and private variables".
# The private var is the use of "_" before our attr or method just to show they are private,
# and it's a common convention for python programmers.

# user1.name = 'heyyyyyyyy'
#
# # print(user1.__dict__)
# print(user1.__dict__)

# 3. Inheritance


# ===============> Initial Video recap <===============
# => "@classmethod" and "@staticmethod"
# => Pillars of OOP
# 1. Encapsulation
# 2. Abstraction
# 3. Inheritance
# 4. Polymorphism
# => Introspection is the ability to determine the type of object at runtime using "dir()"
# function.
# => The dunder method

class User:
    def __init__(self, first, last, other, age, hobby):
        self.first = first
        self.last = last
        self.other = other
        self.age = age
        self.hobby = hobby

    def __iter__(self):
        self.__hash__()

    # def __dir__(self):
    #     return self


user1 = User('Sodiq', 'Ramon', 'Damilare', 25, 'Football')

# print(dir(user1))


# print(dir(us1))

