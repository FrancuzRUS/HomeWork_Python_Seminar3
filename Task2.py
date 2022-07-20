# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint                # подключаю генерацию рандомных чисел
numbers = []                              # объявляем списко
for i in range(10):                       # создаем 10 случайных чисел
    numbers.append(randint(0, 10))        # в диапозоне от 0 до 10 
print(numbers)                            # показываем список


def multiplication(List):                                   # создаем функция умножения 
    multiplicator = 0                                       # переменная суммы
    newlist = []
    for i in range(0, len(List)//2):                        # указываем диапозон выполнения цикла
        multiplicator = List[i] * List[len(List)-i-1]       # умнажаем крайние пары чисел
        newlist.append(multiplicator)                       # добавляем полученные значения в новый список
    return newlist                                          # возвращаем новый список
    
print(multiplication(numbers))                              # выводим результат 

