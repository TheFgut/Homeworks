# Rock Scissors Paper
from random import choice as random_choice, shuffle


def user_choice(*variants):
    msg = f'Choose one of: {", ".join(variants)}: \n'
    while True:
        user_input = input(msg)
        if user_input not in variants:
            print('Wrong!')
        else:
            return user_input


def computer_choice(*variants):
    variants = list(variants)
    shuffle(variants)

    result = random_choice(variants)

    return result


def is_user_win(rules_to_win, user_figure, computer_figure):
    """
    Args:
        rules_to_win:
        user_figure:
        computer_figure:
    Returns:
        (bool|None)
    """
    if user_figure == computer_figure:
        return

    for fig in rules_to_win[user_figure]:
        if fig == computer_figure:
            return True

    return False


def make_message(result, user_figure, computer_figure):

    dct = {
        True: 'User win',
        False: 'Computer win',
        None: 'Draw!',
    }

    msg = f'User - {user_figure}, computer - {computer_figure}, result is - {dct[result]}\n'

    return msg


def save_game_data(username, game_result, user_figure, computer_figure):
    data_file_name = "data_file.txt"
    try:
        opened_file = open(data_file_name, mode='a')
    except ValueError as v:
        opened_file = open(data_file_name, mode='w')

    result_names = {True: "user_win", False: "computer_win", None: "Draw"}
    opened_file.write(f"User - {username}, result - {result_names[game_result]}, "
                         f"User figure - {user_figure}, computer figure- {computer_figure}\n")
    opened_file.close()


def read_winners_statistics():
    """

    :return: dict[line number] = string with player name and count of games where he was winner in it
    """
    data_file_name = "data_file.txt"

    data = []
    try:
        opened_file = open(data_file_name, mode='r')
    except FileNotFoundError as f:
        data.append("No rating data\n")
        return data

    lines = opened_file.readlines()
    opened_file.close()
    players_info = {}
    for line in lines:
        info = line.split(" ")
        info[2] = info[2].replace(",", "")
        if info[5].replace(",", "") == "user_win":
            if players_info.get(info[2]) is None:
                players_info[info[2]] = 1
            else:
                players_info[info[2]] += 1
    if len(players_info.items()) == 0:
        data.append("No top players\n")
        return data

    data.append("Win statistics:\n")

    for key, info in players_info.items():
        data.append(f"{key} - {info}")
    data.append("\n")
    return data


def rsp_game():

    rules_to_win = {
        'Scissors': ['Paper', 'Lizard'],
        'Paper': ['Rock', 'Spok'],
        'Rock': ['Lizard', 'Scissors'],
        'Lizard': ['Spok', 'Paper'],
        'Spok': ['Scissors', 'Rock'],
    }

    user_figure = user_choice(*rules_to_win.keys())

    computer_figure = computer_choice(*rules_to_win.keys())

    game_result = is_user_win(rules_to_win, user_figure, computer_figure)

    global username
    save_game_data(username, game_result, user_figure, computer_figure)

    message = make_message(game_result, user_figure, computer_figure)

    return message


def print_statistics():
    data = read_winners_statistics()
    for line in data:
        print(line)


def ask_what_action_to_do(msg):
    while True:
        reply = input(msg).lower()
        if reply == "y":
            return True
        if reply == "stats":
            print_statistics()
            continue
        if reply == "n":
            return False
        print("Don't understand, please write again")


username = input("Write your name: ")

print_statistics()

while True:

    result = rsp_game()
    print(result)

    if ask_what_action_to_do("Do you want to play again?\n Y/N or \"stats\" to look win statistics\n") is False:
        break

