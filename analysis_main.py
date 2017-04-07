import extract_data as ed
import matplotlib.cm as cm

# main file for calling the analysis functions

# path_to_data = './m_data/21_10_2016/res_curves/'
# path_to_data = './m_data/24_10_2016/phase_res_curves/withoutDC/'
# path_to_data = './m_data/24_10_2016/'
path_to_data = './m_data/26-10-2016/'
# path_to_data = './m_data/24_10_2016/m4-m8/'
# path_to_data = './m_data/25-10-2016/'
# path_to_data = './m_data/19-12-2016/'
# path_to_data = './m_data/20-12-2016/'
# path_to_data = './m_data/04-11-2016/'

# path_to_file = './m_data/26-10-2016/m4_spec_integrated_7to5p5GHz_40mA.txt'
# path_to_file = './m_data/25-10-2016/m3_spec_integrated_7to5p5GHz_00mA.txt'
# path_to_file = './m_data/25-10-2016/m5_spec_integrated_7to5p5GHz_20mA.txt'

# path_to_file = './m_data/24_10_2016/m2_he_00mA.txt'
# path_to_file = './m_data/24_10_2016/m3_he_10mA.txt'
# path_to_file = './m_data/24_10_2016/m3_he_20mA.txt'

# m_name = path_to_file.split('/')[-1][:-4]
# m_date = path_to_file.split('/')[-2]
# print(m_name)

# m_data = ed.extract_data_file(path_to_file, m_name, m_date, m_type='Phase resolved line scan')
# m_data.plot_data_2d_v2(save=1, show=1)


# path_to_file = '/Users/Peter/Documents/bls/non_reciprocity/thermal spectra/raw_spec_e3.dat'
# m_name = 'e3'
# m_date = '13-03-2017'
# m_data = ed.extract_data_file(path_to_file, m_name, m_date, m_type='thermal spectrum field sweep')
# m_data.plot_data_raw(save=0, show=1)

# for loop to analyze multiple data files
# all_data = ed.extract_data_folder(path_to_data, m_date='26102016', m_type='Phase resolved line scan')
# print(all_data)
#
# for data_entry in all_data[3:4]:
#     print(data_entry.mes_name)
#     if 'all' in data_entry.mes_name:
#         data_entry.plot_data_3d(save=0, show=0)
#     elif 'raw' in data_entry.mes_name:
    #       data_entry.plot_data_raw(save=1, show=1)
    # elif 'integrated' in data_entry.mes_name:
    #      data_entry.plot_data_2d(save=0, show=1)
    # else:
    #     data_entry.plot_data_2d(save=0, show=0)