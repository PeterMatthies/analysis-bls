import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

path_to_data = './m_data/15102017_dispersions/'
data_file_1 = 'PyCuPy-dispersion_1.dat'

data_file_2 = 'CoFeBIrCoFeB-dispersion.dat'

with open(path_to_data+data_file_1, 'r') as f:
    data_1 = np.array([[float(Fraction(x)) for x in line.split(',')] for line in f.readlines()])

with open(path_to_data+data_file_2, 'r') as f:
    data_2 = np.array([[float(Fraction(x)) for x in line.split(',')] for line in f.readlines()])

data_x_1 = data_1[:, 0] * 10000
data_y_1 = data_1[:, 1]

data_x_2 = data_2[:, 0] * 10000
data_y_2 = data_2[:, 1]

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.plot(data_x_1, data_y_1)
ax1.set_ylabel('Frequency (GHz)', fontsize=16)
ax1.set_xlabel(r'$k_z$'+' '+r'$(cm^{-1}$)', fontsize=18)
ax1.tick_params(axis='both', which='major', labelsize=14)
ax1.ticklabel_format(axis='x', style='sci', scilimits=(-3, 3), useOffset=False)
ax1.xaxis.major.formatter._useMathText = True

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)

print(data_x_1[data_x_1 >= 1.67e5][0])
print(data_x_1[data_x_1 <= 1.67e5][-1])
ind_k = np.where(data_x_1 <= 1.67e5)[0][-1]
print(data_x_1[ind_k])
print(data_x_1[-ind_k-1])
freq_diff_k45 = data_y_1[ind_k] - data_y_1[-ind_k-1]
print('freq diff for 45 deg inc light: ', freq_diff_k45)

pos_k_1 = data_x_1 > 0
neg_k_1 = data_x_1 < 0

pos_k_2 = data_x_2 > 0
neg_k_2 = data_x_2 < 0

delta_freq_array_1 = data_y_1[pos_k_1] - data_y_1[neg_k_1][::-1]
delta_freq_array_2 = data_y_2[pos_k_2] - data_y_2[neg_k_2][::-1]

ax2.plot(data_x_1[pos_k_1], delta_freq_array_1, color='blue', label='Py/Cu/Py')
ax2.plot(data_x_1[pos_k_2], delta_freq_array_2, color='orange', label='CoFeB/Ir/CoFeB')


ax2.set_ylabel(r'$\Delta f$' + ' ' + r'$(GHz)$', fontsize=16)
ax2.set_xlabel(r'$k_z$'+' '+r'$(cm^{-1}$)', fontsize=18)
ax2.tick_params(axis='both', which='major', labelsize=14)
ax2.ticklabel_format(axis='x', style='sci', scilimits=(-3, 3), useOffset=False)
ax2.xaxis.major.formatter._useMathText = True
#
fig2.tight_layout()

# fig1.text(0.32, 0.81, r'$H_{bias}= 11.5mT$', va='center', rotation='horizontal', fontsize=16)
fig1.tight_layout()
plt.legend(loc=4, prop={'size': 16})
plt.grid()
# save_name = 'pycupy_dispersion_2.pdf'
# save_name = 'cofeb_ir_cofeb_dispersion_1.pdf'
# save_name = 'pycupy_freq_diff.pdf'
save_name = 'comb_freq_diff.pdf'
plt.savefig('./output_pics/nrcl/'+save_name, format='pdf', dpi=100)
# plt.show()
