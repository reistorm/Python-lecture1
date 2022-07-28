# Анонимные функции, lambda

def  f(x):
    x**2

print(type(f)) # выводит тип function

g = f # присвоим 
print(f(1))
print(g(1))

def f(x): # нужно сократить код
    return x**2
print(f(2))

# сокращаем
def f(x): 
    return x**2
print(type(f)) # чем является функция
# у функции есть тип, значит мы можем создать 
# переменную типа функция и положить в нее значение
def f(x): 
    return x**2
g = f

print(type(f))
print(type(g))
print((f(4)))
print((g(4))) # есть переменная, которая хранит в себе ссылку на функцию

# 
def calc(x):
    return x + 10
print(calc(10))

def calc2(x):
    return x * 10
print(calc2(10)) 
# если таких функции будет оч много, то
# 
def math(op, x): # op функция, х - аргумент
    print(op(x))  

math(calc2, 20)

# то же самое, но с двумя переменными
def sum(x, y):
    return x+y
def mylt(x, y):
    return x*y

def calc(op, a, b): # в качестве аргумента мб целая функция
    print(op(a, b))
    # return op(a,b)

calc(mylt, 4, 7)


# чтобы сделать из кода выше, что-то красивое у нас есть lambda
# def sum1(x, y):
#     return x+y

sum1 = lambda x, y: x + y # тоже самое что выше

def mylt(x, y):
    return x*y

def calc1(op, a, b): # в качестве аргумента мб целая функция
    print(op(a, b))
    # return op(a,b)

calc1(sum1, 4, 8)
# или 
calc(lambda x, y: x + y, 4, 3)

# где используется 

# как проще писать листы
# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]

# создаем список от 1 до 100
# list = []
# for i in range(1, 101):
#     if (i%2 == 0):
#         list.append(i)
# print(list)

# проще
list = [i for i in range(1, 55)]
print(list)
# с условием
list1 = [i for i in range(1, 55) if i % 2 == 0]
print(list1)
# список кортежей
list2 = [(i, i) for i in range(1, 55)]
print(list2)
# через функцию
def f(x):
    return x**3
list3 = [f(i) for i in range(1, 55) if i % 2 == 0]
print(list3)
# для наглядности через кортежи (число, куб числа)
def f(x):
    return x**3
list3 = [(i, f(i)) for i in range(1, 55) if i % 2 == 0]
print(list3)


# Задача: в файле числа, нужно выбрать четные и 
# составить список пар (число, его квадрат)
# мой вариант, где я забыла про файл \
list = [1, 2, 3, 5, 8, 15, 23, 38]
list1 = [i for i in list if i % 2 == 0]
def f(x):
    return x ** 2
list2 = [(i, f(i)) for i in list1]
print(list2)

# вариант лектора
with open ('test.txt', 'w', encoding='utf-8') as file:
    file.write('1, 2, 3, 5, 8, 15, 23, 38')
path = 'Users/User/Desktop/IT/II четверть/5 Python/Lecture1/test.txt'
f = open(path, 'r') # связываем файловую переменную с файлом на диске
data = f.read() + ' ' # читаем все и добавляем пробел
f.close() # закрываем файл

# numbers = [] # пустой список

while data != '': # пока строка не пустая
    space_pos = data.index(' ') # найти первую позицию пробела
    numbers.append(int(data[:space_pos])) # взять все от первого символа до позиции первого пробела, превратить в чило и добавить в список чисел 
    data = data[space_pos+1:] # обновить список чисел

out = []
for e in numbers:
    if not e % 2: # проверка условия
        out.append((e, e ** 2))

print(out) # вывод числа и его квадрата

# сделать это проще можно так:
def select(f, col): # описали функцию select которая в качестве первого аргумента принимает функцию f которая будет отвечать за логику обработки наших данных которые передаются вторым аргуменом col 
    return[f(x) for x in col]

def where(f, col): # описали функцию where которая в качестве первого аргумента принимает условие f по которому нужно провести фильтрацию объекта
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split() # на выходе получим набор строк

result = select(int, data) # int - функция преобразования строк в число, data - набор данных
res = where(lambda x: not x%2, result)
res = select(lambda x: (x, x **2), res)
print(res)

# Встроенная функция map 
# Она на вход принимает функцию, которую надо применить 
# на ввод данных
# Функция map() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с новыми объектами.
# f(x) ⇒ x + 10
# map(f, [ 1, 2, 3, 4, 5])
#          ↓  ↓  ↓  ↓  ↓
#       [ 11, 12,13,14,15]
# Нельзя пройтись дважды


li = [q for q in range(1, 20)]
li = list(map(lambda q:q+10, li))
print(li)

# применение
data = list(map(int, input().split('')) )
print(data)
пробежаться по объектам без применения list 
data = list(map(int, '1 2 3 45 55 65'.split()))
for e in data:
    print(e)

# в итоге загоняем map в list чтобы данные сохранились 
# берем пример выше и вместо select загоняем map

def where(f, col): # описали функцию where которая в качестве первого аргумента принимает условие f по которому нужно провести фильтрацию объекта
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split() # на выходе получим набор строк

result = map(int, data) # int - функция преобразования строк в число, data - набор данных
res = where(lambda x: not x%2, result)
res = list(map(lambda x: (x, x **2), res))
print(res)

# чтобы избавиться от where используем filter 
# Функция filter() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с теми объектами, для
# которых функция вернула True.
# f(x) ⇒ x - чётное
# filter(f, [ 1, 2, 3, 4,5])
#                  ↓
#               [ 2, 4 ]
# Нельзя пройтись дважды
# data = [x for x in range(10)]
# res = list((filter(lambda x: not x%2, data)))
# print(res)

# пример выше
data = '1 2 3 5 8 15 23 38'.split() # на выходе получим набор строк

result = map(int, data) # int - функция преобразования строк в число, data - набор данных
res = filter(lambda x: not x%2, result)
res = list(map(lambda x: (x, x **2), res))
print(res)

# функция zip 
# Функция zip() применяется к набору итерируемых
# объектов и возвращает итератор с кортежами из
# элементов входных данных.
# Количество элементов в результате равно минимальному количеству элементов входного набора
# zip ([1, 2, 3], [ ‘о‘, ‘д‘, ‘т‘], [‘f’,’s’,’t’])
#               ↓
# [(1, 'о', 'f'), (2, 'д', 's'), (3, 'т', 't')]
# Нельзя пройтись дважды
users = ['user1', 'user2', 'user3', 'user4']
ids = [4, 8, 15, 2]
salary = [111,222,333]
data = list(zip(users, ids, salary))
print(data)

# функция enumerate
# Функция enumerate() применяется к итерируемому
# объекту и возвращает новый итератор с кортежами
# из индекса и элементов входных данных.
# enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])
#                           ↓
# [(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]
# Нельзя пройтись дважды
users = ['user1', 'user2', 'user3', 'user4']
ids = [4, 8, 15, 2]

data = list(enumerate(ids))
print(data)