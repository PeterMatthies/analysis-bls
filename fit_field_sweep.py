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


def fit_spec(filename, freq_wind_1, freq_wind_2, peak_hwhm, peak_center, peak_intensity, show=True):
    a = np.loadtxt(filename)
    x = a[:, 0]
    y = a[:, 1]
    ind_peak = (x > freq_wind_1) & (x < freq_wind_2)
    x = x[ind_peak]
    y = y[ind_peak]
    # pylab.scatter(x, y)
    # pylab.show()

    # defining the 'background' part of the spectrum #
    # print(freq_wind_1+2.5)
    # print(freq_wind_2-3.0)

    ind_bg_low = (x > freq_wind_1) & (x < freq_wind_1+0.002)
    ind_bg_high = (x > freq_wind_2-0.002) & (x < freq_wind_2)

    x_bg = np.concatenate((x[ind_bg_low], x[ind_bg_high]))
    y_bg = np.concatenate((y[ind_bg_low], y[ind_bg_high]))
    # pylab.plot(x_bg, y_bg)
    # pylab.show()
    # fitting the background to a line #
    coefs = np.polyfit(x_bg, y_bg, 1)

    # removing fitted background #
    background = coefs[0] * x + coefs[1]
    y_bg_corr = y - background
    # pylab.plot(x,y_bg_corr)
    # pylab.show()

    # initial values #
    p = np.array([peak_hwhm, peak_center, peak_intensity])  # [hwhm, peak center, intensity] #

    # optimization #
    pbest = leastsq(residuals, p, args=(y_bg_corr, x), full_output=True)
    best_parameters = pbest[0]
    if show:
        # fit to data #
        fit = lorentzian(x, best_parameters)
        # print(best_parameters)
        # x_err_1 = np.array([0.075] * len(x))
        pylab.scatter(x, y_bg_corr, color='blue', marker='.', label='data')
        pylab.plot(x, fit, 'r-', color='orange', lw=2,
                   label='fit, peak at '+"{0:.5f}".format(abs(best_parameters[1])*1000)+' (mT)')
        # pylab.errorbar(x, y_bg_corr, xerr=x_err_1, linestyle='None', color='black')
        pylab.xlabel('Frequency(GHz)')
        pylab.ylabel('Intensity (a.u.)')
        pylab.legend()

        # pylab.savefig('./output_pics/' + s_name, format='png')
        pylab.show()
    return best_parameters, x, y_bg_corr

path_to_data_1 = './m_data/11072017_magnongradh/'


data_file_1 = 'M1_H-sweep_3p65GHz.txt'
data_file_2 = 'M2_H-sweep_3p65GHz_5mA.txt'
data_file_3 = 'M3_H-sweep_3p65GHz_minus5mA.txt'
data_file_4 = 'M4_H-sweep_3p65GHz_10mA.txt'
data_file_5 = 'M5_H-sweep_3p65GHz_minus10mA.txt'

fitted_params_1, x_1, y_bgcorr_1 = fit_spec(path_to_data_1 + data_file_1, 0.01, 0.04, 1.0, 0.022, 500, show=False)
fitted_params_2, x_2, y_bgcorr_2 = fit_spec(path_to_data_1 + data_file_2, 0.01, 0.04, 1.0, 0.022, 500, show=False)
fitted_params_3, x_3, y_bgcorr_3 = fit_spec(path_to_data_1 + data_file_3, 0.01, 0.04, 1.0, 0.022, 500, show=False)
fitted_params_4, x_4, y_bgcorr_4 = fit_spec(path_to_data_1 + data_file_4, 0.01, 0.04, 1.0, 0.022, 500, show=False)
fitted_params_5, x_5, y_bgcorr_5 = fit_spec(path_to_data_1 + data_file_5, 0.01, 0.04, 1.0, 0.022, 500, show=False)

h1 = fitted_params_1[1] * 1000
h2 = fitted_params_2[1] * 1000
h3 = fitted_params_3[1] * 1000
h4 = fitted_params_4[1] * 1000
h5 = fitted_params_5[1] * 1000

i_values = np.array([-10, -5, 0, 5, 10])
h_values = np.array([h5, h3, h1, h2, h4])

print(h_values)

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)

ax1.scatter(i_values, h_values)
ax1.set_xlabel('I (mA)', fontsize = 16)
ax1.set_ylabel(r'$H_{Res}$'+' '+r'$(mT)$', fontsize = 16)

coefs_line = np.polyfit(i_values, h_values, 1)
I_fit = np.linspace(np.min(i_values)-1, np.max(i_values)+1, 1000)
H_oersted = I_fit*coefs_line[0] + coefs_line[1]
ax1.plot(I_fit, H_oersted, 'r-',
           label=r'$\Delta H / \Delta I=$'+str("{0:.3f}".format(coefs_line[0]))+' '+r'$(mT/mA)$')
ax1.tick_params(axis='both', which='major', labelsize=15)
plt.legend(prop={'size': 16})
plt.tight_layout()
print(coefs_line)

plt.savefig('./output_pics/'+'H_made_by_I.png', format='png', dpi=100)

plt.show()