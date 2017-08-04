import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
from plot_cbls_spec import fit_spec, lorentzian


path_to_data_1 = './m_data/02082017_cbls_tests/'
data_file = 'plexiglass.txt'

fitted_params_1, x_1, y_bgcorr_1 = fit_spec(path_to_data_1+data_file, -22.0, -5.0, 1.0, -15.0, 8000)
fitted_params_2, x_2, y_bgcorr_2 = fit_spec(path_to_data_1+data_file, 5.0, 22.0, 1.0, 15.0, 8000)

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
x_err_1 = np.array([0.075]*len(x_1))
x_err_2 = np.array([0.075]*len(x_2))
fit_1 = lorentzian(abs(x_1), abs(fitted_params_1))
fit_2 = lorentzian(x_2, fitted_params_2)

ax1.scatter(abs(x_1), y_bgcorr_1, label='Stokes peak '+"{0:.2f}".format(abs(fitted_params_1[1]))+' (GHz)',
            marker='.', color='blue')
ax1.scatter(x_2, y_bgcorr_2, label='Anti Stokes peak '+"{0:.2f}".format(abs(fitted_params_2[1]))+' (GHz)',
            marker='.', color='orange')
ax1.errorbar(abs(x_1), y_bgcorr_1, xerr=x_err_1, linestyle="None", color='black')
ax1.errorbar(abs(x_2), y_bgcorr_2, xerr=x_err_2, linestyle="None", color='black')
# peak_1 =  AnchoredText('peak at'+"{0:.2f}".format(fitted_params_1[1]), loc=2)
# ax1.add_artist(peak_1)
ax1.plot(abs(x_1), fit_1, color='blue')
ax1.plot(x_2, fit_2, color='orange')
ax1.set_xlabel('Frequency (GHz)')
ax1.set_ylabel('Intensity (a.u.)')
save_name = 'plexiglass.png'

plt.legend()
plt.savefig('./output_pics/'+save_name, format='png', dpi=100)
plt.show()