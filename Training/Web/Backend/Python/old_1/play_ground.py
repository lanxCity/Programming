from random import random

# name = list(range(15))
#
#
# str_in_name = True
# counter = 0

# while str_in_name:
#     counter += 1
#     for i in name:
#         if type(i) is str:
#             str_in_name = True
#             break
#         else:
#             str_in_name = False
#
#     if str_in_name:
#         for item in name:
#             if type(item) is str:
#                 name.remove(item)

# me = {
#     'name': "ade"
# }
# me.update({'name': 'sodiq', 'age': 5})
#
# print(10 * 'No cheating\n')


#====> Hacking Simulation Algorithm
# import random
# import time
#
#
# def delay(t, suffix='', repeat=3):
#     if suffix:
#         if repeat == 0:
#             return
#
#         t /= 2
#         time.sleep(t)
#         print(suffix, end="")
#         return delay(t, suffix, repeat-1)
#
#     time.sleep(t)
#     return
#
#
# def missile_loader():
#     perc_breakdown = []
#
#     while True:
#         perc_breakdown.append(random.randint(1, 10))
#         perc_sum = sum(perc_breakdown)
#
#         if perc_sum == 100:
#             break
#         elif perc_sum > 100:
#             max_num = max(perc_breakdown)
#             excess_num = perc_sum - 100
#
#             if excess_num == max_num:
#                 perc_breakdown.remove(max_num)
#                 break
#             elif excess_num < max_num:
#                 max_num_pos = perc_breakdown.index(max_num)
#                 yield_num = max_num - excess_num
#
#                 perc_breakdown.remove(max_num)
#                 perc_breakdown.insert(max_num_pos, yield_num)
#                 break
#             else:
#                 perc_breakdown.clear()
#                 continue
#
#     return perc_breakdown
#
#
# msg = ['Opening Injector Box', 'Initialising', 'Accessing Target Address',
#        'Access Granted', 'Launching Missile', 'Mission Accomplished'
#        ]
#
# wlcm = 'Welcome to LanxCity funtack. Please wait while deploying...'
# print(wlcm)
#
# for output in msg:
#     t = random.randint(1, 7)
#     repeat = random.randint(1,5)
#
#     if output is 'Launching Missile':
#         print(output, end='')
#         delay(t, '.', repeat)
#         print()
#
#         load_perc = missile_loader()
#         t1 = 0
#
#         total = 0
#         for i in load_perc:
#             delay(t1)
#             print('\t\t\t\t\tLoading', end='')
#
#             t2 = random.randint(1, 3)
#             delay(t2, '.')
#             total += i
#             print(f' ({total}%)')
#
#             # Resetting "t1"
#             t1 = random.randint(1, 3)
#
#     elif output is 'Mission Accomplished':
#         print(f'{output}!')
#
#     elif output is 'Access Granted':
#         print(f'{output}! Just A Minute.')
#     else:
#         delay(t)
#         print(f'\t\t\t\t\t\t{output}', end='')
#         delay(t, '.', repeat)
#         print('\n')
#

# def counter():
#     count = 0
#
#     def increament():
#         nonlocal count
#         count += 1
#         print(count)
#
#     return increament
# inner_func = counter()
#
# inner_func()
# inner_func()
# inner_func()

# count = 1
#
# def increament():
#     global count
#     count += 1
#     print(count)
#
# increament()
# increament()
# increament()
# print(count)

matrix = []

for row in range(4):
    new_line = []
    for col in range(4):
        if row == col:
            new_line.append(1)
            continue
        new_line.append(0)

    print(new_line)
    matrix.append(new_line)






