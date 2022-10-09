#4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

#Пример:

#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10

number = int(input("Введите десятичное  число "))

def conversion_to_binary(number):
    result = []
    while number > 0:
        remains = number % 2
        number = number // 2
        result.append(remains)
    for i in range(len(result)//2):
        temp = result[i]
        result[i] = result[len(result)-i-1]
        result[len(result)-i-1] = temp
    return result

binary_number = conversion_to_binary(number)
for i in range(len(binary_number)):
    print(binary_number[i], end='')
