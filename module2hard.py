import random


def get_password(rand):
    list_ = []
    for i in range(1, 20):
        for j in range(i + 1, 20):
            if rand % (i + j) == 0:
                list_.append(str(i))
                list_.append(str(j))
    password = int("".join(list_))
    print(n, "-", password)


n = random.randrange(3, 21)
get_password(n)
