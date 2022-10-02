"""
Домашнее задание №1
Функции и структуры данных
"""

"""
power_numbers
функция, которая принимает N целых чисел,
и возвращает список квадратов этих чисел
>>> power_numbers(1, 2, 5, 7)
<<< [1, 4, 25, 49]
"""

def power_numbers(*nums):
    newlist = []
    for num in nums:
        newlist.append(num ** 2)
    return newlist




# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

#Функции для проверки числа
def is_prime(num):
    if num == 1:
        return None
    else:
        count = 0
        for i in range(2, num // 2 + 1):
            if (num % i == 0):
                count = count + 1
        if (count <= 0):
            return num
        else:
            return None


def is_even(num):
    if num % 2 == 0:
        return num
    else:
        pass

def is_odd(num):
    if num % 2 != 0:
        return num
    else:
        pass

def filter_numbers(list, text):
    newlist = []
    for num in list:
        if text == ODD and is_odd(num):
            newlist.append(num)
        elif (text == EVEN and is_even(num)):
            newlist.append(num)
        elif text == PRIME and is_prime(num):
            newlist.append(num)
        else:
            pass
    return newlist



"""Я не смог  использовать filter в функции filter_numbers"""




