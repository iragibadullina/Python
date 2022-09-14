#(ЕСЛИ НЕ ЗНАЕТЕ КАК ДЕЛАТЬ, МОЖНО НЕ ВЫПОЛНЯТЬ)Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Введите число '))
list = []

for i in range(-n,n+1):
    list.append(i)
print(list)

res = 1
with open('file.txt','w') as data:
    data.write('6 \n')
    data.write('0 \n')
    data.write('3 \n')
    

patch = 'file.txt'
data = open(patch, 'r')

for line in data:
    pos = int(line)
    res *= list[pos]
print(res)

n = int(input('Введите N: '))
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