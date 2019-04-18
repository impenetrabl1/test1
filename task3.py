liststr = ['asd', 'asdas', 'as', 'asddfg', 'd', 'asdd']
listnum = [1, 2, 3, 4, 5, 6]


def func3(listnum, liststr, dopdict={}):
    dict1 = dict(zip(listnum, liststr))
    if dopdict == {}:
        return dict1
    else:
        return dopdict.update(dict1)


print(func3(listnum, liststr))
