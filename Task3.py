# 3 - Дан массив размера N. После каждого отрицательного элемента массива 
# вставьте элемент с нулевым значением.
# Пример:
# - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]

import random
number=int(input('Введите целое положительное число: '))
number=abs(number)

arr=[]
for i in range(number):
    arr.append(int(random.randint(-1, 1)*100+random.randint(1, 10)))
print(arr)

for i in range(number):
    if arr[i]<0:
        arr.insert(i+1, 0)
print(arr)