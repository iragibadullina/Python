#Задайте два числа. Напишите программу, которая найдёт НОК 
# (наименьшее общее кратное) этих двух чисел.

#Наименьшее о́бщее кратное (HOK) двух целых чисел — это наименьшее натуральное число, которое делится на оба без остатка, 
#то есть кратно им обоим. К примеру, для чисел 6 и 4, наименьшим общим кратным будет 12.


x = 68
y = 9
if x > y: max_num = x
else: max_num = y
while(True):
     if (max_num % x == 0) and (max_num % y == 0):
         result = max_num
         break
     max_num += 1
print(result)