import numpy as np
import matplotlib.pyplot as plt


path_to_data_1 = './m_data/29082017_nrcl/'
# data_file = 'm2_60mT.txt'
data_file = 'm5_-6mT.txt'

data = np.loadtxt(path_to_data_1 + data_file)
data_x = data[:, 0]
data_y = data[:, 1]

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)

ind_stokes = (data_x > -10) & (data_x < -6)
ind_astokes = (data_x > 6) & (data_x < 10)

data_plot_sx = data_x[ind_stokes]
data_plot_sy = data_y[ind_stokes]

data_plot_asx = data_x[ind_astokes]
data_plot_asy = data_y[ind_astokes]

ax1.plot(abs(data_plot_sx), data_plot_sy, marker='.', color='blue', label='Stokes peak')
ax1.plot(abs(data_plot_asx), data_plot_asy, marker='.', color='orange', label='Anti Stokes peak')

ax1.set_xlabel('Frequency (GHz)', fontsize=15)
ax1.set_ylabel('Intensity (a.u.)', fontsize=15)

# plt.fill(data_x, data_y)
ax1.set_ylim([0, 265])
# ax1.set_xlim([-12, -7])
# ax1.set_xticklabels([str(abs(x)) for x in ax1.get_xticks()])
fig1.tight_layout()
plt.legend(loc=4, prop={'size': 16})
save_name = '-6mT_ch2677_unfiltered.pdf'
plt.savefig('./output_pics/nrcl/'+save_name, format='pdf', dpi=100)
plt.show()