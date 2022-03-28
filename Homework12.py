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
            if len(param) == 0:
                continue
            currency_params.append(param[0][1:-1])
        currency_lst.append(currency_params)
    if len(currency_lst) == 1:
        return currency_lst[0]
    return currency_lst


def write_data(courses_info, date):

    file_object = open(r"Courses.txt", "w")
    file_object.write(f"Courses from: {date.year}.{date.month}.{date.day}\n")
    counter = 1
    if courses_info is None:
        file_object.write("No info")
        return
    for crs_inf in courses_info:
        file_object.write(f"{counter}. {crs_inf[1]} to UAH: {crs_inf[2]}\n")
        counter += 1


res = None
date = datetime.date.today()
while True:
    answer = input("Choose date(format - YYYY.MM.DD):\n")
    if answer == "Today":
        res = requests.request('GET', "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange")
    else:
        if re.fullmatch(r"\d{4}.\d{2}.\d{2}", answer) is None:
            print("Incorrect input")
            continue
        date_str = answer.split(".")
        try:
            date = datetime.date(int(date_str[0]), int(date_str[1]), int(date_str[2]))
            res = requests.request('GET', f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date='
                                          f'{date_str[0]}{date_str[1]}{date_str[2]}')
        except ValueError:
            print("Incorrect date value")
            continue
    courses_info = get_currency_info(res)
    write_data(courses_info, date)
    break
print("Done")















