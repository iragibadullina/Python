# Дана последовательность чисел. Получить список уникальных 
# элементов заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]


a = [1, 2, 3, 5, 1, 5, 3, 10]
res = [x for x in a if a.count(x)==1]
print(res)