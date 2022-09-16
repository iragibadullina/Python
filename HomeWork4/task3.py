#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

list1 = [5, 3, 3, 8, 0, 1, 8]
list2 = [list1[0]]
for   i in list1:
    count = 0
    for   j in list2:
        if i == j:
            count +=1
    if count == 0:
         list2.append(i)   
           
print(list1)
print(list2)




    