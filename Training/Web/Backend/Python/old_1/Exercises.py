import math
import random

# ==> Ex.1  Unit Converter
# def unit_converter(length, init_unit, final_unit):
#     '''
#     :param str length: str
#     :param str init_unit: str
#     :param str final_unit: str
#     :return: str
#     '''
#
#     # The list of the available units
#     available_units = ['mm', 'cm', 'dm', 'm', 'km', 'inch', 'mile', 'yard']
#
#     # Partial conversion
#     mm_to_cm = .1
#     cm_to_dm = .1
#     dm_to_m = .1
#     m_to_km = 1 / 1000
#
#     mile_to_cm = 160934.4
#     inch_to_cm = 2.54
#     yard_to_cm = 91.44
#
#     conversion_data = {
#         'mm': {
#             'mm_to_cm':  mm_to_cm,
#             'mm_to_dm': (mm_to_cm ** 2),
#             'mm_to_m':  (mm_to_cm ** 3),
#             'mm_to_km': (mm_to_cm ** 6),
#             'mm_to_mile': 1 / (mile_to_cm * 10),
#             'mm_to_inch': 1 / (inch_to_cm * 10),
#             'mm_to_yard': 1 / (yard_to_cm * 10),
#         },
#
#         'cm': {
#             'cm_to_mm': 1 / mm_to_cm,
#             'cm_to_dm': cm_to_dm,
#             'cm_to_m': cm_to_dm ** 2,
#             'cm_to_km': cm_to_dm * 5,
#             'cm_to_mile': 1 / mile_to_cm,
#             'cm_to_inch': 1 / inch_to_cm,
#             'cm_to_yard': 1 / yard_to_cm,
#         },
#
#         'dm': {
#             'dm_to_mm': (1 / mm_to_cm) * 10,
#             'dm_to_cm': 1 / cm_to_dm,
#             'dm_to_m': dm_to_m,
#             'dm_to_km': dm_to_m * 4,
#             'dm_to_mile': 1 / (cm_to_dm * mile_to_cm),
#             'dm_to_inch': 1 / (cm_to_dm * inch_to_cm),
#             'dm_to_yard': 1 / (cm_to_dm * yard_to_cm),
#         },
#
#         'm': {
#             'm_to_mm': (1 / mm_to_cm) * 10 * 10,
#             'm_to_cm': (1 / cm_to_dm) * 10,
#             'm_to_dm': 1 / dm_to_m,
#             'm_to_km': m_to_km,
#             'm_to_mile': 1 / (cm_to_dm * mile_to_cm * .1),
#             'm_to_inch': 1 / (cm_to_dm * inch_to_cm * .1),
#             'm_to_yard': 1 / (cm_to_dm * yard_to_cm * .1)
#         },
#
#         'km': {
#             'km_to_mm': (1 / m_to_km) * (10 ** 3),
#             'km_to_cm': (1 / m_to_km) * (10 ** 2),
#             'km_to_dm': (1 / m_to_km) * (10 ** 1),
#             'km_to_m': (1 / m_to_km),
#             'km_to_mile': 1 / (m_to_km * mile_to_cm * .01),
#             'km_to_inch': 1 / (m_to_km * inch_to_cm * .01),
#             'km_to_yard': 1 / (m_to_km * yard_to_cm * .01)
#         },
#
#         'mile': {
#             'mile_to_mm': mile_to_cm * 10,
#             'mile_to_cm': mile_to_cm,
#             'mile_to_dm': mile_to_cm / 10,
#             'mile_to_m': mile_to_cm / 100,
#             'mile_to_km': mile_to_cm / (10 ** 5),
#             'mile_to_inch': mile_to_cm / inch_to_cm,
#             'mile_to_yard': mile_to_cm / yard_to_cm,
#         },
#
#         'inch': {
#             'inch_to_mm': inch_to_cm * 10,
#             'inch_to_cm': inch_to_cm,
#             'inch_to_dm': inch_to_cm / 10,
#             'inch_to_m': inch_to_cm / 100,
#             'inch_to_km': inch_to_cm / (10 ** 5),
#             'inch_to_mile': inch_to_cm / mile_to_cm,
#             'inch_to_yard': inch_to_cm / yard_to_cm,
#         },
#
#         'yard': {
#             'yard_to_mm': yard_to_cm * 10,
#             'yard_to_cm': yard_to_cm,
#             'yard_to_dm': yard_to_cm / 10,
#             'yard_to_m': yard_to_cm / 100,
#             'yard_to_km': yard_to_cm / (10 ** 5),
#             'yard_to_mile': yard_to_cm / mile_to_cm,
#             'yard_to_inch': yard_to_cm / inch_to_cm,
#         }
#     }
#
#     if length.replace('.', '', 1).isdigit() and \
#             (init_unit and final_unit) in available_units:
#
#         init_unit = init_unit.lower()
#         final_unit = final_unit.lower()
#
#         if init_unit == final_unit:
#             return f'{length}{init_unit} ==> {length}{final_unit}'
#
#         # Calculation
#         length = float(length)
#         converting_unit = f'{init_unit}_to_{final_unit}'
#
#         # Getting initial unit converted data
#         init_unit_data = conversion_data.get(init_unit)
#         init_final_unit_converted_format = init_unit_data.get(converting_unit)
#
#         # Calculating the final answer
#         answer = (length) * init_final_unit_converted_format
#
#         return f'{length}{init_unit} ==> {answer}{final_unit}'
#
#     else:
#         if not length.replace('.', '', 1).isdigit():
#             print('Length value is invalid')
#         elif (init_unit or final_unit) in available_units:
#             print('Unit does not exist.')


