#Реализуйте алгоритм перемешивания списка.

list = ['Осень', 'школа', 25, 0.76,'Зима близко']
print(list) 
import random
random.shuffle(list)
print('->', list) 

import random
list = ["Anna", "Alex", 3.14159, 0]
for i in range(len(list)):
index_a = random.randint(0, len(list) - 1)
temp = list[i]
list[i] = list[index_a]
list[index_a] = temp
print(list)


DmitryR: Всем доброе утро.
Sona: Доброе утро!
Любовь Олехова: Доброе утро
allasoloveva: Доброе утро))
almir: +
Sona: +
Татьяна Шумилова: Доброе утро
Евгения Гимранова: Доброе утро)
DmitryR: хорошо слышно
Anastasia Zhukovskaya: нет
almir: нет
DmitryR: сделал
Евгения Макарова, Южно-Сахалинск: сделали
Kristina Grigoreva: нет
Sona: -
almir: времени
almir: ну и не всепонтно
Anastasia Zhukovskaya: времени и не понятно условия
Kristina Grigoreva: сложно(
Anastasia Zhukovskaya: почему первые 1 задачи легкие
Anastasia Zhukovskaya: а остальные не понятно
Anastasia Zhukovskaya: в чате ребята пишут которые очень хорошо понимают
Anastasia Zhukovskaya: я не понимаю о чем они даже пишут
almir: мне вот это не понятно $(1+\frac 1 n)^n$
sonym: +
Любовь Олехова: +
Евгения Макарова, Южно-Сахалинск: +
DmitryR: а вы так и не подключились в группу "GU | Программирование | 5 | будни-утро | 3047"
DmitryR: +
Сергей Сидоренко: +
DmitryR: не могу
DmitryR: прав нет
DmitryR: попробую через куратора, если ответит
Алексей Гаврилов: Сергей, сбросьте, пожалуйста, задачку для единоличников сюда)))
allasoloveva: Да, я то же хотела попросить
allasoloveva: Хочу и д/з послушать, и посмотреть задачу
Сергей Сердюк: t = ['a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '', 'y', '', 'e', 'yu', 'ya']
DmitryR: словарь использовать
Сергей Сердюк: 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

*Пример:*

- 6782 -> 23
- 0,56 -> 11
2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

*Пример:*

- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

*Пример:*

- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
5. Реализуйте алгоритм перемешивания списка.
Kristina Grigoreva: У мен с float не работало(
almir: жду разбор
allasoloveva: Все ок
Наталья Рябкова: +
Elena Seleverstova: Все хорошо)
Евгения Гимранова: +
almir: я решил первую но мне подсказали
anast: мне не было приглашений)
Sona: +
anast: а мне подключаться в 1?
Наталья Рябкова: +
anast: илиздесь остаться?
Алексей Гаврилов: +
Anastasia Zhukovskaya: привет
almir: from curses.ascii import isdigit


num = input()
result = 0
ls = (i for i in num if i.isdigit())

print(sum(int(i) for i in ls))
anast: num = input('Введите вещественное число: ')
sum = 0
for i in num:
if i != '.':
sum += int(i)
print(sum)
Сергей Сердюк: numb = float(input())
summ = 0
for el in str(numb):
if el != '.':
summ += int(el)
print(summ)
almir: lf
Сергей Сердюк: n = float(input('Введите число - '))
while n % 1 > 0:
n *= 10
summ = 0
while n > 0:
summ += n % 10
n //= 10
print(int(summ))
Сергей Сердюк: # s = '0.56'
# summ = 0
# for i in s:
# if i.isdigit():
# summ += int(i)
# print(summ)
anast: n = int(input('Введите число: '))
sum = 0
for n in range(1, n+1):
sum = sum + round((1 + 1 / n)**n, 2)
print(sum)
Elena Seleverstova: n = int(input('Введите число: '))

def sequence(n):

return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]

