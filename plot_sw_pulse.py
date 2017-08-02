import numpy as np
import matplotlib.pyplot as plt

# wrf = with rf excitation, nrf = without rf excitation, tr = time resolved spectrum, sp - bls spectrum

infile_0um_tr = './m_data/15122016/m17_tr.txt'
infile_1um_tr = './m_data/15122016/m11_tr.txt'
infile_2um_tr = './m_data/15122016/m12_tr.txt'
infile_3um_tr = './m_data/15122016/m5_tr.txt'
infile_5um_tr = './m_data/15122016/m10_tr.txt'

infile_0um_sp = './m_data/15122016/m17_spec.txt'
infile_1um_sp = './m_data/15122016/m11_spec.txt'
infile_2um_sp = './m_data/15122016/m12_spec.txt'
infile_3um_sp = './m_data/15122016/m5_spec.txt'
infile_5um_sp = './m_data/15122016/m10_spec.txt'

data_0um_tr = np.loadtxt(infile_0um_tr, comments='#')
data_0um_spec = np.loadtxt(infile_0um_sp, comments='#')
freq_0um = data_0um_spec[:, 0]

data_1um_tr = np.loadtxt(infile_1um_tr, comments='#')
data_1um_spec = np.loadtxt(infile_1um_sp, comments='#')
freq_1um = data_1um_spec[:, 0]

data_2um_tr = np.loadtxt(infile_2um_tr, comments='#')
data_2um_spec = np.loadtxt(infile_2um_sp, comments='#')
freq_2um = data_2um_spec[:, 0]

data_3um_tr = np.loadtxt(infile_3um_tr, comments='#')
data_3um_spec = np.loadtxt(infile_3um_sp, comments='#')
freq_3um = data_3um_spec[:, 0]

data_5um_tr = np.loadtxt(infile_5um_tr, comments='#')
data_5um_spec = np.loadtxt(infile_5um_sp, comments='#')
freq_5um = data_5um_spec[:, 0]



time_vals = np.arange(0, 513, 1) * 0.1

fig1 = plt.figure(figsize=(12, 4),dpi=100, tight_layout=True)
# title_name =  'time resolved measurement'
#fig1.suptitle(title_name, fontweight='bold', fontsize=12)
cmap = plt.get_cmap('jet')
cmap.set_under('black')
eps1 = np.spacing(0)

scale_factor = 11

ax1 = fig1.add_subplot(151)
im1 = ax1.imshow(data_0um_tr.T, origin='lower', aspect='auto', vmin=eps1, vmax=200, cmap=cmap,
                 extent=(min(freq_0um), max(freq_0um), min(time_vals), max(time_vals)))
ax1.set_xlim(-6, -2.5)
ax1.set_ylabel('Time (ns)')
ax1.set_xlabel('Frequency (GHz)')
ax1.set_title(r'$0\mu m$')

ax2 = fig1.add_subplot(152)
im2 = ax2.imshow(data_1um_tr.T, origin='lower', aspect='auto', vmin=eps1, vmax=300, cmap=cmap,
                 extent=(min(freq_1um), max(freq_1um), min(time_vals), max(time_vals)))
ax2.set_xlim(-6, -2.5)
ax2.set_xlabel('Frequency (GHz)')
ax2.set_title(r'$1\mu m$')

ax3 = fig1.add_subplot(153)
im3 = ax3.imshow(data_2um_tr.T, origin='lower', aspect='auto', vmin=eps1, vmax=300, cmap=cmap,
                 extent=(min(freq_2um), max(freq_2um), min(time_vals), max(time_vals)))
ax3.set_xlim(-6, -2.5)
ax3.set_xlabel('Frequency (GHz)')
ax3.set_title(r'$2\mu m$')


ax4 = fig1.add_subplot(154)
im4 = ax4.imshow(data_3um_tr.T, origin='lower', aspect='auto', vmin=eps1, vmax=300, cmap=cmap,
                 extent=(min(freq_3um), max(freq_3um), min(time_vals), max(time_vals)))
ax4.set_xlim(-6, -2.5)
ax4.set_xlabel('Frequency (GHz)')
ax4.set_title(r'$3\mu m$')

ax5 = fig1.add_subplot(155)
im5 = ax5.imshow(data_5um_tr.T, origin='lower', aspect='auto', vmin=eps1, vmax=300, cmap=cmap,
                 extent=(min(freq_5um), max(freq_5um), min(time_vals), max(time_vals)))
ax5.set_xlim(-6, -2.5)
ax5.set_xlabel('Frequency (GHz)')
ax5.set_title(r'$5\mu m$')

for ax in fig1.axes:
    plt.sca(ax)
    plt.xticks(rotation=90)

cbar = fig1.co
cbar.set_label('Intensity (a.u.)', rotation=270)
cbar.ax.get_yaxis().labelpad = 15
# plt.xticks(rotation=70)



plt.show()