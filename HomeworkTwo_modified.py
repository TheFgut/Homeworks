import lib


def check_age():
    age = None
    try_counter = 0
    try_limit = 5
    while try_counter <= try_limit:

        age = input("Введите возраст:")

        if age.isdigit():
            age = int(age)
            return age
        elif try_counter == try_limit:
            result = "Попытки закончились. До свидания!"
            print(result)
            age = None
        else:
            result = f"Я не понимаю, попробуйте ответить снова. Попыток осталось: {try_limit - try_counter}"
            print(result)
        try_counter += 1


def find_age_word_form(age):
    year_strings = ["год", "года", "лет"]
    if age == 11:
        return year_strings[2]
    age = age % 10
    return {
        True: year_strings[2],
        age < 5: year_strings[1],
        age == 0: year_strings[2],
        age == 1: year_strings[0]
    }[True]


def age_analysis(age):

    year_word = find_age_word_form(age.__abs__())

    answers = [f"Тебе {age} {year_word}, где твои мама и папа?",
               f"Тебе {age} {year_word}, а мы не продаем сигареты несовершеннолетним",
               f"Вам уже {age} {year_word}, вы в зоне риска",
               f"Оденьте маску, вам же {age} {year_word}!",
               "Иисуса знаете?",
               f"Даже представить не могу что вам {age} {year_word}"]

    return {
        True: answers[3],
        age < 18: answers[1],
        age < 7: answers[0],
        age > 65: answers[2],
        age > 2000: answers[4],
        age < 0: answers[5]
    }[True]


while True:
    userAge = check_age()
    if userAge is not None:
        result = age_analysis(userAge)
        print(result)
    print("Чтобы попробовать снова")
    if not lib.check_allowance():
        break
