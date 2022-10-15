#Вычислить число c заданной точностью d
#Пример:
#при d = 0.001, π = 3.141 10^(-1) ≤ d ≤10^(-10)

from decimal import *

def get_number(number,accuracy):
    number = Decimal(number).quantize(Decimal(accuracy), rounding=ROUND_UP)
    return number

number = input("Число: = ")
accuracy = input("Точность: ")
print(get_number(number, accuracy))