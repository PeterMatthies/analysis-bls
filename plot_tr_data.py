import numpy as np
import matplotlib.pyplot as plt

# wrf = with rf excitation, nrf = without rf excitation, tr = time resolved spectrum, sp - bls spectrum

infile_wrf_tr = './m_data/15mT/3p65GHz_rf_excited_tr.txt'
infile_nrf_tr = './m_data/15mT/3p65GHz_thermal_tr.txt'
infile_wrf_sp = './m_data/15mT/3p65GHz_rf_excited_spectrum.txt'
infile_nrf_sp = './m_data/15mT/3p65GHz_thermal_spectrum.txt'


data_wrf_tr = np.loadtxt(infile_wrf_tr, comments='#')
data_nrf_tr = np.loadtxt(infile_nrf_tr, comments='#')
data_wrf_sp = np.loadtxt(infile_wrf_sp, comments='#')
data_nrf_sp = np.loadtxt(infile_nrf_sp, comments='#')

freq_wrf = data_wrf_sp[:, 0]
freq_nrf = data_nrf_sp[:, 0]
time_vals = np.arange(0, 513, 1) * 0.1

fig1 = plt.figure(figsize=(8, 9), dpi=100, tight_layout=True)
# title_name =  'time resolved measurement'
#fig1.suptitle(title_name, fontweight='bold', fontsize=12)
cmap = plt.get_cmap('jet')
cmap.set_under('black')
# cmap.set_over('black')
eps1 = np.spacing(0)

scale_factor = 11
ax1 = fig1.add_subplot(311)
im1 = ax1.imshow(data_wrf_tr.T, origin='lower', aspect='auto', vmin=eps1, vmax=100, cmap=cmap,
                 extent=(min(freq_wrf), max(freq_wrf), min(time_vals), max(time_vals)))
ax1.set_ylabel('Time (ns)')

ax2 = fig1.add_subplot(312)
im2 = ax2.imshow(data_nrf_tr.T, origin='lower', aspect='auto', vmin=eps1, vmax=100*scale_factor, cmap=cmap,
                 extent=(min(freq_nrf), max(freq_nrf), min(time_vals), max(time_vals)))
ax2.set_ylabel('Time (ns)')


data_sub = scale_factor*data_wrf_tr - data_nrf_tr
ax3 = fig1.add_subplot(313)
im3 = ax3.imshow(data_sub.T, origin='lower', aspect='auto', vmin=eps1, vmax=1100, cmap=cmap,
                 extent=(min(freq_wrf), max(freq_wrf), min(time_vals), max(time_vals)))
ax3.set_ylabel('Time (ns)')
ax3.set_xlabel('Frequency (GHz)')


plt.show()