print(sequence(n))
print('Сумма последовательности =', round(sum(sequence(n))))
DmitryR: Всем доброе утро.
Sona: Доброе утро!
Любовь Олехова: Доброе утро
allasoloveva: Доброе утро))
almir: +
Sona: +
Татьяна Шумилова: Доброе утро
Евгения Гимранова: Доброе утро)
DmitryR: хорошо слышно
Anastasia Zhukovskaya: нет
almir: нет
DmitryR: сделал
Евгения Макарова, Южно-Сахалинск: сделали
Kristina Grigoreva: нет
Sona: -
almir: времени
almir: ну и не всепонтно
Anastasia Zhukovskaya: времени и не понятно условия
Kristina Grigoreva: сложно(
Anastasia Zhukovskaya: почему первые 1 задачи легкие
Anastasia Zhukovskaya: а остальные не понятно
Anastasia Zhukovskaya: в чате ребята пишут которые очень хорошо понимают
Anastasia Zhukovskaya: я не понимаю о чем они даже пишут
almir: мне вот это не понятно $(1+\frac 1 n)^n$
sonym: +
Любовь Олехова: +
Евгения Макарова, Южно-Сахалинск: +
DmitryR: а вы так и не подключились в группу "GU | Программирование | 5 | будни-утро | 3047"
DmitryR: +
Сергей Сидоренко: +
DmitryR: не могу
DmitryR: прав нет
DmitryR: попробую через куратора, если ответит
Алексей Гаврилов: Сергей, сбросьте, пожалуйста, задачку для единоличников сюда)))
allasoloveva: Да, я то же хотела попросить
allasoloveva: Хочу и д/з послушать, и посмотреть задачу
Сергей Сердюк: t = ['a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '', 'y', '', 'e', 'yu', 'ya']
DmitryR: словарь использовать
Сергей Сердюк: 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

*Пример:*

- 6782 -> 23
- 0,56 -> 11
2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

*Пример:*

- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

*Пример:*

- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
5. Реализуйте алгоритм перемешивания списка.
Kristina Grigoreva: У мен с float не работало(
almir: жду разбор
allasoloveva: Все ок
Наталья Рябкова: +
Elena Seleverstova: Все хорошо)
Евгения Гимранова: +
almir: я решил первую но мне подсказали
anast: мне не было приглашений)
Sona: +
anast: а мне подключаться в 1?
Наталья Рябкова: +
anast: илиздесь остаться?
Алексей Гаврилов: +
Anastasia Zhukovskaya: привет
almir: from curses.ascii import isdigit


num = input()
result = 0
ls = (i for i in num if i.isdigit())

print(sum(int(i) for i in ls))
anast: num = input('Введите вещественное число: ')
sum = 0
for i in num:
if i != '.':
sum += int(i)
print(sum)
Сергей Сердюк: numb = float(input())
summ = 0
for el in str(numb):
if el != '.':
summ += int(el)
print(summ)
almir: lf
Сергей Сердюк: n = float(input('Введите число - '))
while n % 1 > 0:
n *= 10
summ = 0
while n > 0:
summ += n % 10
n //= 10
print(int(summ))
Сергей Сердюк: # s = '0.56'
# summ = 0
# for i in s:
# if i.isdigit():
# summ += int(i)
# print(summ)
anast: n = int(input('Введите число: '))
sum = 0
for n in range(1, n+1):
sum = sum + round((1 + 1 / n)**n, 2)
print(sum)
Elena Seleverstova: n = int(input('Введите число: '))

def sequence(n):

return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]

print(sequence(n))
print('Сумма последовательности =', round(sum(sequence(n))))
Сергей Сердюк: n = int(input())
res = [1]
for i in range(2, n + 1):
res.append(res[-1] * i)
print(res)
almir: num = int(input())
f = 1
for i in range(1, num + 1):
f = f * i
print(f)
almir: а куда энд дописать?
anast: в print
Anastasia Zhukovskaya: да
Алексей Гаврилов: итог
Алексей Гаврилов: 120
DmitryR: да
Sona: да
Евгения Макарова, Южно-Сахалинск: + а можно код в копилку
anast: # s = '0.56'
# summ = 0
# for i in s:
# if i.isdigit():
# summ += int(i)
# print(summ)
anast: n = int(input())
res = [1]
for i in range(2, n + 1):
res.append(res[-1] * i)
print(res)
DmitryR: а можно через рекурсию
DmitryR: вообще в питое округление своеобразно работает
Сергей Сердюк: n = int(input("Введите число : "))
sum = 0
for i in range (1, n + 1):
a = (1 + 1 / i)**i
sum += a
print(a, end=" ")
print(f"Сумма равна: {sum}")
Евгения Макарова, Южно-Сахалинск: +
almir: я не поня лее условия
almir: 4 задачи
Евгения Макарова, Южно-Сахалинск: n = int(input('Введите N: '))
a = []
for i in range(-n, n+1):
a.append(i)
print(a, sep=',')

