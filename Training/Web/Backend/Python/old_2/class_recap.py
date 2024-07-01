# =========================> Caleb Curry ===================>

# class User():
#     def __init__(self, name, mem_status="Silver"):
#         self.name = name
#         self.membership = mem_status
#
#     # Some methods that can be overridden
#     # a. __str__: to convert the object itself to string
#
#     def __str__(self):
#         # print(f'Hi I\'m {self.name}! This is from "__str__" method')
#         return f'Name: {self.name} and member status: {self.membership}'
#
#     def __eq__(self, other):
#         #Used for comparison of two obj e.g mat_num, etc
#         if self.name == other.name and self.membership == other.membership:
#             return True
#         else:
#             return False
#
#     def upgrade_status(self, new_status):
#         #You can send API request
#         #Update dataBase and so on
#         #this can be updated manually but not the best practices.
#         self.membership = new_status
#
#     def greetings(self):
#         print(f'Welcome {self.name}! Nice to have you on board.')
#
#     def print_users(users):
#         # This is called a static method and can be used to perform action, or do something with
#         # user_list in general, or create new class from it based on certain thing.
#         # print('This is called a static method.')
#         for user in users:
#             print(user)
#
#     __hash__ = None  # to let the object to unhashable data structure
#     __repr__ = __str__
#
#
#
#
# # ==> Instance methods are methods used for on the individual obj created from a class
# # ==> Static methods are methods used for to describe the class itself and not limited to
# # individual obj.
#
# # cust_1 = User('Lanx', 'Gold')
# #
# # print(cust_1)   # cust_1.__str__()  == cust_1   (if __str__ is not redefined)
# # print(cust_1.name, cust_1.membership)
# #
# # cust_1.membership = 'Bronze'
# # print(cust_1.membership)
# #
# # cust_1.upgrade_status('Silver')
# # print(cust_1.membership)
# #
# # # Calling the static method on obj returns error but not on class
# # User.do_something()
#
#
# user_list = [
#     User('Sodiq', 'Gold'),
#     User('Lanx', 'Gold'),
#     User('Adigun')
# ]
#
# # print(user_list[0])
#
# # User.print_users(user_list)
#
# # print(user_list[0].__eq__(user_list[1]))
# # print(user_list[0] == user_list[1] )
#
# # Hashable data structure
# # data = {user_list[0]}    #Error
#
# # print(user_list[0].__repr__())   # returns the list of their location in memory. Unless we change the
# # "__repr__" value
# # method
#
#
# print(user_list)


# ******************************** Class Revisit *********************************
# ************************ Udemy 2 ***********
# import random
# from random import randint
# print(randint(1,3))
#
# my_list = ['lanx', 'sodiq', 'adigun']
#
# # random.shuffle(my_list)
#
# print(my_list[:-1])
# print(my_list[-3:])


# ------------------------- Intro

# => _privateAttr or method (conventionally): A private attr (preceded by an "_") only to be accessed internally
# (but it's just a convention as it can be accessed from outside like normal attr).
# used to indicate that an attribute or method is intended for internal use. It is a hint to the programmer that
# the attribute is intended to be private or protected and should not be accessed directly from outside the class.

# => __attr or method is to protect or attach the attr to the class itself (majorly, for inheritance
# purposes). So that the subclass could have its own attr or method of the same name and not
# conflicting with one another. And the use of such means "Name Mangling"; the name of such attr
# is changed behind the scene. E.g. "__password"
#  In large class hierarchies, The interpreter changes the name of the attribute to include the class name
#  before the attr name itself. This to prevent subclasses from accidentally overriding or accessing
#  private attributes of their superclasses.

# => The dunder attr or methods are builtin but their functionality can be overwritten to our
# taste (conventional). e.g. __repr__(self), etc.

# N.B: The use of "self" as the internal param is conventional as another naming could be used.

# class User:
#     def __init__(self, first, last, age=0):
#         '''
#         :param str first: str
#         :param str last: str
#         :param int age: int
#         '''
#         self.first = first
#         self.last = last
#         self._age = age
#         # self.__hobbies = 'Coding'  # Name mangling; it's attached to the class directly.
#
#     def initials(self):
#         return f'{self.first[0].upper()}.{self.last[0].upper()}.'
#     # def hobbies(self):
#     #     return self.__hobbies
#     #
#     def best_food(self, food):
#         return food
#
#
# # ------------- Instance attr and methods
#
# user1 = User('Sodiq', 'ramon', 25)
#
# print(user1.initials())
# print(user1.best_food('Amala'))


