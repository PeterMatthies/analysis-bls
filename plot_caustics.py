import numpy as np
import matplotlib.pyplot as plt


path_to_data = './m_data/02062017_nrcl/extracted/'
data_file = 'm7_4GHz_caustics.txt'
positions_dim1_file = 'm7_pos_dim1.txt'
positions_dim2_file = 'm7_pos_dim2.txt'


fig = plt.figure()

ax1 = fig.add_subplot(111)
ax1.set_xlabel('position along antenna '+r'$(\mu m)$')
ax1.set_ylabel(' norm Intensity (a.u.)')

freq = '4.0 GHz'
fig.suptitle('Caustics for '+freq)


data = np.loadtxt(path_to_data + data_file, comments='#')
dim1_data = np.loadtxt(path_to_data + positions_dim1_file, comments='#')
dim2_data = np.loadtxt(path_to_data + positions_dim2_file, comments='#')
distance_to_antenna_1 = dim1_data[:, 1][0] - dim1_data[:, 1][2]
distance_to_antenna_2 = dim1_data[:, 1][1] - dim1_data[:, 1][2]
length = abs(dim2_data[:, 1][1] - dim2_data[:, 1][0])
real_space_x = np.linspace(0, length, 100)
print(real_space_x[52])
print(length)
# print(distance_to_antenna_1, distance_to_antenna_2)

x1 = data[:, 0]
y1 = data[:, 1]/max(data[:, 1])
x2 = data[:, 2]
y2 = data[:, 3]/max(data[:, 3])

ax1.plot(real_space_x, y1, color='red', label='1 um from antenna')
ax1.plot(real_space_x, y2, color='blue', label='close to antenna')
print(np.average(y1))
print(np.average(y2))

yticks_new = np.linspace(0, 1, 11)
xticks_new = np.linspace(0, length, 12)
ax1.set_yticks(yticks_new)
ax1.set_xticks(xticks_new)
ax1.set_xlim([0, 16.5])
ax1.set_ylim([0, 1.001])

fig.tight_layout()
fig.subplots_adjust(top=0.92)
plt.grid()
plt.legend()
plt.savefig('./output_pics/nrcl/'+'caustics_'+freq+'.png', format='png', dpi=100)
plt.show()