l = []
with open('file.txt', 'r') as f:
for line in f:
l.append(int(line))

c = l[0]
d = l[1]
k = a[c]*a[d]
print('Произведение элементов на указанных в файле позициях = ', k)
almir: а указаны гдеили. кем?
DmitryR: Всем доброе утро.
Sona: Доброе утро!
Любовь Олехова: Доброе утро
allasoloveva: Доброе утро))
almir: +
Sona: +
Татьяна Шумилова: Доброе утро
Евгения Гимранова: Доброе утро)
DmitryR: хорошо слышно
Anastasia Zhukovskaya: нет
almir: нет
DmitryR: сделал
Евгения Макарова, Южно-Сахалинск: сделали
Kristina Grigoreva: нет
Sona: -
almir: времени
almir: ну и не всепонтно
Anastasia Zhukovskaya: времени и не понятно условия
Kristina Grigoreva: сложно(
Anastasia Zhukovskaya: почему первые 1 задачи легкие
Anastasia Zhukovskaya: а остальные не понятно
Anastasia Zhukovskaya: в чате ребята пишут которые очень хорошо понимают
Anastasia Zhukovskaya: я не понимаю о чем они даже пишут
almir: мне вот это не понятно $(1+\frac 1 n)^n$
sonym: +
Любовь Олехова: +
Евгения Макарова, Южно-Сахалинск: +
DmitryR: а вы так и не подключились в группу "GU | Программирование | 5 | будни-утро | 3047"
DmitryR: +
Сергей Сидоренко: +
DmitryR: не могу
DmitryR: прав нет
DmitryR: попробую через куратора, если ответит
Алексей Гаврилов: Сергей, сбросьте, пожалуйста, задачку для единоличников сюда)))
allasoloveva: Да, я то же хотела попросить
allasoloveva: Хочу и д/з послушать, и посмотреть задачу
Сергей Сердюк: t = ['a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '', 'y', '', 'e', 'yu', 'ya']
DmitryR: словарь использовать
Сергей Сердюк: 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

*Пример:*

- 6782 -> 23
- 0,56 -> 11
2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

*Пример:*

- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

*Пример:*

- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
5. Реализуйте алгоритм перемешивания списка.
Kristina Grigoreva: У мен с float не работало(
almir: жду разбор
allasoloveva: Все ок
Наталья Рябкова: +
Elena Seleverstova: Все хорошо)
Евгения Гимранова: +
almir: я решил первую но мне подсказали
anast: мне не было приглашений)
Sona: +
anast: а мне подключаться в 1?
Наталья Рябкова: +
anast: илиздесь остаться?
Алексей Гаврилов: +
Anastasia Zhukovskaya: привет
almir: from curses.ascii import isdigit


num = input()
result = 0
ls = (i for i in num if i.isdigit())

print(sum(int(i) for i in ls))
anast: num = input('Введите вещественное число: ')
sum = 0
for i in num:
if i != '.':
sum += int(i)
print(sum)
Сергей Сердюк: numb = float(input())
summ = 0
for el in str(numb):
if el != '.':
summ += int(el)
print(summ)
almir: lf
Сергей Сердюк: n = float(input('Введите число - '))
while n % 1 > 0:
n *= 10
summ = 0
while n > 0:
summ += n % 10
n //= 10
print(int(summ))
Сергей Сердюк: # s = '0.56'
# summ = 0
# for i in s:
# if i.isdigit():
# summ += int(i)
# print(summ)
anast: n = int(input('Введите число: '))
sum = 0
for n in range(1, n+1):
sum = sum + round((1 + 1 / n)**n, 2)
print(sum)
Elena Seleverstova: n = int(input('Введите число: '))

def sequence(n):

return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]

