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

is_odd = lambda n: True if n % 2 else False
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

def mul_9(n):
    return n % 9 == 0

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
            if len(matrix) != 1:
                bottom_row = matrix[i + 1]
            is_dominant = dominant(el, j, top_row, curr_row, bottom_row)
        else:
            top_row = matrix[i - 1]
            is_dominant = dominant(el, j, top_row, curr_row, bottom_row)

        if is_dominant:
            dominant_list.append(matrix[i][j])

print(dominant_list)


new_list = [i for i in range(10)]

print(new_list)

del new_list[len(new_list) - 1]
print(new_list)

print(not True)

# ---> Bitwise operator
# 1. Bitwise AND operator
print(5 & 4)    # -> 0101 & 0100 = 0100 == 4

# 2. Bitwise OR operator
print(5 | 4)    # -> 0101 & 0100 = 0101 == 5

# 3. Bitwise XOR  operator - Xclusive OR returns True where the operands are different
print(5 ^ 4)    # -> 0101 ^ 0100 = 0001 == 1

# 4. Bitwise NOT  operator
# first, let's store negative number in memory using value "-6"
# It has to be converted to positive int using 2's compliment,
# 2's = 1's + 1
# 1's compliment is by reversing the binary digits
# ----------------------------------
# To store -6, we have ->  bin(6) = 0110
# 1's compliment -> 6 == 1001
# 2's compliment -> 1001 + 1 = 1010 == 10 (in dec)

print(~5)  # -6

# Therefore, ~5 = ~(0101) = 1010 == 10 (in dec) == 2's of "-6"
# In summary, ~n = -(n + 1)

# 5. Bitwise left-shift operator
# This shifts the number to the left by adding xtra digits or bits to the right
# NB: We gain more bits
# therefore, n * (x^x)
n = 5
x = 2
print(n << x)  # 5 == 0101 == 10100 == 20
n = 10
print(n << x)  # 10 == 1010 == 101000 == 40

# 5. Bitwise right-shift operator
# This shifts the number to the left by adding xtra digits to the right
# NB: We lose bits
# therefore, n // (2^x)
n = 5
print(n >> x)  # 5 == 0101 == 001
n = 10
print(n >> x)  # 10 == 1010 == 0010 == 2


# ------> Identity operators ("is" and "is not")
# These are used to compare objects in that;
# a. if both objs are the same or not
# b. share the same memory location
a, b = 5, 5
print(a is b)

a, b = 'lanx', 'lanx'
print(a is b)

print(f'id of a: {id(a)}', f'id of b: {id(b)}')

a, b = 1001, 1001
print(a is b)

print(f'id of a: {id(a)}', f'id of b: {id(b)}')


# It doesn't works for dynamic allocation of memory, especially if it is not a character (ASCII) values
str1 = input("Enter str1: ")
str2 = input("Enter str2: ")

print(str1 is str2)
print(str1 is 'a')  # False if the input is 'a'
print(str1 is '5')  # True if the input is 5
# Implementation-specific behavior:
# Different Python implementations (e.g., CPython, PyPy, Jython) may handle string interning
# and integer caching differently. For example, while CPython (the standard Python implementation)
# extensively uses string interning and integer caching, other implementations might not employ these
# optimizations to the same extent or at all.
#
# May not always occur:
# Even in CPython, the behavior of string interning and integer caching can be influenced by various
# factors such as optimization settings, Python version, and runtime conditions. For instance,
# interning might not occur for dynamically created strings or integers outside the cached range.
# Similarly, in some scenarios, Python may choose not to cache integers for memory reasons.


# str1 = int(input("Enter str1: "))
# str2 = int(input("Enter str2: "))
# print(str1 is str2)  # True for int

# Checking the memory address of an object
str1 = input("Enter str1: ")
str2 = input("Enter str2: ")

print(str1 is 5)
print(f'str1 id: {id(str1)}', f'str2 id: {id(str2)}')
'''

# round() function
# Nearest integer and nearest even integer is applicable for time break
print(round(26.98654))
print(round(26.98654, 2))
print(round(26.98654, -1))
print(round(2.5))
print(round(2.51))
print(round(6.5))
print(round(6.51))
print(round(467, -3))
print(round(567, -3))



































