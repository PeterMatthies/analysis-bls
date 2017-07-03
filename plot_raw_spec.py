import numpy as np
import matplotlib.pyplot as plt
import re

path_to_data = './m_data/01062017_nrcl/'
data_file = 'm1_raw_pos1.dat'

# loading the data
data_raw = np.loadtxt(path_to_data+data_file, comments='#')

# parsing the header
excitation_freq = 0
x_offset, x_multiplier = 0, 0
y_offset, y_multiplier = 0, 0
freq_min, freq_max = 0, 0
x_axis_name = ''
with open(path_to_data+data_file, 'r') as f:
    for line in f:
        if not line.startswith('#'):
             break
        if 'Agilent_E8257D - FREQUENCY (Hz) - value:' in line:
            excitation_freq = float(re.findall(r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", line)[1])
            excitation_freq /= 1000000000
            print(excitation_freq)
        if 'x offset/multiplier:' in line:
            numbers = re.findall(r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", line)
            # print(numbers)
            x_offset = float(numbers[0])
            x_multiplier = float(numbers[1])
        if 'y offset/multiplier:' in line:
            numbers = re.findall(r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", line)
            # print(numbers)
            y_offset = float(numbers[0])
            y_multiplier = float(numbers[1])
        if 'Frequency between:' in line:
            numbers = re.findall(r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", line)
            # print(numbers)
            freq_min = float(numbers[0])
            freq_max = float(numbers[1])
        if 'x axis:' in line:
            x_axis_name = line[9:]
            print(x_axis_name)
        # print(line)

# plotting the data
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)

# freq_points = (freq_max - freq_min) / y_multiplier
# print(freq_points)

fig1.suptitle('BLS Spectrum for excitation at '+str(excitation_freq)+' GHz')

cmap = plt.get_cmap('jet')
cmap.set_under('black')
# cmap.set_over('black')
eps1 = np.spacing(0)
im = ax1.imshow(data_raw.T, origin='lower', aspect='auto', vmin=eps1, vmax=70, cmap=cmap)

print(data_raw.T.shape)

# adjusting the axes ticks


y_ticks = np.arange(0, data_raw.T.shape[0], 16)
print(len(y_ticks))

freq_tick_labels = np.linspace(freq_min, freq_max, len(y_ticks))
freq_tick_labels = ["{0:.1f}".format(y_tick) for y_tick in freq_tick_labels]
ax1.set_yticks(y_ticks)
ax1.set_yticklabels(freq_tick_labels)


x_ticks = np.arange(0, data_raw.T.shape[1], 6)
x_tick_labels = np.linspace (x_offset, (data_raw.T.shape[1] - 1) * x_multiplier - abs(x_offset), len(x_ticks))
x_tick_labels = ["{0:.2f}".format(x_tick) for x_tick in x_tick_labels]
ax1.set_xticks(x_ticks)
ax1.set_xticklabels(x_tick_labels)

ax1.set_xlabel(x_axis_name)
ax1.set_ylabel('Frequency (GHz)')

cbar = fig1.colorbar(im)
cbar.set_label('Intensity (a.u.)', rotation=270)
cbar.ax.get_yaxis().labelpad = 15
# cbar.ax.set_yticklabels('')
# save_name = m_date + '_' + m_name + '_' + m_type + '.png'
# plt.savefig(save_name, format='png', dpi=100)
fig1.tight_layout()
fig1.subplots_adjust(top=0.93, bottom=0.11)
plt.show()