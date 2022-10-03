# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# [1.1, 1.2, 3.1, 5, 10.01] => 0.19


import random

list = []
a = int(input("Введите количество элементов: "))
for i in range(a):
    list.append(round(float(random.random() * 100), 2))
print(f"Cписок:  {list}")


def find_diff(any_numbers):
    numbers = []
    for x in range(len(any_numbers)):
     numbers = numbers.__add__([round(any_numbers[x] - int(any_numbers[x]), 2)])
    print(numbers)
    return max(numbers) - min(numbers)

print('Разница между максимальным и минимальным значением дробной части = ', find_diff(list))
