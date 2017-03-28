import numpy as np
from os import listdir
from os.path import isfile, join
from plotting_functions import plot_res_curves_2d, plot_res_curves_3d, plot_raw_data


class MeasurementData:
    def __init__(self, data):
        self.data = data
        self.mes_name = 'measurement name'
        self.mes_date = 'measurement date'
        self.mes_type = 'measurement type'

    def set_name(self, text):
        self.mes_name = text

    def set_date(self, text):
        self.mes_date = text

    def set_type(self, text):
        self.mes_type = text

    def plot_data_2d(self, show=True, save=False):
        plot_res_curves_2d(self.data, self.mes_name, self.mes_date, self.mes_type, show, save)

    def plot_data_3d(self, show=True, save=False):
        plot_res_curves_3d(self.data, self.mes_name, self.mes_date, self.mes_type, show, save)

    def plot_data_raw(self, show=True, save=False):
        plot_raw_data(self.data, self.mes_name, self.mes_date, self.mes_type, show, save)


def extract_data(path_to_data, m_date, m_type):
    data_files = [f for f in listdir(path_to_data) if isfile(join(path_to_data, f))]
    print(data_files)
    all_data = []
    for data_file in data_files:
        data = np.loadtxt(path_to_data+data_file, comments='#')
        m_data = MeasurementData(data)
        m_data.set_name(data_file[:-4])
        m_data.set_date(m_date)
        m_data.set_type(m_type)
        all_data.append(m_data)
    return all_data
