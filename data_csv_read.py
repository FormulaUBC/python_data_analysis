import csv

class Data(object):
    """Class meant to represent the data stored in one of the AIM dash's csv data files"""

    def __init__(self, file_path):
        self.meta_data = {}
        self.data = {}
        self.data_fields = []
        self.num_data_entries = 0
        
        file = open(file_path, 'rb')
        reader = csv.reader(file, delimiter=',')

        row = reader.next()
        while len(row) != 0:
            self.meta_data[row[0]] = row[1]
            row = reader.next()

        title_row = reader.next()
        reader.next()
        unit_row = reader.next()
        channel_id_row = reader.next()
        for i in range(len(title_row)):
            title = title_row[i]
            self.data_fields.append(title)
            self.data[title] = {'unit': unit_row[i], 'channel_id': channel_id_row[i], 'data': []}

        reader.next()
        for data_row in reader:
            for i in range(len(data_row)):
                self.data[title_row[i]]['data'].append(data_row[i])
                self.num_data_entries += 1

    def __str__(self):
        return "Data object. \n\nMetadata: \n %s \n\nData Fields: \n %s"\
            % (str(self.meta_data), str(self.data_fields))


if __name__ == '__main__':
    test_data = Data('C:\Users\cyrus\Documents\GitHub\python_data_analysis\sample_data\Autocross_10Hz_Data_2a.csv')
    print(test_data)
    print('\n')
    print(test_data.num_data_entries)
