import csv

class Data(object):
    """Class meant to represent the data stored in one of the AIM dash's csv data files"""

    def __init__(self, file_path):
        """Initialize and populate object
        
        @param - file_path, The name of the file to be loaded if it is in the current directory, the full file path otherwise.

        """
        self.meta_data = {}
        self.data = {}
        self._data_fields = []
        self._num_data_entries = 0
        
        file = open(file_path, 'rb')
        reader = csv.reader(file, delimiter=',')

        row = reader.next()
        while len(row) != 0:
            self.meta_data[row[0]] = row[1]
            row = reader.next()

        title_row = reader.next()
        reader.next()  # Skip blank line
        unit_row = reader.next()
        channel_id_row = reader.next()
        for i in range(len(title_row)):
            title = title_row[i]
            self._data_fields.append(title)
            self.data[title] = {'unit': unit_row[i], 'channel_id': channel_id_row[i], 'data': []}

        reader.next()
        for data_row in reader:
            for i in range(len(data_row)):
                self.data[title_row[i]]['data'].append(data_row[i])
                self._num_data_entries += 1

        file.close()

    def __str__(self):
        return "Data object. \n\nMetadata: \n %s \n\nData Fields: \n %s"\
            % (str(self.meta_data), str(self._data_fields))
