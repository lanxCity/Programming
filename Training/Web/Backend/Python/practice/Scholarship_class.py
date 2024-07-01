import random

class User:
    def __init__(self, username, password):
        self.username = username
        self._password = password

    def login(self):
        login_detail = ['username', 'password']
        form = []

        for detail in login_detail:
            user_input = input(f'Enter your {detail: }')
            if detail.replace(' ', ""):
                form.append(user_input)

        username, password = form

        if username  == self.username and password == self._password:

            # =================> Error!!! Unable to access Applicant "first_name" attr from here.
            print(f'Welcome {self.first_name}')


    def logout(self):
        pass

    def forgotten_password(self):
        pass


class Applicant(User):

    profile_titles = ['first name', 'last name', 'other name', 'matric number', 'birth year', 'cgpa']

    def __init__(self, first, last, other, matric, birth_year, cgpa, username, password, id):
        super().__init__(username, password)
        self.first_name = first
        self.last_name = last
        self.other_name = other
        self.matric = matric
        self.age = 2022 - int(birth_year)
        self.cgpa = cgpa
        self.id = id

    def __repr__(self):
        return f'(matric = {self.matric}, cgpa = {self.cgpa})'

    @classmethod
    def apply(cls, id_list):

        def verify_data(new_input, title):
            if title == 'first name' or\
                title == 'last name' or\
                title == 'other name':
                if new_input.isalpha():
                    return True

            elif title == 'matric number' and new_input.isdigit() and len(new_input) is 6:
                return True

            elif title == 'birth year' and new_input.isdigit() and len(new_input) is 4:
                return True

            elif title == 'cgpa' and new_input.replace('.', '').isdigit():
                return True

            print('Sorry! Invalid data input. Please re-start the form.')
            print()
            return False

        def gen_id():
            new_id = ''.join([str(random.randint(0, 9)) for i in range(3)])
            if new_id in id_list:
                return gen_id()
            return new_id

        # Getting the applicant profile and stored in a list
        def create_data():
            data = []
            for title in cls.profile_titles:
                user_input = input(f'Enter your {title}: ')
                verified = verify_data(user_input, title)
                if verified:
                    data.append(user_input)
                    continue
                else:
                    return create_data()
            return data

        # Assigning each data element to their resp variables
        first, last, other, matric, birth, cgpa = create_data()
        applicant_id = gen_id()

        # Creating username and password
        print('For login purposes, please... ')
        username = input('\tCreate username: ').replace(' ', '') or matric
        non_alnum = ["*", "#", "@", "%", "$"]
        password = input('\tCreate password: ').replace(' ', '') or \
                   f'{first}{matric[-3:]}{random.choice(non_alnum)}'

        return cls(first, last, other, matric, birth, cgpa, username, password, applicant_id)


class Admin(User):
    pass

class App:
    @property
    def admins(self):
        admin_list = []







# --------------------------------------------------------------------Coming Back
#
# from abc import ABCMeta, abstractmethod
#
# class Shape:
#
#     __metaclass__ = ABCMeta
#
#     def __init__ (self, shapeType):
#
#         ”’Objective: To initialize object of class Shape Input Parameters:
#
#         self (implicit parameter) – object of type Shape
#
#         shapeType – string
#
#         Return Value: None
#
#         ”’
#
#         self.shapeType = shape Type
#
#     @abstractmethod
#
#     def area(self) :
#
#         pass
#
#     @abstractmethod
#
#     def perimeter (self):
#
#         pass
#
# class Rectangle(Shape):
#
#     def __init__(self, length, breadth):
#
#         ”’Objective: To initialize object of class Rectangle Input Parameters: self (implicit
#         parameter) – object of type Rectangle length, breadth – numeric value
#
#         Return Value: None ”’
#
#         Shape.__init__(self, ‘Rectangle’)
#
#         self.length = length
#
#         self.breadth = breadth
#
#     def area (self):
#
#         ”’Objective: To compute area of the Rectangle Input Parameter:
#
#         self (implicit parameter) object of type Rectangle
#
#         Return Value: numeric value
#
#         ”’
#
#         return self.length * self.breadth
#
#     def perimeter (self):
#
#         return 2 * (self.lenght + self.breadth)
#
# class Circle (Shape):
#
#     pi = 3.14
#
#     def __init__ (self, radius):
#
#         ”’Objective: To initialize object of class Circle Input Parameters: self (implicit
#         parameter) – object of type Circle
#
#             radius – numeric value
#
#             Return Value: None”’
#
#         Shape.__init__(self, ‘Circle’)
#
#         self.radius = radius
#
#     def area (self):
#
#         ”’Objective: To compute the area of the Circle
#
#         Input Parameter:
#
#         self (implicit parameter) – object of type Circle
#
#         Return Value: area – numeric value”’
#
#         return round(Circle.pi * (self.radius ** 2), 2)
#
#     def perimeter(self):
#
#         ”’Objective: To compute the perimeter of the Circle
#
#         Input Parameter:
#
#         self (implicit parameter) – object of type Circle
#
#         Return Value: perimeter – numeric value”’
#
#         return round (2 * Circle.pi * self.radius, 2)
#
# We indicate that a method is abstract by preceding its definition by @abstractmethod (function
# decorator). Note that the definition of an abstract class begins with
#
# __metaclass__ = ABCMeta



