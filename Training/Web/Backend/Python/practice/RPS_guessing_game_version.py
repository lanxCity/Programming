# ------------------------Rock Paper Scissors
import math
from random import random

choices = ["rock", 'paper', 'scissors']
msg = '''
Welcome to "Rock", "Paper", "Scissors" (RPS) guessing game version. Ready to have some fun?!
                Let's get started...
'''

player_list = []

def create_player(players, counter = 3, add_player = True):
    profile = {}

    if counter == 0:
        print('Seems no player to be added... Let\'s start a new game then.')
        return

    def gen_id():
        id = ''
        for _ in range(3):
            id += str(math.floor(random() * 10))

        for player in players:
            if player['id'] == id:
                return gen_id()
        return id
    if add_player:
        player = input('Enter your username: ')
        if not player:
            player = f"Player {len(players) + 1}"

        player_id = gen_id()

        profile.update({'name': player, 'id': player_id, 'points': 0, 'valid': False})
        print(f'\t\t Welcome on board {profile["name"]} of id "{profile["id"]}". Please note your name '
              f'and id for future purposes.')
        players.append(profile)

    # Add new player
    user_input = input('Add another player?(Yes/No)').capitalize()

    if user_input == 'Yes':
        counter = 3
        add_player = True
        return create_player(players, counter, add_player)
    elif user_input == 'No':
        return
    else:
        counter -= 1
        add_player = False
        print(f'Sorry, no valid response... And you have {counter} chances left')
        return create_player(players, counter, add_player)

def remove_player(players):

    counter = 3
    done = False

    while counter > 0:
        user_input = input('Enter your name or id: ')
        if user_input:
            for data in players:
                if user_input.isnumeric() or user_input.isalnum():
                    if data['id'] == user_input or data['name'] == user_input:
                        print(f'Player {data["name"]} removed successfully')
                        players.remove(data)
                        done = True
                        break
            else:
                counter -= 1
                print(f"Sorry, Player does not exit. And you have {counter} chances left")
                continue
        else:
            counter -= 1
            print(f'\tno valid response! And you have {counter} chances left')
            continue
        if done:
            user_input = input('Remove another player? (Yes/No)').capitalize()
            if user_input == 'Yes':
                if len(players) > 1:
                    return remove_player(players)
                else:
                    print('Sorry, there must be at least a player!')
                    return
            else:
                print('Ok. Enjoy the game!')
                return

    else:
        print('Since we\'ve got no valid response, we believe you want to continue the game.')
        return

def final_rslt(players):
    print()
    print('\tPlayer <==> points')
    counter = 0
    loser = players[0]['points']
    winner = players[0]['points']

    for ply in players:
        if ply['points'] <= loser:
            loser = ply['points']
        elif ply['points'] >= winner:
            winner = ply['points']

    if len(players) > 1:
        for ply in players:
            if ply['points'] == winner:
                ply.update({'status' : 'Winner'})
            elif ply['points'] == loser:
                ply.update({'status': 'Loser'})

        for player in players:
            counter += 1
            if 'status' in player:
                print(
                    f'{counter}.\t'
                    f'{player["name"]}\t  '
                    f'{player["points"]}({player["status"]})'
                    )
            else:
                print(
                    f'{counter}. '
                    f'{player["name"]}\t  '
                    f'{player["points"]}'
                )
    else:
        print(
            f' => {players[0]["name"]}\t\t '
            f'{players[0]["points"]}'
        )
    return

def play_game(players, choice_list, start_game = True):
    def ans():
        choice = math.floor(random() * len(choice_list))
        return choice_list[choice]

    def title(data):
        print()
        for el in data:
            print(f'**** {el} ****')

        return

    def players_choices(data):
        for player in data:
            title(choice_list)
            print()
            player_ch = input(f'Enter {player["name"]}\'s choice: ')
            if player_ch.isalpha():
                player_ch = player_ch.lower()

            player.update({'choice': player_ch})

            # Hide the player's choice until the player
            if data.index(player) != len(data) - 1:
                print(20 * '*********** NO CHEATING *************\n')
        return

    def rslt(data, ans):
        print(f'Correct answer was "{ans}"\n')
        # creating table
        print('\tPlayer \t Choice \t Valid \t points')
        counter = 0
        for player in data:
            player['valid'] = False
            counter += 1
            if player['choice'] == ans:
                player['points'] += 5
                player['valid'] = True

            if player['valid']:
                print(f'{counter}.   ' 
                       f'{player["name"]}\t'
                       f'{player["choice"]}\t\t'
                       f'{player["valid"]}(Winner)  '
                       f'{player["points"]}')
            else:
                print(
                    f'{counter}.  '
                    f'{player["name"]}\t '
                    f'{player["choice"]}\t\t'
                    f'{player["valid"]}\t  '
                    f'{player["points"]}'
                    )
        print()
        return

    def start():
        computer_choice = ans()
        print('\t\tOkay. Have your coffee ready...And enjoy!')
        players_choices(players)
        rslt(players, computer_choice)
        return

    def init():
        print(msg)
        create_player(players)
        start()
        return

    init()

    while start_game:
        play_again = input('Continue to play game?(Yes/No) ').capitalize()
        if play_again == 'Yes':
            add_remove = input('"1" to add player, "0" to remove player, "5" to continue: \n')
            if add_remove and add_remove.isnumeric():
                if int(add_remove) == 1:
                    create_player(players)
                    start()
                    continue
                elif int(add_remove) == 0:
                    if len(players) > 1:
                        remove_player(players)
                        start()
                        continue
                    else:
                        print('Sorry, there must be at least a player!')
                        continue
                elif int(add_remove) == 5:
                    start()
                    continue
            else:
                print('\tNo valid response!')
                continue
        elif play_again == 'No':
            print()
            print('\tThanks for trying this game. Hope you all had fun...')
            print('\t  ************ Final Result **********')
            final_rslt(players)
            start_game = False
        else:
            print('\tNo valid response!')
            continue

    return

play_game(player_list, choices)




