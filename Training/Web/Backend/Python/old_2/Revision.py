# import math
# import random

# 1. The Fundamental Data types.

# 1a. "int" and "float" and "complex"

# print(type(2+5))
# print(type(2/5))
# print(2**5)  #This is exponential; 2^5

# print(2//5)        #Returns the floor of the division answer; 0
# print(2%5)       #Returns the remainder of the division; 2

# ==> The "Math" functions. You can google it up
# print(round(12/5))
# print(abs(-14/5))

# ==> Complex
# complex_Num = 5 + 3j
# print(type(complex_Num))
# print(complex_Num * 2)

# ==> bin() function
# print(bin(5))  #returns the binary rep of 5 with prefix "0b" to show it's a binary
# print(int('101',2))   // Converts from any bases to base 10
# print(int('0b101',2))

# ---------------------------Variables
# a. Snake_case is commonly used for variable names in python
# b. starting variable name with "_" isn't a best practice. As it is use
# as "private variable", but it's allowed.
# c. Don't use keywords as variable names
# d. Constant variable; those things or variable that their values
# never changed. E.g. PI = 3.14
# e. Don't create a variable using "Dunder" style; the use of
# double underscore "__". Although, this is allowed, but they are expected
# to be left alone, just like "keywords"
# f. Shorthand method of multiple variable; a,b,c = 1,2,3 is totally valid.


# ---------------------Augmented assignment operator
# num = 5
# # num = num + 45
#
# num += 45
# print(num)

# => 1b. String data type

# Single quotes, double quotes, triple single or double quotes

# name = 'Sodiq'
# greeting = """The University of Ibadan says "Hi" to """
#
# print(greeting + name)


# ---------------------Type Conversion --------
# str, int, float, etc.


# giver_name = 'Sodiq'
# acct_bal = 12555

# borrower_msg = """The University of Ibadan says "Hi" to """

# print(borrower_msg + giver_name + " , Mr. " +str(acct_bal))

# print(float(acct_bal))

# -----------------------The Escape sequence

# borrower_msg = "The University of Ibadan says \"Hi\" to "
#
# print(borrower_msg + giver_name + " , Mr. " +str(acct_bal))

# # ------------------------The formatted string
# first_name = "Sodiq"
# last_name = 'Abdulramon'

# => In python 3
# greeting = f'''Welcome Mr {first_name}! 'learnt your full name is {first_name} {last_name}.'''

# => In python 2

# msg = '''Hi Mr. {}! We learnt your surname \
# is {}'''.format(first_name,last_name)

# msg = '''Hi Mr. {0}! We learnt your \
# full name is {0} {1}'''.format(first_name,last_name)
#
# msg = '''Hi Mr. {first_name}! We learnt your surname \
# is {last_name}'''.format(first_name='Alamu', last_name='Okanlomo')
#
# print(msg)

# ------------------The string indexing
# string[start:end:stepwise]

# print(first_name[0])
# print(first_name[0::2])
# print(first_name[:len(first_name):1])
# print(first_name[-1:-len(first_name)-1:-1])
# print(first_name[::-1])

# -----------------Some built-in function and methods

# msg = 'welcome to the party!'

# print(msg.casefold())  # returns the lowercase or the string
# print(msg.swapcase())
# print(msg.find('party'))  # returns the l_index of the value searched
# print(msg.replace('the','our'))
#

# ==> 1c. Booleans: bool()

# ==> Exercise: Password checker
#
# name = input('Enter your name please? ').capitalize()
# password = input('Set your password? ')
#
# password_len = len(password)
# password_first_char = password[0]
# password_other_chars = password[1:]
#
# msg = f'''Hi {name}! Your password {password_first_char}\
# {len(password_other_chars) * '*'} is of {password_len} characters'''
#
# print(msg)

# ===> 1d. List data type: list()

# list_1 = ['Toyota','Camry','Audi']
# list_2 = list_1       #Always points to the initial list
# list_3 = list_1[:]     #Create a new copy of the original list.
#
# list_1[2] = 'Benz'
# list_2[0] = 'Ferrari'
#
# print(list_1)
# print(list_2)
# print(list_3)


# -------------------Matrix or Multidimensional list
# ====> Some list methods
# name = 'kareemah'
# print(name[:-4:-1])

