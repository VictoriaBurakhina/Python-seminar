#4. Задайте список из
#из промежутка [-N, N].
# Найдите произведение элементов на
# указанных позициях. Позиции хранятся
# в файле file.txt в одной строке одно число.


from random import randint

def func (N):
    lst = []
    mult = 1
    for i in range(N):
        lst.append(randint(-N, N))
    file = open("../../IdeaProjects/Python-seminar/homeWork-seminar2/file.txt", "r")
    for line in file:
        print(line)
        mult *= lst[int(line)]
    file.close()

    print(mult)

if __name__ == "__main__":
    chislo = int(input("Input a number: "))
    func(chislo)