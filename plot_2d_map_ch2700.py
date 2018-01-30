import numpy as np
import matplotlib.pyplot as plt
import re

path_to_data = './m_data/28012018_nrcl/'
data_file = 'm6_2d_map.txt'

# loading the data
data_raw = np.loadtxt(path_to_data+data_file, comments='#')


# plotting the data
fig1 = plt.figure(figsize=(12, 3), dpi=100)
ax1 = fig1.add_subplot(111)
pos_f = ''

# fig1.suptitle('BLS Spectrum '+pos+' antenna\n'+'excitation at '+str(excitation_freq)+' GHz')

cmap = plt.get_cmap('magma')
cmap.set_under('black')
# cmap.set_over('black')
eps1 = np.spacing(0)
im = ax1.imshow(data_raw, origin='upper', aspect='auto', vmin=eps1, vmax=100, cmap=cmap, interpolation='nearest',
                  extent=(0, 300, 5, 0))

print(data_raw.T.shape)
ax1.set_ylim([5, 0])
ax1.set_xlim([0, 300])


# adjusting the axes ticks

y_ticks = np.arange(0, data_raw.shape[0]+1, 1)
print(y_ticks)
y_tick_labels = np.linspace(3.5, 0, len(y_ticks))
y_tick_labels = ["{0:.1f}".format(y_tick) for y_tick in y_tick_labels]
ax1.set_yticks(y_ticks)
ax1.set_yticklabels(y_tick_labels)


x_ticks = np.arange(0, data_raw.shape[1]+37.5, 37.5)
print(x_ticks)

x_line1 = np.array([150 for i in range(10000)])
y_line1 = np.linspace(-5, 5, 10000)
ax1.plot(x_line1, y_line1, linestyle='--', linewidth=4.0, color='green', alpha=1.0, label='middle of antenna')


x_tick_labels = np.linspace(0, 35, 9)
print(x_tick_labels)
x_tick_labels = ["{0:.1f}".format(x_tick) for x_tick in x_tick_labels]
ax1.set_xticks(x_ticks)
ax1.set_xticklabels(x_tick_labels)


ax1.set_xlabel('position along antenna '+r'$(\mu m)$')
# ax1.set_xlabel(x_axis_name)
ax1.set_ylabel('position from antenna '+r'$(\mu m)$')

cbar = fig1.colorbar(im)
cbar.set_label('Intensity (a.u.)', rotation=270)
cbar.ax.get_yaxis().labelpad = 15
# cbar.ax.set_yticklabels('')

ax1.legend(loc=1, bbox_to_anchor=(1.0, -0.07))
fig1.tight_layout()


fig1.tight_layout()
fig1.subplots_adjust(top=0.94, bottom=0.25)
fig1.subplots_adjust(right=1.06, left=0.06)


save_name = '2d_map_4p25GHz_1mT_H6_5dBm_v2.png'
# print(save_name)
plt.savefig('./output_pics/nrcl/'+save_name, format='png', dpi=100)
plt.show()