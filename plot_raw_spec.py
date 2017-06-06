import numpy as np
import matplotlib.pyplot as plt

path_to_data = './m_data/02062017_nrcl/'
data_file = 'm2_extracted_both.txt'

fig1 = plt.figure()

freq = '4.0 GHz'
fig1.suptitle('Freq Spectra for '+freq)

cmap = plt.get_cmap('jet')
cmap.set_under('black')
# cmap.set_over('black')
eps1 = np.spacing(0)
im = ax1.imshow(data.T, origin='lower', aspect='auto', vmin=eps1, vmax=6000, cmap=cmap)

print(data.T.shape)
proper_yticks_labels = np.linspace(0, 160, 13)
ax1.set_yticklabels(proper_yticks_labels)
ax1.set_yticks(proper_yticks_labels)
proper_yticks_labels = np.linspace(-9, 3, 13)
proper_yticks_labels= ["{0:.2f}".format(y_tick) for y_tick in proper_yticks_labels]
ax1.set_yticklabels(proper_yticks_labels)
proper_xticks_labels = np.linspace(0, 100, 11)
ax1.set_xticks(proper_xticks_labels)
proper_xticks_labels = np.linspace(0, 22.3, 11)
proper_xticks_labels = [int(x_tick) for x_tick in proper_xticks_labels]
ax1.set_xticklabels(proper_xticks_labels)

ax1.set_xlabel('Position along Py stripe'+r' ($\mu m$)')
ax1.set_ylabel('BLS Frequency (GHz)')

# fig1.colorbar(im)
if save:
    save_name = m_date + '_' + m_name + '_' + m_type + '.png'
    plt.savefig(save_name, format='png', dpi=100)
if show:
    plt.show()