import time


def illusion():

    timer = 3
    sleepTime = 0.3
    while timer > 0:
        the_text = f"Changing mode, please wait - {timer}"
        print(the_text)
        time.sleep(sleepTime)
        timer -= 1


def task1():
    input_text = "Input word to analise: "
    word = str(input(input_text))
    number = 0

    while True:
        try:
            input_text = "Input number of letter: "
            number = int(input(input_text))
        except ValueError as e:
            print(NotANumbErrMsg)
            continue
        break

    try:
        letter = word[number]
        final_msg = f"The {number} symbol in {word} is {letter}"
        print(final_msg)
    except IndexError as e:
        error_msg = "Something went wrong! Letter number \"{}\" does not exist"
        print(error_msg.format(number))


def task2():
    input_text = "Now input a sentence: "
    sentence = input(input_text)
    words_list = sentence.split(" ")

    words_with_o_counter = 0
    for w in words_list:

        if w.lower()[-1] == "o":
            words_with_o_counter += 1
    final_msg = "Words with character \"o\" at the end: " + str(words_with_o_counter)
    print(final_msg)


def task3():
    lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
    lst2 = []
    for element in lst1:
        if isinstance(element, type("")):
            lst2.append(element)
    print(lst1)
    print(lst2)


def choose_action(action):
    actions_str = "\"1\" - to try again, \"2\" - to choose another task, \"3\" - exit \nInput: "
    while True:
        number_of_action = 0
        try:
            number_of_action = int(input(actions_str))
        except ValueError as e:
            print(NotANumbErrMsg)

        if number_of_action == 1:
            action()
        elif number_of_action == 3:
            quit()
        elif number_of_action == 2:
            break
        else:
            print("Action doesn't exist")


NotANumbErrMsg = "Not a number! Try again"

taskList = [task1, task2, task3]
while True:
    text = "Which task do you want to check?\n Input the number: "

    enableProceed = False
    numberOfTask = 0
    try:

        numberOfTask = int(input(text)) - 1
        taskList[numberOfTask]
        enableProceed = True
    except ValueError as e:
        print(NotANumbErrMsg)
    except IndexError as e:
        errMsg = "Action doesn't exist"
        print(errMsg)

    if enableProceed:
        illusion()
        taskList[numberOfTask]()
        choose_action(taskList[numberOfTask])