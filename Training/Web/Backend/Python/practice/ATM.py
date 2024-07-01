import math
import time
import random


# => Welcome message
lanx_msg = 'Welcome To lanxCity Multi-banking ATM. Please follow the instructions ' \
           'and feel free to explore...\n'
lanx_msg_counter = 1

bank_list = sorted(['First', 'Polaris', 'GT', 'UBA', 'Access', 'Wema', 'Zenith'])

profile_titles = ['first name', 'last name', 'other name', 'date of birth', 'occupation']

banks = {}
# => Creating banks with empty data in banks dict
for bank in bank_list:
    banks.update({bank: {}})


# ***************************************************************
# Process delay function
def delay(t=4, msg='Loading', counter = 4):
    if 0 < counter < 4:
        msg = '.'
        print(f'{msg}', end='')
        if counter == 1:
            time.sleep(t)
            print('\tDone!')
            return
    else:
        t = random.randint(1, t)
        t /= 3
        msg = msg.replace('.', '')
        print(f'\t\t\t\t\t\t{msg}', end='')

    counter -= 1
    time.sleep(t)
    return delay(t + 0.5, msg, counter)


# Fig reformatting
def fig_reform(amount):
        amount = str(amount)
        new_set = ''
        num_reformat = ''

        for i in range(1, len(amount) + 1):
            new_set = f'{amount[-i]}{new_set}'

            if len(new_set) == 3 and i != len(amount):
                num_reformat = f',{new_set}{num_reformat}'
                new_set = ''

        num_reformat = f'{new_set}{num_reformat}'

        return num_reformat


# => Generate pin
def create_pin():
    counter = 3
    while counter > 0:
        pin = input('Create transaction pin (four (4) digits): ')
        if pin.isdigit() and len(pin) == 4:

            pin_confirmation = input('Please re-enter pin for confirmation: ')
            if pin_confirmation == pin:
                return pin
            else:
                print(
                    f'\tError!!! Your input must match the pin you just created. '
                    f'Please create pin again'
                    )
                continue
        else:
            counter -= 1
            print(f'\tInvalid input!!! You have {counter} chances left')
            continue
    else:
        print('Session Closed...')
    return


# => create_profile function
def create_profile(bank_list, user_bank, profile_titles, banks):

    def validate_input(data, data_title):
        if data_title == 'first name' or \
                data_title == 'last name' or \
                data_title == 'other name' or \
                data_title == 'occupation':

            if data.isalpha():
                return True

        else:
            if '-' in data and data.count('-') == 2:

                date, mnth, year = data.replace(' ', '').split('-')
                if (date.isnumeric() and mnth.isnumeric() and year.isnumeric()) and \
                        (0 < len(date) <= 2 and 0 < len(mnth) <= 2 and len(year) == 4) and\
                        (0 < int(date) <= 31 and 0 < int(mnth) <= 12 and 1900 < int(year) <= 2022):
                    return True

        print('\tSorry, invalid data input. Please re-start the form with valid data.')
        return False

    def gen_acct_num():
        acct_num = f'{bank_list.index(user_bank)}'
        acct_num += ''.join([str(math.floor(random.random() * (9 + 1))) for _ in range(9)])

        if acct_num in banks[user_bank]:
            return gen_acct_num()

        return acct_num

    acct = gen_acct_num()

    new_profile = {
        'account details': {
            'balance': 0,
            'debits': [],
            'credits': []
        }
    }

    for title in profile_titles:
        user_input = ''

        if title == 'date of birth':
            user_input = input(f'Enter your {title.capitalize()} (Day-Month-Year): ')
        else:
            user_input = input(f'Enter your {title.capitalize()}: ').capitalize()

        # Validate data
        valid = validate_input(user_input, title)
        if not valid:
            return create_profile(bank_list, user_bank, profile_titles, banks)

        # modifying date of birth
        if title == 'date of birth':
            date, mnth, year = user_input.replace(' ', '').split('-')
            user_input = {'date': date, 'month': mnth, 'year': year}

        new_profile.update({title: user_input})

    # Generate pin
    pin = create_pin()

    if pin:
        masked_pin = pin[0] + len(pin[1:]) * 'x'
        new_profile.update({'pin': pin, 'masked pin': masked_pin})
        banks[user_bank].update({acct: new_profile})

        # Delaying successful reg message
        delay(5, 'Setting Up Account')
        msg = f'\t\t\tDear {new_profile["first name"]}, Welcome to {user_bank}Bank. Your ' \
              f'data is well received and account has been set up. \nPlease NOTE your ' \
              f'account number and pin \n=> Your account number is -> {acct}'
        print(msg, '\n')

    return


