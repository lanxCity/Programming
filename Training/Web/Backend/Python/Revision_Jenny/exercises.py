import math
import random
# Exercise 5 -> calculate how many days left
"""
curr_yrs = int(input("Enter your current age please: "))  # yrs
max_yrs = 90  # yrs

# Assumptions
yr_to_dys = 365  # dys
yr_to_wks = 52  # wks
yr_to_mnths = 12  # mnths

# Solutions
remaining_yrs = max_yrs - curr_yrs
remaining_mnths = remaining_yrs * yr_to_mnths
remaining_wks = remaining_yrs * yr_to_wks
remaining_dys = remaining_yrs * yr_to_dys

print(remaining_yrs)
print(remaining_mnths)
print(remaining_wks)
print(remaining_dys)

print('You have {} days, {} weeks, and {} months left.'.
      format(remaining_dys, remaining_wks, remaining_mnths)
      )



# Exercise - Determine leap year
user_yr = 2000

# Check for non century and century
if user_yr % 4 == 0:
    if user_yr % 100 == 0:
        if user_yr % 400 == 0:
            print('It is a leap year')  # Century
        else:
            print('Not a leap year...')
    else:
        print('It is a leap year')  # Non century
else:
    print('Not a leap year...')


# Exercise 9 -> Pizza order program
# - Menu
small_pizza, medium_pizza, large_pizza = 100, 200, 300

peppezoni_small_pizza = 30
peppezoni_medium_large = 50

xtra_cheese = 20

currency = 'Naira'

# - Ordering
msg = '''\
Welcome to lanxCity! Please, place your order by pressing the \
number key associated to your choice

1 -> Small pizza  (100 Naira)
2 -> Medium pizza  (200 Naira)
3 -> Large pizza   (300 Naira)
Enter option here: 
'''
total = 0
pizza_size = int(input(msg))

if 1 <= pizza_size < 4:
    if pizza_size == 1:
        total += small_pizza
    elif pizza_size == 2:
        total += medium_pizza
    else:
        total += large_pizza

    print("\n\t\tAmount: {} Naira".format(total))
    add_peppezoni= input("==>Do you want to add peppezoni (Y/N)? ")
    if add_peppezoni and add_peppezoni in 'Yy':
        if pizza_size == 1:
            total += peppezoni_small_pizza
        elif 1 < pizza_size <= 3:
            total += peppezoni_medium_large

        print("\n\t\tAmount: {} Naira".format(total))

    add_cheeze = input("\n==> Cheese is 20 Naira. Do you want to add cheese (Y/N)? ")
    if add_cheeze and add_cheeze in 'Yy':
        total += xtra_cheese

    print("Total amount: {} Naira".format(total))
else:
    print("Invalid")

for i, j in [[1,2],[3,3]]:
    print(i, j)


# Exercise - 10 (True Love)
print('This is a matchmaking app... Check if you match')
bf = input("Enter the boyfriend name: ").lower()
gf = input("Enter the girlfriend name: ").lower()

bf_gf = bf + gf

print("==> In {}, we have:".format(bf_gf))
perc_1 = 0
for i in 'true':
    print("{} -> ".format(i.upper()), end='')
    if i in bf_gf:
        perc_1 += bf_gf.count(i)
        print("{}".format(bf_gf.count(i)))
    else:
        print('-')

print('----------------------')
perc_2 = 0
for i in 'love':
    print("{} -> ".format(i.upper()), end='')
    if i in bf_gf:
        perc_2 += bf_gf.count(i)
        print("{}".format(bf_gf.count(i)))
    else:
        print('-')

unit = perc_2 % 10
remainder_tenth = perc_2 // 10

perc_1 *= 10

total = (perc_1 + remainder_tenth) + unit
print('=======> total is: {}'.format(total))


import random

stuff = [random.randint(1, 10) for _ in range(5)]

print(stuff)
print(stuff[-1:0:-1])
print(stuff[-1:-len(stuff)-1:-1])

me = '🧡🗑🕋🌨🌊☔'

print(me)


# Exercise - Reeborg's World (Online Hurdle 1 game)
def up():
    turn_left()
    move()
    return

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    return

def down():
    turn_right()
    move()

for i in range(2, 14):
    move()
    
    if i % 2 == 0:
        up()
        turn_right()
    else:
        down()
        turn_left()



# Exercise 21 - Number of cans to paint the wall
def number_of_cans(width, height, coverage):
    num_of_cans = (width * height) / coverage
    num_of_cans = math.ceil(num_of_cans)
    return num_of_cans


# (1inch - 2.54cm - 0.0254m)
coverage = 7  # m^2
wall_height = 2.30  # m
wall_width = 4.58  # m
# unit = 'm square (m^2)'

paint_cans = number_of_cans(wall_width, wall_height, coverage)
print("The number of cans required is {}".format(paint_cans))


for i in range(2,3):
    print(i)

print(2**.5)
print([True] * 3)


# Exercise - Prime number
# Method 1
def prime_1(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# Method 2
def prime_2(num):
    if num <= 1:
        return False

    for i in range(2, math.ceil(num / 2) + 1):  # Half of the number is inclusive
        if num % i == 0:
            return False
    return True


# Method 3 - Square root method
def prime_3(num):
    if num <= 1:
        return False

    prime = []
    sieve = [True] * (num + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, math.ceil(num**0.5) + 1):  # Square of the number is inclusive
        if sieve[i]:
            prime[len(prime):] = [i]

            for bl_idx in range((i * i), len(sieve), i):  # the step is the multiple of i
                sieve[bl_idx] = False

    # print(prime)
    # To get all prime numbers within the range of num supplied
    for i in range(math.ceil(num ** 0.5) + 1, num + 1):
        if sieve[i]:
            prime[len(prime):] = [i]
    # print(prime)
    return sieve[num]


num = 47
print(f"Prime function 1 -> {num} is {'prime' if prime_1(num) else 'not prime'}")
print(f"Prime function 1 -> {num} is {'prime' if prime_2(num) else 'not prime'}")
print(f"Prime function 1 -> {num} is {'prime' if prime_3(num) else 'not prime'}")



# Exercise - Convert marks to grade
grading_system = {
    tuple(range(91, 101)): 'A+',
    tuple(range(81, 91)): 'A',
    tuple(range(71, 81)): 'B+',
    tuple(range(61, 71)): 'B',
    tuple(range(51, 61)): 'C',
    tuple(range(40, 51)): 'D',
    tuple(range(40)): 'F',
}

score_sheet = {
    'Abdulgafar': 84,
    'Abiola': 64,
    'Sahadat': 51,
    'Omotayo': 45,
    'Damola': 64,
    'Anuoluwapo': 97,
    'Drey': 75,
}

score_sheet.update({'Pricscilia':51})


def grading(grading_sys, sc):
    for grade in grading_sys:
        if sc in grade:
            return grading_sys[grade]


for student in score_sheet:
    score = score_sheet[student]
    score_sheet[student] = tuple([score, grading(grading_system, score)])


print(score_sheet)
"""

