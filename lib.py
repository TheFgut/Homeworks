def check_allowance():
    while True:
        print("Write Y/N:")
        answer = input().lower()
        if isinstance(answer, type("")):
            if answer == "y":
                return True
            elif answer == "n":
                return False
        print("Incorrect input")

