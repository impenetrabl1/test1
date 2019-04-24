import calendar
from ContextManager import FileOpen

with FileOpen(r'C:\Users\Aliaksandr.Baryhin\Desktop\dataFiles\task4_data.txt', 'r') as open_file:
    year = int(open_file.read())


def is_leap_year(year_param):
    return (year_param % 4 == 0) and (year_param % 100 != 0) or (year_param % 400 == 0)


def is_leap_year_2(year_param):
    return calendar.isleap(year_param)


with FileOpen(r'C:\Users\Aliaksandr.Baryhin\Desktop\dataFiles\task4_data.txt', 'a') as open_file:
    open_file.write('\nIs this year is leap? ' + str(is_leap_year(year)))
    open_file.write('\nIs this year is leap? ' + str(is_leap_year_2(year)))