# Exercise - Determine the number of days of the month entered
def is_leap(yr):
    if yr % 100 == 0:
        if yr % 400 == 0:
            return True
    elif yr % 4 == 0:
        return True

    return False


months_list = ['january', 'february', 'march', 'april',
               'may', 'june', 'july', 'august', 'september',
               'octomber', 'november', 'december']

months_days = [31, 28, 31, 30,
               31, 30, 31, 31,
               30, 31, 30, 31]

user_month = int(input('Enter the month value: '))
user_year = int(input('Enter the year value: '))

if 1 <= user_month <= 12 and 1582 < user_year < 3000:
    user_month -= 1
    days_in_month = months_days[user_month]

    # For leap year
    if user_month == 1 and is_leap(user_year):
        days_in_month += 1
        print(f'The month {months_list[user_month]} of the year {user_year} has => {days_in_month} days (leap year)')
    else:
        print(f'The month {months_list[user_month]} of the year {user_year} has => {days_in_month} days')
else:
    print('Invalid input!!!')


# Introduction to oop
"""
import math
class Circle:
    PI = math.pi  # class attr
    def __init__(self, radius):
        self.radius = radius
    @property
    def area(self):
        return Circle.PI * (self.radius ** 2)
    @property
    def circumference(self):
        return 2 * (Circle.PI * self.radius)


c1 = Circle(6)

print(round(c1.area, 3))
print(round(c1.circumference, 3))


print("{:d}".format(78) * 10)
print(10_34)

"""



















































