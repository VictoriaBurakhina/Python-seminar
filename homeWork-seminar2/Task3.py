#3. Задайте список из n чисел последовательности (1+ 1/n)^n
# # и выведите на экран их сумму (округляйте до 3 знаков после запятой).

#Пример:

#- Для n = 6: [2, 2.25, 2.37, 2.441, 2.488, 2.522]

n = int(input('Введите число: '))
array = []
for i in range(1, n + 1):
    array.append(round(((1 + 1/i) ** i), 3))
sum = 0
for i in range(n):
    sum = sum + array[i]
print('Сумма всех чисел из списка ', array, 'равна', sum)
