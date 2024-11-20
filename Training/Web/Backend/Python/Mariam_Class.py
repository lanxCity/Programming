# import sys
# def palindromic(n):
#     start = 10 ** (n - 1)  # starting point
#     n_mod = 10 ** n
#
#     palindromic_li = []
#
#     for x in range(start, n_mod):
#         if x % 9 == 0:
#             # Checking number with '0' digit
#             zero_exist = False
#             new_x = x
#             while new_x > 0:
#                 if new_x % 10 == 0:
#                     zero_exist = True
#                     break
#
#                 new_x //= 10
#
#             # Add eligible element
#             if not zero_exist:
#                 new_x_str = str(x)
#                 new_x_str_rev = new_x_str[-1::-1]
#                 if new_x_str == new_x_str_rev:
#                     palindromic_li.append(x)
#
#     return palindromic_li
#
#
# input().strip()
# # if len(sys.argv) > 1:
# #     # Take the first argument as the number
# #     print(sys.argv)
# #     n = int(sys.argv[1])
# #     print(sum(palindromic(n)))


# li = [-9, -1, 0]
# n = len(li)
# max_sum = 0
#
# for i in range(n):
#     total = li[i]
#     for j in range(i + 1, n):
#         total += li[j]
#
#     if total > max_sum:
#         max_sum = total
#
# print(max_sum)
#
# ''.rstrip()

def do_max_sum(n, li):
    max_sum = li[0]
    current_sum = li[0]

    for i in range(1, n):
        # Either add the current element to the existing sum or start a new subarray from li[i]
        current_sum = max(li[i], current_sum + li[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


li = [-1, 2, 3]
n = len(li)

print(do_max_sum(n, li))
