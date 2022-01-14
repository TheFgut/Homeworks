# task 1 "age input" with input checker and limited attempts
age = None
tryCounter = 0
tryLimit = 5
while tryCounter <= tryLimit:

    age = input("Your age:")

    if age.isdigit():
        age = int(age)
        break
    elif tryCounter == tryLimit:
        result = "Club is closed now!"
        print(result)
        age = None
    else:
        result = f"Incorrect input, try again. Attempts left: {tryLimit - tryCounter}"
        print(result)
    tryCounter += 1

if age is not None:
    # task 2 "answers according to age"
    answers = ["Where is your parents?", "Where is your vaccination certificate?", "We don't sell alcohol to minors!",
               "Discount for pensioners today!", "Wear your mask please!"]

    if age < 7:             # condition 1
        print(answers[0])
    elif age % 10 == 0:     # condition 4
        print(answers[1])
    elif age < 18:          # condition 2
        print(answers[2])
    elif age > 65:          # condition 3
        print(answers[3])
    else:                   # condition 5
        print(answers[4])
