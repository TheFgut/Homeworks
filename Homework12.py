import datetime
import requests
import re


def get_currency_info(response):

    currency_str_list = re.split(r"<currency>", response.text.replace("</currency>", ""))
    if len(currency_str_list) <= 1:
        return None
    currency_str_list.remove(currency_str_list[0])
    currency_str_list[-1].replace("</exchange>", "")

    currency_lst = []
    for currency_str in currency_str_list:
        strs = re.findall(r"[\w<>\./ ()]+", currency_str)
        strs.remove(strs[-1])


        currency_params = []
        for s in strs:
            param = re.findall(">[\w\.() ]+<", s)
            currency_params.append(param[0][1:-1])
        currency_lst.append(currency_params)
    if len(currency_lst) == 1:
        return currency_lst[0]
    return currency_lst


def write_data(courses_info):
    file_object = open(r"Courses.txt", "w")
    if courses_info is None:
        file_object.write("No info")
        return
    for crs_inf in courses_info:
        file_object.write(f"{crs_inf[1]} to UAH: {crs_inf[2]}")


res = None
while True:
    answer = input("Choose date(format - YYYY.MM.DD):\n")
    if answer == "Today":
        res = requests.request('GET', "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange")
    else:
        if re.fullmatch(r"\d{4}.\d{2}.\d{2}", answer) is None:
            print("Incorrect input")
            continue
        date = answer.split(".")
        try:
            datetime.date(int(date[0]), int(date[1]), int(date[2]))
            res = requests.request('GET', f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date='
                                          f'{date[0]}{date[1]}{date[2]}')
        except ValueError:
            print("Incorrect date value")
            continue
    courses_info = get_currency_info(res)
    write_data(courses_info)
    break