# print(list(range(15,-2)))   # range(start,stop,stepwise)

# ==>1e. The Dictionary: dict()

# new_dict = dict(name='Lanx', age=25,greetings=None)
# new_dict['greetings'] = 'Hi'

# ==>1f. The Tuple data type: tuple()
# ==>1e. The set:set()


# ------------------------------------------The control flow--------------------------

# ------------------------------Car racing game------------------------
# welcome_msg = "Welcome to lanxCity car racing game. Type \"help\" to see the guideline."
# help = '''
# "stop": To stop the car;
# "start": To start the car;
# "quit": To quit the game;
# '''
#
# car_started = False
# quit_game = False
# wrong_val_counter = 1
# print(welcome_msg)
#
# while not quit_game and wrong_val_counter != 3:
#     user_input = input('Enter your input? ').lower()
#
#     if user_input == 'start':
#         if not car_started:
#             print('\tCar started...')
#             car_started = True
#         else:
#             print('\tCar has already started...')
#     elif user_input == 'stop':
#         if car_started:
#             print('\tCar stopped...')
#             car_started = False
#         else:
#             print('\tCar has been stopped...')
#     elif user_input == 'help':
#         print(help)
#         car_started = False
#     elif user_input == 'quit':
#         quit_game = True
#         print('\tI hope you enjoy the game. See you soon...')
#     else:
#         print('\tPlease, enter the right data. And you can type "help" to see the guideline.')
#         wrong_val_counter += 1


# ===============================> Basic 2

# Truthy and Falsy

# ==> The ternary operator or conditional expression
# E.g. counter = 50
# For JS, counter === 10 ? console.log('Sorry, you're wrong') : console.log('Great')
# For Py, print('Sorry, you're wrong') if counter == 10 else print('Great')

# num_to_guess = 50
# user_input = float(input('Guess a number from 1-50? '))
#
# # In js, let msg = user_input === 50 ? 'You won!' : 'Sorry, try again.'
#
# msg = 'You won!' if user_input == 50 else 'Sorry, try again'
#
# print(msg)

# ==> Short Circuiting: The use of "and" and "or"
# ==> The logical operator

# name = 'sodiq'
# new_name = 'sodiq'

# print(name is new_name) # True
#
# print('c' > "A")

# The "is" vs "="
# Data structure are created separately in the memory
# "==" only cares about value equality

# print(name is new_name ) #true. Not because they are stored in the same memory, but they are
# exact same thing
# print([] is [])  #false

# my_list = []
# my_new_list = my_list #true
# my_new_list = my_list[:] #false
#
# print(my_list is my_new_list)

# print((1,2,3,4)[3])  #tuple supports indexing


# =============================> Loops

# 1. The "for" loop

# container = []
# for shelve in range(10):
#     container.append('orange')

# container = {}
# for shelve in range(10):
#     container.update({shelve + 1: 'orange'})
#   container.update({'shelve ' + str(shelve + 1): 'orange'})

# for shelve in range(10):
#     container.append({'shelve ' + str(shelve + 1): 'orange'})
#
# print(container)

# profile = {
#     'name': 'sodiq',
#     'age': 32,
#     'is_cool': True
# }

# for item in profile.items():
#     print(item)
#
# for key, value in profile.items():
#     print(key + ': ' + str(value))

# print(type(profile.items()))

# ====================================Exercise: Average of a list====================>

# my_list = [1,2,3,4,5,1,2,2,4,2]

# counter = 0
# total = 0
#
# for i in my_list:
#     counter += 1
#     total += i


# avr = total/counter


# avr = sum(my_list)/len(my_list)
#
# print(F'The total avr of list "my_list" is ', avr)

# ====================>  The range() and enumerate(iterable,start(optional)) functions
# range(start,stop, step) only deals with num of times we'd want loop and also deals with those
# nums it just created in  in particular

# my_list = [1,2,3,4,5,1,2,2,4,2]

# for i in range(10):
#     print(i)

# new_List = {}
# for l_index,i in enumerate(my_list):
#     new_List.update({f'{i} * 2': i * 2})
#
# print(new_List)


# =================> Exercise: Create a loop that's going count each element inside a list

# my_list = [1,2,3,4,5,1,2,2,4,2]
#
# new_List = {}


