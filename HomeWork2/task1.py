#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#- 6782 -> 23
#- 0,56 -> 11

num = input("Введите число: ")
sum = 0
for i in num:
    if i != '.' and i != '-':
        sum += int(i)
print("Сумма цифр числа равна: ", sum)

numb = float(input())
summ = 0
for el in str(numb):
  if el != '.':
    summ += int(el)
print(summ)

n = float(input('Введите число - '))
while n % 1 > 0:
n *= 10
summ = 0
while n > 0:
sum += n % 10
n //= 10
print(int(summ))
# s = '0.56'
# summ = 0
# for i in s:
# if i.isdigit():
# summ += int(i)
# print(summ)


