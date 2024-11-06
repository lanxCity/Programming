import random, os, math

# =========> Project 1 (Rock -> Paper -> Scissors)
'''
rps = ['Rock', 'Paper', 'Scissors']
scores = []  # list of score lists e.g. [[Computer, User]]
game_choices = []  # list of game choices lists e.g. [[Computer, User]]

print('Welcome to Rock Paper Scissors game. '
      'Choose between 1 - 3 to select your option')

# play_game = True
counter = 0
while counter < 9:
    for i in range(len(rps)):
        print("'{}' -> {}".format(i + 1, rps[i]))

    computer_choice = rps[random.randint(0, 2)]
    user_choice = rps[int(input('Enter your choice: ')) - 1]
    game_choices.append([computer_choice, user_choice])

    last_score = None

    # Grabbing the last score
    for i in range(len(scores) - 1, -1, -1):
        if 'Draw' not in scores[i]:
            last_score = scores[i][:]
            break

    # For new scores
    if computer_choice == 'Rock':
        if user_choice == computer_choice:
            scores.append(['Draw'])
        elif user_choice == 'Paper':
            if last_score:
                last_score[1] += 5
            else:
                last_score = [0, 5]
            scores.append(last_score)
        else:
            if last_score:
                last_score[0] += 5
            else:
                last_score = [5, 0]
            scores.append(last_score)

    elif computer_choice == 'Paper':
        if user_choice == computer_choice:
            scores.append(['Draw'])
        elif user_choice == 'Scissors':
            if last_score:
                last_score[1] += 5
            else:
                last_score = [0, 5]
            scores.append(last_score)
        else:
            if last_score:
                last_score[0] += 5
            else:
                last_score = [5, 0]
            scores.append(last_score)
    else:
        if user_choice == computer_choice:
            scores.append(['Draw'])
        elif user_choice == 'Rock':
            if last_score:
                last_score[1] += 5
            else:
                last_score = [0, 5]
            scores.append(last_score)
        else:
            if last_score:
                last_score[0] += 5
            else:
                last_score = [5, 0]
            scores.append(last_score)

    # Printing and Initializing score-sheet to draw
    print('\t\tComputer\t  Player\tPoints')
    print('-----------------------------------------------')

    for i in range(len(scores)):
        new_sheet = 'Draw'
        if 'Draw' not in scores[i]:
            new_sheet = f'{scores[i][0]}--{scores[i][1]}(Player)'

        print(f'\t\t{game_choices[i][0]}\t\t{game_choices[i][1]}\t{new_sheet}')

    print()
    counter += 1
    # play_again = input("Would you like to play again (Y/N)? ")
    # #if play_again in "No/no":
    #  play_game = False


# =============> Project 2 (Password Generator)
# - Alphabets
no_of_alpha = int(input('Enter the number of alphabet: '))
alpha = ''
alpha_list = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)]
for _ in range(no_of_alpha):
    alpha += random.choice(alpha_list)

# - Digits
no_of_digits = int(input('Enter the number of digits: '))
digits = ''
digits_list = [i for i in range(10)]
for _ in range(no_of_digits):
    digits += str(random.choice(digits_list))

# - Symbols
no_of_symbols = int(input('Enter the number of symbols: '))
symbolic = ''
symbolic_list = [chr(i) for i in range(33, 43)] + ['@']
symbolic_list.remove('\'')
symbolic_list.remove('"')
for _ in range(no_of_symbols):
    symbolic += random.choice(symbolic_list)

# Join the whole sequence
password = alpha + digits + symbolic
password = [i for i in password]
random.shuffle(password)
password = ''.join(password)

print()
print('Suggested password is: {}'.format(password))



# Hangman game
items = ['apple', 'orange', 'butter', 'zebra', 'disk', 'steven', 'abdugafar', 'sahadat']
computer_choice = random.choice(items)
disp_choice = ['-' for _ in range(len(computer_choice))]

hangman_limit = 6
is_hanged = False
is_won = False

while not is_hanged and not is_won:
    print("\t\t", disp_choice)
    guessed_letter = input('Enter a letter: ').lower()

    if (guessed_letter in computer_choice) and (guessed_letter not in disp_choice):
        for i in range(len(computer_choice)):
            if computer_choice[i] == guessed_letter:
                if guessed_letter not in disp_choice:
                    print(f'\t\tGreat! Letter "{guessed_letter}" Match...')
                disp_choice[i] = guessed_letter

        if '-' not in disp_choice:
            print("\t\t", disp_choice)
            print('You won!!!')
            is_won = True
    elif guessed_letter in disp_choice:
        # if a correct letter already guessed
        print("Letter already exist!!!\n")
    else:
        # if wrong input is entered
        hangman_limit -= 1
        if hangman_limit > 0:
            print(f'\t\tSorry, Not match... You have {hangman_limit} chances left')

        # Display hangman
        hangman = ''
        if hangman_limit == 5:
            hangman += ' O'
        elif hangman_limit == 4:
            hangman += ' O |'
        elif hangman_limit == 3:
            hangman += ' 0/|'
        elif hangman_limit == 2:
            hangman += ' O/|\\'
        elif hangman_limit == 1:
            hangman += ' O/|\\/'
        else:
            hangman += ' O/|\\/ \\'
            print("\t\tYou lose")
            is_hanged = True

        print(' +---+')
        print(' |   |')
        for i in range(len(hangman)):
            print(hangman[i], end="")

            # Breaking into new line
            if i == 1 or i == 4:
                print()
        print()



# ========> Project 3 - Caesar Cipher
def encrypt(passwd, shift=1):
    lower_letters = [chr(i) for i in range(97, 123)]
    passwd = passwd.lower()

    encrypted_passwd = ''
    for i in range(len(passwd)):
        if passwd[i] in lower_letters:
            alpha_idx = lower_letters.index(passwd[i])
            new_alpha_idx = (alpha_idx + shift) % 26
            encrypted_passwd += lower_letters[new_alpha_idx]
        else:
            encrypted_passwd += passwd[i]
    return encrypted_passwd


def decrypt(passwd, shift=1):
    lower_letters = [chr(i) for i in range(97, 123)]
    passwd = passwd.lower()

    decrypted_passwd = ''
    for i in range(len(passwd)):
        if passwd[i] in lower_letters:
            alpha_idx = lower_letters.index(passwd[i])
            new_alpha_idx = (alpha_idx - shift) % 26

            if new_alpha_idx < 0:
                new_alpha_idx += 26

            decrypted_passwd += lower_letters[new_alpha_idx]
        else:
            decrypted_passwd += passwd[i]

    return decrypted_passwd



def encrypt_decrypt(text, op=1, shift=1):
    """
    :param str text: str
    :param int op: int
    :param int shift: int
    :return:
    """

    if op == 1 or op == 2:
        lower_letters = [chr(i) for i in range(97, 123)]
        text = text.lower()

        new_passwd = ''
        for i in range(len(text)):
            if text[i] in lower_letters:
                alpha_idx = lower_letters.index(text[i])

                if op == 1:
                    new_alpha_idx = (alpha_idx + shift) % 26
                else:
                    new_alpha_idx = (alpha_idx - shift) % 26
                    if new_alpha_idx < 0:
                        new_alpha_idx += 26

                new_passwd += lower_letters[new_alpha_idx]
            else:
                new_passwd += text[i]

        return new_passwd
    else:
        print("Invalid option")


password = 'Hello World!'

encrypted = encrypt_decrypt(password, 1, 3)
print(f"Encryption ===> {encrypted}")

decrypted = encrypt_decrypt(encrypted, 2, 3)
print(f"Decryption ===> {decrypted}")


# =========> Silent Auction Program

product = 'Hard drive'
min_prize = 500  # dollars

bidders_list = []
bidding = True

wlc_msg = 'Welcome to our grand new auction of 500,000$! Please, place your bid sir/ma'
print(wlc_msg)
print(wlc_msg)

while bidding:
    new_bidder = input("Enter your name: ")
    new_bidder_prize = int(input("Enter your bid: "))  # dollars

    new_bid = {
        'name': new_bidder,
        'prize': new_bidder_prize
    }

    bidders_list.append(new_bid)

    # Add new bid or not
    other_bidder = input('Add another bidder?(Y/N) => ')

    if other_bidder not in 'Yy':
        bidding = False

    # For this to work, enable "Emulate python console" option
    # right-click -> modify run config -> more option
    os.system('cls')
    print(wlc_msg)

highest_bid = bidders_list[0]['prize']
winner_name = ''
for item in bidders_list:
    if item['prize'] > highest_bid:
        highest_bid = item['prize']
        winner_name = item['name']

os.system('cls')
print(wlc_msg)
print(f'The highest bid is {highest_bid}!!! congratulations Mr. {winner_name}')



# Simple Calculator

def operaions(a, b, op):
    def add():
        return a + b
    def subtract():
        return a - b
    def divide():
        return a / b
    def multiply():
        return a * b

    # operations dict
    ops = {
        '+': add,
        '-': subtract,
        '/': divide,
        '*': multiply
    }

    return ops[op]()

def calculator(a=0, on=False, cleared=True, exit=False):
    if exit:
        print('\t\t\t\tGood Bye!!!')
        return

    # Program initialize
    if not on:
        print('\t\t\t\t\tWelcome to lanxCity Simple Calculator\n')
        print('\t\t\t\t\tWelcome to lanxCity Simple Calculator\n')
        on = True

    # previous answer is not needed
    if cleared:
        a = float(input('Enter first value: '))

    print('+', '-', '/', '*', sep='\n')
    op = input('Pick an operation: ')
    b = float(input('Enter next value: '))
    ans = operaions(a, b, op)
    print(f'{a} {op} {b} = {ans}')

    # Continue with prev ans or not
    cont = input(f'Enter "y" to continue with {ans} or "n" to start new calculation or "x" to exit: ').lower()

    if cont == 'y':
        a = ans
        cleared = False
        os.system('cls')
        print(f'previous answer => {ans}')
    elif cont == 'n':
        cleared = True
        os.system('cls')
    else:
        exit = True

    return calculator(a, on, cleared, exit)


calculator()



# Guessing game
# NB: Const variables are uppercase
EASY_ATTEMPT = 10
HARD_ATTEMPT = 5

# math.floor((random.random() * ((max + 1) - min))) + min
logo1 = __import__('project_logos').logo1
print(logo1)
print('Let think of a number between 1 to 50')
answer = math.floor((random.random() * ((50 + 1) - 1))) + 1
difficulty_level = input('Choose level of difficulty... Type "easy" or "hard": ')
attempt = EASY_ATTEMPT if difficulty_level == 'easy' else HARD_ATTEMPT

def guessing_game(ans, attempt=0):
    if attempt == 0:
        print('=' * 10, '>', 'GAME OVER!!!')
        print(f'The correct value is: {ans} ')
        return

    print(f'You have {attempt} attempt(s) remaining')
    guessed_num = int(input('Guess a number: '))

    if guessed_num == ans:
        print('\t\t\tGreat! You\'ve guessed right...')
        return
    elif guessed_num > ans:
        print(f'\t\tNumber guessed, {guessed_num:d}, is too high')
    else:
        print(f'\t\tNumber guessed, {guessed_num:d}, is too low')

    attempt -= 1
    return guessing_game(ans, attempt)


guessing_game(answer, attempt)


# Higher-Lower Game
data = __import__('higher_lower_data').data
higher_lower_logo1 = __import__('project_logos').higher_lower_logo1
higher_lower_logo2 = __import__('project_logos').higher_lower_logo2

def disp(cmp,profile):
    name = profile['name']
    description = profile['description']
    country = profile['country']

    if description[0].lower() in ['a', 'e', 'i', 'o', 'u']:
        print(f'=> Compare {cmp}: {name}, an {description.lower()}, from {country}')
    else:
        print(f'=> Compare {cmp}: {name}, a {description.lower()}, from {country}')


def game(data):
    print(higher_lower_logo1)
    score = 0

    # Choosing random profiles and remove from the data
    acct1_idx = random.randint(0, len(data) - 1)
    acct1 = data[acct1_idx]
    del data[acct1_idx]

    while True:
        acct2_idx = random.randint(0, len(data) - 1)
        acct2 = data[acct2_idx]
        del data[acct2_idx]

        new_cmp_list = [acct1, acct2]
        followers_count_list = [acct1['followers'], acct2['followers']]
        highest_followers_idx = followers_count_list.index(max(followers_count_list))

        # Taking user input
        disp(1, acct1)
        print(higher_lower_logo2)
        disp(2, acct2)
        user_input = int(input('Who has more followers on instagram? Type "1" or "2": ')) - 1

        # Clear the screen
        # os.system('cls')
        print(higher_lower_logo1)
        if user_input != highest_followers_idx:
            print(f'Sorry, you are wrong. Your score is {score}')
            return
        else:
            score += 1
            print(f'Great! You are right. Your score is {score}')
            acct1 = new_cmp_list[highest_followers_idx]

            if not data:
                print('\t\t\tGame Over!!!!!!!!!')
                return


game(data)

'''

