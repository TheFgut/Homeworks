import re


class CarNumber:
    value = ""
    limits = ['[A-Z]{2}[0-9]{4}[A-Z]{2}', "[0-9]{2}\s[0-9]{3}-[0-9]{2}\s[A-Z]{2}",
                "[a-z]{1}[0-9]{5}[A-Z]{2}"]

    def __init__(self, value, need_to_check=True):
        """

        :param value: number value
        :param need_to_check: if you have enough money to make number without any limitations - set this to False
        """
        if need_to_check:
            if self.check(value) is False:
                print("car_number init error, incorrect value")
            else:
                self.value = value
        else:
            self.value = value

    def check(self, value):
        for limit in self.limits:
            coincided = re.fullmatch(limit, value)
            if coincided:
                return value
        return False

    def find_all_ret_str_list(text):
        """
        :param text: text where method will look
        :return: list of strings with car numbers from text or False if nothing found
        """
        lst = []
        for limit in CarNumber.limits:
            coincided = re.findall(limit, text)
            if coincided:
                lst.extend(coincided)
        if len(lst) != 0:
            return lst
        return False

    def find_all_ret_car_num_obj_list(text):
        """
        :param text: text where method will look
        :return: list of CarNumber objects or False if nothing found
        """
        lst = []
        for limit in CarNumber.limits:
            coincided = re.findall(limit, text)
            if coincided:
                for coincidence in coincided:
                    lst.append(CarNumber(coincidence, True))
        if len(lst) != 0:
            return lst
        return False


txt = "AB1234CD  12 345-67 AB  a12345BC"
lst = CarNumber.find_all_ret_str_list(txt)
print(lst)

lst = CarNumber.find_all_ret_car_num_obj_list(txt)
for part in lst:
    print(part.value)


