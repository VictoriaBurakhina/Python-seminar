#Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

def find_simple_mult(n):
    list = []
    for i in range(2, int(n/2)+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            if n % i == 0:
                n = n / i
                list.append(i)
    return list

def main():
    num = int(input("Введите натуральное число: "))
    list = find_simple_mult(num)
    if len(list) > 0:
        print(f'Число {num} имеет простые множители: ')
        print(list)
    else:
        print(f"Число {num} является простым ")


main()









