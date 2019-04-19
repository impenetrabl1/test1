import calendar
from ContextManager import FileOpen

with FileOpen(r'.\dataFiles\task4_data.txt', 'r') as open_file:
    given_year = int(open_file.read())


def given_year_is_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    return True


def given_year_is_leap_2(year):
    if calendar.isleap(year):
        return True
    return False


with FileOpen(r'.\dataFiles\task4_data.txt', 'a') as open_file:
    open_file.write('\nIs given year is leap? ' + str(given_year_is_leap(given_year)))
    open_file.write('\nIs given year is leap? ' + str(given_year_is_leap_2(given_year)))
