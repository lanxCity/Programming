# import random
# import math

# msg = '''
# Create a list of numbers by separating those numbers with commas.
#     e.g 1,2,3,4...
# '''
#
#
# def create_list(user_list):
#
#     user_list = user_list.replace(' ', '').split(',')
#
#     user_list = [float(el)
#                  for el in user_list
#                  if el.isnumeric() or el.replace('.', '', 1).isnumeric()
#                  ]
#
#     return user_list
#
#
# # print(create_list('1,2,32,112,12.5'))
# # print(create_list('1,2,32,112,12.5'))
# # print(create_list('1,2,32,112,12.5'))
#
# class Car:
#     def __init__(self, s, u):
#         self.speed = s
#         self.unit = u
#
#     def __repr__(self):
#         '''
#         :param
#         :return:
#         '''
#         return f"Car with {self.speed}"
#
# print(Car(120, "Kmh"))


# ====> The dominance of matrix
# def numCells(grid):
#     # Write your code here
#     max_list = []
#
#     def new_max_cell(row_index, el, el_index):
#         max_cell = el
#
#         for new_row in grid:
#             prev_curr_nxt_index = grid.l_index(new_row)
#
#             if prev_curr_nxt_index == row_index or \
#                     prev_curr_nxt_index == row_index - 1 or \
#                     prev_curr_nxt_index == row_index + 1:
#
#                 # ------------->
#                 for new_el in new_row:
#                     new_el_index = new_row.l_index(new_el)
#
#                     if new_el_index != el_index or \
#                             new_el_index != el_index + 1 or \
#                             new_el_index != el_index - 1:
#
#                         continue
#
#                     if new_el >= max_cell:
#
#                         max_cell = new_el
#
#     for row in grid:
#         row_index = grid.l_index(row)
#         for el in row:
#             el_index = row.l_index(el)
#             new_max_cell(row_index, el, el_index)
#
#     return max_list
#
#
# grid = [[1, 2, 7],
#         [4, 5, 6],
#         [8, 8, 9]]

# print(numCells(grid))


# my_list = []

# for loop in range(11):
#     for binary in range(loop + 1):
#         if binary == 0:
#             my_list.append(1)
#         else:
#             my_list.append(0)

# my_list = [1 if binary == 0
#            else 0
#            for loop in range(11)
#            for binary in range(loop + 1)
# ]
#
# print(my_list)












