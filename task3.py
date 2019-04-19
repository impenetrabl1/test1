from ContextManager import FileOpen

with FileOpen(r'.\dataFiles\task3_data.txt', 'r') as open_file:
    data_from_file = open_file.readlines()
first_list_from_file = list(data_from_file[0].replace('\n', '').split(' '))
second_list_from_file = list(map(int, data_from_file[1].replace('\n', '').split(' ')))
opt_dictionary = dict(zip(list(data_from_file[2].replace('\n', '').split(' ')),
                          list(map(int, data_from_file[3].replace('\n', '').split(' ')))))


def lists_merge(first_merging_list, second_merging_list, optional_dict={}):
    united_dict = dict(zip(first_merging_list, second_merging_list))
    if optional_dict == {}:
        return united_dict
    optional_dict.update(united_dict)
    return optional_dict


with FileOpen(r'.\dataFiles\task3_data.txt', 'a') as open_file:
    open_file.write('\nUnited dictionary: ')
    for i, j in lists_merge(first_list_from_file, second_list_from_file, opt_dictionary).items():
        open_file.write(str(i)+':'+str(j)+' ')
