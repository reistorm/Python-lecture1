from operator import truediv

# print() – отвечает за вывод данных
# input() – отвечает за ввод данных
print('Hello world')
# Определить тип переменных
# value = None
# print(type(value))

a = 213
b = 1.23
# print(type(b))
# print(type(a))
value = 12342
# print(value)

s = 'hello world'
# print(type(s))

# print(a, b, s)
# print('{} - {} - {}'.format(a,b,s))
# print(a, '-',b, '-', s)
# print(f'{a} - {b} - {s}')

# f = True
# print(f)

# Массивы

# list = ['1', '3', '2', 'hello']
# print(list)


# Вещественные числа
# print('Введите а');
# a = float(input())
# print('Введите b');
# b = float(input())
# print(f'{a}, {b}')

# print(a, ' + ' , b, '=', a+b)

# Целые числа
# print('Введите а');
# a = int(input())
# print('Введите b');
# b = int(input())
# c = 30
# print(a, ' + ', b, ' = ', c)
# print('{} + {} = {}'.format(a, b, c))


# Арифметические операции
# +, -, *, /, %, //, **
# Приоритет операций
# **, ⊕, ⊖, *, /, //, %, +, -
# ( ) Скобки меняют приоритет


# a = 12
# b = 5
# c = a + b
# d = a / b # обычное деление
# k = a // b #деление с целым числом
# r = a % b
# t = a ** b # возведение в степень
# print(c)
# print(d)
# print(k)
# print(r)
# print(t)

# a = 1.3
# b = 3
# c = round(a * b, 5) # округление, 5 - число знаков
# print(c)

# a = 1.31213212
# b = 3
# c = round(a * b, 6) # округление, 6 - число знаков
# print(c)

# a =3
# a += 5
# print(a)

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |, ^
# Кое-что ещё: is, is not, in, not in

# a = 1 > 4
# print(a)

# a = 1 < 4 and 5> 2
# print(a)

# a = 'qwe'
# b = 'qwe'
# print(a == b)

# a = [1,2]
# b = [1,2]
# print(a == b)

# a = 1 < 3 < 5
# print(a)

# a = 1 < 3 < 5 < 44
# print(a)

# func = 1
# T =4
# x = 123
# print(func<T>x)

# f = 1 > 2 or 4 < 6  # Хотя бы одно - истина
# print(f)

# f = [1,2,3,4]
# print(f)
# print(2 in f)

# f = [1,2,3,4]
# print(f)
# print(not 2 in f)

# f = [1,2,3,4]
# is_odd = f[0] % 2 ==0
# print(is_odd)

# f = [1,2,3,4]
# is_odd = not f[0] % 2
# print(is_odd)


# Операции if - else

# username = input('Введите имя: ')
# if(username == 'Маша'):
#     print('Ура, это же МАША!');
# else:
#     print('Привет, ', username);

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# Операции if, if - else
# username = input('Введите имя: ')
# if username == 'Маша':
# print('Ура, это же МАША!')
# elif username == 'Марина':
# print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
# print('Ильнар - топ)')
# else:
# print('Привет, ', username)

# Операция while
# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# Операция while-else
# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)

# Операция for
# for i in 1, -2, 3, 14, 5:
#     print(i**2)

# r = range(1, 10, 2)
# for i in r:
#     print(i)


# for i in 'rqwerty':
#     print(i)

# Работа со строками
# text = 'съешь ещё этих мягких французских булок'
# print(len(text)) # 39длина строки
# print('ещё' in text) # True элемент в строке
# print(text.isdigit()) # False символы являются числами?
# print(text.islower()) # True есть нижнее подчеркивание?
# print(text.replace('ещё','ЕЩЁ')) # что-то можно заменить
# for c in text:
# print(c)

# Вызов помощи
# help(str)

# # Обращение к элементам строки 
# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text) от нулевого до последнего
# print(text[:2]) # съ от 0 до 2
# print(text[len(text)-2:]) # ок с конца строки
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...

#Списки 
# numbers = [1, 2, 3, 4, 5]
# print(numbers) # [1, 2, 3, 4, 5]

# numbers = list(range(1, 6))
# print(numbers) # [1, 2, 3, 4, 5]

# numbers[0] = 10
# print(numbers) # [10, 2, 3, 4, 5]

# for i in numbers:
#   i *= 2
#   print(i) # [20, 4, 6, 8, 10]
# print(numbers) # [10, 2, 3, 4, 5]


# colors = ['red', 'green', 'blue']

# for e in colors:
# print(e) # red green blue

# for e in colors:
# print(e*2) # redred greengreen blueblue

# remove -удалить, append - добавить
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент

# # range k list
# numbers = [1,2,3,4,5]
# # print(numbers)
# # ran = range(1, 6)
# # print(type(ran))
# # numbers = list(ran)
# # print(type(numbers))

# print(numbers)
# numbers[0] = 10
# print(numbers)
# for i in numbers:
#     i *= 2
#     print(i)
# print(numbers)

# Функции в Python
# def function_name(x):
# body line 1
# . . .
# body line n
# optional return

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 2
print(f(arg))
print(type(f(arg)))
            