# Задача 18: Требуется найти в списке A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# Решение построено на сортировке массива по возрастанию. 
# Далее находится между какими числами в последовательности стоит Х и вычисляется наименьшия дистанция до числа
import random
List_1 = []
N = int(input("введите длинну массива который нужно сгенерировать "))

for i in range(N):
    List_1.append(random.randint(0, 100))
print(f'{List_1} - ваш массив')

X = int(input("введите число Х "))
List_1 = set(List_1)
List_1 = list(List_1)
List_1.sort()
print(List_1)

right_number = None
left_number = None
if X < List_1[0]:
    right_number = List_1[0]
    left_number = None
    print(f'число {right_number} является ближайшим к числу {X}')
elif X > List_1[len(List_1) - 1]:
    left_number = List_1[len(List_1) - 1] 
    right_number = None
    print(f'число {left_number} является ближайшим к числу {X}')
elif X == List_1[0]:
    right_number = List_1[0]
    left_number = None
    print(f'число {right_number} является ближайшим к числу {X}')
elif X == List_1[len(List_1)-1]:
    left_number = List_1[len(List_1) - 1] 
    right_number = None
    print(f'число {left_number} является ближайшим к числу {X}')
else:
    for i in range(len(List_1)):   
        if List_1[i] > X:
            right_number = List_1[i]
            left_number = List_1[i-1]
            break
        elif List_1[i] == X:
            right_number = List_1[i+1]
            left_number = List_1[i-1]
            break


if right_number == None or left_number == None:
    print('все')
else:
    distance_right = 0
    distance_left = 0
    for i in range(X, right_number):
        distance_right += 1
    for i in range(left_number, X):
        distance_left += 1
    if distance_right > distance_left:
        print(f'число {left_number} является ближайшим к числу {X}')
    elif distance_right < distance_left:
        print(f'число {right_number} является ближайшим к числу {X}')
    elif distance_left == distance_right:
        print(f'ближайшими к числу {X} являются числа {left_number} и {right_number} - одинаковая удаленность')
