from lib import check_allowance

while True:
    sentence = input("Write something: ")
    print(sentence)

    print("Do you want to try again?")
    if check_allowance() is False:
        break
