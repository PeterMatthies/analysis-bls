import numpy as np
import matplotlib.pyplot as plt


# path_to_data = './m_data/30052017_nrcl/'
# path_to_data = './m_data/30012018_ncrl/m6/'
path_to_data = './m_data/30012018_ncrl/'
# data_file_1 = 'm6_f06_pos2.txt'
# data_file_2 = 'm6_f06_pos1.txt'
# field_values_file ='m6_field_values.txt'

data_file_1 = 'm8_pos2.txt'
data_file_2 = 'm8_pos1.txt'


fig = plt.figure()

ax1 = fig.add_subplot(111)
ax1.set_xlabel('Frequency (GHz)', fontsize=15)
ax1.set_ylabel('Intensity (a.u.)', fontsize=15)
ax1.tick_params(axis='both', which='major', labelsize=12)

#field_data = np.loadtxt(path_to_data+field_values_file)
#magn_field = field_data[:, 1][int(data_file_1[4:6])-1] * 1000

magn_field = -0.73

fig.suptitle('Freq Spectra for '+str(magn_field)+ ' mT')

data_1 = np.loadtxt(path_to_data + data_file_1, comments='#')
x_pos1 = data_1[:, 0] / 1e9
y_pos1 = data_1[:, 1] # /max(data[:, 1])

data_2 = np.loadtxt(path_to_data + data_file_2, comments='#')
x_pos2 = data_2[:, 0] / 1e9
y_pos2 = data_2[:, 1] # /max(data[:, 1])

ax1.plot(x_pos1, y_pos1, color='blue', label='above antenna (+k)')
ax1.plot(x_pos2, y_pos2, color='red', label='below antenna (-k)')

ax1.set_xlim([min(x_pos1), max(x_pos1)])
max_y = max(np.maximum(y_pos1, y_pos2))
print(max_y)
ax1.set_ylim([0, max_y+0.05*max_y])


fig.tight_layout()
fig.subplots_adjust(top=0.95)
plt.grid()
# plt.legend(loc=1, bbox_to_anchor=(1.05, 1.0), prop={'size': 14})
plt.legend(loc=2, prop={'size': 14})
magn_field_save = str(magn_field).replace('.', 'p') + 'mT'
plt.savefig('./output_pics/nrcl/h3/'+'freq_spec_h3_'+magn_field_save+'.png', format='png', dpi=100)
plt.show()
