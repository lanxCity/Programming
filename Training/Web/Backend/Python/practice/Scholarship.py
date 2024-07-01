# # -------------------------------------------------Project 1------------------------

# -----The list of details title
details_titles = ['matric no.','first name','last name','level','year of birth']

# -----Creating an empty list to store the profile of each applicant
welcome_message = '''\nWELCOME TO LANXCITY UNDERGRADUATE STUDENTS SCHOLARSHIP PAGE.
=>>>NOTE: Dear student, this opportunity is strongly for undergraduate students of the 
\tUniversity of Ibadan alone. Good Luck!!!\n'''
list_of_applicants = []



# ==>Validating each data input
def validata_data_input(input,title):
    validated = False

    # 1. validating each data
    if input:
        if title == 'matric no.':
            if input.isdigit() and len(input) == 6:
                validated = True

        elif title == 'first name' or title == 'last name':
            if input.isalpha():
                validated = True

        elif title == 'level' or title == 'year of birth':
            if input.isnumeric():
                validated = True

    # ------After validation
    if validated:
        return validated
    else:
        return False

# ==> Create new profile
def create_new_profile(titles):

    profile = {}
    data_validated = False
    print('\n\t Hi! Please, fill out the form...')
    for title in titles:
        user_input = input(f'Enter your {title}? ')
        data_validated = validata_data_input(user_input,title)
        if data_validated:
            profile.update({title:user_input})
            continue
        else:
            data_validated = False
            break

    if data_validated:
        age = str(2022 - int(profile['year of birth']))
        profile.update({'age': age})
        return profile
    else:
        print('\tIs either you\'ve entered invalid data or nothing')
        print('\t Please, restart the application process with valid infomation')
        return create_new_profile(titles)


# ==> Checking for existing profile
def existing_profile_checking(data_input,list):

    def check(data):
            for profile in list:
                if data == profile['matric no.']:
                    return True
            return False

    # Checking if profile exist before or after new reg.
    if type(data_input) is str:
        return check(data_input)
    else:
        return check(data_input['matric no.'])


# ==>Creating the Table of all applicants.
def applicants_table(my_list):

    table = ''

    def table_head(titles):
        row = ""
        for title in titles:
            row += ' '
            row += title
            row += ' '
        row += '\n'
        return row

    def table_row(item):
        row = ""
        for el in item:
            row += item[el]
            row += '\t\t'
        row += '\n'
        return row

    if type(my_list) is dict:
        table += table_head(my_list)
        table += table_row(my_list)
        return table

    elif type(my_list) is list:
        data = my_list[0]

        table += table_head(data)
        numbering = 0
        for profile in my_list:
            numbering += 1
            table += f'{numbering}. {table_row(profile)}'
        return table


# -----Creating welcoming function
def welcome_function(titles, my_list):
    chances_counter = 3
    if not my_list:
        print(welcome_message)

    # ---------------Initialising
    def initialise():

        apply_msg = ""
        if not my_list:
            apply_msg = input('Do you want apply? (Yes/No) ').capitalize()
        else:
            apply_msg = input('Apply for others? (Yes/No) ').capitalize()

        if apply_msg:
            if apply_msg.isalpha():
                if apply_msg == 'Yes':
                    return True
                elif apply_msg == 'No':
                    return False
        else:
            return 'unverified'

    # -----------End initialisation

    while chances_counter > 0:
        start = initialise()
        chances_counter -= 1
        if start is True:
            # Check if the list is empty
            if not my_list:
                new_profile = create_new_profile(titles)
                my_list.append(new_profile)
                print(f'\n\tDear {new_profile["first name"]}, your data is received\n')
                print(applicants_table(new_profile))
                return welcome_function(titles,my_list)
            else:

                # Verifying new applicant against existing data
                profile_exist = True
                counter = 3
                while profile_exist and counter > 0:
                    new_mat_num = input('Please, enter matric number to check if data exist or not? ')
                    if new_mat_num.isnumeric() and len(new_mat_num) == 6:
                        profile_exist = existing_profile_checking(new_mat_num,my_list)
                        if profile_exist:
                            counter -= 1
                            print(f'\t\t Sorry! profile exist already. And you have {counter} '
                                  f'chance(s) left')
                            continue
                        else:
                            break
                    else:
                        counter -= 1
                        print(f'\n\tERROR! you\'ve either entered nothing or wrong value. '
                              f'And you have {counter} chance(s) left.....')
                        continue
                else:
                    print(f'-----Seems you are not ready. See you next time...')
                    return

                if profile_exist is False:
                    new_profile = create_new_profile(titles)
                    profile_exist = existing_profile_checking(new_profile,my_list)
                    if profile_exist is False:
                        my_list.append(new_profile)
                        print(f'\n\tDear {new_profile["first name"]}, your data is received\n')
                        print(applicants_table(new_profile))
                        return welcome_function(titles,my_list)
                    else:
                        print(f'\t\t But I think I said data already exist!!!')
                        print(f'Seems you are not ready. See you next time...')
                        return
        else:
            if start is False:
                print('Okay dear. See you next time. And if you\'d apply before, '
                      'check back to see if you\'ve been shortlisted.')
                print('\n\t\t\t DETAILS OF APPLICANTS SO FAR\n')
                if my_list:
                    print(applicants_table(my_list))
                    return
                else:
                    print('--------------------No Student has applied so far-------------')
                    return
            else:
                print(f'\n\tERROR! you\'ve either entered nothing or wrong value. '
                 f'And you have {chances_counter} chance(s) left.....')
                continue
    else:
        print(f'\t\tOkay. Seems you are not ready. See you next time...')
        return


# ------------------------Running my program
welcome_function(details_titles, list_of_applicants)




