from data_csv_read import Data

def test_dataset_object():
    test_data = Data('C:\Users\cyrus\Documents\GitHub\python_data_analysis\sample_data\Autocross_10Hz_Data_2a.csv')
    print(test_data)
    print('\n')
    print(test_data.num_data_entries)

if __name__ == '__main__':
    test_dataset_object()