number = int(input("Number: "))
number_str = str(number)


def palindrom(number_str: str) -> bool:
    """
    Функция переворачивает число и сравнивает его с тем, которое мы передали. Если переданное число и
    перевернутое число равны между собой, то функция возвращает True, иначе False
    """
    new_number_str = ''
    for item in range(len(number_str)-1, -1, -1):
        new_number_str += number_str[item]

    new_number_int = int(new_number_str)

    if number == new_number_int:
        return True
    else:
        return False


print(palindrom(number_str))