# 2 - Напишите программу, которая принимает на вход число N 
# и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] #(1, 1*2, 1*2*3, 1*2*3*4)

number=int(input('Введите целое число '))
number=abs(number)
    
multi=[]

for i in range(number):
    if i==0:
        multi.append(1)
    else:
        multi.append(multi[i-1]*(i+1))

print(multi,end=' ')

