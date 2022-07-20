# 1 Задайте список. Напишите программу, которая определит,
# присутствует в заданном списке строк некое число

# '12' -> ['asd12', '12', 'asd', '87'] -> 'asd12', '12'

# list = ['asd12', '12', 'asd', '87']
# for i in list:
#     if '12' in i:
#         print(i)


# 2. Напишите программу, которая определит позицию второго 
# вхождения строки в списке либо сообщит, что её нет.
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

# count = 0
# list2 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# for i in range(len(list2)):
#     if list2[i] == "qwe":
#         count +=1

#         if count > 1:
#             print(i)
#             break

# Другое решение
# дописать и разобраться в скрине 22
list11 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
list22 = ["qwe", "asd", "qwe"]
count = 0
new = []
for i in range(len(list11)):
    if list11[i] == "qwe":
        new.append(i)
        count += 1
if count <=1:
    print("-1")
else:
    print(new[1])


# Другое решение скрин 111
def there_is_number(list, number):
    result = False
    for elements in list:
        if len(elements) == len(number):
            if elements == number:
                result = True
                print(elements)
        if len(elements) > len(number):
            for i in range(len(elements) - len(number) + 1):
                result = True
                print(elements)
    return result

list = ['trwe12', '123', '12jf']
number = '12'
if there_is_number(list, number):
    print(f'Число {number} присутствует в списке')
else: 
    print(f'Число {number} нет в списке')

# Другое решение скрин 222
def get_2nd_pos(list, strg):
    result = -1
    count = 0
    for i in range(len(list)):
        if list[i] == strg:
            count += 1
            if count == 2:
                result = i
    return result

list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
strg = 'qwe'

result = get_2nd_pos(list, strg)
if result != -1:
    print(f'Элемент \{strg}\' имеет второе вхождение в список на позиции {result}')
else:
    print(f'Элемент \{strg}\'  не имеет второго вхождения в список')


# Реализуйте алгоритм задания случайных чисел без использования 
# встроенного генератора псевдослучайных чисел.
# Решение из нета
# import random
 
# class Generator:
#     def __init__(self):
#         self.buffer = []
#         self.__init_buffer()
 
#         # подразумевает под собой n-24
#         self.first_index = 31
 
#         # подразумевает под собой n-55
#         self.second_index = 0
 
#         # основание
#         self.base = 128
 
#     def next(self):
#         value = (self.buffer[self.second_index] + self.buffer[self.first_index]) % self.base
#         del self.buffer[self.second_index]
#         self.buffer.append(value)
#         return value
 
 
#     def __init_buffer(self):
#         for _ in range(55):
#             self.buffer.append(random.randint(0, 10))
 
 
# generator = Generator()
 
# for _ in range(10):
#     print(generator.next())

# через время 
# import time
# def sum_numbers(number):
#     sum = 0 
#     for i in range(len(number)):
#         if number[i].isdigit():
#             sum +=int(number[i])
#     return sum

# seconds = str(time.time())
# print(seconds)
# print(sum_numbers(seconds))

# другое решение
# import time

# l = int(input('Введите длинну числа: '))
# a = time.time()
# print(a)
# ms = int(((a % 1) * (10 ** (l + 1))) % (10 ** (l)))
# #ms = time.time()
# #ms = int(time.time() % 10)

# print(ms)


# другое решение, где отбрасывается целая часть
import time

l = int(input('Введите длинну числа: '))
ms = int(((time.time() % 1) * (10 ** (l + 1))) % (10 ** (l)))
print(ms)

