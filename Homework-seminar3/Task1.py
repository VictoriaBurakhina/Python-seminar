#1. Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

from random import sample

number_of_elements = int(input("Введите количество элементов списка "))

def get_array(number_of_elements):
    array = sample(range(1, 20), number_of_elements)
    return array

def sum_of_odd_elements(array):
    sum = 0
    for i in range(0, len(array), 2):    #указываем шаг 2
        sum = sum + array[i]
    return sum

my_array = get_array(number_of_elements)
print(my_array)
print(sum_of_odd_elements(my_array))