# => transaction function
def transaction(bank_list, banks, user_bank, perform_trans=True):

    # => Quit transaction
    if not perform_trans:
        print('Session Closed...Thanks for using lanxCity')
        print()
        return

    # => Transaction options
    def deposit(acct):
        user_amount = input('Enter amount to deposit: $')
        acct_detail = banks[user_bank][acct]

        delay(5, 'Just a minute')
        if user_amount.replace(',', '').isdigit() and int(user_amount.replace(',', '')) > 0:
            amount = int(user_amount.replace(',', ''))
            print(f'\tDear {acct_detail["first name"]}, deposition of ${fig_reform(amount)} was '
                  f'successful')

            # Updating database
            banks[user_bank][acct]["account details"]["balance"] += amount
            banks[user_bank][acct]["account details"]["credits"].append(amount)

            # Getting new balance and reformatting it
            new_balance = banks[user_bank][acct]["account details"]["balance"]
            print(f'Account balance is: ${fig_reform(new_balance)}')
            return
        print('Invalid amount entry!')
        return

    def withdraw(acct):
        amount = input('Enter amount to withdraw: $')
        acct_detail = banks[user_bank][acct]

        delay(5, 'Just a minute')
        if amount.replace(',', '').isdigit() and int(amount.replace(',', '')) > 0:
            if int(amount.replace(',', '')) < acct_detail['account details']['balance']:

                amount = int(amount.replace(',', ''))

                print(f'\tDear {acct_detail["first name"]}, withdrawal of ${amount} is successful')

                # Updating database
                banks[user_bank][acct]["account details"]["balance"] -= amount
                banks[user_bank][acct]["account details"]["debits"].append(amount)

                # Reformatting balance
                new_balance = acct_detail["account details"]["balance"]

                print(f'Account balance is: {fig_reform(new_balance)}')

            else:
                print(f'Insufficient balance! Your account balance: '
                      f'{fig_reform(acct_detail["account details"]["balance"])}')
        else:
            print('Invalid amount entry!')

        return

    def transfer(acct, recip_bank_name, recip_acct):
        amount = input('Enter amount to transfer: $')
        sender_data = banks[user_bank][acct]
        recip_data = banks[recip_bank_name][recip_acct]

        if amount.replace(',', '').isdigit() and int(amount.replace(',', '')) > 0:
            if int(amount.replace(',', '')) <= sender_data['account details']['balance']:

                amount = int(amount.replace(',', ''))

                print(f'Dear {sender_data["first name"]}, you are about to send total amount of'
                      f' ${fig_reform(amount)} to \n\t\t {recip_data["first name"]} '
                      f'{recip_data["other name"][0]}., '
                      f'{recip_data["last name"].upper()}')

                verify = input('Are you sure about this?(Yes/No)').capitalize()
                if verify == 'Yes':

                    delay(10, 'Processing')
                    print('{:^100s}'.format('Transfer successful!'))

                    # For sender account
                    banks[user_bank][acct]['account details']['balance'] -= amount
                    banks[user_bank][acct]['account details']['debits'].append(amount)

                    # For recipient account
                    banks[recip_bank_name][recip_acct]['account details']['balance'] += amount
                    banks[recip_bank_name][recip_acct]['account details']['credits'].append(amount)
            else:
                print('\t\tInsufficient balance!')
        else:
            print('Invalid input! Please re-start the process.')

        return

    # => User login credentials

    user_acct = ''
    valid_credentials = False
    counter = 3

    user_bank_dict = banks[user_bank]

    while counter > 0:
        user_acct = input('Enter your account number: ')
        user_pin = input('Enter your account pin: ')

        if (user_acct.replace(' ', '').isdigit() and len(user_acct) == 10) and \
            (user_pin.replace(' ', '').isdigit() and len(user_pin) == 4):

            # => For wrong inputs
            if user_acct not in user_bank_dict or user_pin != user_bank_dict[user_acct]['pin']:
                    counter -= 1
                    if counter:
                        print('{:^50s}'.format(f'Error!!! Account not exist or wrong login credentials '
                                               f'was entered. ({counter} chances left) \n'))

                        continue

                    # if counter is exceeded
                    perform_trans = False
                    return transaction(bank_list, banks, user_bank, perform_trans)

            # If account exist
            valid_credentials = True
            break
        else:
            counter -= 1
            print(f'\t\tInvalid input as ACCOUNT NUMBER or PIN... ({counter} chances left)')

    if valid_credentials:
        # => Transaction options
        trans_opt = ['Back To Main Menu', 'Deposit', 'Withdraw', 'Transfer']

        # => Displaying options
        trans = help(trans_opt)
        if not trans:
            perform_trans = False
            return transaction(bank_list, banks, user_bank, perform_trans)

        # => Start transaction
        if trans == 1:
            deposit(user_acct)
        elif trans == 2:
            withdraw(user_acct)
        else:
            recipient_acct_num = input('Enter recipient account number: ')
            recipient_bank_index = help(bank_list, 'Bank')

            if (recipient_acct_num.isdigit() and
                len(recipient_acct_num) == 10) and recipient_bank_index is not False:

                recip_bank_name = bank_list[recipient_bank_index]
                if user_acct != recipient_acct_num:
                    if recipient_acct_num in banks[recip_bank_name]:
                        recip_data = banks[recip_bank_name][recipient_acct_num]

                        delay(3)
                        validate = input(f'Is recipient\'s name '
                                         f'{recip_data["first name"]} '
                                         f'{recip_data["last name"].upper()}?(Yes/no) ').capitalize()
                        if validate == 'Yes':
                            transfer(user_acct, recip_bank_name, recipient_acct_num)
                    else:
                        print('\t\tRecipient Account Not Exist!')
                else:
                    print('Error!!!')
                    return
            else:
                print('Invalid recipient details.')

        # => After transaction
        another_trans = input('Perform another transaction?(Yes/No) ').capitalize()
        if another_trans == 'Yes':
            return transaction(bank_list, banks, user_bank, perform_trans)

    # Quitting
    perform_trans = False
    return transaction(bank_list, banks, user_bank, perform_trans)