# print(unit_converter('15.5', 'inch', 'mile'))


# ==> Ex.2 The Battleship
# def gen_binary():
#     rand_num = math.floor(random.random() * (1 + 1))
#     return rand_num
#
# # ==> Building matrix
# matrix = [[gen_binary() for col in range(5)] for row in range(5)]
#
# msg = 'Choose a value from a row and column of 5 x 5 matrix ' \
#       'e.g. "2,5", for value at row 2, column 5. '
# user_choice = input('Enter your choice: ').replace(' ', '')
# user_choice = user_choice.replace(',', '', 1)
#
# # ==> Verifying user input
# if user_choice.isdigit() and len(user_choice) == 2:
#     user_choice_list = [int(i) for i in user_choice]
#     min_user_entry = min(user_choice_list)
#     max_user_entry = max(user_choice_list)
#
#     if 0 < min_user_entry <= 5 and 0 < max_user_entry <= 5:
#         row = user_choice_list[0]
#         col = user_choice_list[1]
#
#         el_at_pos = matrix[row-1][col-1]
#         print(matrix)
#         print()
#         print(f'The element at row {row}, column {col} is {el_at_pos}')
#
#         if el_at_pos == 1:
#             print('\nTarget: Hit')
#         else:
#             print('\nTarget: Missed')
#     else:
#         print('Invalid input')
# else:
#     print('Invalid input')


# ==> Matrix Entries Representation
#
# matrix = [
#     [2, 2, 2],
#     [2, 4, 2],
#     [9, 3, 1]
# ]

# def mat_pos(matrix, pos, format = 0):
#
#     # Matrix row-column format
#     def row_col():
#         row_col_list = [int(i) for i in pos.split(',')]
#
#         standard_row = row_col_list[0]
#         standard_col = row_col_list[1]
#
#         row_index = standard_row - 1
#         col_index = standard_col - 1
#
#         if 0 < standard_row <= len(matrix) and 0 < standard_col <= len(matrix[row_index]):
#
#             choice_el = matrix[row_index][col_index]
#             return f'The element at row {row_col_list[0]} and ' \
#                    f'column {row_col_list[1]} is: {choice_el}'
#
#         else:
#             return 'Row or column values out of range!'
#
#     # Matrix numbering format
#     def num_format():
#         one_dim_format = [j for i in matrix for j in i]
#
#         if pos.isdigit() and 0 < int(pos) <= len(one_dim_format):
#             choice_el = one_dim_format[int(pos) + 1]
#             return f'The element at position {pos} is: {choice_el}'
#
#     if format == 0:
#         return row_col()
#
#
# print(mat_pos(matrix, '2,3'))












