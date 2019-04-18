liststr = ['asd', 'asdas', 'as', 'asddfg', 'd', 'asdd']


def func2(liststr):
    return sorted(liststr, key=len)


print(func2(liststr))
