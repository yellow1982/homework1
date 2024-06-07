numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i == 1:
        continue
    is_prime = False
    for j in range(2, i):
        if i % j == 0:
            is_prime = True
            break
    if is_prime:
        not_primes.append(numbers[numbers.index(i)])
    else:
        primes.append(numbers[numbers.index(i)])
print("Primes:", primes)
print("Not primes:", not_primes)
#Выведите списки primes и not_primes на экран(в консоль).
#Пункты задачи:
#Создайте пустые списки primes и not_primes.
#При помощи цикла for переберите список numbers.
##Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.
##Отметить простоту числа можно переменной is_prime, записав в неё занчение True перед проверкой.
#В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes в зависимости от значения перменной is_prime после проверки (True - в prime, False - в not_prime).
#Выведите списки primes и not_primes на экран(в консоль).