# def get_matrix_position(matrix):
#
#     # i. Counter representation
#     counter_repr = {}
#     position_repr = {}
#
#     count = 0
#
#     pos_row_counter = 0
#
#     for row in matrix:
#         pos_col_counter = 0
#         for col in row:
#             # for counter
#             counter_repr.update({count: col})
#             count += 1
#             # for possition
#             position_repr.update({(pos_row_counter, pos_col_counter): col})
#             pos_col_counter += 1
#
#         pos_row_counter += 1
#
#     print(counter_repr)
#     print(position_repr)

# get_matrix_position(matrix)

# Q1. Print from 1 - 50

# ==> Solution 1.

# print(1)
# print(2)
# print(3)

# ==> Solution 2.
# for i in range(1, 51):
#     print(i)
# else:
#     print('Done')


# ==> Solution 3.
# counter = 1
# while counter <= 50:
#     print(counter)
#     counter += 1
# else:
#     print('I\'m done sir...')

# ---------------->
#
# if counter <= 50:
#     print(counter)

# # Shopping website using "while loop" to add items

# item_list = []

#
# while True:
#     if item_list:
#         user_input = input('Add another item to the list: ')
#     else:
#         user_input = input('Enter item to be added to the list: ')
#
#     break

# ===>
# matrix = [[0 for j in range(5)] for i in range(5)]
# print(matrix)
# print()
#
# num_of_ones_in_matrix = 10
# rows_num_of_ones = []
#
# # Generate list of number of ones at respective rows in matrix
# while sum(rows_num_of_ones) != 10:
#     rows_num_of_ones.append(random.randint(0, 5))
#
#     if sum(rows_num_of_ones) > 10 or len(rows_num_of_ones) > 5:
#         rows_num_of_ones.clear()
#
#
# # Replacing generated number of ones with zeroes at respective rows in matrix
#
# l_index = 0
# for num_of_ones in rows_num_of_ones:
#     row = matrix[l_index]
#
#     replaced_col_indices = random.sample(range(5), num_of_ones)
#
#     for col in replaced_col_indices:
#         row.pop(col)
#         row.insert(col, 1)
#
#     l_index += 1


# print(matrix)


# password = 'Lanx651@'
#
# user_input = input('Enter your password: ')
# chances = 4
# password_correct = False

# while not password_correct and chances > 0:
#     if user_input != password:
#         print(f'Incorrect password!!! You have {chances} chance(s) left')
#         user_input = input('Re-enter your password: ')
#         chances -= 1
#
#     if user_input == password:
#         password_correct = True
#
#
# if password_correct:
#     print('Login Successful!')
# else:
#     print('\t\tLogin failed. Account freeze till it is verified...')
#

# ===>

# while True:
#     user_input = input('Enter value (in kg) to convert to pounds(ibs): ')
#
#     if user_input.replace('.', '', 1).replace('-', '', 1).isnumeric():
#         if float(user_input) > 0:
#             ans = round(2.20462 * float(user_input), 2)
#             print(f'{user_input}kg ===> {ans}lbs')
#             break
#         else:
#             print('Negative entry. Pls try again!')
#
#     else:
#         print('Invalid data!')

# user_input = input('Enter value (in kg) to convert to pounds(ibs): ')
# valid_data = False
#
# while not valid_data:
#     modified_user_input = user_input.replace('-', '', 1).replace('.', '', 1)
#
#     if modified_user_input.isnumeric() and float(user_input) > 0:
#
#             ans = round(2.20462 * float(user_input), 2)
#             print(f'{user_input}kg ===> {ans}lbs')
#             valid_data = True
#
#     else:
#         print('Invalid data!')
#         user_input = input('Enter value (in kg) to convert to pounds(ibs): ')
#














