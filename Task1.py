# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


# Задать рандомный список
# сумировать элементы списка стоящие на нечетных позициях
#


from random import randint                # подключаю генерацию рандомных чисел
numbers = []                              # объявляем список
for i in range(10):                       # создаем 10 случайных чисел
    numbers.append(randint(0, 10))        # в диапозоне от 0 до 10 
print(numbers)                            # показываем список


def sumnumbers(List):                     # создаем функция суммирования
    sum = 0                               # переменная суммы
    for i in range(0, len(List)):         # указываем диапозон выполнения цикла
        if i % 2 != 0:                    # условие цикла (нечетная позиция в списке )
            sum = sum+List[i]             # складываем подходящие числа
    return sum                            # возвращаем результат функции

print(sumnumbers(numbers))                # выводим результат 
