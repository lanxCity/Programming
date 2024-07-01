# ------------------------The data types.

# 1. FUNDAMENTAL DATA TYPE
# int,float,bool,str,list,tuple,set,dict,complex.
from pyflakes.scripts import pyflakes

complexNum = 3 + 4j

print(type(complexNum))

# 2. CLASSEs -> a custom type of data; a data type that's
# created manually.

# 3. specialized data type: data type that are non-built-in
# or customised but special packages or modules that can be used
# from libraries.

# 4. NONE.

# name = None

# print(type(name))

# --------------Introduction to "int" and "float"
# print(2//3) #print the "int" of the ans or round down
# print(2**5) #print 2^5


# -------------Use of "Math" function

# print(round(3.5))
# print(abs(43-53))

# print(complex(13, 45)*3)

# print('From binary of ', bin(34) + ' to decimal', + int(bin(34),2))
# print('From hex 54453 to decimal ', + int('54453',6))
#
# print(bin(34)) #converts "int" to "binary"

# ---------------naming variables: snake_case
# phone_number = 334233323

# 1. if a variable name is in uppercase, it means it's constant and
# that the variable shouldn't be re-assign to new value.
# Although, it can be overwritten but best practices means
# it shouldn't be changed when another programmer came across it.


# PI = 3.14

# 2. the use of "double underscores" called built-in "Dunder variables".
# Best practices is your naming convention shouldn't be like that as
# such method is one of built-in functions naming methods. just as follows;

# __my_name = "Lanx"
# print(__my_name)

# 3. the use of shorthand

# a,b,c = 1,4,6
# print(a,b,c)

# -------------------Expression vs Statement
# 1. An expression is a piece of code that produces a value
# e.g. function expression. or the following

totalNum = 165
avrg = totalNum / 54

# In the above, "totalNum/54" is the expression
# on the other hand, the whole line of code that performs
# action, e.g. "avrg = totalNum/54", is called a statement.

# --------------------Introduction to string

# long_message = '''
# WOW
# 0 0
# ---
# Hello to you'''
#
# print(long_message)

# greetings = 'Engr. Lanx. Bawo\
#  ni? Se aje n wa? \
#  Beeni, adupe sir.'
#
# print(greetings)

# name = "sodiq"
# age = 45
#
# message_1 = 'Hi ' + name + '. You are ' + str(age) + ' years old.'
# print(message_1)
#
# message_2 = name, age, message_1
# print(message_2)

# A. Escape sequence or masking: the use of "\" within a string.

# message = 'Hello! I\'m a \'great\' programmer.'
#
# print(message)

# 1. "\" is also used to add "tab" and "newline" to a string

# print('This following below has a "tab" behind...\n' +
#       "\t" + message)

# B. Formatting string

# print(f'The binary number "{bin(5)}" returns the integer '
#       f'{int(bin(5), 2)}')
#
# print(f'The binary number "10100" returns the integer '
#       f'{int("10100", 2)}')

# username = "sodiq"
# matric_number = 200268

# the following was introduced in "python 3"

# print(f'''Hi contestant {first_name} with matric number \
# {matric_number}!
# You have be awarded 2 years scholarship program
# at Harvard University.''')

# # while the following was introduced in "python 2" but
# # also works for "python 3"
#

# # we can also turn the l_index of the "{}" around
#
# print('''\n------------------------For python 2
# And changing the indexing\n''')
#
# print('''Hi contestant {1}, with matric number {0}!
# You have be awarded 2 years scholarship program at
# Harvard University.'''.format(first_name, matric_number))

# print('''Hi contestant {new_username}, \
# with matric number {new_matric_number}!
# You have be awarded 2 years scholarship program at
# Harvard University.'''.format(new_username='Abdulrasheed',
#                                 new_matric_number=200265))

# C. String indexing

natural_numbers = '123456789'

# i. accessing the string; like an array or "slicing"
# print(natural_numbers[5])
#
# # ii. stringName[start:stop]

# print(natural_numbers[0:5])

# iii. stringName[start:stop:stepwise], default stepwise = 1.

# print(natural_numbers[0:9:2])

# iv. negative l_index: starts from the end
# print(natural_numbers[-1])
# print(natural_numbers[-3])
#
# print(natural_numbers[::-2]) # reverse of [0:10:-2]

# ------------------ Primitives are immutable

# natural_numbers[5] = 11  # unlike array, this is Not possible

# print(natural_numbers)


# -------------------------Built-in functions and methods

# ----Built-in functions are functions that are used to perform actions on data type e.g. print(
# ). And they
# just a word followed by "()"

