#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример:
#- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num = int(input('Введите число: ')) 
n1 = 0
n2 = 1
if num <= 0:
    k =((-1)**(n1+1)) + fib(-n1)
elif num == 1:
    print(n1)
elif num == 2:
    print(n2)
else:
    print(0, 1, end=' ')
    for i in range(2, num):
        n1, n2 = n2, n1 + n2
        print(n2, end=' ')

