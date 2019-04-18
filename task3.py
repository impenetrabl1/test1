from ContextManager import FileOpen

with FileOpen(r'C:\Users\Aliaksandr.Baryhin\Desktop\dataFiles\task3_first_list.txt') as open_file:
    first_list_from_file = list(open_file.read().split(' '))
with FileOpen(r'C:\Users\Aliaksandr.Baryhin\Desktop\dataFiles\task3_second_list.txt') as open_file:
    second_list_from_file = list(map(int, open_file.read().split(' ')))


def lists_merge(first_merging_list, second_merging_list, optional_dict={}):
    united_dict = dict(zip(first_merging_list, second_merging_list))
    if optional_dict == {}:
        return united_dict
    return optional_dict.update(dict1)


print(first_list_from_file, second_list_from_file)
print(lists_merge(first_list_from_file, second_list_from_file))
