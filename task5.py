import random

list1 = [random.randrange(10) for i in range(0, 10)]


def func5(list1):
    for i in range(len(list1)):
        for j in range(len(list1) - 1):
            if list1[j] > list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
    return list1


print(func5(list1))
