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


def fit_spec(filename, freq_wind_1, freq_wind_2, peak_hwhm, peak_center, peak_intensity):
    a = np.loadtxt(filename)
    x = a[:, 0]
    y = a[:, 1]
    ind_stokes = (x > freq_wind_1) & (x < freq_wind_2)
    x = x[ind_stokes]
    y = y[ind_stokes]
    # pylab.scatter(x, y)
    # pylab.show()

    # defining the 'background' part of the spectrum #
    print(freq_wind_1+2.5)
    print(freq_wind_2-3.0)

    ind_bg_low = (x > freq_wind_1) & (x < freq_wind_1+2.5)
    ind_bg_high = (x > freq_wind_2-3.0) & (x < freq_wind_2)

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

    # fit to data #
    fit = lorentzian(x, best_parameters)
    print(best_parameters)
    # pylab.plot(x, y_bg_corr, 'go', label='data')
    # pylab.plot(x, fit, 'r-', lw=2, label='fit')
    # pylab.xlabel('Frequency(GHz)')
    # pylab.ylabel('Intensity (a.u.)')
    # pylab.legend()

    if filename[-10] == '_':
        # pylab.suptitle('incident light at ' + filename[-9:-7] + r'$^\circ$' + '\n50mT')
        s_name = filename[-9:-7] + 'angle.png'
    else:
        # pylab.suptitle('incident light at ' + filename[-10:-7] + r'$^\circ$' + '\n50mT')
        s_name = filename[-10:-7] + 'angle.png'
    # print(save_name)
    # pylab.savefig('./output_pics/' + s_name, format='png')
    # pylab.show()
    return best_parameters


path_to_data_1 = './m_data/02082017_dr_pyref/'
path_to_data_2 = './m_data/03082017_dr_pyref/'
data_files_1 = [f for f in listdir(path_to_data_1) if isfile(join(path_to_data_1, f))]
data_files_2 = [f for f in listdir(path_to_data_2) if isfile(join(path_to_data_2, f))]

incident_angles = []
peak_centers = []
for data_file in data_files_1:
    angle = float(data_file[-9:-7])
    print(angle)
    if angle == 70:
        incident_angles.append(angle)
        fitted_params = fitted_params = fit_spec(path_to_data_1 + data_file, -15.5, -3, 0.25, -12.0, 50)
        peak_centers.append(abs(fitted_params[1]))
    elif angle == 80:
        incident_angles.append(angle)
        fitted_params = fitted_params = fit_spec(path_to_data_1 + data_file, -15.5, -3, 0.25, -12.0, 50)
        peak_centers.append(abs(fitted_params[1]))
    elif angle == 20:
        incident_angles.append(angle)
        fitted_params = fitted_params = fit_spec(path_to_data_1 + data_file, -15.5, -3, 0.25, -9.0, 50)
        peak_centers.append(abs(fitted_params[1]))
    elif angle == 10:
        incident_angles.append(angle)
        fitted_params = fitted_params = fit_spec(path_to_data_1 + data_file, -15.5, -3, 0.25, -7.0, 50)
        peak_centers.append(abs(fitted_params[1]))
    else:
        incident_angles.append(angle)
        print(data_file)
        fitted_params = fit_spec(path_to_data_1 + data_file, -15.5, -3, 0.25, -10.0, 50)
        peak_centers.append(abs(fitted_params[1]))

incident_angles_2 = []
peak_centers_2 = []
for data_file in data_files_2:
    angle = float(data_file[-10:-7])
    print(angle)
    incident_angles_2.append(angle)
    print(data_file)
    fitted_params = fit_spec(path_to_data_2 + data_file, 3.0, 15.5, 0.25, 11.0, 50)
    peak_centers_2.append(abs(fitted_params[1]))

fig1 = plt.figure()
fig1.suptitle('Dispersion Relation for Py Reference Sample')
ax1 = fig1.add_subplot(111)

incident_angles = np.array(incident_angles)
incident_angles_2 = np.array(incident_angles_2)
incident_angles -= 3.0
incident_angles_2 -= 3.0
incident_angles_2 = abs(incident_angles_2)
print(incident_angles)
q_parallel = (4 * np.pi / 532e-9) * np.sin(incident_angles * np.pi / 180.0) / 100
q_parallel_2 = (4 * np.pi / 532e-9) * np.sin(incident_angles_2 * np.pi / 180.0) / 100
# pylab.scatter(incident_angles, peak_centers)
ax1.scatter(q_parallel, peak_centers, label='+k 50mT')
ax1.scatter(q_parallel_2, peak_centers_2, label='-k 50mT')
# ax1.scatter(incident_angles, peak_centers, label='50mT')

ax1.ticklabel_format(axis='x', style='sci', scilimits=(-3, 3), useOffset=False)
ax1.xaxis.major.formatter._useMathText = True
ax1.set_xlabel(r'$q_{||}(cm^{-1}$)', fontsize=14)
ax1.set_ylabel('Frequency(GHz)', fontsize=14)

fig1.tight_layout()
fig1.subplots_adjust(top=0.91, bottom=0.14)
plt.legend()
plt.grid()
save_name = 'PyRef_50mT_dispersion_curve.png'
plt.savefig('./output_pics/'+save_name, format='png', dpi=100)
plt.show()
