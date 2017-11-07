import numpy as np
import pylab
import matplotlib.pyplot as plt
from scipy.optimize import leastsq  # Levenberg-Marquadt Algorithm #
from os import listdir
from os.path import isfile, join


def lorentzian(x, p):
    numerator = (p[0] ** 2)
    denominator = (x - (p[1])) ** 2 + p[0] ** 2
    y = p[2] * (numerator / denominator)
    return y


def residuals(p, y, x):
    err = y - lorentzian(x, p)
    return err


def fit_spec(filename, peak_hwhm, peak_center, peak_intensity, show=True):
    a = np.loadtxt(filename)
    x = a[:, 0]
    y = a[:, 1]

    # initial values #
    p = np.array([peak_hwhm, peak_center, peak_intensity])  # [hwhm, peak center, intensity] #

    # optimization #
    pbest = leastsq(residuals, p, args=(y, x), full_output=True)
    best_parameters = pbest[0]
    if show:
        # fit to data #
        fit = lorentzian(x, best_parameters)
        # print(best_parameters)
        # x_err_1 = np.array([0.075] * len(x))
        pylab.scatter(x, y, color='blue', marker='.', label='data')
        pylab.plot(x, fit, 'r-', color='orange', lw=2,
                   label='fit, peak at '+"{0:.2f}".format(abs(best_parameters[1])/1e9)+' (GHz)')
        # pylab.errorbar(x, y_bg_corr, xerr=x_err_1, linestyle='None', color='black')
        pylab.xlabel('Frequency(GHz)')
        pylab.ylabel('Intensity (a.u.)')
        pylab.legend()

        # pylab.savefig('./output_pics/' + s_name, format='png')
        pylab.show()
    return best_parameters

path_to_data_1 = './m_data/11072017_magnongradh/rf_sweeps_27102016/'


data_file_1 = 'extracted_diag_lines_0mA_20mT.txt'
data_file_2 = 'extracted_diag_lines_10mA_20mT.txt'
data_file_3 = 'extracted_diag_lines_20mA_20mT.txt'
data_file_4 = 'extracted_diag_lines_30mA_20mT.txt'
data_file_5 = 'extracted_diag_lines_40mA_20mT.txt'

data_file_6 = 'extracted_diag_lines_0mA_10mT.txt'
data_file_7 = 'extracted_diag_lines_10mA_10mT.txt'
data_file_8 = 'extracted_diag_lines_20mA_10mT.txt'
data_file_9 = 'extracted_diag_lines_30mA_10mT.txt'
data_file_10 = 'extracted_diag_lines_40mA_10mT.txt'


current_values = np.array([0, 10, 20, 30, 40])
peak_freq = []

freq_1 = fit_spec(path_to_data_1 + data_file_1, 1.5e9, 3.0e9, 5000, show=False)[1]/1e9
freq_2 = fit_spec(path_to_data_1 + data_file_2, 1.5e9, 3.5e9, 5000, show=False)[1]/1e9
freq_3 = fit_spec(path_to_data_1 + data_file_3, 1.5e9, 4.0e9, 5000, show=False)[1]/1e9
freq_4 = fit_spec(path_to_data_1 + data_file_4, 1.5e9, 4.2e9, 5000, show=False)[1]/1e9
freq_5 = fit_spec(path_to_data_1 + data_file_5, 1.5e9, 4.5e9, 5000, show=False)[1]/1e9

# freq_6 = fit_spec(path_to_data_1 + data_file_6, 1.5e9, 4.1e9, 100, show=True)[1]/1e9
# freq_7 = fit_spec(path_to_data_1 + data_file_7, 1.5e9, 4.5e9, 5000, show=True)[1]/1e9
# freq_8 = fit_spec(path_to_data_1 + data_file_8, 1.5e9, 4.0e9, 5000, show=True)[1]/1e9
# freq_9 = fit_spec(path_to_data_1 + data_file_9, 1.5e9, 3.0e9, 5000, show=True)[1]/1e9
# freq_10 = fit_spec(path_to_data_1 + data_file_10, 1.5e9, 3.2e9, 5000, show=True)[1]/1e9

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)

freqs_20mT = np.array([freq_1, freq_2, freq_3, freq_4, freq_5])
fit_line_20mT = np.polyfit(current_values, freqs_20mT, 1)
ax1.scatter(current_values, freqs_20mT, color='black', marker='x')
i_values = np.linspace(0, 40, 1000)
fit_freqs_20mT = i_values * fit_line_20mT[0] + fit_line_20mT[1]



# freqs_10mT = np.array([freq_6, freq_7, freq_8, freq_9, freq_10])
# fit_line_10mT = np.polyfit(current_values, freqs_10mT, 1)
# pylab.scatter(current_values, freqs_10mT, color='black', marker='o')
# i_values = np.linspace(0, 40, 1000)
# fit_freqs_10mT = i_values*fit_line_10mT[0] + fit_line_10mT[1]


ax1.plot(i_values, fit_freqs_20mT, 'r-',
         label=r'$\Delta f / \Delta I=$'+str("{0:.3f}".format(fit_line_20mT[0]*1e3))+' '+r'$(MHz/mA)$')
# pylab.plot(i_values, fit_freqs_10mT, 'r-')
ax1.set_xlabel('I (mA)', fontsize = 16)
ax1.set_ylabel(r'$f_{Res}$'+' '+r'$(GHz)$', fontsize = 16)
ax1.tick_params(axis='both', which='major', labelsize=15)
plt.legend(prop={'size': 16})
plt.tight_layout()
print(fit_line_20mT[0])
# print(fit_line_10mT[0])

plt.savefig('./output_pics/'+'f_made_by_I.png', format='png', dpi=100)

plt.show()