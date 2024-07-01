# -------------------------Introduction to function---------------------
# We use "def" to define a function and followed by "func_name()"

# first_name = input('Welcome! please enter your first_name? ').capitalize()

# def greetings():
#     if first_name:
#         print('Hi {}'.format(first_name))
#     else:
#         print('Heeyyy!')
#
# greetings()
# print('Done!!!!!!!!!!!!!')

# 2. --------------------------- parameters and argument

# my_students =[
#     {
#         'matric': None,
#         'first_name': None,
#         'last_name': None,
#         'level': None,
#         'year_of_birth': None
#     },
#     {
#         'matric': None,
#         'first_name': None,
#         'last_name': None,
#         'level': None,
#         'year_of_birth': None
#     },
#     {
#             'matric': None,
#             'first_name': None,
#             'last_name': None,
#             'level': None,
#             'year_of_birth': None
#         }
# ]

# def create_profile(my_list):
#
#     user_input = None
#
#     for student in my_list:
#         print('Create a profile for this scholarship')
#         loop_counter = 0
#
#         for detail in student:
#             user_input = input(f'Enter your {detail}? ')
#             loop_counter += 1
#
#             if user_input:
#                 student[detail] = user_input
#                 if user_input.isalpha():
#                     student[detail] = user_input.capitalize()
#                 else:
#                     student[detail] = int(user_input)
#             # End
#
#             if len(student) == loop_counter:
#                 user_input = None
#                 print(f"\n\tHi {student['first_name']}! Registration completed...")
#                 print(student,'\n')
#             # End
#
# # ----------The end of the function "crete_profile"
#
#
# create_profile(my_students)


# # start the unicode for an emoji with "\" and change "+" with "000"
# first_name = 'lnax'
# def greetings(first_name):
#     if first_name:
#         print('Hi {}!'.format(first_name))
#     else:
#         print('Heeyyy!')
#
# greetings(first_name)
# print('Done!!!!!!!!!!!!!')

# def greetings(user):
#
#     if user and user.isalpha():
#         gender = input('"M" for male and "F" for female? ').upper()
#         if gender == 'M':
#             print(f'Hello Mr. {user}')
#         elif gender == 'F':
#             print(f'Hello Mrs. {user}')
#         else:
#             print(f'Hi {user}')
#     else:
#         print(f'Dear user, it\'s either you\'ve entered no values or numbers are \n'
#               f'present in the data you\'ve entered.')
# End of the function, greetings ------------------------------------------


# Calling the function
# greetings(first_name)

# --------------------"Parameters", "Arguments", "default parameters", and "Argument" keyword

# def greetings():
#     """
#     This function determines the title to address the user whilst greeting.
#     :return:
#     """
#     chances = 3
#     while chances > 0:
#         name = input('Enter your name please? ').capitalize()
#         if name and name.isalpha():
#             gender_counter = 3
#             while gender_counter > 0:
#                 gender = input('"M" for male and "F" for female? ').upper()
#                 if gender and gender.isalpha():
#                     if gender == 'M':
#                         message = f'Hello! Mr. {name}. Nice to meet you sir.'
#                         print('\n\t',message)
#                         return
#                     elif gender == 'F':
#                         message = f'Hello! Mrs. {name}. Nice to meet you sir.'
#                         print('\n\t',message)
#                         return
#                     else:
#                         message = f'Hello {name}! Nice to meet you.'
#                         print('\n\t',message)
#                         return
#                 else:
#                     gender_counter -= 1
#                     if gender_counter is not 0:
#                         message = f'Sorry, you need to enter the right value for gender and must be alphabet.\n ' \
#                                   f'You can still try again since you have {gender_counter} chance(s) left.'
#                         print('\n\t',message)
#                         continue
#             else:
#                 message = f'You are not ready {name}. Bye...'
#                 print('\n\t',message)
#                 return
#         else:
#             chances -= 1
#             if chances is not 0:
#                 message = f'You\'ve either enter no value(s) or wrong values as your name.\n ' \
#                           f'You can still try again since you have {chances} chance(s) left'
#                 print('\n\t',message)
#                 continue
#     else:
#         message = 'You are not ready buddy. Bye...'
#         print('\n\t',message)
#         return
# #
# #
# greetings()


# NB: Note that parameters and arguments parsed to a function are
# called positional params and arguments. Because they have to be arranged relative to their
# respective position.

# --------------------The use "return" keyword in a function-----------------
# We use "return" keyword to return value from a function and exit.

