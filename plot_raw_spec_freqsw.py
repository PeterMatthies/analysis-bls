import numpy as np
import matplotlib.pyplot as plt
import re

path_to_data = './m_data/30052017_nrcl/'
data_file = 'm3_raw_pos1.dat'
# data_file = 'm3_raw_pos1_50mT.dat'

# loading the data
data_raw = np.loadtxt(path_to_data+data_file, comments='#')


# parsing the header
excitation_freq = 0
x_offset, x_multiplier = 0, 0
y_offset, y_multiplier = 0, 0
freq_min, freq_max = 0, 0
x_axis_name = ''
file_info = ''
position = 0
ext_field = -80
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
        if 'data file:' in line:
            file_info = line[12:]
            print(file_info)
        if 'MICROSCOPE - ScanDimension_1 - value:' in line:
            numbers = re.findall(r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", line)
            position = float(numbers[1])
            print(numbers)
        if 'linked controls - field - Control Voltage Kepco - value:' in line:
            numbers = re.findall(r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", line)
            ext_field = int(float(numbers[0]))
        # print(line)

# plotting the data
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)

if position == 1.0:
    pos = 'above'
else:
    pos = 'below'
# fig1.suptitle('BLS Spectrum '+pos+' antenna\n'+'at '+str(ext_field)+' mT ext. field')

cmap = plt.get_cmap('magma')
cmap.set_under('black')
# cmap.set_over('black')
eps1 = np.spacing(0)
im = ax1.imshow(data_raw.T, origin='lower', aspect='auto', vmin=eps1, vmax=100, cmap=cmap, interpolation='nearest')

print(data_raw.T.shape)

# adjusting the axes ticks

y_ticks = np.arange(0, data_raw.T.shape[0], 16)
print(len(y_ticks))

freq_tick_labels = np.linspace(freq_min, freq_max, len(y_ticks))
freq_tick_labels = ["{0:.1f}".format(y_tick) for y_tick in freq_tick_labels]
ax1.set_yticks(y_ticks)
ax1.set_yticklabels(freq_tick_labels)
ax1.tick_params(axis='both', which='major', labelsize=12)


x_ticks = np.arange(0, data_raw.T.shape[1], 6)

print(x_offset, x_multiplier)
print(x_offset, (data_raw.T.shape[1] - 1) * x_multiplier)
x_tick_labels = np.linspace(x_offset, (data_raw.T.shape[1] - 1) * x_multiplier + x_offset, len(x_ticks))
print(x_tick_labels)
x_tick_labels = ["{0:.1f}".format(x_tick/1000000000) for x_tick in x_tick_labels]
ax1.set_xticks(x_ticks)
ax1.set_xticklabels(x_tick_labels)


ax1.set_xlabel('Excitation Freq. (GHz)', fontsize=15)
# ax1.set_xlabel(x_axis_name)
ax1.set_ylabel('BLS Frequency (GHz)', fontsize=15)

cbar_ax = fig1.add_axes([0.92, 0.15, 0.02, 0.8])
cbar = fig1.colorbar(im, cax=cbar_ax)
cbar.set_label('Intensity', rotation=270, fontsize=12)
cbar.ax.get_yaxis().labelpad = 15
cbar.ax.set_yticklabels('')
cbar.ax.tick_params(axis='y', which='both', length=0)

fig1.tight_layout()
fig1.subplots_adjust(right=0.9, left=0.15, top=0.95)

file_info = file_info.split('\\')
print(file_info)
save_name = file_info[-1][:-5] + '_' + 'RAW' + '.pdf'
save_name = save_name.replace('both', pos)
print(save_name)
plt.savefig('./output_pics/nrcl/'+save_name, format='pdf', dpi=100)
plt.show()