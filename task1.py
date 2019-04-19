from ContextManager import FileOpen

with FileOpen(r'C:\Users\Aliaksandr.Baryhin\Desktop\dataFiles\task1_data.txt', 'r') as open_file:
    list_of_numbers_from_file = list(map(int, open_file.read().split(' ')))


def max_count_element(processing_list):
    count_list = [processing_list.count(j) for j in processing_list]
    return processing_list[count_list.index(max(count_list))]


with FileOpen(r'C:\Users\Aliaksandr.Baryhin\Desktop\dataFiles\task1_data.txt', 'a') as open_file:
    open_file.write('\nMax element is: ' + str(max_count_element(list_of_numbers_from_file)))
