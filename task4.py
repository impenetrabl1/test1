import calendar


def func4(year):
    if year % 4 != 0:
        print('обычный')
    elif year % 100 != 0:
        print('высокосный')
    elif year % 400 != 0:
        print('обычный')
    else:
        print('высокосный')


def func4_2(year):
    if calendar.isleap(year):
        print('высокосный')
    else:
        print('обычный')


func4(2019)
func4_2(2019)
