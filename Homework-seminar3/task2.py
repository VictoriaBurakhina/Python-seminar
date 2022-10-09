#Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#Пример:

#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

from random import sample

number_of_elements = int(input("Введите число элементов списка "))

def get_array (number_of_elements):
    array = sample(range(1, 10), number_of_elements)
    return array

def multiply(array):
    result = []
    if len(array) % 2 == 0:   #проверяем четное количество элементов в массиве или нет
        length = len(array)//2
    else:
        length = len(array)//2 + 1
    for i in range(0, length):
        if i != len(array) - i - 1:
            mult = array[i] * array[len(array) - i - 1]
        else:
            mult = array[i]
        result.append(mult)
    return result

my_array = get_array(number_of_elements)
print(my_array)
print(multiply(my_array))



