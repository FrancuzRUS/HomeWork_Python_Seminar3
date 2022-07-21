
# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k=int(input("Введите k = ")) 
 
def fib (n): 
    if n in [1, 2]: 
        return 1 
    else: 
        return fib(n-1) + fib(n-2) 
 
list = [0] 
 
for i in range(1, k+1): 
    list.append(fib(i)) 
    list.append(-fib(i)) 
     
list.sort() 
 
if k%2!=0: 
    for i in range(0, k,2): 
        list[i]=-list[i] 
else: 
    for i in range(1, k,2): 
        list[i]=-list[i] 
 
 
print(list)







