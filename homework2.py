#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

# import random


# num = input("Введите число: ")

# while not num.isdigit():
#     print("Вы ввели не целое число")
#     num = input("Введите целое число:")
# num = int(num)
# flip0 = 0
# flip1 = 0

# for _ in range(num):
#     side = random.randint(0, 1)
#     print(side)
#     if side == 0:
#         flip0 += 1
#     else:
#         flip1 += 1
        
# if flip0 < flip1:
#     print(f'Нужно перевернуть {flip0} монеток')
# else:
#     print(f'Нужно перевернуть {flip1} монеток')

#Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# import math


# sum = input("Введите сумму: ")
# while not sum.isdigit():
#     print("Вы ввели не целое число")
#     sum = input("Введите целое число:")
# sum = int(sum)
# mul = input("Введите произведение: ")
# while not mul.isdigit():
#     print("Вы ввели не целое число")
#     mul = input("Введите целое число:")
# mul = int(mul)

# discr = 0
# # нахождение дискриминанта для решения квадратного уравнения
# discr = sum * sum - 4 * mul
# print(discr)
# if discr > 0:
#     num1 = (sum + math.sqrt(discr)) / 2
#     num2 = (sum - math.sqrt(discr)) / 2
#     # при условии discr > 0 будет 2 корня, но при вычислении второго числа получается идентичная пара, поэтому
#     # я здесь её не учитывала
#     if num1 >= 1 and num2 >= 1:
#         print(num1, num2)
#     else:
#         print(f'таких чисел нет')
        
# elif discr == 0:
#     num1 = sum / 2
#     num2 = sum / 2
#     print(num1, num2)
    
# elif discr < 0:
#      print(f'таких чисел нет')
     
#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k ), не превосходящие числа N.

import math

num = input("Введите число: ")
while not num.isdigit():
    print("Вы ввели не целое число")
    num = input("Введите целое число:")
num = int(num)

k = 0
res = 1
while res <= num:
    print(res, end=' ')
    res = 2 ** (k+1)
    k += 1
    