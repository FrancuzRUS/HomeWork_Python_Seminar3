# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform                # подключаю генерацию рандомных чисел
numbers = []                              # объявляем список
for i in range(5):                       # создаем 10 случайных чисел
    numbers.append(uniform(0, 10))        # в диапозоне от 0 до 10 
print(numbers)                            # показываем список

def finder(List):                                       # создаем функцию поиска минимальной и максимальной дробной части числа
    min = List[0]                                       # приравнивам минимальный к первому элементу
    max = 0                                             # приравнимаем максимальный к 0 
  
    for i in range(0, len(List)):                        # указываем диапозон выполнения цикла
        if (List[i] - (int(List[i]))) < min:             # Условие поиска минимального дробного остатка
            min = List[i] - (int(List[i]))               # Присваиваем значение min
        elif (List[i] - (int(List[i]))) > max:           # Условие поиска максимального дробного остатка
            max = List[i] - (int(List[i]))               # Присваиваем значение max

    print("Min = ", min)
    print("Max = ", max)

    Answer = max - min
    return Answer                                       # возвращаем новый список
    
print('Разница между максимальным и минимальным остатком = ', finder(numbers))                              # выводим результат 