# ---------------The class attr and methods
# class User:
#     # class attr or var
#     num_of_users = 0
#
#     def __init__(self, first, last, age=0):
#         self.first = first
#         self.last = last
#         self._age = age
#         self.__is_active = True
#
#         "self.num_of_users += 1" can also be used. But to distinguish btwn the class and
#         instance, we use the following.
#         User.num_of_users += 1
#
#     def logout(self):
#         if self.__is_active:
#             self.__is_active = False
#             User.num_of_users -= 1
#             return f'You just logged out.'
#         else:
#             return f'You\'ve logged out already.'
#
#     def login(self):
#         if not self.__is_active:
#             self.__is_active = True
#             User.num_of_users += 1
#             return f'You\'ve logged in.'
#         else:
#             return f'Already logged in...'
#
#     def active(self):
#         return self.__is_active
#
#     # class methods are useful for creating a new instance from the class.
#     @classmethod
#     def display_num_of_users(cls):
#         return cls.num_of_users


# user1 = User('sodiq', 'ramon', 25)
# user2 = User('adigun', 'amoke', 65)
# user3 = User('adigun', 'amoke', 65)

# print(User.num_of_users)
# print(user1.num_of_users)

# print(User.display_num_of_users())
# print(user1.display_num_of_users())

# user1.num_of_users = 3
# print(user1.num_of_users)

# user1.friends = ['lanx', 'reemah']
# print(user1.friends)


# print(User.num_of_users)
# print(user3.logout())
# print(user3.login())
# print(user3.active())
# print(User.num_of_users)


# Example of class method using "dict" data type
# print(dict.fromkeys(['name', 'age', 'hobby'], 'lanx'))


# ---------------------------------Example of class method
# import random
# class Game:
#     players_list = list()
#     players = 0
#
#     def __init__(self, username):
#         self.username = username
#         self.id = self.player_id()
#         Game.players += 1
#         Game.players_list.append({'username':self.username, 'id': self.id})
#
#     def __repr__(self):
#         return self.username
#
#     def player_id(self):
#         # id generator function
#         def gen_id():
#             id = ''
#             for _ in range(3):
#                 id += str(random.randint(0,9))
#             is_id_exist = id_exist(id)
#             if is_id_exist:
#                 return gen_id()
#             return id
#
#         def id_exist(id):
#             for player in Game.players_list:
#                 if player['id'] == id:
#                     return True
#             return False
#
#         return gen_id()
#
#     @classmethod
#     def add_player(cls):
#         username = input('Create username: ')
#
#         if not username or username.isspace():
#             username = f'Player_{len(cls.players_list) + 1}'
#         return cls(username)
#
#
# user1 = Game.add_player()
# user2 = Game.add_player()
#
# print(user1)
# print(user2)


# =========================> Inheritance
# A. Implement inheritance and multiple inheritance
# -> Inheritance is the ability to define a class which inherits from another class called a base
# or parent class. In python, inheritance works by passing the parent class as an argument to the
# definition of the child class.
#
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def make_sound(self, sound):
#         print(f'{self.name} {sound}')
#
#
# class Dog(Animal):
#     def __repr__(self):
#         return f'{self.name} is a dog'
#
#
# class Cat(Animal):
#     def __repr__(self):
#         return f'{self.name} is a cat'
#
#
# bingo = Dog('Bingo')
# print(bingo)
# bingo.make_sound('bark')
#
# bruno = Cat('Bruno')
# print(bruno)


# me = []
#
# print(isinstance(me, list))


# Ai.] ====> Properties in class

# class User:
#     def __init__(self, name, age):
#         self.name = name
#         # if age >= 0:
#         #     self._age = age
#         # else:
#         #     self._age = 0
#
#         self._age = max(0, age)
#
#
#     # def get_age(self):
#     #     return self._age
#     #
#     # def set_age(self, age):
#     #     self._age = max(0, age)
#     #
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, age):
#         if age < 0:
#             raise ValueError('Age can\'t be negative!')
#         self._age = max(0, age)


# janet = User('Janet', -45)
# If there is going to be an update or modification in a particular attr such as "age", the age can
# be overwritten from outside, which is totally fine, as,
# print(janet.age)

