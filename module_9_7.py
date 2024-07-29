def is_prime(func):
    def wrapper(*args):
        i = func(*args)
        print(i)
        if i == 1 or i == 2:
            res = "Не простое, не составное"
            return res
        for j in range(2, i):
            if i % j == 0:
                res = "Составное"
                return res
            res = "Простое"
            return res

    return wrapper


@is_prime
def sum_three(first, second, third):
    return first + second + third


result = sum_three(2, 3, 6)
print(result)
