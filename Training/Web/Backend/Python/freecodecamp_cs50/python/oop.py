# Decorators
# -> Layman procedure
# def fact_positive(func):
#     def wrapper(li):
#         positive_data = list(filter(lambda el: el > 0, li))
#
#         for n in positive_data:
#             print(f'The factorial of {n} is: {func(n)}')
#         return
#
#     return wrapper

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)


# data = [12, 10, 5, -4, -1, 0]
# fact_pos = fact_positive(factorial)
# fact_pos(data)


# ---> Dev procedure
# Means the factorial func is wrapped inside the fact_positive
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)
#
#
# @fact_positive
# def process_list(li):
#     return [factorial(n) for n in li]
#
#
# data = [12, 10, 5, -4, -1, 0]
# process_list(data)

# -------------------------------------- The above is inconclusive
