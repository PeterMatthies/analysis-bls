import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

path_to_data = './m_data/15102017_dispersions/'
data_file_1 = 'Isofrequency_3GHz-d1_6d2_6Ms1_800Ms2_800-Py-Cu-Py.txt'
data_file_2 = 'Isofrequency_4GHz-d1_6d2_6Ms1_800Ms2_800-Py-Cu-Py.txt'
data_file_3 = 'Isofrequency_5GHz-d1_6d2_6Ms1_800Ms2_800-Py-Cu-Py.txt'

data_1 = np.loadtxt(path_to_data+data_file_1)
data_2 = np.loadtxt(path_to_data+data_file_2)
data_3 = np.loadtxt(path_to_data+data_file_3)

k_x_1 = data_1[:, 0] * 10000 / (2 * np.pi)
k_z_1 = data_1[:, 1] * 10000 / (2 * np.pi)

k_x_2 = data_2[:, 0] * 10000 / (2 * np.pi)
k_z_2 = data_2[:, 1] * 10000 / (2 * np.pi)

k_x_3 = data_3[:, 0] * 10000 / (2 * np.pi)
k_z_3 = data_3[:, 1] * 10000 / (2 * np.pi)

dk_x = np.gradient(k_x_1)
dk_z = np.gradient(k_z_1)

vel = np.array([[dk_x[i], dk_z[i]] for i in range(dk_x.size)])
print(vel)

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.plot(k_z_1, k_x_1, label='3 GHz', color='blue')
ax1.plot(k_z_2, k_x_2, label='4 GHz', color='orange')
ax1.plot(k_z_3, k_x_3, label ='5 GHz', color='red')

ax1.set_xlabel(r'$k_z$'+' '+r'$(cm^{-1}$)', fontsize=18)
ax1.set_ylabel(r'$k_x$'+' '+r'$(cm^{-1}$)', fontsize=18)
ax1.tick_params(axis='both', which='major', labelsize=14)
ax1.ticklabel_format(axis='x', style='sci', scilimits=(-3, 3), useOffset=False)
ax1.ticklabel_format(axis='y', style='sci', scilimits=(-3, 3), useOffset=False)
ax1.xaxis.major.formatter._useMathText = True
ax1.yaxis.major.formatter._useMathText = True

fig1.tight_layout()

plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.legend(loc=4, prop={'size': 16})
save_name = 'isofreq_curves_comb.pdf'
plt.savefig('./output_pics/nrcl/'+save_name, format='pdf', dpi=100)
# plt.plot(k_x, k_z)
# plt.plot(vel[:, 0], vel[:, 1])
# plt.grid()
plt.show()