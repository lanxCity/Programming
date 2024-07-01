# =========> Functional Programming
# Like OOP, It is all about separation of concerns; each part concerned itself with one thing
# that is good at.
# OOP involves dividing each part into chunk of classes in which each class encapsulate both its
# data and functionality. But Functional Programming focus on the idea of "pure function".
# Because there is no idea of "classes and object" but instead, functions operate on well-defined
# data structures like list, dict, etc. as data and functions are separated.

# Note:-
# 1. The function should only perform action on the input and produces resulted output; Given the
#    same input, same output must be returned.
# 2. The function should not have any side effect such as interacting with the outside scope(
#    variables or functions) or calling another function in such function.

# => Examples
# 1.
# def mult_increment(li):
#     return [i * 2 for i in li]
#
#
# print(mult_increment([2,34,5]))

# 2.
# # -> data
# user = {
#     'name': 'Lanx', 'power':50
# }
#
# # -> function
# def attack(player, qty = 0):
#     ply_pow = player['power']
#
#     if ply_pow:
#         if ply_pow > qty:
#             player['power'] -= qty
#         else:
#             player['power'] -= ply_pow
#
#         return f'{qty} power used.'
#     else:
#         return 'Out of power!'
#
#
# print(attack(user, 5))
# print(user)

# Some useful functions that allows one to think in a functional programming paradigm.
# And they are map(), filter(), zip() and reduce()

# a. Like JS (array.map(function)), map also returns a list with same size of input list.
# Note: A the map function must be wrapped with "list object" before returning a value

# From example 1,
# def mult_increment(el):
#     if el % 2 == 0:
#         return el * 2
#
#
# num = [2, 34, 5]
# print(list(map(mult_increment, num)))


# b. filter function
# More like modified "map" function as doesn't necessarily return list of same size as input but
# filters the unwanted values from the list.

# def even(el):
#     return el % 2 == 0
#
#
# print(list(filter(even, [1, 2, 3, 4])))


# c. The "zip function"
# This works more like a "zippers" where two or more lists are needed and zip them together
# in their index format in a tuple

# names = ['Sodiq', 'Kareemot', 'Abdulwaris']
# emails = ['sodiqramon0@gmail.com', 'kereemotmaruff@gmail.com',
#          'warisabdulramon2419@gmail.com']
#
# print(list(zip(names, emails)))


# d. Reduce function
# You import from "functool" and it returns an int by reducing iterable to in e.g. adding
# The default accumulator value is 0
# from functools import reduce
#
# m_list = [2,3,4,5]
#
#
# def add(accumulator, el):
#     return accumulator + el
#
#
# print(reduce(add, m_list))

# e. lambda expression
# This involves the use of anonymous function in python by using the keyword "lamda"
# from "filter" example,
# (lambda param: param % 2 == 0, [1, 2, 3, 4])

# def even(el):
#     return el % 2 == 0
#
#
my_list = [1, 2, 3, 4, None, True, False]

print(list(
    filter(lambda el: type(el) is int, my_list)
))
#
# # for reduce function
# from functools import reduce
#
#
# print(reduce(
#     lambda acc, el: acc + el,
#     filter(
#         lambda el: type(el) is int, my_list
#     )   # This return a list that reduce function can work with
# ))

# f. list, set, dict comprehension

# i. For "set" data type. It does not support indexing and scatters non_numeric data type in the
# set as you run the code.

# my_itr = {i for i in 'Lanx'}

# ii. For "list" data type.

# my_itr = [i for i in 'Lanx']

# iii. For "dict" data type.
# name_list = ['sodiq', 'kareemot', 'abdulwaris', 'ridwan', 'abdulrasheed']
#
# data = {index + 1: name for index, name in enumerate(name_list)}
#
# print(data)










