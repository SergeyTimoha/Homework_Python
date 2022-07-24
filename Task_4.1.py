# Задача №1.Вычислить результат деления двух чисел c заданной точностью d

from random import randint
d = int(input('Enter the number of numbers after the decimal point: '))
res = 0
for i in range(1, 10**d):
    res += 1 / (i**2)
pi = (res * 6)**0.5
print(round(pi, d))

input('Enter')
#Задача №2. Задайте натуральное число N. Напишите программу, которая составит список 
# простых множителей числа N.

def prime_check(number):
    for i in range(int(number ** 0.5), 1, -1):
        if number % i == 0:
            return False
    return True

def find_divs(number):
    divs = []
    for i in range(2, int(number ** 0.5)):
        if number % i == 0:
            if prime_check(i):
                divs.append(i)
    return divs

num = int(input('Enter a number: '))
print(find_divs(num))


