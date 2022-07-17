# Задача № 1: Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.

def find_number(arr, number):
    if number in arr:
        return 'Is in the list'
    return 'Not in the list'


list_elem = ['hello', '12', 'red', '567', '5','7']
num = input('Enter a number:')
print(find_number(list_elem, num))

input('Enter a space to proceed to the next task')


# Задача № 2: Напишите программу, которая определит позицию второго вхождения 
# строки в списке либо сообщит, что её нет.
# Пример:
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1


def find_element(arr, element):
    count = 0
    for i in range(len(arr)):
        if arr[i] == element:
            count += 1
        if count == 2:
            return f'There is an index position: {i}'
    return '-1'

list_elem = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
print(find_element(list_elem, 'qwe'))