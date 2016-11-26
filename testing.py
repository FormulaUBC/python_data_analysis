from plotting import plots
from file_handling.aim_data_csv_read import Data

def test_dataset_object(dat):
    print(dat)
    print('\n')
    print(dat.num_data_entries)

def test_ax_vs_t(dat):
    plots.plot_ax_vs_t(dat)

def test_g_g_diagram(dat):
    plots.g_g_diagram(dat)

if __name__ == '__main__':
    test_data_path = 'C:\Users\cyrus\Documents\GitHub\python_data_analysis\sample_data\Autocross_10Hz_Data_2a.csv'
    dat = Data(test_data_path)
    # test_ax_vs_t(dat)
    test_g_g_diagram(dat)
