import extract_data as ed
import matplotlib.cm as cm

# main file for calling the analysis functions

# path_to_data = './m_data/21_10_2016/res_curves/'
# path_to_data = './m_data/24_10_2016/phase_res_curves/withoutDC/'
# path_to_data = './m_data/24_10_2016/'
# path_to_data = './m_data/24_10_2016/m4-m8/'
path_to_data = './m_data/25-10-2016/'
# path_to_data = './m_data/19-12-2016/'
# path_to_data = './m_data/20-12-2016/'
# path_to_data = './m_data/04-11-2016/'

# m_names = ['point 4', 'point 8', 'point 10', 'point 12', 'point 14']
# m_names = ['4.4GHz', '4.4GHz #2', '5.1GHz']
m_names = []


all_data = ed.extract_data(path_to_data, m_date='25102016', m_type='Phase resolved line scan')
print(all_data)

for data_entry in all_data[:]:
    print(data_entry.mes_name)
    if 'all' in data_entry.mes_name:
        data_entry.plot_data_3d(save=0, show=0)
    elif 'raw' in data_entry.mes_name:
          data_entry.plot_data_raw(save=1, show=1)
    # elif 'he' in data_entry.mes_name:
    #      data_entry.plot_data_2d(save=0, show=0)
    # else:
    #     data_entry.plot_data_2d(save=0, show=0)
