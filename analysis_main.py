import extract_data as ed
import matplotlib.cm as cm

# path_to_data = './m_data/21_10_2016/res_curves/'
path_to_data = './m_data/24_10_2016/phase_res_curves/withoutDC/'

m_names = ['point 4', 'point 8', 'point 10', 'point 12', 'point 14']
m_names = ['4.4GHz', '4.4GHz #2', '5.1GHz']
all_data = ed.extract_data(path_to_data, m_names, m_date='24102016', m_type='phase resolved line scans')
print(all_data)

for data_entry in all_data:
    data_entry.plot_data_2d(save=1, show=0)
    # data_entry.plot_data_3d(save=0, show=1)