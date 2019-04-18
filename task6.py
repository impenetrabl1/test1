import time

n = 10000


def func6(n):
    num = [i ** i for i in range(1, n + 1)]
    str1 = str(sum(num))
    return str1[-10:]


start = time.time()
print(func6(n))
print((time.time() - start))
