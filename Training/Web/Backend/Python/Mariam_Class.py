# -------Data Types
# 1. Numbers
my_int = 5
print(type(my_int))
my_int = 6

my_float = 5.9
print(type(my_float))


# 2. String
my_str = "Hey there! I am learning python"
my_str2 = 'Hey there! I am'\
          'learning python'

def do_stuff(any_str):
    new_str = ''

    for i in any_str:
        if i == "e":
            new_str += 'j'
        else:
            new_str += i
    return new_str

print(do_stuff(my_str))
print(my_str)

my_list = [24, 2, 9, 10]

def do_stuff2(any_list):
    count = 0
    for m in any_list:
        if m == 2:
            any_list[count] = 25
        count += 1
    return any_list

print(do_stuff2(my_list))
print(my_list)