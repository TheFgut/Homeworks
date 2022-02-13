from random import randint


def guess_num_game():
    computer_guess = randint(minNum, maxNum)
    prev_guess = 0
    while True:
        player_guess = ask_player_number()
        if player_guess != computer_guess:
            data = check_is_it_near(player_guess, computer_guess, prev_guess)
            print(data[1])
            prev_guess = data[0]
        else:
            print(f"Number {player_guess} is correct! You are winner!")
            return


def check_is_it_near(real, expected, previous_dif):
    """
    :param real: player guess int
    :param expected: real int
    :param previous_dif: previous difference int
    :return: list data
    data[0] = difference between real and expected,
    data[1] = verdict
    """
    answers = ["Less ", "Cold", "Warm", "er", "Hot", "Hotter"]

    data = [abs(real - expected)]
    if previous_dif == 0 or previous_dif == data[0]:
        better_or_worse = None
    else:
        better_or_worse = previous_dif > data[0]

    result = ""
    if data[0] > 10:
        result = better_or_worse_func(better_or_worse, answers[1], answers[0] + answers[1], answers[1] + answers[3])
    if data[0] >= 5:
        result = better_or_worse_func(better_or_worse,answers[2], answers[2] + answers[3], answers[0] + answers[2])
    else:
        result = better_or_worse_func(better_or_worse, answers[4], answers[5], answers[0] + answers[4])
    data.append(result)
    return data


def better_or_worse_func(is_better_bool, default, if_better_text, if_worse_text):
    """
    :param is_better_bool: condition bool
    :param default: is_better_bool None condition
    :param if_better_text: is_better_bool True condition
    :param if_worse_text: is_better_bool False condition
    :return: string due to is_better_bool condition
    """
    result = default
    if is_better_bool:
        result = if_better_text
    elif is_better_bool is not None:
        result = if_worse_text
    return result


def ask_yes_or_no(msg):
    while True:
        print(msg)
        answer = input("type Y/N\n").lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        print("Incorrect input, try again")


def ask_player_number():
    while True:
        player_input = input(f"Input number from {minNum} to {maxNum}: ")
        try:
            num = int(player_input)
            if minNum <= num <= maxNum:
                return num
            else:
                print("Number is not in allowed range, try again")
        except ValueError as e:
            print("Invalid input, try again")


lvl = 1
minNum = 1
while True:
    print(f"Level {lvl}")
    maxNum = 10 + (lvl * 5)
    guess_num_game()

    answer = ask_yes_or_no("Do you want to continue?")
    if answer is False:
        break
    lvl += 1
