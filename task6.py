import time
from ContextManager import FileOpen

with FileOpen(r'C:\Users\Aliaksandr.Baryhin\Desktop\dataFiles\task6_data.txt', 'r') as open_file:
    number = int(open_file.read())


def function_time(func):
    def wrapper(arg):
        start = time.time()
        value = func(arg)
        print((time.time() - start))
        return value
    return wrapper


@function_time
def calc_range(n):
    squares = [i ** i for i in range(1, n + 1)]
    sum1 = str(sum(squares))
    return sum1[-10:]


with FileOpen(r'C:\Users\Aliaksandr.Baryhin\Desktop\dataFiles\task6_data.txt', 'a') as open_file:
    open_file.write('\nLast 10 numbers of range: '+str(calc_range(number)))
