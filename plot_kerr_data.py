import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes, inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

path_to_data = './m_data/kerr_ch2700/'
data_file = 'loop_data_4.txt'
field_calib_file = 'field_calib.txt'

data = np.loadtxt(path_to_data+data_file)
field_calib_data = np.loadtxt(path_to_data+field_calib_file)
v_x = field_calib_data[:, 0]
field_x = field_calib_data[:, 1]*10

# fig_field_calib = plt.figure()
# ax = fig_field_calib.add_subplot(111)
# ax.plot(v_x, field_x)
coefs = np.polyfit(v_x, field_x, 1)


voltage_x = data[:, 0]
kerr_signal = data[:, 1]

h_x = coefs[0] * voltage_x + coefs[1]

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)


ax1.plot(h_x, kerr_signal)
ax1.set_xlim([min(h_x), max(h_x)])
ax1.set_ylim([-1.05, 1.05])
ax1.axhline(0, color='grey')
ax1.axvline(0, color='grey')

ax1.set_xlabel('Applied Magnetic Field (Oe)', fontsize=16)
ax1.set_ylabel('Kerr Signal (a.u.)', fontsize=16)
ax1.tick_params(axis='both', which='major', labelsize=14)


# ax2 = inset_axes(ax1, width=2.2, height=3.0, loc=5)
# ax2.plot(h_x, kerr_signal)
# ax2.axis([-100, 100, -0.42, 0.33])
# ax2.tick_params(axis='both', which='major', labelsize=14)
# x1, x2, y1, y2 = -100, 100, -0.42, 0.33 # specify the limits
# plt.xticks(rotation=45)
# mark_inset(ax1, ax2, loc1=3, loc2=2, fc="none", ec="0.5")

fig1.tight_layout()
save_name = 'hard_axis_loop_kerr.png'
plt.legend()
plt.savefig('./output_pics/nrcl/'+save_name, format='png', dpi=100)
plt.show()