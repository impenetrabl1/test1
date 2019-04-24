from ContextManager import FileOpen

with FileOpen(r'C:\Users\Aliaksandr.Baryhin\Desktop\dataFiles\task2_data.txt', 'r') as open_file:
    list_of_strings_from_file = list(open_file.read().split(' '))


def list_sort(sortable_list):
    return sorted(sortable_list, key=len)


with FileOpen(r'C:\Users\Aliaksandr.Baryhin\Desktop\dataFiles\task2_data.txt', 'a') as open_file:
    open_file.write('\nSorted list: ')
    for i in list_sort(list_of_strings_from_file):
        open_file.write(str(i) + ' ')
