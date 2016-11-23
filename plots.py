import matplotlib.pyplot as plt
from aim_data_csv_read import Data

def plot_ax_vs_t(dat):
    fig = plt.figure()
    plt.plot(dat.data['Time']['data'], dat.data['AccelerometerX']['data'])
    plt.show(fig)


def g_g_diagram(dat):
    fig = plt.figure()
    plt.plot(dat.data['AccelerometerX']['data'], dat.data['AccelerometerY']['data'], '+')
    plt.show()