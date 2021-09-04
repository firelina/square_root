from tkinter import *
import cmath
from math import sqrt
from decimal import Decimal
# import gmpy
from sys import maxsize
import googletrans


# ычисление квадратного корня небольших чисел и комплексных, возвращает либо результат вычислений, либо ошибку
def calculate(string):
    try:
        res = sqrt(float(string))

        if(int(res) == float(res)):
            res = str(int(res))
        else:
            res = str(float(res))
        return res
    except OverflowError:
        return calculate_big_numbers(int(string))

    except ValueError:
        try:
            tmp = string
            tmp = tmp.replace(' ', '')
            res = str(cmath.sqrt(complex(tmp)))
            return res
        except ValueError:
            return 'Please, enter a number'


# вычисление корня из очень больших чисел
def calculate_big_numbers(number):
    high = 1
    degree = 2

    while high ** degree < number:
        high *= 2
    low = high // 2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid ** degree < number:
            low = mid
        elif high > mid and mid ** degree > number:
            high = mid
        else:
            return mid
    return mid + 1


# вычисление корня из очень больших чисел
def calculate_big_numbers1(number):
    degree = 2
    nd = Decimal(number)
    exponent = Decimal("1.0") / Decimal(degree)
    return nd ** exponent