print(sequence(n))
print('Сумма последовательности =', round(sum(sequence(n))))
Сергей Сердюк: n = int(input())
res = [1]
for i in range(2, n + 1):
res.append(res[-1] * i)
print(res)
almir: num = int(input())
f = 1
for i in range(1, num + 1):
f = f * i
print(f)
almir: а куда энд дописать?
anast: в print
Anastasia Zhukovskaya: да
Алексей Гаврилов: итог
Алексей Гаврилов: 120
DmitryR: да
Sona: да
Евгения Макарова, Южно-Сахалинск: + а можно код в копилку
anast: # s = '0.56'
# summ = 0
# for i in s:
# if i.isdigit():
# summ += int(i)
# print(summ)
anast: n = int(input())
res = [1]
for i in range(2, n + 1):
res.append(res[-1] * i)
print(res)
DmitryR: а можно через рекурсию
DmitryR: вообще в питое округление своеобразно работает
Сергей Сердюк: n = int(input("Введите число : "))
sum = 0
for i in range (1, n + 1):
a = (1 + 1 / i)**i
sum += a
print(a, end=" ")
print(f"Сумма равна: {sum}")
Евгения Макарова, Южно-Сахалинск: +
almir: я не поня лее условия
almir: 4 задачи
Евгения Макарова, Южно-Сахалинск: n = int(input('Введите N: '))
a = []
for i in range(-n, n+1):
a.append(i)
print(a, sep=',')

l = []
with open('file.txt', 'r') as f:
for line in f:
l.append(int(line))

c = l[0]
d = l[1]
k = a[c]*a[d]
print('Произведение элементов на указанных в файле позициях = ', k)
almir: а указаны гдеили. кем?
DmitryR: Всем доброе утро.
Sona: Доброе утро!
Любовь Олехова: Доброе утро
allasoloveva: Доброе утро))
almir: +
Sona: +
Татьяна Шумилова: Доброе утро
Евгения Гимранова: Доброе утро)
DmitryR: хорошо слышно
Anastasia Zhukovskaya: нет
almir: нет
DmitryR: сделал
Евгения Макарова, Южно-Сахалинск: сделали
Kristina Grigoreva: нет
Sona: -
almir: времени
almir: ну и не всепонтно
Anastasia Zhukovskaya: времени и не понятно условия
Kristina Grigoreva: сложно(
Anastasia Zhukovskaya: почему первые 1 задачи легкие
Anastasia Zhukovskaya: а остальные не понятно
Anastasia Zhukovskaya: в чате ребята пишут которые очень хорошо понимают
Anastasia Zhukovskaya: я не понимаю о чем они даже пишут
almir: мне вот это не понятно $(1+\frac 1 n)^n$
sonym: +
Любовь Олехова: +
Евгения Макарова, Южно-Сахалинск: +
DmitryR: а вы так и не подключились в группу "GU | Программирование | 5 | будни-утро | 3047"
DmitryR: +
Сергей Сидоренко: +
DmitryR: не могу
DmitryR: прав нет
DmitryR: попробую через куратора, если ответит
Алексей Гаврилов: Сергей, сбросьте, пожалуйста, задачку для единоличников сюда)))
allasoloveva: Да, я то же хотела попросить
allasoloveva: Хочу и д/з послушать, и посмотреть задачу
Сергей Сердюк: t = ['a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '', 'y', '', 'e', 'yu', 'ya']
DmitryR: словарь использовать
Сергей Сердюк: 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

*Пример:*

- 6782 -> 23
- 0,56 -> 11
2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

*Пример:*

- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

*Пример:*

- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
5. Реализуйте алгоритм перемешивания списка.
Kristina Grigoreva: У мен с float не работало(
almir: жду разбор
allasoloveva: Все ок
Наталья Рябкова: +
Elena Seleverstova: Все хорошо)
Евгения Гимранова: +
almir: я решил первую но мне подсказали
anast: мне не было приглашений)
Sona: +
anast: а мне подключаться в 1?
Наталья Рябкова: +
anast: илиздесь остаться?
Алексей Гаврилов: +
Anastasia Zhukovskaya: привет
almir: from curses.ascii import isdigit


num = input()
result = 0
ls = (i for i in num if i.isdigit())

