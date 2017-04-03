import extract_data as ed
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares


def decaying_func(parameters, x_input):
    print(parameters)
    return parameters[0] * np.exp(-parameters[1] * x_input + parameters[2]) * \
                   np.power(np.cos(parameters[3] * x_input + parameters[4]), 2) + parameters[5]


def error_func(parameters, x_input, y_data):
    return decaying_func(parameters, x_input) - y_data

# plot a combined graph for 3 phase resolved measurements with fitting for each of the graphs

path_to_file_1 = './m_data/25-10-2016/m3_spec_integrated_7to5p5GHz_00mA.txt'
path_to_file_2 = './m_data/25-10-2016/m5_spec_integrated_7to5p5GHz_20mA.txt'
path_to_file_3 = './m_data/26-10-2016/m4_spec_integrated_7to5p5GHz_40mA.txt'

# loading data from file 1
m_name_1 = path_to_file_1.split('/')[-1][:-4]
m_date_1 = path_to_file_1.split('/')[-2]
m_data_1 = ed.extract_data_file(path_to_file_1, m_name_1, m_date_1, m_type='Phase resolved line scan')

# loading data from file 2
m_name_2 = path_to_file_2.split('/')[-1][:-4]
m_date_2 = path_to_file_2.split('/')[-2]
m_data_2 = ed.extract_data_file(path_to_file_2, m_name_2, m_date_2, m_type='Phase resolved line scan')

# loading data for file 3
m_name_3 = path_to_file_3.split('/')[-1][:-4]
m_date_3 = path_to_file_3.split('/')[-2]
m_data_3 = ed.extract_data_file(path_to_file_3, m_name_3, m_date_3, m_type='Phase resolved line scan')

# normalizing the data:
# m_data_1.data.T[1] /= max(m_data_1.data.T[1])
# m_data_2.data.T[1] /= max(m_data_2.data.T[1])
# m_data_3.data.T[1] /= max(m_data_3.data.T[1])

# defining the x axis
x_real_space = np.linspace(0, 22.3, 100)

# start plotting
fig_phr = plt.figure(figsize=(8, 7), dpi=100)
title_name = 'Phase resolved line scan along Py stripe\n 6GHz, 30mT'
fig_phr.suptitle(title_name, fontweight='bold', fontsize=12)

# plotting curve 1
ax1 = fig_phr.add_subplot(313)
ax1.scatter(x_real_space, m_data_1.data.T[1], color='black', marker='.', label=m_data_1.mes_name[-4:])

# plotting fit 1
fit_params_1 = np.array([1.28697228e+03, 1.53982330e-01, 1.67576877e+00, 1.11037877e+00, 4.50999392e+00,
                         1.46674641e+03])
wave_number = fit_params_1[3]
wave_length = np.pi / wave_number
print(wave_length)
x_coord_1 = np.linspace(x_real_space[3], x_real_space[91], 1000)
data_fit_1 = decaying_func(fit_params_1, x_coord_1)
print(data_fit_1)
ax1.plot(x_coord_1, data_fit_1, color='blue', label='fit ' + r'$\lambda$' + '=' +
                                                      "{0:.2f}".format(wave_length) + r'$\mu m$')


# plotting curve 2
ax2 = fig_phr.add_subplot(312)
ax2.scatter(x_real_space, m_data_2.data.T[1], color='black', marker='x', label=m_data_2.mes_name[-4:])

# plotting fit 2
fit_params_2_before = np.array([5.38533554e+03, 2.09031869e-01, 1.59725107e+00, 9.89025845e-01, 1.22621132e+00,
                                2.01963278e+03])
wave_number_before_2 = fit_params_2_before[3]
wave_length_before_2 = np.pi/wave_number_before_2
x_coord_2 = np.linspace(x_real_space[3], x_real_space[29], 500)
data_fit_2_b = decaying_func(fit_params_2_before, x_coord_2)
ax2.plot(x_coord_2, data_fit_2_b, color='blue', label='fit ' + r'$\lambda$' + '=' +
                                                      "{0:.2f}".format(wave_length_before_2) + r'$\mu m$')

fit_params_2_after = np.array([8.66850569e+03, 1.20289364e-01, 5.53267113e-01, 1.06275741e+00, 4.01126588e+00,
                               1.87251179e+03])
wave_number_after_2 = fit_params_2_after[3]
wave_length_after_2 = np.pi/wave_number_after_2
x_coord_2 = np.linspace(x_real_space[31], x_real_space[95], 1000)
data_fit_2_a =decaying_func(fit_params_2_after, x_coord_2)
ax2.plot(x_coord_2, data_fit_2_a, color='green', label='fit ' + r'$\lambda$' + '=' +
                                                      "{0:.2f}".format(wave_length_after_2) + r'$\mu m$')

