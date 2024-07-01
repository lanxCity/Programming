# ==> Types of parameters and arguments
'''
# 1. Positional arguments
def summation(a, b):
    """
    :param int a: int
    :param int b: int
    :return: int
    """
    return a + b


print(summation(4, 5))
print(summation(15, 10))

# 2. Default arguments
# NB: default params and args come after positional
def person1(name, gender, cgpa=0):
    """
    :param str name: str
    :param str gender: str
    :param float cgpa: float
    :return:
    """
    print(f"Hey there! {name} is a {gender} and graduated with cgpa of {cgpa}.")
    return


print('--------> Default parameters')
person1('Lanx', 'male', 4.00)
person1('Lanx', 'male')

# 3. keyword arguments (kwargs)
def person2(name, gender, cgpa=0):
    """
    :param str name: str
    :param str gender: str
    :param float cgpa: float
    :return:
    """
    print(f"Hey there! {name} is a {gender} and graduated with cgpa of {cgpa}.")
    return


# NB: positional args come before the keyword args

print('--------> Keyword arguments')
person2(gender='male', 'Lanx', 4.00)  # Error
person2('Lanx', 'male', cgpa=4.00)
person2(cgpa=4.00, name='Lanx', gender='male')
person2('Lanx', cgpa=4.00, gender='male')
person2('male', 4.00, name='Lanx')  # Error - param "name" is given two args


# 4. Arbitrary parameters and arguments (*args)
def add(a, b, c, d, *numbers):
    """
    :param int a: int
    :param numbers: iterable
    :return:
    """
    print(f'Param "a" = {a}')
    print(f'A => {numbers}')
    print(*numbers, sep=', ')

    my_list = [*numbers]
    print(my_list)
    # my_list2 = list(*numbers) # Error
    # print(my_list2)

    # return a + numbers

# add(2, d=6, b=5, c=4, 4, 5, 2)  # Error - positional args must come before kwargs
# add(2, 4, 5, 2, d=6, b=5, c=4)  # Error - many args are passed to each keywords args-params
add(4, 5, 2, 6, 4, 10, 11)


# 5. *args && **kwargs
# For example,
# for i, j in ((1, 3), (0, 19)):
#     print(i, j, sep=', ')
# The above prints:
# 1, 3
# 0, 19

# -> *args  (Arbitrary positional args) - returns tuple
def add(*data):
    print(data)
    print([data])
    print([*data])
    print(list(data))
    # print(list(*data))  # Error
    total = 0
    for i in data:
        total += i
    print(total)

add(1,2,3,4,5,6,7,8,9)


# -> **kwargs  (Arbitrary keyword args) - returns dictionary
def info(**data):
    print(data)


info(name='Lanx', age=26, occupation='dev')
info(name='Abdulgafar', age=24, occupation='dev', status='married')



# NB: "*args" must come before "**kwargs"
# NB: exiting parameter name must not equal to any of the kwargs passed
def info(name, height, *num, **data):
    print(name)
    print(height)
    print(num)
    print(data)


info(1, 89, 2,3,4,5, user='lanx',age=50)
# info(1, height=89, 2,3,4,5, user='lanx',age=50)  # Error - positional comes after kwarg
# info(1,2,3,4,5, height=89, user='lanx',age=50)  # Error - many args passed to height

# NB: args arrangement -> positional, kwargs, *args, **kwargs
# In the case of kwargs & *args, it depends on the parameter arrangement


def info2(name, *num, height, **data):
    print(name)
    print(height)
    print(num)
    print(data)


info2(1, 89, 2,3,4,5, height=23, user='lanx',age=50)
# info(1, height=89, 2,3,4,5, user='lanx',age=50)  #Error



def info2(name, height=0,*num, **data):
    print(name)
    print(height)
    print(num)
    print(data)


info2(1, 1.5, 2,3,4,5, user='lanx',age=50)
'''


# Global keyword
data = []

def add_stuff(new):
    data.append(new)
    return

add_stuff('lanx')
add_stuff('lanx')
add_stuff('lanx')
add_stuff('lanx')
print(data)


#a = 68

def increament():
    # It is impossible to modify immutable global variable from a fun
    # But using "global" keyword, there would be no error
    global a
    #a += 23
    a = 23  # if a var is not created globally, we can Create one within the func using the global keyword
    return

increament()
print(a)














