# 1 - Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр. Учтите, что числа могут быть отрицательными
# Пример:
# 67.82 -> 23
# (-0.56) -> 11


number = float(input('Введите вещественное число: '))
number = str(number)
summ=0
for i in range(len(number)):
    if number[i] == "-" or number[i] == ".":
         continue
    else:
        summ += int(number[i])
        
print(summ)