# for l_index, i in enumerate(my_list):
#     if i not in new_List:
#         new_List.update({i: 1})
#     else:
#         new_List.update({i: new_List[i] + 1})
# print(new_List)

#
# new_List = {}
# for l_index, i in enumerate(my_list):
#     if i in new_List:
#         continue
#     new_List.update({i: my_list.count(i)})
#
#
# print(new_List)


# for l_index, i in enumerate(range(100)):
#     if i is 50:
#         print(f'"{i}" is at l_index {l_index}')


# 2. The "while" loop
# 3. Function
# ==> Default params and kwargs (keyword args)
# Types of params and args:
# A. positional: this is a normal way of passing args to a function in the same pattern or order
# of its (the func) params. e.g.

# N:B JS only supports positional params and args........................

# def greetings(name, year_of_birth):
#     age = 2022 - year_of_birth
#     print(f'Hello {name}! You are {age} years old.')

#
# username = input('Enter your name? ')
# user_birth_year= input('Enter your birth year? ')

# greetings(username,user_birth_year) # this args follows the order of the params

# B. Keyword args: We do not have to worry about the position of the params
# this is not best practice and can be confused with "default params"
# greetings(year_of_birth= user_birth_year, name = username)


# C. Default params: These are used if args are not provided

# def greetings(name = 'Lanx', year_of_birth = 1999):
#     year_of_birth = year_of_birth if \
#         year_of_birth and year_of_birth.isnumeric() \
#         else 1999
#
#     if name and year_of_birth:
#         age = 2022 - int(year_of_birth)
#         print(f'Hello {name}! You are {age} years old.')
#
# greetings(username,user_birth_year)

# D. DocString: Just like in JS, we can also have some documentation on our custom function.
# /*
# * this is used in JS.
# */

# '''this is used in python
# '''


# username = input('Enter your name? ')
# user_birth_year= input('Enter your birth year? ')
# print()
# def greetings(name , year_of_birth):
#     '''
#     :param str name: str,
#     :param int year_of_birth: int,
#     :return: None,
#     Greets user_list with respect to their input names and year of birth.
#     '''
#     year_of_birth = year_of_birth if \
#         year_of_birth and year_of_birth.isnumeric() \
#         else 1999
#
#     if name and year_of_birth:
#         age = 2022 - int(year_of_birth)
#         print(f'Hello {name}! You are {age} years old.')
#
#
# # Apart from "hovering" over the func to view its doc, we can use "help(func)" or "print(
# # func.__doc__)"
#
# # greetings(username,user_birth_year)
# help(greetings)
# print(greetings.__doc__)

# E. args and kwargs continued------------------------
# my_list = [3,4,5,6,7]
#
# def list_summation(new_list):
#     return sum(new_list)


# list_summation(1,2,3,5,5) # error: 1 pos param is given, therefore 1 arg is expected.

# ===> The use of "*args" and "**args"

# def list_summation(*new_list):
#     print(new_list)
#     print(type(new_list))   #This is a "tuple"
#     return sum(new_list)
#
# print(list_summation(1,2,3,5,5))
#
# username = input("Enter your name please? ")
# user_math_operation_type = input("Enter the type of operation you want to perform? ")
#
#
# def list_summation(name, operation_type="summation", *new_tuple, **new_dic):
#
#    if operation_type.isalpha():
#         operation_type = operation_type if \
#             operation_type.lower() == "addition" or \
#             operation_type.lower() == 'sum'  \
#             else 'summation'
#    else:
#        operation_type = "summation"
#
#    total = sum(new_tuple) + sum(new_dic.values())
#    message = f'Dear {name.capitalize()}! the {operation_type} of the data given  is {total}'
#
#    message = message if name.isalpha() else message.replace(f'Dear {name.capitalize()}', 'Hi')
#    print(message)
#
#
# list_summation(username, user_math_operation_type, 1, 2, 3, 4, 5, n1=6, n2=7, n3=8, n4=9)
#
# # N:B ==> Rules: pos params, default params, *arg, **args


