# 1 Напишите программу, которая принимает на вход
#  число N и выдаёт последовательность из N членов.

# Для N = 5: 1, -3, 9, -27, 81

def searchNumber(a, b):
    my_list = [1]
    i = 1
    while len(my_list) < a:
        my_list.append(my_list[i - 1]* b) # в конец списка добавляем
        i += 1 # можно счетчик убрать и в верхней строке написать (my_list[- 1]* b)
    print(my_list)

searchNumber(5, -3)


# через for

def func(x):
    s = 1
    print(s, end=' ')
    for i in range(1, x):
        s = s * -3
        print(s, end=' ')

n = int(input())
func(n)

# вне задач 
def searchNumber(num=7, *args, **key):
    print(args) # args добавляет остальные символы в картеж
    print(key) # key оставшиеся символы отдельно


searchNumber(5, 10, 123, 5432, 324, 76, a=1, b=2)

# Приколюха от Святослава
def print_numbers(x=[]):
    x.append(5)
    print(x)

a = []
print_numbers(x=a)
print_numbers(x=a)
print_numbers(x=a)
print_numbers(x=a)
print(f'---> {a}')

# 3 Написать программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

def str(text1, text2):
    s = 0
    for i in range(len(text1) - len(text2)):
        if (text1[i : i + len(text2)] == text2):
            s = s + 1
    return s
text1 = 'Привет, Мир, привет, Привет!'
text2 = 'Мир'

print(str(text1, text2))


# вариант короче со встроенными функциями
def find_line(string:str, under_strind:str):
    print(string.count(under_strind))

user_string = input('Введите текст: ')
user_understring = input('Введите текст: ')
find_line(user_string, user_understring)


# еще один вариант
symbol = 'so'
base_string = 'some pernal'
position = 0
qty = 0

while(True):
    position = base_string.find(symbol, position)
    if position == -1:
        break
    else:
        position += 1    # как вариант len(symbol)
        qty += 1
print(qty)
