from tkinter import *
import cmath
from math import sqrt
import googletrans


#Validating input values and calculating result value
def calculate(string):
    try:
        res = sqrt(float(string))
        if(int(res) == float(res)):
            res = str(int(res))
        else:
            res = str(float(res))
        return res
    except ValueError:
        try:
            tmp = string
            tmp = tmp.replace(' ', '')
            res = str(cmath.sqrt(complex(tmp)))
            return res
        except ValueError:
            return 'Please, enter a number'


def calculate_big_numbers(number):
    pass


