# # 1. --------------------------Conditional logic---------------------
# name = input('Your name please? ').capitalize()
# birth_year = input(f'Welcome {name}! Please enter your birth year? ')
# age = None
# is_licensed = input('Do you have the driving license? ("Yes" or "No") ').capitalize()
#
# #--------Setting conditions
#
# if birth_year:
#     age = 2022 - int(birth_year)
#
#     if age >= 18 and is_licensed == 'Yes':
#         print(f"Hello {name}! Let's have a drive.")
#
#     elif age < 18 and is_licensed == 'Yes':
#         print(f"Hi kid! Let's have a drive but we need to go gently.")
#
#     elif age >= 18 and is_licensed == 'No':
#         print(f"Hello {name}! It's a pity you do have a driving license.")
#
#     else:
#         print(f'Sorry {name}, you are still young to drive with me...')
#
# else:
#     print("Sorry, you entered no value as your birth year.")


# -------a. "Truthy" and "Falsy"
# Truthy values: if it's not an "" (empty val) or 0 (zero) for numbers, etc.
# And you convert them to "bool"
# is_good = bool('yes of course')
# is_a_boy = bool(56)
#
# print(is_good)
# print(is_a_boy)   #they both return "True"
#
# # Falsy values: "",0,{},[],(),None,0j,b''(empty bytes)
# his_score = bool(0)
# his_name = bool('')
#
# print(his_score)
# print(his_name)


#---------b. Ternary Operator

# in JS, "Level = (point === 10 ? 'You are king': 'You are still young'); "
# In python, "level = ('You are the king' if point = 10 else 'You are still you')"

# point = int(input('Enter any value from 0 - 10? '))
# level = None

# # Assigning the return value to variable
# level = 'You are the king' if point == 10 else 'You are still young'
#
# # Setting conditions
# print(level)

# ----------c. Short circuiting: "and" and "or"

# if name and point == 10:
#     print(f'Great {name}! You are the king')
# elif not name and point == 10:
#     print('Hello "No name"! You are the king')
# elif name and point < 10:
#     print(f'Hi {name}! You are still a kid')
# else:
#     print('Hello "No name"! You aren\'t welcome here.')

#-----------------------------------Comparation---------------------

# a.------------------alphabetical order:- like "1 < 5"
# print('banana' < 'zebra')  #True
# print('banana' < 'apple')  #False

# b.------------------upper and lower:- lowercase  > uppercase
# print('zebra' > 'Apple')  #True
# print('Zebra' < 'Apple')  #False

# c.----------------- Letters and numbers:- uncomparable
# d. ----------------- "is" and "=="
# Using "is" with mutable objects returns "False" as they exist in diff memory under the hood
# While "==" only cares about values of comparing objects.

# 2.------------------------------------------- The "for" loop
# A variable that allows looping or iteration is called an "iterable"
# N.B. Noticed any variables created in the loop is accessible from outside
profile = {
    'name': 'Sodiq',
    'age': 45,
    'gender': 'male'
}

# print(profile.items())

# for item in profile:
#     print(f'{item}: {profile[item]}')    #-----------key:value

# for item in profile.items():
#     print(item)

# for key,value in profile.items():   # value unpacked from tuple
#     print(f'{key}: {value}')

# print(key)  # NOTE THIS: How come a block scope variable can be accesed from outside

# for item in profile.keys():
#     print(item)

# for item in profile.values():
#     print(item)

# --------------------------------------Iterable
# An object that can be iterated, unlike primitive "number"

# ---------------------------------The "range()" function
# a. useful in looping with "_"
# for _ in range(1, 11):
#
#     # the underscore "_" is a variable too, just like "item". But variable that is not really
#     # useful but just for iteration purposes is named with "_"
#     print(_)
#
# print('Done')

# b.  ascending and descending order
# for _ in range(10,1,-2): # (10,1,1) won't work
#
#     # Range only has (start,stop,stepwise)
#     print(_)

# print(len(range(1, 10)))

# ------------------------------enumerate()
# Just like range(), this is also used like range() but slightly different.
# And not widely used.
# It returns tuple form of each "value" and its "the l_index" e.g. (3,q)

# for i in enumerate('sodiq'):
#     print(i)
# print('Done')
# print(type(i))

# unpacking the above, we have
# for l_index, value in enumerate('sodiq'):
#     print(l_index,value)

# print('Done')
# print(type(i))

# 3.----------------------------------The "while" loop
# l_index = 0
# while l_index < 50:
#     print('l_index', l_index)
#     l_index += 1
# else:
#     print('I am done sir.')
#

# my_list = [2,3,4,5,6]
#
# for item in [1,2,3]:
#     print(item)
# else:
#     print('Done with the first list boss')
#
# # Using the "while" loop
# i = len(my_list)-1
# while i >= 0:
#     print(my_list[i])
#     i -= 1
# else:
#     print('Done')

# 4.-------------------------------"break", "continue", "pass"
# The use of "pass" in a loop serves as a placeholder in the loop
# when nothing done (no codes) inside the loop. And there won't be any error
# because of absence code within the loop.
#
# for item in my_list:
#     # No code yet
#     pass
#
# # The following codes run
# print('Hi Sodiq')





