# ----Built-in methods are similar to functions but owned by something or a certain data type.
# And they are usually attached to their respective data type e.g. string.format()

# A. string methods

# print(first_name.upper())
# print(first_name.isupper())
# print(first_name.islower())
# print(first_name.capitalize())
# print(len(first_name))
# print(first_name.find('do'))
# # returns the l_index of 1st letter of the searched words
# print(first_name.replace('diq','lanx'))


# ----------------------Booleans
# "0~False" and "1 ~ True"

# print("1 is " + str(bool(1)))
# print("0 is " + str(bool(0)))


# -----------------------------Exercises-----------------------#

# Exercise Takeaway:
# a. "print(5 * 'm')" returns m^5

# -----------------------------------------The Data Strutures
# 1. Structure-----------------------Lists------------------------

# shopping_cart = [
#     'Bread',
#     'Textbook',
#     'Youghurt',
#     'Butter'
# ]

# Just like "string", "list" can be accessed using "[::]"

# print(shopping_cart[::-1])

# A.------------- List can be manipulated and are mutable

# shopping_cart[4] = 'adigun' #-------can't add new item like this (unlike JavaScript)

# i. the following is pointing directly to the original list so that any alteration in "new_cart"
# affect the original.
# So it's diff from copying

# new_cart_1 = shopping_cart
#
# new_cart_1[2] = 10
#
# print(f'Pointing directly to the original: {shopping_cart}')

# ii. To make copy of the original List, we have

# new_cart_2 = shopping_cart[:]            # the use of [:] make the copy of the original list
#
# new_cart_2[2] = 4576
#
# print(f'Making copy:  {new_cart_2}')
#
# # Original copy after copy
# print(f'Original LIST after copied: {shopping_cart}')

# B. ------------------------ Matrix-----------------------------
# This is a 2D or multidimensional list
#
# matrix = [
#     [1,2,3],
#     [3,4,5],
#     [7,2,5]
# ]
#
# print(matrix[::2])
#
# matrix[2][1] = 52   #changing column 2 of the row 3
#
# print(matrix[2])

# C. ------------------- The "LIST methods"
# Ordered collection of data
# 1.----------------------------------------Adding-------------#
# append(), insert(), extend() etc.

# numbers = [1,2,10,35,50,3,3,2,1,3,4,5,6,7,'Sodiq',8,10,11,9]

# new_numbers = numbers.append()   #only append the original list but returns "None" to new
# assignment
#
# numbers.append(10)   #a.-------------------add ONLY a new item to list end
#
# print(f'The original: {numbers}')
# print(f'The reassigning variable: {new_numbers}')


# numbers.insert(4,10)  #b.-------add new item to a list at any position (or l_index) e.g.
# list.insert(l_index,new_item)

# numbers.extend([13,26,18])   #c. ------- takes new iteration or
# list of values to add to the existing one "([])"

# 2.--------------------------------Removing------------------#
# pop(),remove(),clear()

# numbers.pop()   #a.--------------------removes item at the end 0f the list.

# new_number_1 = numbers.pop(4)  # romoves item at l_index 4
# new_number_2 = numbers.pop(5)
# new_number_3 = numbers.pop(6)
# new_number_4 = numbers.pop(2)
#
# print(new_number_1)
# print(new_number_2)
# print(new_number_3)
# print(new_number_4)

# b.---------------- remove(): removes that particular value given as the method argument

# numbers.remove('Sodiq')

# c.--------------- clear(): it clear the list entirely.

# numbers.clear()
# print(f'The original: {numbers}')

# 3.------------------------Searching And manipulating-------------------

# a.------ l_index()   # returns error if the element is not found

# l_index(value, start, stop)
# print(f'''The item "Sodiq" is at l_index {numbers.l_index('Sodiq',0,9)}''')

# returns the l_index of item "9"
# print(f'''The item "9" is at l_index {numbers.l_index(9)}''')
#
# # b.----- "in" keyword
#
# print("Sodiq" in numbers)
#
# # c. ------ count()
# print(numbers.count(10))  # ------returns the number of occurence of a value in a list
#
# # d. ------ sort()
# new_numbers = [1,2,10,35,50,3,3,2,1,3,4,5,6,7,8,10,11,9]
#
# new_numbers.sort()
#
# print(new_numbers)

# 1. Sort() method vs built-in "sorted()"

# numbers = [2, 1, 16, 34, 11, 7, 10, 88, 100, 20]

# sorted() built-in function
# print(sorted(numbers), '\n')
# print(f'After "sorted()" built-in func, the new list is: {numbers} \n')
#
# # sort() method
# numbers.sort()
# print(f'After "sort()" method, the new list is: {numbers}')

