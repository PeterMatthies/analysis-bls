import numpy as np
import matplotlib.pyplot as plt

# loading the data

path_to_data = './m_data/30012018_nrcl/'
data_file = 'm6_raw_above.txt'
field_values_file ='m6_field_values.txt'

data_raw = np.loadtxt(path_to_data+data_file, comments='#')
print(data_raw.shape)
field_data = np.loadtxt(path_to_data+field_values_file)
magn_field = field_data[:, 1] * 1000


# plotting the data
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
pos = 'above'
fig1.suptitle('BLS Spectrum '+pos+' antenna')

cmap = plt.get_cmap('magma')
cmap.set_under('black')
# cmap.set_over('black')
eps1 = np.spacing(0)
im = ax1.imshow(data_raw, origin='lower', aspect='auto', vmin=eps1, vmax=400, cmap=cmap, interpolation='nearest',
                extent=(0, 6, 0, 50))


# adjusting the axes ticks


y_tick_labels = np.linspace(3, 8, 6)
y_tick_labels = ["{0:.1f}".format(y_tick) for y_tick in y_tick_labels]
x_tick_labels = np.linspace(min(magn_field), max(magn_field), 7)
print(x_tick_labels)
x_tick_labels = ["{0:.2f}".format(x_tick) for x_tick in x_tick_labels]
ax1.set_xticklabels(x_tick_labels)
ax1.set_yticklabels(y_tick_labels)

# axis labels

ax1.set_xlabel(r'$\mu_0 H$'+' (mT)', fontsize=15)
ax1.set_ylabel('Excitation frequency (GHz)', fontsize=15)

# color bar for the intensity

cbar = fig1.colorbar(im)
cbar.set_label('Intensity (a.u.)', rotation=270)
cbar.ax.get_yaxis().labelpad = 15
# cbar.ax.set_yticklabels('')

# tight layout, borders etc

fig1.tight_layout()
fig1.subplots_adjust(top=0.94, bottom=0.25)
fig1.subplots_adjust(right=0.98, left=0.16)

# saving resulting plot

plt.savefig('./output_pics/nrcl/rf_field_sweep_'+pos+'.png', format='png', dpi=100)
plt.show()