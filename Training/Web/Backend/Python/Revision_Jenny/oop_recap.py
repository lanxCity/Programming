# -> Introduction
# Naming convention for class is PascalCase
"""
print('>' * 20, 'Introduction')


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__is_active = True

    def logout(self):
        self.__is_active = False
        print("You have logged out successfully!")


user1 = User('Sodiq', '27')
print(user1.name)

# -> Inheritance (Single)
print('>' * 20, 'Inheritance')


class Animal:
    '''
    Superclass/Base/ParentClass
    :param name: str
    :param legs: int
    :param family: str (default is 'Mammal')
    '''

    def __init__(self, name, legs, family='Mammal'):
        self.name = name
        self.num_of_legs = legs
        self.family = family

    def __repr__(self) -> str:
        return f"(name: '{self.name}', family: '{self.family}')"

    def eat(self) -> None:
        print('I can eat')

    def talk(self) -> None:
        print('I can talk')

    def walk(self) -> None:
        print('I can walk')


class Cat(Animal):
    '''
    Subclass/DerivedClass/Child
    '''

    def __repr__(self) -> str:
        return f"Cat{super().__repr__()}"

    def talk(self) -> None:
        print('I can Meow')


class Bird(Animal):
    '''
    Subclass/DerivedClass/Child
    '''

    def __init__(self, name, legs):
        super().__init__(name, legs, family='Aves')

    def __repr__(self) -> str:
        return f"Bird{super().__repr__()}"

    # def __str__(self):
    #     return "Yeeeeeeeeeeeeeeeeeeeeeeeeeeeh"  # overrides "repr" if print() or str() is used

    def walk(self) -> None:
        super().walk()
        print('I can fly')

    def talk(self) -> None:
        print('I can chirp')


cat1 = Cat('Brad', 4)
bird1 = Bird('Kane', 2)

print(cat1)
print(bird1)

cat1.talk()
bird1.walk()

# -> Multiple Inheritance
# -> Multiple parents with a child
print('>' * 20, 'Multiple Inheritance')


class A:
    def __init__(self):
        print('From A "init"')

    def talk(self):
        print('A is talking')

    def eat(self):
        print('A is eating')


class B:
    def __init__(self):
        print('From B "init"')

    def talk(self):
        print('B is talking')

    def eat(self):
        print('B is eating')

    def walk(self):
        print('B is walking')


class C(B, A):
    '''
    MRO - Method Resolution Order
    '''

    def __init__(self):
        print('From C init')
        super().__init__()  # This invokes the first class that's parsed

        # To include other super classes init method
        print('* Include other super classes')
        A.__init__(self)  # The self param is a must
        print('- End C init method-')


c = C()

c.eat()  # From B
A.eat(c)  # From A

print(C.mro())


# -> Multilevel Inheritance
class Human:
    def __init__(self):
        print('From Human class')

    def eat(self):
        print('I am a human. I eat...')


class Student(Human):

    def __init__(self):
        print('From Student class')

    def study(self):
        print('I am a student. I study...')


class Graduate(Student):
    def do_project(self):
        print('I am a final year student and currently doing project')


student = Student()
graduate = Graduate()

graduate.eat()
print(Graduate.mro())


# -> Hierarchy Inheritance
# - A parent with multiple children
class Animal:
    '''
    Basic info about the animal object
    :param name: str
    :param age: int
    '''

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayDetails(self) -> None:
        print(f'name: {self.name}, age: {self.age} months old')

    def move(self) -> None:
        print('I can move')


class Bird(Animal):
    '''
    :param name: str
    :param age: int
    '''
    def __init__(self, name, age):
        Animal.__init__(self, name, age)
        self.legs = 2
    def speak(self) -> None:
        print('I chirp...')

    def has_feather(self):
        return True


class Cat(Animal):
    '''
    :param name: str
    :param age: int
    :param babies: int
    '''

    def __init__(self, name, age, babies):
        super().__init__(name, age)
        self.legs = 4
        self.babies = babies
    def speak(self) -> None:
        print('I meow...')

    def displayDetails(self) -> None:
        super().displayDetails()
        print(f'I have {self.babies} babies...')

    def has_fur(self):
        return True


bird1 = Bird('Whyte', 5)
cat1 = Cat('Adam', 6, 3)

bird1.displayDetails()
cat1.displayDetails()



# -> Hybrid Inheritance
# This is by combining 2 or more different inheritance

class Animal:
    def move(self):
        print('I am moving')

class Mammal:
    def has_fur(self):
        print('Mammal has fur')
        return True

class Bird(Animal):
    def has_feathers(self):
        print('Mammal has fur')
        return True

class Bat(Bird, Mammal):
    def can_fly(self):
        print('I enjoy flying!!!')
        return True

bat1 = Bat()
bat1.can_fly()

print(Bat.mro())

"""

# -> Diamond Problem in Inheritance | MRO | C3 Linearization Algorithm
# - Classic Diamond problem (Hybrid inheritance - Hierarchical and multiple)
# - MRO -> Local precedence, Monotonicity
# Lecture 94 explains everything

class Animal:
    def move(self):
        print('I am moving')

    def speak(self):
        print('Animal makes sound')

class Mammal(Animal):
    def has_fur(self):
        print('Mammal has fur')
        return True
    def speak(self):
        print('Mammal makes sound')

class Bird(Animal):
    def has_feathers(self):
        print('Mammal has fur')
        return True
    def speak(self):
        print('Bird chirps...')

class Bat(Bird, Mammal):
    def can_fly(self):
        print('I enjoy flying!!!')
        return True
    # def speak(self):
    #     print('Bat is quite...')

bat1 = Bat()
bat1.can_fly()

print(Bat.mro())
