# Design Coffee machine
# available_material = {
#     'coffee': 100,  # grams
#     'milk': 500,  # ml
#     'water': 500  #ml
# }
# coffee_data = __import__('coffee_data').coffee_data
# coffee_list = [item['name'] for item in coffee_data]
# coffee_list_disp = [item['name'].capitalize() for item in coffee_data]  # Just for display
# coins_list = [10, 50, 100]  # Naira
#
#
# def check_material(material_left, order_material):
#     for item in order_material:
#         if order_material[item] > material_left[item]:
#             return False
#
#     return True
#
#
# is_on = True
# order_report = ''
#
# while is_on:
#     choice = input(f"What would like to have? ({'/'.join(coffee_list_disp)}): ").lower()
#
#     if choice in coffee_list:
#         order_data = coffee_data[coffee_list.index(choice)]
#         order_prize = order_data['prize']
#         order_report = order_data['material']
#
#         payment = 0
#         change = 0
#
#         material_sufficient = check_material(available_material, order_report)
#
#         if material_sufficient:
#             for coin in coins_list:
#                 num_of_coins = int(input(f'How many {coin}-Naira coins: '))
#                 payment += num_of_coins * coin
#
#             if payment >= order_prize:
#
#                 if payment > order_prize:
#                     change += (payment - order_prize)
#                     print(f'Here is your {change}Naira change')
#
#                 print(f'====> Enjoy your {choice}')
#
#                 # Adjusting the available material
#                 for item in order_report:
#                     available_material[item] -= order_report[item]
#
#             else:
#                 print('Sorry, insufficient payment!')
#                 continue
#         else:
#             print(f'{choice.capitalize()} not available... Please, check back later.')
#
#     else:
#         if choice == 'off':
#             print('\t\tGood Bye!')
#             is_on = False
#         elif choice == 'report':
#             if order_report:
#                 for item in order_report:
#                     unit = 'g' if item == 'coffee' else 'ml'
#                     print(f'{item}: {order_report[item]}{unit}')
#             else:
#                 print('\t\t\tNo report...')
#         else:
#             os.system('cls')
#             print('Invalid input! Please choose from the options shown below...')
#             order_report = ''


