# 1. Напишите программу, которая принимает на вход вещественное число и 
# показывает сумму его цифр.

# *Пример:*55

# - 6782 -> 23
# - 0,56 -> 11


# try:
#     number = float(input("Введите вещественное число: "))
# except:
#     print("Нужно было ввести вещественное число!")
#     exit()



number = int(input('Enter a multiple real number: '))

def Sum_number(n):
    num = int(str(n).replace('.', ''))

    sum = 0
    while num != 0:
        sum += num % 10
        num //= 10
    return sum

print(Sum_number(number))

input("Enter")

# 2. Напишите программу, которая принимает на вход число N и выдает
# набор произведений чисел от 1 до N. Факториал



N = int(input('Enter the number N^: '))


def Num_sequence(n):
    res = []

    for i in range(1, n+1):
        if i > 1:
            res.append(res[-1] * i)
        else:
            res.append(i)
    return res


print(Num_sequence(N))