# def arithmetic():
#     user_input = ''
#     while True:
#         if not user_input:
#             user_input = input('Do you wants to perform operation on variables?(Yes/No) ').capitalize()
#         elif user_input and user_input.isdigit():
#             user_input = input('Perform another operation?(Yes/No)').capitalize()
#         else:
#             user_input = ''
#             continue
#         if user_input == 'Yes':
#             perform_operation = True
#             count = 3
#             unwanted_char = ''
#             while perform_operation and count > 0:
#                 user_input = input('Enter the expression you want to calculate? ')
#                 unwanted_char = False
#                 for i in user_input:
#                     if i.isnumeric() or i == '+' or i == '-' or i == '*' or i == '/' or i == '%' or i == '(' or i == ')':
#                         unwanted_char = False
#                     else:
#                         count -= 1
#                         unwanted_char = True
#                 if unwanted_char:
#                     if count is not 0:
#                         print(
#                             f'\n\tError!!! Unwanted character(s) is/are found in your expression... And you have {count} chances left.')
#                         continue
#                     else:
#                         return 'Bye Bye...'
#                 else:
#                     def operation(user_input):
#                         return eval(user_input)
#
#                     print(f'\n\t\tAnswer is {operation(user_input)}\n')
#                     break
#             if not unwanted_char:
#                 continue
#         elif user_input == 'No':
#
#             return '\n\tThank you buddy. See you next time...'
#         else:
#             continue
#
# print(arithmetic())


# The use "args" and "kwargs" (keyword argument)
# 1. The "*args" means parsing numerous of arguments more than required parameters
# my_list = [1,2,3,4,5,6,7,8,9]

# def summation(my_num):
#     return sum(my_num)

# print(summation(5))  #Error!!! Because the "sum()" func returns the total of iterable argument e.g list
# print(summation(my_list))

# print(summation(1,2,3,4,5,6,7,8,9)) #Error!!! one arg is expected but bunches were parsed
# Solution is as follows
# def summation(*nums):
#     print(nums)   #This is a tuple
#     return sum(nums)
#
# print(summation(1, 2, 3, 4, 5))

# 2. The "**kwargs" create a dictionary for args that are explicity parsed. e.g my_sum(n0 = 2, n2 = 5)
# n0,n2,n3,n4,n5,n6,n7 = [1,2,3,4,5,6,7]
#
# def summation(*my_args,**my_kwargs):
#     my_kwargs_total = 0
#     for n in my_kwargs.values():
#         my_kwargs_total += n
#
#     return sum(my_args) + my_kwargs_total
#
# print(summation(n0,n2,n3,n4,n5,n6,n7, n8 = 8, n9 = 9,n10 = 10))

# NB: The rules of parameters arrangement is >>>> args > *args > default params > **kwargs

# username = input('Your name please? ')
# n0, n1, n2, n3, n4, n5, n6 = [1, 2, 3, 4, 5, 6,7]
#
# def summation(name,*my_args, def_name = 'Sodiq',**my_kwargs):
#     my_kwargs_total = 0
#     for n in my_kwargs.values():
#         my_kwargs_total += n
#
#     # NB: If nothing is entered for the "username",
#     # the "name" = "" as the default value is not effective at that position.
#     msg = f'Dear {name}, the total of 1 - 10 is {sum(my_args) + my_kwargs_total}' if name else f'Dear {def_name}, the total of 1 - 10 is {sum(my_args) + my_kwargs_total}'
#
#     return msg
#
# print(summation(username, n0, n1, n2, n3, n4, n5, n6, n7 = 8, n8 = 9, n9 = 10, n10 = 11))


# --------------------The idea of "Scope"

#------ The following has no effect on the global variable scope
my_num = 1

def new_num(my_num):
    my_num += 1
    return my_num


print(new_num(my_num))
print(new_num(my_num))
print(new_num(my_num))
print(my_num)

# 1. ------The use of the "Global" keyword is the solution to the above task
# NB: The idea is not a best practice but rather the "dependency injection"

# def new_num():
#     global my_num
#     my_num += 1
#     return my_num
#
# print(new_num())
# print(new_num())
# print(new_num())
# print(my_num)

# # The dependency injection is parsing arg to a function as follows
# def new_num(num):
#     num += 1
#     return num
#
# print(new_num(new_num(new_num(my_num))))
# print(my_num)

# 2. ----------------- The "nonlocal" keyword
# This points to the parent variable, excluding the global.
# def outer_name():
#     name = 'Sodiq'
#     def inner_name():
#         nonlocal name
#         name = 'Lanx'
#         print('Inner name is', name)
#
#     inner_name()
#     print('Outer name is', name)
#
# outer_name()



