# --------------------------Exercise: Create a func that gets the highest even number from a list
#
# my_list = [2,3,4,5,6,2,4,1,8,4,4,4,2,47]
#
# def highest_even(*data):
#
#     # Checking for invalid input
#     for i in data:
#         if type(i) is list:
#             raise Exception('Invalid input')   # throwing an error
#     # Operating starts
#     if type(data[0]) is list:
#         data = data[0]
#
#     even = []
#     for i in data:
#         if not i % 2 and i not in even:
#             even.append(i)
#     return max_sum(even)
# # End function highest_even
#
#
# print(highest_even(2,3,4,3,2,2,2,26,6,4,4,4))


# ==> Scope in python
# Any variables defined are global variables except those within a function.


# def count():
#     total += 1
#     #  error! as total isn't defined before refereced inside the local scope
#     return total


# => Use of "global" keyword. Not a good idea doing the following

# def count():
#    global total
#    total += 1
#    return total

# => The best way is "dependecy injection";
# total = 0
# def count(total):
#     total += 1
#     return total

# print(count(total))
# print(count(total))
# print(count(total))   #They all return 1

# print(count(count(count(total))))  #returns 3

#
# =>The "non-local" keyword
# def outer():
#     x = 10
#     def inner():
#         nonlocal x  #just unlike "global", it means deals with only parent scope of function
#         x += 1
#         return x
#     return inner()
#
#
# print(outer())


# 2. Classes => Custom data types
# 3. Specialized data type => available inside module e.g. (libraries and frameworks, etc.)

# name = 'sodiq'

# print(name)
# print(name)
# print(name)
# print(name)
# print(name)

# for i in range(5):
#     print(name)

# my_name = 'sodiq'
# msg = f'Hi! I\'m {my_name}. Some of my friends include '
#
# my_list = ['sodiq', 'adigun', 'me']
#
# separator = ', '
# end = '.'
#
# msg += separator.join(my_list) + end
#
# print(msg)

# my_list = ['sodiq', 'adigun', 'Maryam']

# my_list_to_string = ''
#
# for name in my_list:
#     my_list_to_string += name
#
#     if name == my_list[-1]:
#         my_list_to_string += '.'
#     else:
#         my_list_to_string += ', '
# print(my_list_to_string)

#
# my_profile = {
#     'name': 'sodiq',
#     'age': 25,
#     'hobbies': ['coding', 'eating', 'eating']
# }
#
# msg = f"My name is {my_profile['name']}. I love "

# for item in my_profile:
#     if type(my_profile[item]) is list:
#         msg += ', '.join(my_profile[item])
#         msg += '.'

# print(msg)


# # 6.---------------------Our First GUI

# list_of_titles = ['Name', 'Age', 'Matric. number']
#
# students = [
#     {
#         'name': 'lanx',
#         'age': '2',
#         'mat_num': '200268',
#     },
#     {
#         'name': 'adigun',
#         'age': '3',
#         'mat_num': '200272'
#     },
#     {
#         'name': 'igi iwe',
#         'age': '10',
#         'mat_num': '212345'
#     },
#     {
#         'name': 'baba o',
#         'age': '5',
#         'mat_num': '200265'
#     },
#     {
#         'name': 'maryam',
#         'age': '16',
#         'mat_num': '200124'
#     }
# ]
# row = ''
#
# for el in list_of_titles:
#     row += el
#     row += '\t\t\t'
#
# row += '\n'
#
#
#
# for data in students:
#     for detail in data:
#         row += data[detail]
#         row += '\t\t\t '
#     row += '\n'
#
# print(row)


# quiz = [
#     'How many continents do we have in the world? ',
#     'South Korea is located in what continent? ',
#     'There are how many states in Nigeria? ',
#     'What is the official language that is used in Nigeria (without "LANGUAGE" included)? ',
#     'Nigeria became republic immediately after independence in what year? '
# ]
#
# ans = [
#     7,
#     'asia',
#     36,
#     'english',
#     1963
# ]
#
# counter = 0
# correct_ans = []
# wrong_ans = []
#
# for quest in quiz:
#     user_input = input(quest)
#     current_ans = ans[counter]
#
#     if type(current_ans) is int:
#         current_ans = str(current_ans)
#
#     # Checking if user input is correct
#     if user_input == current_ans:
#         print('Correct!')
#         correct_ans.append(quest + current_ans)
#     else:
#         print('Incorrect!')
#         wrong_ans.append(quest + current_ans)
#
#     counter += 1
#
#
# print()
# print(f'Number of correct answers: {len(correct_ans)}')
# print(f'Number of wrong answers: {len(wrong_ans)}')


