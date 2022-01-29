# 1
import random


glasnie = ("а", "о", "и", "е", "ё", "э", "ы", "у", "ю", "я")
soglasnie = ("б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ")


# генератор предложения (гласная с небольшим шансом дублируется и иногда утраивается)
def gen_sentence(words_count, min_word_length, max_word_length):
    sentence = ""

    word_dict = ["" for _ in range(words_count)]
    word_dict[0] = chr(random.randint(1040, 1071))
    word_counter = len(word_dict) - 1
    for word in word_dict:
        letters_count = random.randint(min_word_length, max_word_length)

        switcher = True if random.randint(0, 3) == 1 else False
        while letters_count > 0:
            if switcher:
                letter = glasnie[random.randint(0, len(glasnie) - 1)]
                word += letter * 2 if random.randint(0, 8) == 1 else letter
                if random.randint(0, 4) == 1:
                    word += letter

                switcher = False
            else:
                word += soglasnie[random.randint(0, len(soglasnie) - 1)]
                switcher = True
            letters_count -= 1

        if word_counter > 0:
            word += chr(32)
        sentence += word
        word_counter -= 1

    sentence += chr(33)
    return sentence


def glasnaya_check(letter):
    for ltr in glasnie:
        if letter == ltr:
            return True
    return False


def find_shortest_word(sentence):
    words = sentence.split(" ")
    smallest_word = None

    for word in words:
        prev_let = ""
        letters_repeated = 0
        with_doubled_glasn = False
        for letter in word:  # проверка на дублирование гласной, тройной повтор и более пропускается
            if letter == prev_let:
                letters_repeated += 1
                if glasnaya_check(letter) is False:
                    letters_repeated = 0
            elif letters_repeated == 1:
                with_doubled_glasn = True
                break
            else:
                letters_repeated = 0
            prev_let = letter
        if with_doubled_glasn:
            if smallest_word is None or len(smallest_word) > len(word):
                smallest_word = word

    return smallest_word


wordsCount = random.randint(5, 8)
Sentence = gen_sentence(wordsCount, 3, 8)
phrase1 = "Один сумасшедший сказал: " + Sentence
print(phrase1)

shortest = find_shortest_word(Sentence)
phrase2 = "А второй ему ответил: "
if shortest is None:
    phrase2 += "Слов с удвоением гласных нет"
else:
    phrase2 += "Самое короткое слово с двумя гласными подряд это - " + shortest
print(phrase2)

# 2
shopsInfo = {"citrus": 47.999, "istudio": 42.999, "moyo": 49.999, "royal-service": 37.245,
             "buy.ua": 38.324, "g-store": 37.166, "ipartner": 38.988, "sota": 37.720, "rozetka": 38.003}
minPrice = 38
maxPrice = 40
matchShops = "Match: "

for name, price in shopsInfo.items():
    if maxPrice > price > minPrice:
        matchShops += name + ", "

lLimit = "\nLower limit: " + str(minPrice)
hLimit = "Higher limit: " + str(maxPrice)
print(lLimit)
print(hLimit)
print(matchShops)
