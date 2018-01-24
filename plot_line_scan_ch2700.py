import numpy as np
import matplotlib.pyplot as plt


# path_to_data = './m_data/30052017_nrcl/'
path_to_data = './m_data/23012018_nrcl/'
data_file_1 = 'm7_linescan.txt'
data_file_2 = 'm7_positions_x.txt'

fig = plt.figure()

ax1 = fig.add_subplot(111)
ax1.set_xlabel('Distance '+r'$\perp$'+' antenna '+r'$(\mu m)$', fontsize=15)
ax1.set_ylabel('Intensity (a.u.)', fontsize=15)
ax1.tick_params(axis='both', which='major', labelsize=12)


magn_field = '0mT'
fig.suptitle('Line scan for '+magn_field)

data_1 = np.loadtxt(path_to_data + data_file_1, comments='#')
x_pos1 = data_1[:, 0]
y_pos1 = data_1[:, 1]

data_2 = np.loadtxt(path_to_data + data_file_2, comments='#')
x_pos2 = data_2[:, 0]
y_pos2 = data_2[:, 1]

x_pos1_corrected = np.linspace(0, y_pos2[0]-y_pos2[-1], 100)

ax1.plot(x_pos1_corrected, y_pos1, color='blue', label='data')
antenna_index = y_pos1 < 15
ax1.axvspan(x_pos1_corrected[antenna_index][0], x_pos1_corrected[antenna_index][-1], color='grey', alpha=0.3, label='antenna')


max_y = max(y_pos1)
# max_y = max(np.maximum(y_pos1, y_pos2))
print(max_y)
ax1.set_ylim([0, max_y+0.05*max_y])


fig.tight_layout()
fig.subplots_adjust(top=0.95)
plt.grid()
# plt.legend(loc=1, bbox_to_anchor=(1.05, 1.0), prop={'size': 14})
plt.legend(loc=1, prop={'size': 14})
plt.savefig('./output_pics/nrcl/'+'line_scan_'+magn_field+'.png', format='png', dpi=100)
plt.show()