# => change_pin function
def change_pin(banks, user_bank):
    counter = 3

    while counter > 0:
        user_acct = input('Enter your account number: ')
        user_bank_dict = banks[user_bank]
        if user_acct.isdigit() and len(user_acct) == 10:
            if user_acct not in user_bank_dict:
                print('\t\t\tError!!! Account not exist.\n')

                user_input = input('Do you want to re-enter data?(Yes/No) ')
                if user_input.capitalize() == 'Yes':
                    return change_pin(banks, user_bank)

                # If "user_input" is 'No'
                return

            # If account exist
            user_pin = input('Enter your current pin: ')
            curr_pin = user_bank_dict[user_acct]['pin']
            if user_pin == curr_pin:
                delay(3, 'Checking')
                new_pin = create_pin()
                if not new_pin:
                    return

                # If pin is generated
                masked_pin = new_pin[0] + len(new_pin[1:]) * 'x'

                banks[user_bank][user_acct].update({'pin': new_pin, 'masked_pin': masked_pin})
                delay(5)
                print('{:^50s}'.format('Pin changed successfully!!!'))
                return

        counter -= 1
        delay(3)
        if counter:
            print('{:^50s}'.format('Error! Please try again.'))
            continue

    print('\t\t\tSession Closed...')
    return


# Balance function
def check_balance(bank_list, user_bank, banks, chances = 3):
    if chances == 0:
        print('{:^20s}'.format('See you next time'))
        return

    user_bank_dict = banks[user_bank]

    user_acct = input('Enter your account number: ')
    user_pin = input('Enter your account pin: ')

    if (user_acct.replace(' ', '').isdigit() and len(user_acct) == 10) and \
            (user_pin.replace(' ', '').isdigit() and len(user_pin) == 4):

        # => For wrong inputs
        if user_acct in user_bank_dict:
            if user_pin == user_bank_dict[user_acct]['pin']:

                user_first = user_bank_dict[user_acct]['first name']

                acct_balance = user_bank_dict[user_acct]['account details']['balance']
                acct_balance = fig_reform(acct_balance)

                delay(8)
                print('{:^50s}'.format(f'Dear {user_first}, your account balance is: ${acct_balance}'))
                print('{:^100s}'.format('Thank you\n'))
                return

    # For wrong login credentials
    chances -= 1
    user_input = ''
    delay(3)

    if chances:
        print(
            '{:^50s}'.format(
                f'Error!!! Account not exist or wrong login credentials '
                f'was entered. ({chances} chances left) \n'
            )
        )
        user_input = input('Try to login again?(Yes/no) ').capitalize()

    if user_input == 'Yes':
        return check_balance(bank_list, user_bank, banks, chances)

    return


