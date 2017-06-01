import numpy as np
import matplotlib.pyplot as plt


path_to_data = './m_data/30052017_nrcl/'
data_file = 'm5_extracted_both.txt'


fig = plt.figure()

ax1 = fig.add_subplot(111)
ax1.set_xlabel('Frequency(GHz)')
ax1.set_ylabel(' norm Intensity (a.u.)')

magn_field = '-80mT'
fig.suptitle('Freq Spectra for '+magn_field)

data = np.loadtxt(path_to_data + data_file, comments='#')
x_pos1 = data[:, 0]
y_pos1 = data[:, 1]/max(data[:, 3])
x_pos2 = data[:, 2]
y_pos2 = data[:, 3]/max(data[:, 3])

ax1.plot(x_pos1, y_pos1, color='blue', label='above antenna')
ax1.plot(x_pos2, y_pos2, color='red', label='below antenna')

xticks_new = np.linspace(5e9, 11e9, 13)
yticks_new = np.linspace(0, 1, 11)
print(xticks_new)
print(yticks_new)
ax1.set_xticks(xticks_new)
ax1.set_yticks(yticks_new)
ax1.ticklabel_format(axis='x', style='sci', scilimits=(-3, 3), useOffset=False)
ax1.xaxis.major.formatter._useMathText = True
ax1.set_xlim([5.0e9, 11.0e9])
ax1.set_ylim([0, 1.001])


fig.tight_layout()
fig.subplots_adjust(top=0.92)
plt.grid()
plt.legend()
plt.savefig('freq_spec_'+magn_field+'.png', format='png', dpi=100)
plt.show()