# import time
# time.sleep(5)
# print('Hello')


# list_1 = [2,3,4,4,4,1,2,3,4,12,3,1,1]
#
# list_2 = [1,2,3,1,1,23,3,3,4,2,1,2,2,34,2,1,1,1]
# import random
#
# # me = random.sample()
# me = [1,2,3,4,4,5,12,42]
#
# print(random.sample(me, 2))
#
#
# help(random.sample)


# list_1_Uni_list_2 = list()
#
# for el in list_1:
#     if el in list_2 and el not in list_1_Uni_list_2:
#         list_1_Uni_list_2.append(el)
#
# print(list_1_Uni_list_2)
#
#
# #         ---------OR
# list_1_to_set, list_2_to_set = set(list_1), set(list_2)
#
# list_1_Union_list_2 = list_1_to_set.intersection(list_2_to_set)

# print(list_1_Union_list_2)


#
# username = input('Enter your name: ')
# current_age = input('Enter your age: ')
# current_year = 2022

# future_age = 100
#
#
# if current_age.isdigit():
#
#     difference_in_age = future_age - int(current_age)
#     year_to_be_future_age = current_year + difference_in_age
#
#     print(f'You would be {future_age}years old by {year_to_be_future_age}')
#
# else:
#     print('Invalid age input!!!')


# Question: Write a program to determine the year that you'd turn 100years from the current year
# or age of a user


# patient = input('Enter your name: ')
# current_age = input('Enter current age: ')
# current_year = input('Enter current year: ')
#
# if current_year.isdigit() and current_age.isdigit():
#     future_age = 100
#
#     year_left = future_age - int(current_age)
#
#     future_year = int(current_year) + year_left
#
#     print(f'You would turn {future_age} in year {future_year}')
# else:
#     print('Invalid input!')


# while and function

# name_on_server = 'Adigun'
#
# name_valid = False
#
# while not name_valid:
#     username = input('What is your name? ')
#
#     if username and username.isalpha():
#         username = username.capitalize()
#
#         if username == name_on_server:
#             name_valid = True
#             print('Access granted')


# help = '''
# "5" to start
# "2" to stop
# "0" to quit
# '''
#
# car_started = False
# car_stop = True
# quit = False
#
# print('Welcome to Lanx car race\n', help)
#
# while not quit:
#
#     user_input = input('Enter value here: ')
#
#     if user_input and user_input.isdigit():
#         if user_input is "5":
#             car_started = True
#             print('Car started.')
#         elif user_input is "2":
#             car_stop = True
#             print('Car stopped.')
#         elif user_input is "0":
#             quit = True
#         else:
#             continue
#     else:
#         print('invalid command!')

# random.choices()

# prev =
# print(next(my_list))

# for i in range(50):

# help(next)

# m(row) and n(col)

# def gen_two_dim_array(row, col):
#
#     my_list = []
#     for i in range(int(row)):
#         new_row = []
#         for j in range(int(col)):
#             new_row.append(i * j)
#         my_list.append(new_row)
#
#     return my_list
#
#
# print(gen_two_dim_array(5, 6))
# print()
# print(gen_two_dim_array(3, 4))
# print()
# print(gen_two_dim_array(2, 2))
# print()
# print(gen_two_dim_array(3, 3))


# my_str = input('Determine number of letters and digits in your input value: ')
#
# num_of_letters = 0
# num_of_digits = 0
#
# for el in my_str:
#     if el.isalpha():
#         num_of_letters += 1
#     elif el.isdigit():
#         num_of_digits += 1
#
# print(f'The string "{my_str}" consists of {num_of_letters} letters and {num_of_digits} digits. ')


# def factorial(a = 0):
#     if a == 0:
#         return 1
#
#     return a * factorial(a - 1)
#
#
# print(factorial(5))


