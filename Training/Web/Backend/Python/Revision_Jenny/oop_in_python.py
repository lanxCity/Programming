# Naming of a class is "PascalCase"
# e.g class ClassName:
'''
class User:
    def __init__(self, firstname, lastname, age, department):
        # Object/Instance attributes
        ''
        Class constructor - This "__init__" method is called automatically,
        and it initializes the newly created object

        :param str firstname: str
        :param str lastname: str
        :param int age: int
        :param str department: str
        ''
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.department = department

    def __str__(self):
        return "heyyyyyyyyyyyyyy"


user1 = User('sodiq', 'Abdulrahmon', 27, 'Agric and Env. Engineering')
user2 = User('Abdulgafar', 'Hassan', 15, 'Political Science')

print(user1)
print(user2)

'''

# ==========> Quick review of OOP



# ==> Inheritance
# Single inheritance -> A subclass inherits from a single superclass
# Multilevel inheritance -> A subclass inherits from another subclass, creating a chain of inheritance.
# Multiple inheritance -> A subclass can inherit from more than one superclass
# Hierarchical inheritance -> Multiple subclasses inherit from a single superclass.

# When creating a subclass, it's common to override the __init__ method of the superclass to initialize
# the subclass-specific attributes. However, you often want to call the
# superclass's __init__ method to ensure that the superclass's attributes are also initialized properly.
# This can be done using the super() function.

# Base, Parent, Super class
class Pet:
    def __init__(self, name, dietary, legs):
        self.name = name
        self.dietary = dietary
        self.legs = legs

    def eat(self):
        print('Pet class -> I eat fish')
    def speak(self):
        pass


# ---> Hierarchical Inheritance

# Child, Derived, subclass
class Dog(Pet):
    
    def __init__(self, name, dietary):
        super().__init__(name, dietary, legs=4)  # accessing superclass attributes

    def eat(self):
        # Accessing the parent class method
        print('--------------')
        super().eat()
        print('Dog class -> I also eat bone')
    def speak(self):
        print('Dog class -> Woooof!!!!!!!!')  # overriding the speak method


class Cat(Pet):
    def __init__(self, name, dietary):
        super().__init__(name, dietary, legs=4)
    def speak(self):
        print('Cat class -> Meeooooowwwwwwwww!!!!!!!!')  # overriding the speak method


cat1 = Cat('Bili', 'Carnivore')
dog1 = Dog('Bingo', 'Carnivore')

cat1.eat()
dog1.eat()
print()

cat1.speak()
dog1.speak()
















