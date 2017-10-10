import numpy as np
import matplotlib.pyplot as plt
import re

path_to_data = './m_data/02062017_nrcl/raw/'
data_file_2 = 'm7_3GHz_closer.dat'
data_file_1 = 'm7_3GHz_further.dat'

# loading the data
data_raw_1 = np.loadtxt(path_to_data + data_file_1, comments='#')
data_raw_2 = np.loadtxt(path_to_data + data_file_2, comments='#')


# parsing the header
excitation_freq_1 = 0
x_offset_1, x_multiplier_1 = 0, 0
y_offset_1, y_multiplier_1 = 0, 0
freq_min_1, freq_max_1 = 0, 0
x_axis_name_1 = ''
file_info_1 = ''
position_1 = 0
ext_field_1 = -80

with open(path_to_data+data_file_1, 'r') as f:
    for line in f:
        if not line.startswith('#'):
            break
        if 'Agilent_E8257D - FREQUENCY (Hz) - value:' in line:
            excitation_freq_1 = float(re.findall(r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", line)[1])
            excitation_freq_1 /= 1000000000
            print(excitation_freq_1)
        if 'x offset/multiplier:' in line:
            numbers = re.findall(r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", line)
            # print(numbers)
            x_offset_1 = float(numbers[0])
            x_multiplier_1 = float(numbers[1])
        if 'y offset/multiplier:' in line:
            numbers = re.findall(r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", line)
            # print(numbers)
            y_offset_1 = float(numbers[0])
            y_multiplier_1 = float(numbers[1])
        if 'Frequency between:' in line:
            numbers = re.findall(r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", line)
            # print(numbers)
            freq_min_1 = float(numbers[0])
            freq_max_1 = float(numbers[1])
        if 'x axis:' in line:
            x_axis_name_1 = line[9:]
            print(x_axis_name_1)
        if 'data file:' in line:
            file_info_1 = line[12:]
            print(file_info_1)
        if 'MICROSCOPE - ScanDimension_1 - value:' in line:
            numbers = re.findall(r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", line)
            position_1 = float(numbers[1])
            print(numbers)
        if 'linked controls - field - Control Voltage Kepco - value:' in line:
            numbers = re.findall(r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", line)
            ext_field_1 = int(float(numbers[0]))
        # print(line)


excitation_freq_2 = 0
x_offset_2, x_multiplier_2 = 0, 0
y_offset_2, y_multiplier_2 = 0, 0
freq_min_2, freq_max_2 = 0, 0
x_axis_name_2 = ''
file_info_2 = ''
position_2 = 0
ext_field_2 = -80

with open(path_to_data+data_file_2, 'r') as f:
    for line in f:
        if not line.startswith('#'):
            break
        if 'Agilent_E8257D - FREQUENCY (Hz) - value:' in line:
            excitation_freq_2 = float(re.findall(r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", line)[1])
            excitation_freq_2 /= 1000000000
            print(excitation_freq_1)
        if 'x offset/multiplier:' in line:
            numbers = re.findall(r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", line)
            # print(numbers)
            x_offset_2 = float(numbers[0])
            x_multiplier_2 = float(numbers[1])
        if 'y offset/multiplier:' in line:
            numbers = re.findall(r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", line)
            # print(numbers)
            y_offset_2 = float(numbers[0])
            y_multiplier_2 = float(numbers[1])
        if 'Frequency between:' in line:
            numbers = re.findall(r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", line)
            # print(numbers)
            freq_min_2 = float(numbers[0])
            freq_max_2 = float(numbers[1])
        if 'x axis:' in line:
            x_axis_name_2 = line[9:]
            print(x_axis_name_2)
        if 'data file:' in line:
            file_info_2 = line[12:]
            print(file_info_2)
        if 'MICROSCOPE - ScanDimension_1 - value:' in line:
            numbers = re.findall(r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", line)
            position_2 = float(numbers[1])
            print(numbers)
        if 'linked controls - field - Control Voltage Kepco - value:' in line:
            numbers = re.findall(r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", line)
            ext_field_2 = int(float(numbers[0]))
        # print(line)

# plotting the data
fig1 = plt.figure(figsize=(12, 4), dpi=100)

ax1 = fig1.add_subplot(211)
ax2 = fig1.add_subplot(212)

pos_f_1 = ''
if position_1 == 2.0:
    pos_1 = 'close'
    pos_f_1 = 'close'
else:
    pos_1 = '1' + r'$\mu m$' + ' from'
    pos_f_1 = '1um_from'

pos_f_2 = ''
if position_2 == 2.0:
    pos_2 = 'close'
    pos_f_2 = 'close'
else:
    pos_2 = '1' + r'$\mu m$' + ' from'
    pos_f_2 = '1um_from'

# fig1.suptitle('BLS Spectrum '+pos+' antenna\n'+'excitation at '+str(excitation_freq)+' GHz')

cmap = plt.get_cmap('magma')
cmap.set_under('black')
# cmap.set_over('black')
eps1 = np.spacing(0)
im1 = ax1.imshow(data_raw_1.T, origin='lower', aspect='auto', vmin=eps1, vmax=400, cmap=cmap, interpolation='nearest',
                 extent=(0, 100, freq_min_1, freq_max_1))

im2 = ax2.imshow(data_raw_2.T, origin='lower', aspect='auto', vmin=eps1, vmax=400, cmap=cmap, interpolation='nearest',
                 extent=(0, 100, freq_min_2, freq_max_2))

print(data_raw_1.T.shape)

# plotting the line showing the middle position of the antenna
x_line1 = np.array([51 for i in range(10000)])
y_line1 = np.linspace(-excitation_freq_1 - 1, -excitation_freq_1 + 1, 10000)
ax1.plot(x_line1, y_line1, linestyle='--', linewidth=4.0, color='green', alpha=0.6, label='middle of antenna')

x_line1 = np.array([51 for i in range(10000)])
y_line1 = np.linspace(-excitation_freq_2 - 1, -excitation_freq_2 + 1, 10000)
ax2.plot(x_line1, y_line1, linestyle='--', linewidth=4.0, color='green', alpha=0.6)


# adjusting the axes ticks

ax1.set_ylim([-excitation_freq_1 - 1, -excitation_freq_1 + 1])
ax1.set_xlim([0, 99])
x_ticks = np.arange(0, data_raw_1.T.shape[1], 11)
x_tick_labels = np.linspace(0, 16.5, 10)
print(x_tick_labels)
x_tick_labels = ["{0:.1f}".format(x_tick) for x_tick in x_tick_labels]
ax1.set_xticks(x_ticks)
ax1.set_xticklabels(x_tick_labels)


ax2.set_ylim([-excitation_freq_2 - 1, -excitation_freq_2 + 1])
ax2.set_xlim([0, 99])
x_ticks = np.arange(0, data_raw_2.T.shape[1], 11)
x_tick_labels = np.linspace(0, 16.5, 10)
print(x_tick_labels)
x_tick_labels = ["{0:.1f}".format(x_tick) for x_tick in x_tick_labels]
ax2.set_xticks(x_ticks)
ax2.set_xticklabels(x_tick_labels)

# ax1.set_ylabel('BLS Frequency (GHz)', fontsize=10)
# ax2.set_ylabel('BLS Frequency (GHz)', fontsize=15)
fig1.text(0.01, 0.55, 'BLS Frequency (GHz)', va='center',rotation='vertical', fontsize=15)
ax2.set_xlabel('position' + r'$\parallel$' + ' to antenna '+r'$(\mu m)$', fontsize=12)
ax1.tick_params(axis='both', which='major', labelsize=12)
ax2.tick_params(axis='both', which='major', labelsize=12)
# ax1.set_xticklabels('')

cbar_ax = fig1.add_axes([0.95, 0.15, 0.01, 0.8])
cbar = fig1.colorbar(im1, cax= cbar_ax)
cbar.set_label('Intensity', rotation=270, fontsize=12)
cbar.ax.get_yaxis().labelpad = 15
cbar.ax.set_yticklabels('')
cbar.ax.tick_params(axis='y', which='both', length=0)
ax1.annotate('', xy=(1.102, 0.5), xycoords='axes fraction', xytext=(1.1, -1.0),
                 arrowprops=dict(arrowstyle='->', color='black'))
fig1.text(0.902, 0.55, 'position '+r'$\perp$'+' to antenna', va='center',rotation='vertical', fontsize=15)
fig1.text(0.86, 0.8, '1'+r'$\mu m$', va='center',rotation='horizontal', fontsize=15)
fig1.text(0.86, 0.3, '0'+r'$\mu m$', va='center',rotation='horizontal', fontsize=15)

ax1.legend(loc=1, bbox_to_anchor=(1.0, 1.05))
fig1.tight_layout()
fig1.subplots_adjust(right=0.85, left=0.06)
# fig1.subplots_adjust(top=0.94, bottom=0.15)


file_info_1 = file_info_1.split('\\')
print(file_info_1)
save_name = file_info_1[-1][:-5] + '_' + str(excitation_freq_1)[0] + 'GHz_' + pos_f_1 + pos_f_2 + '_RAW_v4' + '.pdf'

print(save_name)
plt.savefig('./output_pics/nrcl/'+save_name, format='pdf', dpi=100)
plt.show()