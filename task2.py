from ContextManager import FileOpen

with FileOpen(r'C:\Users\Aliaksandr.Baryhin\Desktop\dataFiles\task2_data.txt') as open_file:
    list_of_strings_from_file = list(open_file.read().split(' '))


def list_sort(sortable_list):
    return sorted(sortable_list, key=len)


print(list_of_strings_from_file)
print(list_sort(list_of_strings_from_file))
