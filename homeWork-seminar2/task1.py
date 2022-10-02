#1. Напишите программу, 
# которая принимает на вход 
# вещественное число и 
# показывает сумму его цифр.    
#    Пример:    
#    - 6782 -> 23
#    - 0,56 -> 11


def func(number):
    sum = 0
    number = number.replace(",", ".")

    print(number)

    for symbol in number:
        if symbol != ".":
         sum += int(symbol)
    return sum


if __name__ == "__main__":
    chislo = input("Введите число ")
    summary = func(chislo)
    print(summary)