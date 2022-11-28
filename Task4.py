# 4 - По кругу стоят n человек. Ведущий посчитал m человек по кругу, начиная с первого.
#  При этом каждый из тех, кто участвовал в этом счете, получил по одной монете, 
# остальные получили по две монеты. Далее человек, на котором остановился счет, 
# отдает все свои монеты следующему по счету человеку, а сам выбывает из круга. 
# Процесс продолжается с места остановки аналогичным образом до последнего человека в круге. 
# Составьте алгоритм, который проводит эту игру. Если хотите делать паузы, 
# то импортируйте библиотеку time и используйте оттуда функцию sleep. 
# Определите номер этого человека и количество монет, которые оказались у 
# него в конце игры.


people=[] # список людей
num_people=int(input('Введите учавствующее количество людей: '))

for i in range(num_people):
    people.append(i)
print(f'Первоначальный список людей {people}')

money=[] # количество монет у людей
for i in range(num_people):
    money.append(0)
print(f'деньги в самом начале {money}')

def count(count_people):
    for i in range(len(people)):
        if i<=count_people-1:
            money[i]+=1
        else:
            money[i]+=2
    print(f'деньги после подсчета {money}')
   
    people.pop(count_people-1)
    money[count_people]+=money[count_people-1]
    money.pop(count_people-1)
    return money,people

while True:
    yes='y'
    no='n'
    question=input("Если хотите продолжить нажмите 'y' если нет, то 'n': ")
    if question in yes:
        n=(int(input('Сколько людей нужно посчитать? ')))
        count(n)
        print(f'стало людей {people}')
        print(f'стало денег {money}')
        if len(people)==1:
            exit()
        people=people[n-1:]+people[0:n-1]
        print(f'стало людей (сдвиг) {people}')
        money=money[n-1:]+money[0:n-1]
        print(f'стало денег(сдвиг) {money}')
                
    if question in no:
        exit()



   
   