# plotting curve 3
ax3 = fig_phr.add_subplot(311)
ax3.scatter(x_real_space, m_data_3.data.T[1], color='black', marker='p', label=m_data_3.mes_name[-4:])


# plotting fit 3
fit_params_3_before = np.array([3.28044160e+04, 1.50068847e-01, -7.30652923e-01, 7.61198015e-01, 7.35453628e+00,
                                2.01802320e+03])
wave_number_before_3 = fit_params_3_before[3]
wave_length_before_3 = np.pi/wave_number_before_3
x_coord_3 = np.linspace(x_real_space[7], x_real_space[29], 500)
data_fit_3_b = decaying_func(fit_params_3_before, x_coord_3)
ax3.plot(x_coord_3, data_fit_3_b, color='blue', label='fit ' + r'$\lambda$' + '=' +
                                                      "{0:.2f}".format(wave_length_before_3) + r'$\mu m$')

fit_params_3_after = np.array([6.62049522e+03, 8.48238614e-02, 2.50222961e-01, 1.02604472e+00, 5.88648264e+00,
                               1.13990328e+03])
wave_number_after_3 = fit_params_3_after[3]
wave_length_after_3 = np.pi/wave_number_after_3
x_coord_3 = np.linspace(x_real_space[31], x_real_space[95], 1000)
data_fit_3_a =decaying_func(fit_params_3_after, x_coord_2)
ax3.plot(x_coord_3, data_fit_3_a, color='green', label='fit ' + r'$\lambda$' + '=' +
                                                      "{0:.2f}".format(wave_length_after_3) + r'$\mu m$')


# plotting the position of the step in the DC line
y_line = np.linspace(0, 1.1*max(m_data_3.data.T[1]), 100000)
x_line = np.array([x_real_space[30] for i in range(len(y_line))])
ax1.plot(x_line, y_line, linestyle='--', color='red', label='DC-line\nstep pos (6.7' + r'$\mu m$' + ')')
ax2.plot(x_line, y_line, linestyle='--', color='red', label='DC-line\nstep pos (6.7' + r'$\mu m$' + ')')
ax3.plot(x_line, y_line, linestyle='--', color='red', label='DC-line\nstep pos (6.7' + r'$\mu m$' + ')')


# making the plot beautiful - axes labels, ticks, limits etc. for all of the subplots
new_xticks = np.linspace(0, 22.3, 12)
new_xticks = [int(xtick) for xtick in new_xticks]

ax1.grid()
ax1.set_xticks(new_xticks)
ax1.set_xlim([0, 21])
ax1.set_ylim([0, 1.1*max(m_data_1.data.T[1])])
ax1.set_xlabel('Position along Py stripe' + r' ($\mu m$)')
ax1.set_ylabel('Intensity (a.u.)')
ax1.ticklabel_format(axis='y', style='sci', scilimits=(-3, 3), useOffset=False)
ax1.yaxis.major.formatter._useMathText = True
ax1.legend(prop={'size': 9}, loc=1)

ax2.grid()
ax2.set_xticks(new_xticks)
ax2.set_xlim([0, 21])
ax2.set_ylim([0, 1.1*max(m_data_3.data.T[1])])
# ax2.set_xlabel('Position along Py stripe' + r' ($\mu m$)')
ax2.set_ylabel('Intensity (a.u.)')
ax2.ticklabel_format(axis='y', style='sci', scilimits=(-3, 3), useOffset=False)
ax2.yaxis.major.formatter._useMathText = True
ax2.legend(prop={'size': 9}, loc=1)

ax3.grid()
ax3.set_xticks(new_xticks)
ax3.set_xlim([0, 21])
ax3.set_ylim([0, 1.1*max(m_data_3.data.T[1])])
# ax2.set_xlabel('Position along Py stripe' + r' ($\mu m$)')
ax3.set_ylabel('Intensity (a.u.)')
ax3.ticklabel_format(axis='y', style='sci', scilimits=(-3, 3), useOffset=False)
ax3.yaxis.major.formatter._useMathText = True
ax3.legend(prop={'size': 9}, loc=1)

fig_phr.tight_layout()
fig_phr.subplots_adjust(top=0.91)
# fig_phr.legend()

plt.savefig('./output_pics/phase_res_combined_6GHz_30mT_0_20_40mA.png', format='png', dpi=100)

plt.show()