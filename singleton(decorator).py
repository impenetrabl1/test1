def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return getinstance


@singleton
class MyClass:
    pass


a = MyClass()
b = MyClass()
print(a is b)  # True
