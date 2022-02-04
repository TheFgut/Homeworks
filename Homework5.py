
# 1
def operation1(par1, par2):
    if type(par1) is type(par2) is int:
        return par1 + par2
    elif type(par1) is type(par2) is str:
        return par1 + par2
    elif type(par1) is str:
        return {par1: par2}
    else:
        tupl = (par1, par2)
        return tupl


# 2
def disassemble_word(word):
    length = 0
    signs = []
    pure_word = word.lower()
    for lettr in word:
        if lettr.isalpha():
            length += 1
        elif lettr != "’":
            pure_word = pure_word.replace(lettr, "")
            signs.append(lettr)
    return [length, pure_word, signs]


def parse_the_word(sentence):
    """
    :param sentence: принимает предложение
    :return dict: возвращает словарь
    key 0 - кол-во пробелов
    key 1:infinity - словарь слов с колличеством букв - key, из предложения
    """
    dictionary = {}
    words = sentence.split(" ")
    signs = []
    dictionary[0] = len(words) - 1
    for word in words:
        word_data = disassemble_word(word)
        for a in word_data[2]:
            signs.append(a)

        if dictionary.get(word_data[0]) is None:
            dictionary[word_data[0]] = [word_data[1]]
        elif word_data[0] > 0:
            dictionary.get(word_data[0]).append(word_data[1])

    dictionary["Signs"] = tuple(signs)
    for key, value in dictionary.items():  # удаляет повторяющиеся данные
        if key != 0:
            dictionary[key] = list(set(value))
    return dictionary

def print_task1_result():
    print("Task 1\n")

    i1, i2 = 5, 3
    print(f"int1: {i1}")
    print(f"int2: {i2}")
    print(f"two Ints: {operation1(i1, i2)}\n")

    str1, str2 = "sda", "dasd"
    print(f"string1: {str1}")
    print(f"string2: {str2}")
    print(f"two strings: {operation1(str1, str2)}\n")

    print(f"string1: {str1}")
    print(f"not string2: {i1}")
    res = operation1(str1, i1)
    print(f"result({type(res)}): {res}\n")

    res = operation1(i2, str2)
    print(f"other({type(res)}): {res}")
    print("\n\nTask2\n")

# выводит результат первого задания
print_task1_result()

# выполняет второе задание
# читает текстовый файл и разбирает содержимое функцией parse_the_word()
result = ""
way = input("Input way to open txt file:\n")
#"stih.txt"
try:
    if way[len(way)-4:] == ".txt":
        file = open(way, "r", encoding="utf8")
        text = file.readlines()
        txt = ""
        for t in text:
            txt += " " + t
        result = parse_the_word(txt)
        file.close()
    else:
        print("Not a txt file")
except FileNotFoundError as err:
    print("File not found")


print(result)