# 2. copy() method instead of list[:]


# 3. reverse() method

# numbers.sort()
# print(f'After "sort()" method, the new list is: {numbers}')
#
# numbers.reverse()
#
# print(numbers, '\n')
#
# #------------Common list pattern
#
# # a. Use of slicing method "[:]", But only makes copy
#
# print(numbers[::-1], '\n')
# print(numbers)

# b. The use of "range"

# my_new_list = list(range(1,50))
# my_new_list_2 = list(range(50))  # "start" default is 0

# print(my_new_list,'\n')
# print(my_new_list_2)

# c. "join(list)" and "separator" must come before

# names = ['sodiq', 'ojo', 'rasheed', 'mariam', 'Abdullah']

# names_joined = ', '.join(names)
# print(names_joined)
#
# names_resplit = names_joined.split(', ')
# print(names_resplit)

# d. List unpacking

# assign each item in a list to variables

# a,b,c,*others,d = [1,2,3,4,5,6,11,23,12,55]
#
# print(a)
# print(b)
# print(c)
# print(others)
# print(d)

# first_list = [1,2,3,4]
# second_list = [first_list,5,6,7,8,9,10]
#
# print(second_list)

# ------------------------------------"None" data type ("undefined" or
# "null"in JS)

# name = None
# print(type(name))

# 2. Structure-----------------------------------------Dictionaries or "dict"
# Unordered collection of data

# profile = {
#     'my_name': 'Sodiq',
#     'age': 45,
#     'contact': '+2348146257816'
# }
# #
# # print(f'''My name is {profile['my_name'].capitalize()}. I'm {profile['age']}\
# #  years of age.\n''')
# #
# # profile['is_a_student'] = True
# # print(profile)
#
# # Another way of creating dictionary is using "dict" constructor
#
# # new_dict = dict(website='Lanxcity.org.ng')
# #
# # new_dict['name'] = 'Lanx'
# # new_dict['Alma mata'] = 'University of Ibadan'
# #
# # print(new_dict)
#
# N.B. Dict keys must be immutable; list cannot be a key since it's mutable
# # a. Dictionary methods
#
# # i. the "get(keyToCheck,fallBackValue)" method
# # this is used to search if a "key" is present in an object.
# # And if not, then the fallBackValue is used.
#
# # print(profile.get('is_marrried',False))
# # print("\n")
# # print(profile)
#
# # ii. the use of "in"
#
# # print('age' in profile)
#
# # iii. 'keys()', 'values()', 'item()', 'clear()', 'pop()', 'clear()'
# # 'pop()', 'popitem()','update()'.
#
# print(profile.keys())
# # print('siblings' in profile.keys())
#
# print(profile.values())
# # print(45 in profile.values())
#
# print(profile.items())  # the outcome is like list item (Tuple)

# print(profile.clear())
# print('--------------------', profile)

# print(profile.pop('age'))
#
# Be careful with 'popitem' method as keys are unordered, and this method removes
# some keys-values (and not necessarily have to be last one); it is useful to destructive
# iterate over a dictionary.
# print(profile.popitem())

# print(profile)
# print(len(profile))

# The 'update({})' method

# you give it a new dictionary '{}' to update the initial
# it's meant to update the value of an existing key. but if the key doesn't
# exist in the "dict", it creates new one

# print(profile.update({'name': 'Abdulrasheed'}))
# print(profile.update({'my_name': 'OLaide'}))
# print(profile)

# 3. Structure--------------------------------------------Tuples
# Tuple is "List-like" but can not be modified like a list (Immutable list)
#
# my_tuple = ('sodiq','rasheedah','abdulwaris','rasheed','ajoke','sodiq','rasheed')
#
# print(type(my_tuple))
# print('sodiq' in my_tuple)
# print(my_tuple[3])

# N.B. Tuple, unlike list, can be a key name in dict
# new_profiles = {
#
#     ('name_1','name_2','name_3'): ('Abdulrasheed','sodiq','kareemot'),
#     'occupation':'student',
# }
#
# print(new_profiles.update({('name_1','name_2','name_3'):('sodiq')}))
# print(new_profiles[('name_1','name_2','name_3')])

# new_tuple = (2,3,1,1,4,2,5)
# print(sorted(new_tuple))

# ------------Tuple methods
# --- "count()" and "l_index()"

# print(my_tuple.count('resheed'))
# print(my_tuple.l_index('resheed'))


