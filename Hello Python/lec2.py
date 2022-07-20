# # Хранение в файлах

# # a - добавление в файл данных, w - перезапись
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') # w - старые данные удаляются, новые записываются
# # data.writelines(colors) # файловую переменную связали с файлом
# data.write('\nLINE12\n')
# data.write('LINE13\n')
# data.close()

# exit()
# path = 'file.txt' # путь к папке
# data = open(path, 'r') # откроем в режиме чтения
# for line in data:
#     print(line) # пробежимся по файлу и считаем все строки
# data.close() # разорвем связь файловой переменной с файлом

# # еще вариант добавления

# with open('file.txt', 'w') as data: # Не нужно закрывать файл, он сам
#     data.write('line 1\n')
#     data.write('line 2\n')


# Функции и модули

def new_string(symbol, count):
    return symbol * count
print(new_string('!', 5))
# print(new_string('!')) выдает ошибку

def new_string(symbol, count=3):
    return symbol * count
print(new_string('!'))
print(new_string(4)) # перемножится == 12

# возможность передачи "неогранниченного" количества переменных
def concatenatio(*params): # перед аргументом ставим *
    res: str = ""
    for item in params:
        res += item
    return res

print(concatenatio('a', 's', 'd', 'f'))
print(concatenatio('a', '1', 'd', '2'))

# Рекурсия

def fib(n):
    if n in [1,2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

list = []
for e in range(1, 10):
    list.append(fib(e))
print(list)

# Кортеж
# состоит из большого количества координат
# обязательно должна быть запятая, если одна координата
# (3,)
a1 = (3, 4)
print(a1)
print(a1[-1])

b1 = (3, 5, 7)
print(b1[-1])

c1 = (3, 5, 7)
for item in c1:
    print(item)


# Словарь 
# - неупорядоченные коллекции произвольных объектов с 
# доступом по ключу

dictionary = {} # создать пустой словарь
dictionary = {
        'up': '|',
        'left': '<-',
        'down': '|',
        'right': '->'
    }
print(dictionary)
print(dictionary['left'])

for k in dictionary.keys(): # показать ключи
    print(k)

for k in dictionary.values(): # только значения
    print(k)

# for v in dictionary(): # все значения
#     print(dictionary[v])

# чтобы просмотреть значения в словаре

print(dictionary['up'])
dictionary['up'] = 'up'

# Множества
# содержат уникальные элементы

colors = {'red', 'green', 'blue'}
print(type(colors))

colors.add('red')
print(colors)

colors.add('gray')
print(colors)

colors.remove('red')
print(colors)

colors.discard('red')
print(colors)

colors.clear()
print(colors)

# Операции для множеств

a1 = {1,2,3,5,8}
b1 = {2,5,8,13,21}
c1 = a1.copy() # множество на основе имеющегося
u = a1.union(b1) # объединение множеств
i = a1.intersection(b1) # пересечение
dl = a1.difference(b1) # отличие а от б
dr = b1.difference(a1) # отличие б от а
print(c1)
print(u)
print(i)
print(dl)
print(dr)

s = frozenset(a1) # замороженные множества, действия с ними не доступны

# Списки 

list1 = [1,2,3,4,5]
list2 = list1
list1[1] = 123 # меняя значение 1-го списка меняем значение во 2-ом
list2[1] = 333 # меняя значение 2-го списка меняем значение в 1-ом
for e in list1:
    print(e)

print()

for e in list2:
    print(e)



# Как удалять последний элемент списка

list1 = [1,2,3,4,5]
print(len(list1))
print(list1.pop())
print(list1)
print(list1.pop())
print(list1)
# print(list1.pop()) # для удаления оставшихся элементов с конца
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)

print(list1.pop(1)) # удаление определенного элемента
print(list1)


list4 = [1,2,3,4,5]
print(list4.insert(2, 11)) # добавление числа 11 на вторую позицию

print(list4)


list4 = [1,2,3,4,5]
print(list4.append(11)) # добавление числа 11 в конец

print(list4)