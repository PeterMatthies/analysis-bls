import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
from plot_cbls_spec import fit_spec, lorentzian


path_to_data_1 = './m_data/29082017_nrcl/'
data_file = 'm3_6mT.txt'
# data_file = 'plexiglass.txt'

fitted_params_1, x_1, y_bgcorr_1 = fit_spec(path_to_data_1+data_file, -8.0, -4.0, 1.0, -6.0, 500)
fitted_params_2, x_2, y_bgcorr_2 = fit_spec(path_to_data_1+data_file, 4.0, 8.0, 1.0, 6.0, 500)

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
x_err_1 = np.array([0.075]*len(x_1))
x_err_2 = np.array([0.075]*len(x_2))
fit_1 = lorentzian(abs(x_1), abs(fitted_params_1))
fit_2 = lorentzian(x_2, fitted_params_2)

ax1.scatter(abs(x_1), y_bgcorr_1, label='Stokes peak '+"{0:.2f}".format(abs(fitted_params_1[1]))+' (GHz)',
            marker='o', color='blue')
# ax1.scatter(abs(x_1), y_bgcorr_1, label='Stokes data',
#             marker='o', color='blue')
# ax1.scatter(x_2, y_bgcorr_2, label='Anti Stokes peak '+"{0:.2f}".format(abs(fitted_params_2[1]))+' (GHz)',
#             marker='x', color='orange')
ax1.scatter(x_2, y_bgcorr_2, label='Anti Stokes data',
            marker='x', color='orange')
ax1.errorbar(abs(x_1), y_bgcorr_1, xerr=x_err_1, linestyle="None", color='black')
ax1.errorbar(abs(x_2), y_bgcorr_2, xerr=x_err_2, linestyle="None", color='black')
# peak_1 =  AnchoredText('peak at'+"{0:.2f}".format(fitted_params_1[1]), loc=2)
# ax1.add_artist(peak_1)
ax1.plot(abs(x_1), fit_1, color='blue')
# ax1.plot(x_2, fit_2, color='orange')
ax1.set_xlabel('Frequency (GHz)', fontsize=16)
ax1.set_ylabel('Intensity (a.u.)', fontsize=16)
# save_name = 'plexiglass.pdf'
max_y = max(np.maximum(y_bgcorr_1, y_bgcorr_2))
ax1.set_xlim([min(x_2), max(x_2)])
ax1.set_ylim([-30, max_y + 0.12*max_y])
ax1.tick_params(axis='both', which='major', labelsize=14)


# plt.legend(loc=2)
plt.legend(loc=2, bbox_to_anchor=(0.0, 1.1), prop={'size': 15})
fig1.tight_layout()
fig1.subplots_adjust(top=0.93)
save_name = '6mT_ch2677_fitted.pdf'
plt.savefig('./output_pics/nrcl/'+save_name, format='pdf', dpi=100)
plt.show()