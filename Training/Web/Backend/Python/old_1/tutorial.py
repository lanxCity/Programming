# # def list_avr(data):
# #     total = 0
# #
# #     for el in data:
# #         total += el
# #
# #     avr = total/len(data)
# #
# #     return avr
# #
# #
# # list_1 = [23,4,2,1,2,3,11,12]
# #
# # print(list_avr(list_1))
#
#
#
#
#
#
#
#
# list_1 = [23,4,2,1,3,1,123]
# list_2 = [1,2,2,3,2,2,2,1]
# list_3 = [2,3,2,3,23,3,3,34,3,43,43,43,4,3,43]
#
#
# def list_sum(any_list):
#     total = 0
#
#     for el in any_list:
#         total += el
#
#     avr = total / len(list_1)
#
#     print(avr)
#
# list_sum(list_1)
# list_sum(list_2)
# list_sum(list_3)


# import random

# list_1 = ['lanx','sodiq','me']
# list_2 = []
#
# print(random.choice(list_2))

# my_list = [i for i in range(35, 101, 5)]
#
#
# print(my_list)


# players = [
#     {
#         'name': 'lanx',
#         'age': 35
#     },
#     {
#         'name': 'sodiq',
#         'age': 45
#     },
#     {
#         'name': 'me',
#         'age': 55
#     }
# ]
#
# msg = "Welcome to ETIHAD Pitch"
#
# def greetings():
#     for profile in players:
#         print(f'{msg} {profile["name"]}')
import math
from random import random

user_not_correct = True

while user_not_correct:
    num_to_guess = math.floor((random() * 9) + 1)
    user_input = input('Guess any number from 1 - 9: ')

    if user_input.isdigit():
        if int(user_input) == num_to_guess:
            user_not_correct = False
            print('You are a genius!')
            continue

    print('Invalid input!')