# But especially if there is going to be some checks or modification before such value is set,
# using the idea of "properties"; setter and getter is advisable. And these are accessed as
# instance attr.
# @property decorator is used for "getter" while @getterName.setter is used for "setter"

# N:B The following are accessed as instance method which slightly introduces the idea getter and
# setter.
# janet.set_age(-1)
# print(janet.get_age())
#
# janet.set_age(45)
# print(janet.get_age())


# N:B The following are accessed as normal instance attr which are getter and setter.
# janet.age = -56
# print(janet.age)


# Aii.] ===> The use of "super()" to extend parent ppties (e.g. attr) inside the child object

# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#
#     def __repr__(self):
#         return f'{self.name} is a {self.species}'
#
#     def make_sound(self, sound):
#         print(f'{self.name} {sound}')
#
#
# class Cat(Animal):
#     def __init__(self, name, species, breed, toy):
#         # if cat is not having another attr where "__init__" method would be used, extending
#         # the parent isn't necessary; there must one initialization for both child and parent
#         # unless there is additional info for the child.
#
#         # Animal.__init__(self, name, species)  # Valid.
#         # But using "super" is best practice where "self" is not required.
#
#         super().__init__(name, species)
#         self.breed = breed
#         self.toy = toy
#     pass
#
#
# kitty = Cat('Bruno', 'Cat', 'Russian', 'Piano')
# print(kitty)


# ==> Example 2.

# class User:
#
#     num_of_users = 0
#     active_users = 0
#
#     def __init__(self, first, last, age = 0):
#         self.first = first
#         self.last = last
#         self.age = max(0, age)
#         self._is_active = True
#         User.num_of_users += 1
#         User.active_users += 1
#
#     def __repr__(self):
#         return f'{self.first}'
#
#     @property
#     def active(self):
#         return self._is_active
#
#     def logout(self):
#         if self._is_active:
#             self._is_active = False
#             User.active_users -= 1
#             return f'You just logged out.'
#         else:
#             return f'You\'ve logged out already.'
#
#     def login(self):
#         if not self._is_active:
#             self._is_active = True
#             User.active_users += 1
#             return f'You\'ve logged in.'
#         else:
#             return f'Already logged in...'
#
#     @classmethod
#     def display_num_of_users(cls):
#         return cls.num_of_users
#
#
# class Moderator(User):
#     def __init__(self, first, last, age, community):
#         super().__init__(first, last, age)
#         self.community = community
#
#     def remove_post(self):
#         return f'{self.first} removes a certain post from the {self.community}'
#
#
# user_1 = User('Sodiq', 'Abdulramon', 100)
# user_2 = User('Abdurasheed', 'Bogunmbe', 200)
# user_3 = User('Janet', 'Klobb', 76)
#
# mod_1 = Moderator('Maryam', 'Ayoade', 150, 'Education')
# mod_2 = Moderator('Moshudah', 'Olowookere', 150, 'Soccer')
#
#
# user_1.logout()
#
# print(mod_1)
# print(mod_2)
#
# print(mod_2.community)


# Aiii.] ===>       Multiple inheritance

# class Aquatic:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f'{self.name}'
#
#     def swim(self):
#         return f'{self.name} swims in water'
#
#
# class Ambulatory:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f'{self.name}'
#
#     def swim(self):
#         return f'{self.name} walks on the land'
#
# class Penguin(Ambulatory, Aquatic):
#     def __init__(self, name):
#         super().__init__(name)

#
# dog = Ambulatory('Bingo')
# tilapia = Aquatic('Watermendi')
# penguin = Penguin('King Penguin')
#
# print(dog)
# print(tilapia)
# print(penguin)


# Aiv. ] ====> The order of method are resolving; Method Resolution Order (MRO)
# This is the order in which python looks for methods on instances of that class (Just like
# hierarchy).
# You can programmatically reference the MRO in 3 ways:

# i. __mro__ attr on the class
# ii. use the mro() method on the class
# iii. use the builtin help(cls_name) method


# class A:
#     def do_stuff(self):
#         print('Calling from class A')
# class B(A):
#     def do_stuff(self):
#         print('Calling from class B')
#     pass
# class C(A):
#     def do_stuff(self):
#         print('Calling from class C')
# class D(B, C):
#     # def do_stuff(self):
#     #     print('Calling from class D')
#     pass
#
# thing = D()

# Order of methods is: D -> B -> C -> A(base obj) -> builtin object; When calling super(),
# B is being invoked.