# def base_converter(num, init= 10,final = 10):
#     '''
#     :param str num: str
#     :param int init: int
#     :param int final: int
#     :return str:
#     Converts number from one base to another and returns a string. init: initial base of the
#     number passed or to be converted, default decimal. final: final base to be converted to,
#     default decimal.
#     '''
#
#     if not isinstance(num, str):
#         raise ValueError('Invalid data type. str is expected instead of int')
#
#     def num_to_dec(data):
#         '''
#         :param str data: str
#         :return int:
#         Converts num from initial base to decimal
#         '''
#         if init == 10:
#             return int(data)
#
#         exp = len(data) - 1
#         ans = 0
#
#         for el in data:
#             if el.isalpha():
#                 el = dec_to_alpha(el)
#             ans += int(el) * (init ** exp)
#             exp -= 1
#
#         return ans
#
#     def dec_to_alpha(num):
#         dec_list = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
#         if type(num) is int or num.isdigit():
#             return dec_list[num] if num in dec_list else str(num)
#         else:
#             for i in dec_list:
#                 if num == dec_list[i]:
#                     return i
#
#     def dec_to_final(num):
#         '''
#         :param int num: int
#         :return str:
#         Converts from dec to final base
#         '''
#         if final == 10:
#             return num
#
#         # If the final base is not decimal
#         if final > num:
#             return dec_to_alpha(num)
#         return f'{dec_to_alpha(num % final)}{dec_to_final(num // final)}'
#
#     def data_exist(new_dec):
#         if not base_converter.storage:
#             return False
#
#         for data in base_converter.storage:
#             if data['dec'] == new_dec and data['final'] == final:
#                 print(f'Answer exist already: {data["ans"]}')
#                 return True
#
#     # Check for valid data
#     max_num = max_sum([int(dec_to_alpha(i)) for i in num])
#     if max_num >= init:
#         raise ValueError('Invalid data!!!')
#
#     # Converts the from initial base to decimal
#     dec = num_to_dec(num)
#
#     # Checking if answer exist already or not
#     if data_exist(dec):
#         return 'Done!!!'
#     else:
#         final_base = dec_to_final(dec)
#         refined_ans = final_base
#
#         if type(refined_ans) is int:
#             refined_ans = str(refined_ans)
#         else:
#             refined_ans = refined_ans[-1::-1]
#
#         base_converter.storage.append({'dec': dec, 'final': final, 'ans': refined_ans})
#         return refined_ans


# Memoization
# base_converter.storage = []

# print(base_converter('10a', 16, 10))
# print(base_converter('aa', 16, 2))
# print(base_converter('101', 2, 10))
# print(base_converter('aa', 16, 2))
#
# print(base_converter('301', 5, 2))
# print(base_converter('1111100011', 2, 10))
# print(base_converter('10a', 16, 10))
# print(base_converter('aa', 16, 2))
#
# print(base_converter.storage)

# user_input = input('Enter number from range 1 - 10: ')
# print(f'Your number is {user_input}' if int(user_input) in range(1, 10) else 'Invalid input!')


# ---------------The time converter

def time_converter(user_time):
    user_time_hr = user_time[:user_time.l_index(':')]
    user_time_hr_int = int(user_time_hr)

    unit = user_time[-2:]
    if unit.isalpha():
        unit = unit.lower()
        user_time = user_time[:-2]

    # =========> Implementation
    new_unit = ''

    # 1. For "AM"
    if (0 <= user_time_hr_int < 12 and unit.isdigit()) or \
        (0 < user_time_hr_int <= 12 and unit == 'am'):

        # 24hrs to 12hrs init
        if user_time_hr_int == 0:
            user_time_hr_int = 12

        # 12hrs to 24hrs init
        elif user_time_hr_int == 12:
            user_time_hr_int = 0

        # Setting 12hrs unit
        if unit.isdigit():
            new_unit = 'AM'

    # 2. For "PM"

    elif (12 <= user_time_hr_int < 24 and unit.isdigit()) or \
        (0 < user_time_hr_int <= 12 and unit == 'pm'):

        # For "12noon"
        if user_time_hr_int == 12:
            if unit.isdigit():
                new_unit = 'PM'
        else:
            if user_time_hr_int > 12:
                user_time_hr_int -= 12
                new_unit = 'PM'
            else:
                user_time_hr_int += 12

    else:
        print('Oo bii')
        raise ValueError('Invalid input!!!')

    time = user_time.replace(user_time_hr, str(user_time_hr_int), 1)
    time += new_unit
    return time


print(time_converter(input('Convert time: ')))

my_name = 'lanx'

def do_stuff():
    pass