# Quiz Game
class QuizData:
    questions = [
        'What is the capital of France',
        'Which planet is known as the "Red Planet"',
        'Who wrote "Romeo and Juliet',
        'Which element has the atomic number 1',
        'What is the largest ocean on Earth',
        'What is the square root of 64',
        'In which year did World War II end',
        'What is the chemical symbol for gold',
        'Which of the following is a prime number',
        'What language is primarily spoken in Brazil'
    ]

    options = [
        ('Rome', 'Madrid', 'Paris', 'Berlin'),
        ('Earth', 'Mars', 'Jupiter', 'Venus'),
        ('Charles Dickens', ' J.K. Rowling', 'William Shakespeare', 'George Orwell'),
        ('Helium', 'Hydrogen', 'Oxygen', 'Nitrogen'),
        ('Atlantic Ocean', 'Indian Ocean', 'Pacific Ocean', 'Arctic Ocean'),
        (6, 7, 8, 9),
        (1940, 1942, 1945, 1948),
        ('Ag', 'Go', 'Au', 'Gd'),
        (9, 15, 21, 13),
        ('Spanish', 'Portuguese', 'French', 'English')
    ]

    ans_ind = (2, 1, 2, 1, 2, 2, 2, 2, 3, 1)

class Quiz:

    def __init__(self):
        self.score = 0

    def start(self):
        print('Welcome to LanxCity quiz competition')
        print('*' * 50)

        num_of_qeustions = len(QuizData.questions)
        counter = 0
        point = 100 / num_of_qeustions
        total_got = 0

        # option dictionary for direct lookup
        opt = {'A': 0, 'B': 1, 'C': 2, 'D': 3}

        while counter < num_of_qeustions:
            print()
            print(f'{QuizData.questions[counter]}?')
            ans = QuizData.options[counter]
            correct_ans = QuizData.ans_ind[counter]

            for el in opt:
                print(f'{el}. {ans[opt[el]]}')

            user_input = input('Enter your answer (A/B/C/D): ').upper()
            if user_input in opt and opt[user_input] == correct_ans:
                self.score += point
                total_got += 1
                print(f'Correct Answer! Points: {self.score}')
            else:
                print('**Sorry, Incorrect Answer...')
                print(f'The correct answer is "{ans[correct_ans]}"')
                print(f'Your current point is {self.score}')

            counter += 1

        print(f'You got {total_got} correctly out of {num_of_qeustions} questions')


Quiz().start()



















