# 4. Structure----------------------------------The "Set" data type
# Unordered collection of "unique" object; no repetition of a value as it won't allow that.
# Just like "dictionary", "set" doesn't support indexing
# most of "list" methods also works in set

# my_set = {10,2,3,4,5,5,4,2,1,8,6}
# print(my_set)
# # print(my_set[3])   #Error: set does not support indexing; they aren't stored nxt to one another
#
# # print(my_set)
#
# my_list = list(my_set)
# print(my_list)

# --------------Some other "set" methods
#
# first_set = {1,2,3,4,5}
# second_set = {1,3,4,4,9,6,7,10}

# a. difference(): returns uncommon elements between two set;
# print(first_set.difference(second_set))

# b. discard(): removes certain element parsed from the set
# first_set.discard(3)
# print(first_set)

# c. difference_update(): removes all the common values between two set and update the
# referer one to a disjoint set
# first_set.difference_update(second_set)
# print(first_set)

# d. intersection() or the use of "&"
# print('Using "intersection" method:', first_set.intersection(second_set))
# print('Using shorthand "&" method:', first_set & second_set)
#
#
# # e. isdisjoint(): returns "true" of "
# print(first_set.isdisjoint(second_set))
#
# # f. union() or "|"
# print('Using "union" method:', first_set.union(second_set))
# print('Using shorthand "|" method:', first_set | second_set)

# g. issubset()
# print(first_set.issubset(second_set))
#
# # h. issuperset()
# print(second_set.issuperset(first_set))

# name = {
#     'me': 'sodiq',
#     'mat_num': 200268
# }
#
# matric_number = 200268
#
# if 200268 in name['mat_num']:
#     print('Hello world')

# sorted_list = list(set([2,1,4,4,5,2,1,2,4,53,2,3]))
# # sorted_list.sort()
# #
# print(sorted_list)

# container = ((('orange,') * 16).split(","))
# container.remove("")
#
# a,b,c,d = container[:4], container[4:8], container[8:12], container[12:16]
#
# print(container)
#
# print("a: ", a)
# print("b: ", b)
# print("c: ", c)
# print("d: ", d)


# person = {
#     "name": 'Sodiq',
#     "age": 25,
#     "gender": "Male"
# }
#
# for i in person:
#     print(person[i])

# def do_stuff(num):
#     if num == 0:
#         print('Adigun is 0')
#         return
#
#     print('Mr. Sodiq')
#     print('Mr. Sodiq')
#     print('Mr. Sodiq')
#     print('Mr. Sodiq')
#     print('Mr. Sodiq')
#     print('Mr. Sodiq')
#
# do_stuff(0)

# import random
#
# my_list = [
#     'mike', 'socks', 'pen', 'biro', 'paper',
#     'book', 'bag', 'laptop', 'system', 'battery'
# ]
#
# choice = ''
#
# while True:
#
#     rand_index = random.randint(0, len(my_list) - 1)
#     choice = my_list[rand_index]
#
#     counter = 0
#     is_valid = False
#
#     for i in choice:
#         counter += 1
#         num_of_occur = choice.count(i)
#         if num_of_occur > 1:
#             break
#         elif num_of_occur == 1 and counter == len(choice):
#             is_valid = True
#
#     if is_valid:
#         break
#
# print(choice)

import random
import math

list_item = [
    'Japan', 'Canada', 'Hungary', 'Sweden', 'Lybia',
    'Ethiopia', 'Cuba', 'Brazil', 'Mexico', 'Australia'
]
list_item = [item.upper() for item in list_item]

rand_num = math.floor(random.random() * (len(list_item)))
comp_choice = list_item[rand_num]
comp_choice_gaps = ['-' for i in range(len(comp_choice))]

wrng_guess_limit = 5
limit_exceeded = False

msg = '''
Welcome to lanxCity. In this game, the computer would choose
a country and would start guessing letters that might be present in that 
country's name.

NOTE:- 
=> A letter must be entered at a time. 
=> if wrong letter is entered five(5) times, then you loose. 
=> As you keep guessing each letter, if a letter is guessed right,
   it would be filled in its positions and start building up 
   to form the country's name e.g. if letter "i" is guessed 
   while the country's name is "Nigeria", then letter "i" gaps 
   would be filled as, "-i---i-".

                    Good luck!!!
'''

print(msg)
print()

while not limit_exceeded:
    guessed_word = input('Guess a letter that exist in the country\'s name: ').replace(' ', '')

    if len(guessed_word) == 1:
        if guessed_word.isalpha():
            if guessed_word in comp_choice:
                pass


    print('{:^20s}'.format('Invalid! A letter is required at a time.'))
