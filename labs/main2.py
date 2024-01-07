import math as m
import matplotlib.pyplot as plt
import numpy as n


def task1():
    k = 0
    while True:
        a = float(input('Введите значение'))
        if a <= 0:
            print(a, 'Не является кубом числа')
        elif a ** (1 / 3) == int(a ** (1 / 3)):
            print(a, 'Является кубом числа')
        else:
            print(a, 'Не являетcя кубом числа')
        for i in range(2, int(a) + 1):
            if a % i == 0:
                k += 1
            if k == 1:
                print(a, 'Является простым число')
            else:
                print(a, 'Не является простым число')
                break
def task2():
    def f1(x):
        return x ** 2 + 2 * x

    def f2(x):
        return -m.sin(x)

    obl_y = (int(input("введите область определения функции  \n ")), int(input()))
    zn_x = n.linspace(obl_y[0], obl_y[1], 500)
    zn_y = []
    for elem in zn_x:
        if elem >= 0:
            zn_y.append(f1(elem))
        else:
            zn_y.append(f2(elem))
    plt.plot(zn_x, zn_y)
    plt.grid()
    plt.show()
def task3():
    def number_in_new_numeral_system(number, base):
        t = 1
        d = 0
        while number > 0:
            d = d + (number % base) * t
            t = t * 10
            number = number // base
        return d

    osn = int(input('Вести значение основания = '))
    print(number_in_new_numeral_system(int(input('Число в десятичной системе = ')), osn))
def task4():
    x = float(input('Введите значение x = '))
    y = float(input('Введите значение y = '))
    one = ((y <= (4 / 3) * x + 9) and (y >= -3 * x - 30) and (y >= 3.5 * x + 22))
    two = ((y <= 3.5 * x + 22) and (y >= 2 * x + 10) and (x <= -6))
    there = ((x <= -6) and (y >= -6 * x - 30) and (y >= 2 * x + 10))
    four = ((y <= 2 * x + 10) and (y >= x + 4) and (x <= -5))
    five = ((x >= -5) and (y <= (2 / 3) * x + (10 / 3)) and (y >= x + 4))
    six = ((y <= x + 4) and (y >= -2 * x - 14) and (y <= -5 * x - 26))
    seven = ((y <= 10 * x + 14) and (y <= -8 * x - 4) and (y >= x - 4))
    eight = ((y <= x - 4) and (y >= (2 / 3) * x - (14 / 3)) and (y <= - 4))
    nine = ((y <= (10 / 3) * x - 4) and (y >= 6 * x - 12) and (y >= 2 * x - 4))
    ten = ((y <= 2 * x - 4) and (y <= -(4 / 3) * x + (8 / 3)) and (y >= -4))
    figure = one or two or there or five or four or six or seven or eight or nine or ten
    print(f'точка лежит в области - {figure}')

def task5():
    def calculate_digit_sum(number):
        a = int(input())
        sum_of_digits = 0
        while number > 0:
            sum_of_digits += number % 10
        number //= 10
        return sum_of_digits

    def print_numbers_greater_than_k_with_digit_sum_greater_than_l(numbers, k, l):
        for number in numbers:
            if number > k and calculate_digit_sum(number) > l:
                print(number)


    print_numbers_greater_than_k_with_digit_sum_greater_than_l(numbers, k, l)


def task6():
    herbivores = int(input('Введите кол-во травоядных'))
    predators = int(input('Введите кол-во хищников'))
    weeks = int(input('Введите число недель'))

    for week in range(weeks):
        herbivores *= 1.1
        predators *= 1.1

    herbivores *= 0.99
    predators *= 0.97

    herbivores -= predators * 0.1

    if herbivores <= 0 or predators <= 0:
        print("Популяции вымерли.")
    else:
        print(f'Неделя {week + 1}: Травоядные - {round(herbivores)}, Хищники - {round(predators)}')

# def task7():
#     def fact(x):
#         factorial = 1
#         for multiplier in range(1, x + 1):
#             factorial *= multiplier
#         return factorial
#         dlina_ryda = int(input('Введите длину = '))
def task8():
    count1 = 0
    for i in range(1, 9):
        for j in range(1, j + 1):
            count1 = (m.log(2.7, i + j)) ** m.cos(i)