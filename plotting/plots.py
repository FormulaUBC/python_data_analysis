import matplotlib.pyplot as plt
from aim_data_csv_read import Data
import numpy as np

def plot_ax_vs_t(dat):
    fig = plt.figure()
    plt.plot(dat.data['Time']['data'], dat.data['AccelerometerX']['data'])
    plt.show(fig)


def g_g_diagram(dat):
    fig = plt.figure()
    gx_temp = dat.data['AccelerometerX']['data']
    gy_temp = dat.data['AccelerometerY']['data']
    gx = []
    gy = []
    for i in range(len(gx_temp) - 1):
        if np.sqrt(np.abs(float(gx_temp[i+1]) - float(gx_temp[i]))**2 + np.abs(float(gy_temp[i+1]) - float(gy_temp[i]))**2) < 2:
            gx.append(gx_temp[i+1])
            gy.append(gy_temp[i+1])

    plt.plot(gx, gy, '+')
    plt.show()