print(sum(int(i) for i in ls))
anast: num = input('Введите вещественное число: ')
sum = 0
for i in num:
if i != '.':
sum += int(i)
print(sum)
Сергей Сердюк: numb = float(input())
summ = 0
for el in str(numb):
if el != '.':
summ += int(el)
print(summ)
almir: lf
Сергей Сердюк: n = float(input('Введите число - '))
while n % 1 > 0:
n *= 10
summ = 0
while n > 0:
summ += n % 10
n //= 10
print(int(summ))
Сергей Сердюк: # s = '0.56'
# summ = 0
# for i in s:
# if i.isdigit():
# summ += int(i)
# print(summ)
anast: n = int(input('Введите число: '))
sum = 0
for n in range(1, n+1):
sum = sum + round((1 + 1 / n)**n, 2)
print(sum)
Elena Seleverstova: n = int(input('Введите число: '))

def sequence(n):

return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]

print(sequence(n))
print('Сумма последовательности =', round(sum(sequence(n))))
Сергей Сердюк: n = int(input())
res = [1]
for i in range(2, n + 1):
res.append(res[-1] * i)
print(res)
almir: num = int(input())
f = 1
for i in range(1, num + 1):
f = f * i
print(f)
almir: а куда энд дописать?
anast: в print
Anastasia Zhukovskaya: да
Алексей Гаврилов: итог
Алексей Гаврилов: 120
DmitryR: да
Sona: да
Евгения Макарова, Южно-Сахалинск: + а можно код в копилку
anast: # s = '0.56'
# summ = 0
# for i in s:
# if i.isdigit():
# summ += int(i)
# print(summ)
anast: n = int(input())
res = [1]
for i in range(2, n + 1):
res.append(res[-1] * i)
print(res)
DmitryR: а можно через рекурсию
DmitryR: вообще в питое округление своеобразно работает
Сергей Сердюк: n = int(input("Введите число : "))
sum = 0
for i in range (1, n + 1):
a = (1 + 1 / i)**i
sum += a
print(a, end=" ")
print(f"Сумма равна: {sum}")
Евгения Макарова, Южно-Сахалинск: +
almir: я не поня лее условия
almir: 4 задачи
Евгения Макарова, Южно-Сахалинск: n = int(input('Введите N: '))
a = []
for i in range(-n, n+1):
a.append(i)
print(a, sep=',')

l = []
with open('file.txt', 'r') as f:
for line in f:
l.append(int(line))

c = l[0]
d = l[1]
k = a[c]*a[d]
print('Произведение элементов на указанных в файле позициях = ', k)
almir: а указаны гдеили. кем?
Сергей Сердюк: from random import randint
n = int(input('Введите число N - '))
numbers = []
for i in range(n):
numbers.append(randint(-n, n+1))
print(numbers)

f = open('file.txt', 'w')
while True:
s = input('Укажите позицию для вычисления - ')
if s == "":
break
f.write(s+"\n")
f.close()

