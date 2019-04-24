from ContextManager import FileOpen

with FileOpen(r'.\dataFiles\task5_data.txt', 'r') as open_file:
    list_of_numbers_from_file = list(map(int, open_file.read().split(' ')))


def sorting_list(processing_list):
    for i in range(len(processing_list)):
        for j in range(len(processing_list) - i - 1):
            if processing_list[j] > processing_list[j + 1]:
                processing_list[j], processing_list[j + 1] = processing_list[j + 1], processing_list[j]
    return processing_list


with FileOpen(r'.\dataFiles\task5_data.txt', 'a') as open_file:
    open_file.write('\nSorted list: ')
    for a in sorting_list(list_of_numbers_from_file):
        open_file.write(str(a) + ' ')
