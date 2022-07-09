# 1 По двум заданным числам проверить является ли одно
#  квадратом второгo

a = int(input())
b = int(input())
c = a * a
d = b * b
if c == b:
    print('Число а является квадратом числа b')
elif d == a:
    print('Число b является квадратом числа a')


# 2 Найти максимальное из пяти чисел


list = [11,22,13,4,15, 44,]
for i in list:
    print(i)
max = list[0]
for i in range(1, len(list)):
    if list[i] > max:
        max = list[i]
print('Максимальный элемент: ')
print(max)


# 3 Вывести на экран числа от -N до N

n = int(input('Введите число: '))
if n < 0:
    n = -n
for i in range(-n, n+1):
    print(i)

# 4 Показать первую цифру дробной части числа

a = float(input())
print(int(a * 10 % 10))

# 5 Дано число. 
# Проверить кратно ли оно 5 и 10 или 15 но не 30  

a = int(input('Введите число: '))
answer1 = True
for i in 5,10,15:
    if a % i == 0 and a % 30 == 0:
        answer1 = False
        break
    elif a % i == 0:
        answer1 = True
        break
    else:
        answer1 = False
print(answer1)

# Короткая запись 5 задачи
a = int(input('Введите число: '))
print(a % 5 == 0 and (a % 10 == 0 or a % 15 == 0) and a % 30 != 0)




