# Задача №1. Напишите программу, которая принимает на вход цифру, обозначающую 
# день недели, и проверяет, является ли этот день выходным.
 
def week_day(day):
    if day >= 1 and day <= 5:
        print('Working day')
    elif day >= 6 and day <= 7:
        print('Weekend') 
    else:
        print('U entered a wrong number!') 
    input('Enter a space to proceed to the next task')


# Задача №2. Напишите программу, которая принимает на вход координаты точки
#  (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
#   в которой находится эта точка (или на какой оси она находится).
def number_quarter(x, y):
    if x > 0 and y > 0:
        print('First quarter')
    elif x < 0 and y > 0:
        print('Second quarter')
    elif x < 0 and y < 0:
        print('Third quarter')
    elif x == 0 or y == 0:
        print('Error!!! Coordinate must not be 0')
    else:
        print('Fourth quarter')
    
    input('End of homework') 

day = int(input('Enter day number '))
week_day(day)
x = int(input('Enter the coordinates X = '))
y = int(input('Enter the coordinates Y = '))
number_quarter(x, y)