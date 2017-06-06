import numpy as np
import matplotlib.pyplot as plt


path_to_data = './m_data/01062017_nrcl/'
data_file = 'm1_extracted_both.txt'
field_values_file = 'field_values_m1.dat'


fig = plt.figure()

ax1 = fig.add_subplot(111)
ax1.set_xlabel('Magn. Field(mT)')
ax1.set_ylabel(' norm Intensity (a.u.)')

freq = '2.8 GHz'
fig.suptitle('Field Sweep for '+freq)

x_line1 = np.array([6.2 for i in range(10000)])
y_line1 = np.linspace(0, 1, 10000)
x_line2 = np.array([14.5 for i in range(10000)])
y_line2 = np.linspace(0, 1, 10000)

ax1.plot(x_line1, y_line1, linestyle='--', color='grey')
ax1.plot(x_line2, y_line2, linestyle='--', color='grey')
ax1.axvspan(6.2, 14.5, color='grey', alpha=0.3, label='AF-coupled region')

data = np.loadtxt(path_to_data + data_file, comments='#')
field_values = np.loadtxt(path_to_data + field_values_file, comments='#')
print(field_values[:, 1])
x_pos1 = field_values[:, 1]*1000
# x_pos1 = data[:, 0]
y_pos1 = data[:, 1]/max(data[:, 1])
# x_pos2 = data[:, 0]
x_pos2 = field_values[:, 1]*1000
y_pos2 = data[:, 3]/max(data[:, 1])

ax1.plot(x_pos1, y_pos1, color='blue', label='above antenna')
ax1.plot(x_pos2, y_pos2, color='red', label='below antenna')

xticks_new = np.linspace(-15, 15, 16)
yticks_new = np.linspace(0, 1, 11)
print(xticks_new)
print(yticks_new)
ax1.set_xticks(xticks_new)
ax1.set_yticks(yticks_new)
# ax1.ticklabel_format(axis='x', style='sci', scilimits=(-3, 3), useOffset=False)
# ax1.xaxis.major.formatter._useMathText = True
ax1.set_xlim([-9.71, 15])
ax1.set_ylim([0, 1.001])


fig.tight_layout()
fig.subplots_adjust(top=0.92)
plt.grid()
plt.legend()
plt.savefig('field_sweep_'+freq+'.png', format='png', dpi=100)
plt.show()