# => help function
def help(opt_list, suffix = ""):
    delay(3)
    chances = 3
    # => Options display function
    def display_opt():
        num = 1
        for bank in opt_list:
            print(f'"{num}" {bank} {suffix}')
            num += 1
        print()
        return num

    while chances > 0:
        # => Displaying functions
        opt_length = display_opt()
        user_input = input('==> Enter option here: ')

        if user_input.replace(' ', '').isdigit() and 0 < int(user_input) <= opt_length:
            opt_index = int(user_input) - 1
            return opt_index
        else:
            chances -= 1
            if chances:
                print(f'Error! Please select the right option... {chances} chance(s) left\n')
    return False


# => welcome function
def welcome(bank_list, profile_titles, banks, exploring = True):
    '''
    :param list bank_list: list
    :param list profile_titles:  list
    :param dict banks: dict
    :param bool exploring: bool
    :return:
    '''

    # => Closing program
    if not exploring:
        print('Program Closed!!! Thanks for using lanxCity')
        return

    # Display message
    global lanx_msg_counter
    if lanx_msg_counter == 1:
        print(lanx_msg)
        lanx_msg_counter -= 1

    # => user navigating options
    nav_list = [
        'Quit', 'Create account',
        'Perform Transaction', 'Check Account Balance', 'Change Pin'
    ]
    user_navigation = help(nav_list)
    if not user_navigation:
        exploring = False
        return welcome(bank_list, profile_titles, banks, exploring)
    # => Choosing user bank
    user_bank_index = help(bank_list, 'Bank')
    if user_bank_index is False:
        exploring = False
        return welcome(bank_list, profile_titles, banks, exploring)

    # => Exploration starts
    delay(5, 'Connecting To Bank')
    user_bank_name = bank_list[user_bank_index]
    if user_navigation == 1:
        print('{:^100s}'.format(f'Welcome to {user_bank_name}Bank Plc.'))
        print(f'Please fill out the following form with the right data to create a new account.\n')
        create_profile(bank_list, user_bank_name, profile_titles, banks)
        print()

    elif user_navigation == 2:
        print('{:^100s}'.format(f'Welcome to {user_bank_name}Bank Plc.'))
        transaction(bank_list, banks, user_bank_name)
        print()
    elif user_navigation == 3:
        check_balance(bank_list, user_bank_name, banks)
    else:
        print('{:^100s}'.format(f'Welcome to {user_bank_name}Bank Plc.'))
        change_pin(banks, user_bank_name)
        print()

    lanx_msg_counter = 1
    return welcome(bank_list, profile_titles, banks, exploring)

# ================> End


welcome(bank_list, profile_titles, banks)


