from ContextManager import FileOpen
from abc import ABC, abstractmethod
import re


class CsvJsonConverter(ABC):
    @abstractmethod
    def read_csv(self):
        pass

    @abstractmethod
    def data_convert(self, data_list):
        pass

    @abstractmethod
    def write_json(self, data_for_json):
        pass


class Converter(CsvJsonConverter):
    def __init__(self):
        self.csv_file_name = input('Enter .csv file name: ')
        self.json_file_name = input('Enter .json file name: ')

    def read_csv(self):  # read csv data from file
        with FileOpen(self.csv_file_name, 'r') as open_file:
            csv_data_from_file = open_file.readlines()
        csv_data = []
        for i in csv_data_from_file:
            result = re.findall(r'(".+?"|[^,]+)', i.replace('\n', ''))
            result = [re.sub(r'"(.+)"', r'\1', x) for x in result]
            csv_data.append(result)
        print('Data successfully read from .csv file.')
        return csv_data

    def data_convert(self, data_list):  # convert csv to json
        json_data = ''
        for i in data_list:
            json_data_element = ''
            if data_list[0] != i:
                for j, z in enumerate(i):
                    json_data_element += '"{}" : "{}",\n'.format(data_list[0][j], z)
                json_data += '{\n%s\n},\n' % json_data_element[:len(json_data_element) - 2]
        print('Data successfully converted from .csv to .json.')
        return json_data[:len(json_data) - 2]

    def write_json(self, data_for_json):  # write converted data in json file
        with FileOpen(self.json_file_name, 'a') as open_file:
            open_file.write('{ "csv_data":\n[\n%s\n]\n}' % data_for_json)
        print('Data successfully write in .json file.')


if __name__ == '__main__':
    converter = Converter()
    data_from_csv = converter.read_csv()
    converted_to_json_data = converter.data_convert(data_from_csv)
    converter.write_json(converted_to_json_data)
