# 35 В файле находится Н натуральных чисел, 
# записанных через пробел. Среди чисел не хватает 
# одного, чтобы выполнялось условие A[i] - 1 = A[i - 1].
# Найдите это число

# with open('file_test.txt', 'w', encoding='UTF=8') as file:
#     file.write(input('Введите последовательность: '))

# with open('file_test.txt', 'r') as file:
#     my_list = list(map(int, file.read().split()))
# print(f'Начальный список: ', my_list)
# for i in range(1, len(my_list)):
#     if my_list[i] - 1 != my_list[i - 1]:
#         print(f'Отсутствует число:', my_list[i - 1] + 1)

# 1 Дан список чисел. Создайте список, в который попадают 
# числа, которые описывают возрастающую 
# последовательность. Порядок элементов менять нельзя.
# [1,5,2,3,4,6,1,7] => [1,2,3] or [1,7] or [1,6,7]
# решение одного коллеги, недорешенное, смысл в 
# отбрасывании первого элемента, если он макс
# my_list = [1, 5, 2, 3, 4, 6, 1, 7]
# new_list = []
# for i in range(1, len(my_list)):
#     if my_list[0] == max(my_list):
#         my_list = my_list[1:]
# print(my_list)
# new_list = []
# new_list.append(my_list[0])
# max_number = my_list[0]
# for i in range(1, len(my_list)):
#     if max_number < my_list[i]:
#         new_list.append(my_list[i])
#         max_number = my_list[i]
# print(new_list)

# from tokenize import maybe


# a = [1, 5, 2, 3, 4, 6, 1, 7]
# def func(num):
#     my_list = []
#     my_list.append(a[num])
#     for i in range(num, len(a)):
#         if a[i] > my_list[-1]:
#             my_list.append(a[i])
#     numb = num # проверка если берем второй индекс, то сравниваем его с первым, чтобы 1 входила
#     while numb != -1:
#         if a[numb] < my_list[0]:
#             my_list.insert(0, a[numb])
#         numb -= 1
#     print(my_list)

# for i in range(len(a)-1):
#     func(i)

# Другое решение со словарями 
# почему-то list_input не работает
def max_in_list(list_of_numbers):
    max = list_of_numbers[0]
    for i in list_of_numbers:
        if i > max:
            max = i
    return max

new_list_dic = {}

index = 0
for n in range(1, len(list_input)):
    for i, item in enumerate(list_input[:-n]):
        new_list = [list_input[i]]
        for j, item_2 in enumerate(list_input[i+n:]):
            if item_2 > max_in_list(new_list):
                new_list.append(item_2)
        if new_list not in new_list_dic.values():
            new_list_dic[index] = new_list
            index +=1
for i in new_list_dic:
    print(f"{i} : \t{new_list_dic[i]}")