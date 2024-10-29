# # import math
# #
# # def cosine_taylor(x, terms=10):
# #     result = 1.0
# #     sign = -1.0
# #     power = 2
# #
# #     x = (x * math.pi) / 180
# #     print(math.pi)
# #
# #     for i in range(1, terms):
# #         term = (sign * (x ** power)) / math.factorial(power)
# #         result += term
# #         sign *= -1
# #         power += 2
# #
# #     return result
# #
# # # Example usage:
# # x = float(input("Enter the value of x: "))  # Replace with your desired value
# # approximation = cosine_taylor(x)
# # print(f"Approximate cosine({x}): {approximation}")
#
#
#
#
#
#
#
# my_name = 'Lanx'
#
# my_customers = ['Faith','Ife','Adigun']
#
# print(my_name)
#
# for name in my_customers:
#     print(name)
#
#name = input("Enter your name: ")
#me = "Hey Aunty! there"

#print(me.index("there"))


# Anonymous Functions

# lambda arg1, arg2, ...: expression
'''
add = lambda x, y: x + y
print(add(5, 2))

is_odd = lambda num: True if num % 2 else False
print(is_odd(25))

my_list = lambda max_range: [i * 2 for i in range(max_range)]

print(my_list(5))

print_stuff = lambda: print("Heeeeeeeey there!")
print_stuff()


import random

head_tail = [random.choice(['H', 'T']) for _ in range(100)]

print("Heads : {:d}".format(head_tail.count('H')))
print("Tails : {:d}".format(head_tail.count('T')))


# Map Function - It allows us to execute a function on a list
l1 = list(range(10))
l2 = list(range(10, 0, -2))
print(l1, l2)
print(list(map((lambda x: x * 2), l1)))
print(list(map((lambda x, y: x + y), l1, l2)))


# Fiter -> Select items from a list based on a function
print(list(filter((lambda x: x % 2 == 0), range(15))))

import random

def mul_9(num):
    return num % 9 == 0

my_list = list(random.randint(1, 1000) for _ in range(100))

print(list(filter(mul_9, my_list)))


# Reduce -> Takes a list and returns a single value based on the function passed
# it is a function of a library, functools
from functools import reduce
print(reduce((lambda x, y: x + y), range(10)))



user = {
    'name': 'Mariam',
    'age': 13,
}

# Dominant Cell in matrix

matrix = [
    [1, 2, 7, 0],
    [4, 5, 1, 4],
    [8, 4, 12, 7],
    [9, 1, 5, 5],
]


def dominant(el, col_idx, *top_bottom):
    for i in range(len(top_bottom)):
        for j in range(len(top_bottom[i])):
            if i == 1 and j == col_idx:
                continue

            if (
                    (j == 0 and (j == col_idx or j + 1 == col_idx)) or
                    j == col_idx - 1 or
                    j == col_idx or
                    j == col_idx + 1
            ) and top_bottom[i][j] >= el:
                return False
    return True


is_dominant = False
dominant_list = []

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        el = matrix[i][j]
        top_row = []
        curr_row = matrix[i]
        bottom_row = []

        if i != 0 and i != len(matrix) - 1:
            top_row = matrix[i - 1]
            bottom_row = matrix[i + 1]
            is_dominant = dominant(el, j, top_row, curr_row, bottom_row)
        elif i == 0:
            if len(matrix[i]) != 1 and matrix[i + 1]:
                bottom_row = matrix[i + 1]
            is_dominant = dominant(el, j, top_row, curr_row, bottom_row)
        else:
            top_row = matrix[i - 1]
            is_dominant = dominant(el, j, top_row, curr_row, bottom_row)

        if is_dominant:
            dominant_list.append(matrix[i][j])

print(dominant_list)

#--------------------> ASCII values
print(chr(76))  # returns character
print(ord('a'))  # returns integer

new = []
#new = new + 'a'  # Error
new += 'a'  # No error

print(new)

print(len('\n'))
'''


class Do_stuff:
    def __init__(self, data):
        self.__data = data

    def __repr__(self):
        return '{:.2f}'.format(self.__data)

    @staticmethod
    def me():
        pass


stuff = Do_stuff(50)
print(stuff)

li = ['2', '100', '1', '56', '-12', '0', '-10']
li2 = [2, 100, 1, 56, -12, 0, -10]
li.sort()
print(li)
li2.sort()
print(li2)



