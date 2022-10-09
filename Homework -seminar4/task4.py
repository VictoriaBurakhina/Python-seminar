# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x^2 + 4*x + 5 = 0 или x^2 + 5 = 0 или 10*x^2 = 0


from random import randint
import itertools

k = randint(0, 10)

def get_number(k):
    number = [randint(0, 10) for i in range (k + 1)]
    while number[0] == 0:
        number[0] = randint(1, 10)
    return number

def get_polynomial(k, number):
    var = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(number, var, range(k, 1, -1), fillvalue = '') if a !=0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x',' x')


num = get_number(k)
polynom = get_polynomial(k, num)
print(polynom)

with open('poly.txt', 'w') as file:
    file.write(polynom)
    file.close()