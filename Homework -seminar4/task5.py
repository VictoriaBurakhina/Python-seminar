#Даны два файла,
# в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

def get_sum_polynomial():
    data1 = open('file1.txt', 'r', encoding='utf_8')
    data2 = open('file2.txt', 'r', encoding='utf_8')

    polynomial1 = data1.read()
    p1 = polynomial1.split(sep='\n')
    polynomial2 = data2.read()
    p2 = polynomial2.split(sep='\n')
    print(p1)
    print(p2)
    with open('out.txt', 'a', encoding='utf_8') as data_save:
            polynomial = []
            for i in range(len(p1)):
                p1[i] = p1[i].replace(' = 0', " + ")
                polynomial.append(p1[i] + p2[i])

                data_save.write('\n\n'.join(polynomial))

get_sum_polynomial()