import random

list1 = [random.randrange(10) for i in range(0, 10)]


def func1(list1):
    list2 = [list1.count(j) for j in list1]
    return list1[list2.index(max(list2))]


print(list1)
print(func1(list1))