result = 1
f = open('file.txt', 'r')
for line in f:
if line == "":
break
result *= numbers[int(line)]
f.close()
print(result)
almir: ну что бы понять чт озакончили
almir: слушаю внимательно
Elena Seleverstova: все хорошо
DmitryR: да
almir: да понятно
Алексей Гаврилов: всё чудесно)
Sona: +
Elena Seleverstova: все понятно
almir: да
Kristina Grigoreva: +
Евгения Макарова, Южно-Сахалинск: +
Сергей Сидоренко: +
DmitryR: +
Anastasia Zhukovskaya: всегда понятно когда кто-то решает
almir: import random
list = [1, 2, 3, 4, 5, 6, 7]
t = 0
while t < len(list):
r = random.randint(0,len(list) - 1)
j = 1
swap = list[r]
list[r] = list[len(list) - j]
list[len(list) - j] = swap
j += 1
t += 1
print(list)
Евгения Макарова, Южно-Сахалинск: some_list = ['a', 'b', 'c', 'd', 'f']
shuffle(some_list)
print(some_list)
almir: ну тут же указно именно алгоритм
Kristina Grigoreva: Скажите пожалуйста еще раз что делает
Kristina Grigoreva: shuffle
Сергей Сердюк: import random
list = ["Anna", "Alex", 3.14159, 0]
for i in range(len(list)):
index_a = random.randint(0, len(list) - 1)
temp = list[i]
list[i] = list[index_a]
list[index_a] = temp
print(list)
DmitryR: Всем доброе утро.
Sona: Доброе утро!
Любовь Олехова: Доброе утро
allasoloveva: Доброе утро))
almir: +
Sona: +
Татьяна Шумилова: Доброе утро
Евгения Гимранова: Доброе утро)
DmitryR: хорошо слышно
Anastasia Zhukovskaya: нет
almir: нет
DmitryR: сделал
Евгения Макарова, Южно-Сахалинск: сделали
Kristina Grigoreva: нет
Sona: -
almir: времени
almir: ну и не всепонтно
Anastasia Zhukovskaya: времени и не понятно условия
Kristina Grigoreva: сложно(
Anastasia Zhukovskaya: почему первые 1 задачи легкие
Anastasia Zhukovskaya: а остальные не понятно
Anastasia Zhukovskaya: в чате ребята пишут которые очень хорошо понимают
Anastasia Zhukovskaya: я не понимаю о чем они даже пишут
almir: мне вот это не понятно $(1+\frac 1 n)^n$
sonym: +
Любовь Олехова: +
Евгения Макарова, Южно-Сахалинск: +
DmitryR: а вы так и не подключились в группу "GU | Программирование | 5 | будни-утро | 3047"
DmitryR: +
Сергей Сидоренко: +
DmitryR: не могу
DmitryR: прав нет
DmitryR: попробую через куратора, если ответит
Алексей Гаврилов: Сергей, сбросьте, пожалуйста, задачку для единоличников сюда)))
allasoloveva: Да, я то же хотела попросить
allasoloveva: Хочу и д/з послушать, и посмотреть задачу
Сергей Сердюк: t = ['a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '', 'y', '', 'e', 'yu', 'ya']
DmitryR: словарь использовать
Сергей Сердюк: 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

*Пример:*

- 6782 -> 23
- 0,56 -> 11
2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

*Пример:*

- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

*Пример:*

- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
5. Реализуйте алгоритм перемешивания списка.
Kristina Grigoreva: У мен с float не работало(
almir: жду разбор
allasoloveva: Все ок
Наталья Рябкова: +
Elena Seleverstova: Все хорошо)
Евгения Гимранова: +
almir: я решил первую но мне подсказали
anast: мне не было приглашений)
Sona: +
anast: а мне подключаться в 1?
Наталья Рябкова: +
anast: илиздесь остаться?
Алексей Гаврилов: +
Anastasia Zhukovskaya: привет
almir: from curses.ascii import isdigit


num = input()
result = 0
ls = (i for i in num if i.isdigit())

print(sum(int(i) for i in ls))
anast: num = input('Введите вещественное число: ')
sum = 0
for i in num:
if i != '.':
sum += int(i)
print(sum)
Сергей Сердюк: numb = float(input())
summ = 0
for el in str(numb):
if el != '.':
summ += int(el)
print(summ)
almir: lf
Сергей Сердюк: n = float(input('Введите число - '))
while n % 1 > 0:
n *= 10
summ = 0
while n > 0:
summ += n % 10
n //= 10
print(int(summ))
Сергей Сердюк: # s = '0.56'
# summ = 0
# for i in s:
# if i.isdigit():
# summ += int(i)
# print(summ)
anast: n = int(input('Введите число: '))
sum = 0
for n in range(1, n+1):
sum = sum + round((1 + 1 / n)**n, 2)
print(sum)
Elena Seleverstova: n = int(input('Введите число: '))

def sequence(n):

return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]

print(sequence(n))
print('Сумма последовательности =', round(sum(sequence(n))))
Сергей Сердюк: n = int(input())
res = [1]
for i in range(2, n + 1):
res.append(res[-1] * i)
print(res)
almir: num = int(input())
f = 1
for i in range(1, num + 1):
f = f * i
print(f)
almir: а куда энд дописать?
anast: в print
Anastasia Zhukovskaya: да
Алексей Гаврилов: итог
Алексей Гаврилов: 120
DmitryR: да
Sona: да
Евгения Макарова, Южно-Сахалинск: + а можно код в копилку
anast: # s = '0.56'
# summ = 0
# for i in s:
# if i.isdigit():
# summ += int(i)
# print(summ)
anast: n = int(input())
res = [1]
for i in range(2, n + 1):
res.append(res[-1] * i)
print(res)
DmitryR: а можно через рекурсию
DmitryR: вообще в питое округление своеобразно работает
Сергей Сердюк: n = int(input("Введите число : "))
sum = 0
for i in range (1, n + 1):
a = (1 + 1 / i)**i
sum += a
print(a, end=" ")
print(f"Сумма равна: {sum}")
Евгения Макарова, Южно-Сахалинск: +
almir: я не поня лее условия
almir: 4 задачи
Евгения Макарова, Южно-Сахалинск: n = int(input('Введите N: '))
a = []
for i in range(-n, n+1):
a.append(i)
print(a, sep=',')

