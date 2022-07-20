#Работа с файлами

#Открывает test.txt и открывает в файл file 
with open ('test.txt', 'w', encoding='utf-8') as file:
    file.write('hello,world!')


#Файл с числами от 1 до n введенного пользователем
n = int(input(' Введите число: '))

with open('text_2.txt', 'w', encoding='utf-8') as file:
    for i in range(n+1):
        file.write(f'{i}')


n1 = int(input(' Введите число: '))
spisok = list(range(n1+1))
with open('test.txt', 'w') as file:
    for i in spisok:
        file.write(f'{str(i)}f\n')

#Способы чтения

with open('test.txt', 'r') as file:
    a = file.read()
    print(a)

with open('test.txt', 'r') as file:
    for i in file:
        print(i)

with open('test.txt', 'r') as file:
    for i in range(len(file.readlines())):
        file.seek(i*3)
        a = file.readline()
        print(a)

with open('test.txt', 'r') as file:
    k = len(file.readlines())
    file.seek(k)
    for i in range(k):
        a = file.readline()
        if a != '\n':
            print(a)

with open('test.txt', 'r') as file:
    read_file = file.read()
    list_of_rows = read_file.split() # split берет из read файла строка без пробелов и формирует список из элементов разделенных чем-нибуль
print(list_of_rows)
# Список в int 
# for i in range(len(list_of_rows)):
#     list_of_rows[i] = int(list_of_rows[i])

# print(list_of_rows)

# к каждому элементу списка применить функцию
list_of_rows = map(int, list_of_rows) # комментирует 
# без map 
a=[]
with open('test.txt','r') as file:
    for line in file:
        a.append(int(line.rstrip()))


# 18 задача. # Задайте список из N элементов, 
# заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов 
# на указанных позициях. Позиции вводит 
# пользователь через пробел





#чье-то решение
import random

def get_num_list (n):
    user_list = []
    while len(user_list) < n:
        user_list.append(random.randint(-n, n))
    return user_list

def get_mult_result (user_list):
    mult_result = 1
    with open('file.txt', 'r') as f:
            for line in f:
                index = int(line)
                if index > -1 and index < n:
                    mult_result = mult_result * user_list[index]
    f.close()
    return mult_result

n = int(input('Введите число N: '))
list_to_multiply = get_num_list(n)
print(f'Сгенерирован список: {list_to_multiply}')
result = get_mult_result(list_to_multiply)
print(f'Результат перемножения элементов списка по допустимым индексам из файла: {result}')

#другое решение
list_of_numbers = [-3, -2, -1, 0, 1, 2, 3]

file = open('test.txt', "r")
data = file.read()
list_of_rows = data.split()
file.close()
print(f"{list_of_rows}")

result = 1
for i in list_of_rows:
    result *= list_of_numbers[int(i)]

print(f"{list_of_numbers} -> {list_of_rows} -> {result}")

#Greg
def sequence(num):
    list = []
    i = num * -1
    while i <= num:
        list.append(i)
        i += 1
    return list

def find_position(list, position):
    print(f'Произведение элементов на указанных позициях = {list[int(position[0])] * list[int(position[1])]}')
 
def create_file():
    with open ('position.txt', 'w') as files:
        files.writelines(f'6\n7\n')
    with open ('position.txt', 'r') as files:
        read_files = files.read()
        list_of_rows = read_files.split()
        print 
        return list_of_rows
    
positions = create_file()    
n = 4
my_list = sequence(n)
print(my_list)
find_position(my_list, positions)


#c файлом на запись 
with open('file.txt', 'w') as file:
    for i in range(15):
        file.write(f'{i}\n')


my_list = []
number = int(input('Введите число: '))
result = 1
for i in range(-number, number+1):
    if i == 0:
        continue
    else:
        my_list.append(i)
with open('file.txt', 'r') as file:
    a = file.read().split()
    for i in a:
        if int(i) in range(len(my_list)):
            result *= my_list[int(i)]
print('Элементы в файле', a)
print('Список:', my_list)
print('Произведение всех элементов в списке:', result)

#через переменную

file_name = 'test_2.txt'
a = 'a'
with open(file_name, a, encording='utf-8') as file:
    file.writelines(['hello, world!\n', 'how are you?\n', 'i am fine\n'])

#другое решение
n = int(input('Введите число: '))
spisok = [0,1,2,3,4,5]

with open('test.txt', 'w') as file:
    for i in spisok:
        file.write(str(i))

#другое решение с преподом

list_of_nums = [-3, -2, -1, 0, 1, 2, 3]

with open('test.txt', 'r') as file:
    a = file.read()
    list_of_indices = a.split()
list_of_indices = list(map(int, list_of_indices))

res = 1
for el in list_of_indices:
    if el < len(list_of_nums):
        res *= list_of_nums(el)
print(res)