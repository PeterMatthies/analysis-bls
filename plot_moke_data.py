import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes, inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

path_to_data = './m_data/CFB_Ir_CFB/'
data_file = 'CH2700_CFB10nm_Ir_CFB10nm_Ir_2nmcap.dat'

data = np.loadtxt(path_to_data+data_file)
h_x = data[:, 2]
kerr_signal = data[:, 3]*(-1)

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)

ax1.plot(h_x, kerr_signal)
ax1.set_xlim([min(h_x), max(h_x)])
ax1.set_ylim([-1.05, 1.05])
ax1.axhline(0, color='grey')
ax1.axvline(0, color='grey')
# ax1.axvspan(-110, 50, color='yellow', alpha=0.3, label='AF state')
# ax1.annotate('-110 Oe', xy= (-110, 0.3), xytext=(-600, 0.5), color='black',
#              arrowprops=dict(arrowstyle='->'), fontsize= 16)
# ax1.annotate('50 Oe', xy= (50, -0.3), xytext=(200, -0.5), color='black',
#              arrowprops=dict(arrowstyle='->'), fontsize= 16)
ax1.set_xlabel('Applied Magnetic Field (Oe)', fontsize=16)
ax1.set_ylabel('Kerr Signal (a.u.)', fontsize=16)
ax1.tick_params(axis='both', which='major', labelsize=14)

# axins = zoomed_inset_axes(ax1, 2.5, loc=5)
ax2 = inset_axes(ax1, width=2.2, height=3.0, loc=5)
ax2.plot(h_x, kerr_signal)
# axins.plot(h_x, kerr_signal)
ax2.axis([-150, 100, -0.35, 0.35])
ax2.tick_params(axis='both', which='major', labelsize=14)
x1, x2, y1, y2 = -150, 100, -0.35, 0.35 # specify the limits
# axins.set_xlim(x1, x2) # apply the x-limits
# axins.set_ylim(y1, y2) # apply the y-limits
plt.xticks(rotation=45)
# mark_inset(ax1, axins, loc1=3, loc2=2, fc="none", ec="0.5")
mark_inset(ax1, ax2, loc1=3, loc2=2, fc="none", ec="0.5")

fig1.tight_layout()
save_name = 'easy_axis_loop.png'
plt.legend()
plt.savefig('./output_pics/nrcl/'+save_name, format='png', dpi=100)
plt.show()