l = []
with open('file.txt', 'r') as f:
for line in f:
l.append(int(line))

c = l[0]
d = l[1]
k = a[c]*a[d]
print('Произведение элементов на указанных в файле позициях = ', k)
almir: а указаны гдеили. кем?
Сергей Сердюк: from random import randint
n = int(input('Введите число N - '))
numbers = []
for i in range(n):
numbers.append(randint(-n, n+1))
print(numbers)

f = open('file.txt', 'w')
while True:
s = input('Укажите позицию для вычисления - ')
if s == "":
break
f.write(s+"\n")
f.close()

result = 1
f = open('file.txt', 'r')
for line in f:
if line == "":
break
result *= numbers[int(line)]
f.close()
print(result)
almir: ну что бы понять чт озакончили
almir: слушаю внимательно
Elena Seleverstova: все хорошо
DmitryR: да
almir: да понятно
Алексей Гаврилов: всё чудесно)
Sona: +
Elena Seleverstova: все понятно
almir: да
Kristina Grigoreva: +
Евгения Макарова, Южно-Сахалинск: +
Сергей Сидоренко: +
DmitryR: +
Anastasia Zhukovskaya: всегда понятно когда кто-то решает
almir: import random
list = [1, 2, 3, 4, 5, 6, 7]
t = 0
while t < len(list):
r = random.randint(0,len(list) - 1)
j = 1
swap = list[r]
list[r] = list[len(list) - j]
list[len(list) - j] = swap
j += 1
t += 1
print(list)
Евгения Макарова, Южно-Сахалинск: some_list = ['a', 'b', 'c', 'd', 'f']
shuffle(some_list)
print(some_list)
almir: ну тут же указно именно алгоритм
Kristina Grigoreva: Скажите пожалуйста еще раз что делает
Kristina Grigoreva: shuffle
Сергей Сердюк: import random
list = ["Anna", "Alex", 3.14159, 0]
for i in range(len(list)):
index_a = random.randint(0, len(list) - 1)
temp = list[i]
list[i] = list[index_a]
list[index_a] = temp
print(list)
Наталья Рябкова: А можно еще раз 132 строку пояснить
Наталья Рябкова: понятно, спасибо
allasoloveva: кортежами
Наталья Рябкова: +
Сергей Сидоренко: +
Наталья Рябкова: +
Sona: +
DmitryR: lang = {'а': 'a',
'б': 'b',
'в': 'v',
'г': 'g',
'д': 'd',
'е': 'e',
'ё': 'e',
'ж': 'zh',
'з': 'z',
'и': 'i',
'й': 'y',
'к': 'k',
'л': 'l',
'м': 'm',
'н': 'n',
'о': 'o',
'п': 'p',
'р': 'r',
'с': 's',
'т': 't',
'у': 'u',
'ф': 'f',
'х': 'kh',
'ц': 'ts',
'ч': 'ch',
'ш': 'sh',
'щ': 'shch',
'ъ': '',
'ы': 'y',
'ь': '',
'э': 'e',
'ю': 'yu',
'я': 'ya',
' ': ' '
}

value = 'Мама мыла раму'
result = ''

for i in value:
result += lang[i.lower()]

print(result)

t = ['a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '', 'y', '', 'e', 'yu', 'ya']

start_index = ord('а')
title = 'Переводим этот текст, сейчас!'
print(title.lower())

slug = ""
for s in title.lower():

if "а" <= s <= "я":
slug += t[ord(s) - ord('а')]
# elif s == "ё":
# slug = 'yo'
# elif s in " !?;:.,":
# slug = "-"
else:
slug += s

# while slug.count('--'):
# slug = slug.replace('--', '-')

print(slug)