# thing.do_stuff()
# print(D.mro())   # returns list
# print(D.__mro__)   # returns tuple
# help(D)   # returns full detail


# B. ==> Polymorphism: means an object can take on many(poly) forms(morph).
# i. The same class works in a similar way for diff classes e.g.
# Cat.speak()
# Dog.speak()
# Human.speak()

# A common implementation of this is to have a method in a base (or parent) class that is
# overridden by a subclass. This is called method overriding; each subclass will have a diff
# implementation of the method.
#
# class Animal:
#     def speak(self):
#         raise NotImplementedError('Subclass needs to implement this method')
#
# class Dog:
#     def speak(self):
#         return 'woof'
#
# class Cat:
#     def speak(self):
#         return 'meow'


# ii. The same operation works for diff kinds of objects e.g.
# me = 'lanx'
# you = [1,4,3,2,1]
# them = 43

# len(me)
# len(you)
# len(them)

# It involves the use of special or magic methods that are dunders (i.e. double
# underscore-named). And give instructions to python for how to deal with objects.
# Another ex. is 2 + 3 and '2' + '3' are diff.
# The "+" operator is shorthand for a special method called "__add__()" that get called on the
# first operand. If the first operand is an instance of int, math operation is performed,
# else if it's a str instance, concatenation is done.

# Some magic methods

# class Human:
#     def __init__(self, first, last, gender, age):
#         self.first = first
#         self.last = last
#         self.gender = gender
#         self.age = age
#
#     def __repr__(self):
#         full_name = f'{self.first} {self.last}'
#         return f'{full_name} is a {self.gender.lower()}'
#
#     def __len__(self):
#         return self.age
#
#     def __add__(self, other):
#         # if type(other) is Human:
#         if isinstance(other, Human):
#
#             return Human('Newborn', 'Spiderman', 'Male', 0)
#
#         return 'You are not compatible!'
#
#     def __mul__(self, other):
#         if isinstance(other, int):
#             import random
#
#             msg = str(self)
#             # return [f'Newborn Spiderman {child}' for child in range(1, other + 1)]
#             return [(msg).
#                         replace('Spiderman', f'Spiderman{child}').
#                         replace('male', random.choice(['male', 'female']))
#                     for child in range(1, other + 1)]
#
#         return 'Not compatible'
#
# k_maruff = Human('Kareemot', 'Maruff', 'Female', 26)
# future_husband = Human('Unknown', 'Adigun', 'Male', 30)
#
# # print(k_maruff)
# # print(future_husband)
#
# # print(k_maruff + future_husband)
#
#
# print((k_maruff + future_husband) * 11)
# print((k_maruff + future_husband) * 3)


# Making Grumpy dictionary - overriding dict or inheriting from the "dict data type"
# It involves keeping the original functionality but adding some grumpiness; no need to define (or
# alter) the existing "__init__()" method.

# class GrumpyDict(dict):
#     def __repr__(self):
#         print('This is from "__repr__()"')
#         # return super(GrumpyDict, self).__repr__()
#         return super().__repr__()
#
#     def __missing__(self, key):
#         '''
#         :param str key: str
#         :return str:
#         This is invoked when a non-existing key is being called
#         '''
#
#         return 'Are you trying to find what you didn\'t stored here?!'
#
#     def __setitem__(self, key, value):
#         print('Hey buddy! You just love to keep changing things...')
#         print(f'Well, {key} is added.')
#         return super(GrumpyDict, self).__setitem__(key, value)
#
#     def __contains__(self, item):
#         '''
#         :param str item: str
#         :return bool:
#         This checks if a key exist in a dict or not by using the keyword 'in'
#         '''
#         print(f'Why not see for yourself: {self}')
#         return super(GrumpyDict, self).__contains__(item)
#
#
# d = GrumpyDict({'name': 'Lanx', 'age': 25})

# print(d.__repr__())
# print(d)
# print(d['city'])

# d['city'] = 'Alamu'
# print(d)
#
# print('city' in d)


# ===========================> Revision 2
# 2019 Video






# ====>  Error Handling (Try-except-else-finally)
# try:
#     # user_data = {'name': 'lanx'}
#     # user_name = user_data['name']
#     x = 5
#
#     print(x[0])
#
# # except KeyError:
# except Exception as e:
#
#     print(e)
#
# else:
#     print(x)
#
# finally:
#     print('YEh')


























