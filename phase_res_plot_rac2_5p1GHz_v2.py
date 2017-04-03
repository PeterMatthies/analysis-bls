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

path_to_file_1 = './m_data/24_10_2016/m2_he_00mA.txt'
path_to_file_2 = './m_data/24_10_2016/m3_he_10mA.txt'
path_to_file_3 = './m_data/24_10_2016/m3_he_20mA.txt'

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


# start plotting
fig_phr = plt.figure(figsize=(8, 9), dpi=100)
title_name = 'Phase resolved line scan along Py stripe\n 5.1GHz, 30mT'
fig_phr.suptitle(title_name, fontweight='bold', fontsize=12)

# plotting curve 1

# defining the x axis
x_real_space = np.linspace(0, 22.3, 100)
ax1 = fig_phr.add_subplot(313)
ax1.scatter(x_real_space, m_data_1.data.T[1], color='black', marker='.', label=m_data_1.mes_name[-4:])

# plotting fit 1
fit_params_1 = np.array([8.21188443e+03, 1.52146694e-01, 1.13579389e+00, 7.04091717e-01,
                         5.98642226e+00, 4.32826076e+03])
wave_number = fit_params_1[3]
wave_length = np.pi / wave_number
print(wave_length)
x_coord_1 = np.linspace(x_real_space[3], x_real_space[91], 1000)
data_fit_1 = decaying_func(fit_params_1, x_coord_1)
print(data_fit_1)
ax1.plot(x_coord_1, data_fit_1, color='blue', label='fit ' + r'$\lambda$' + '=' +
                                                      "{0:.2f}".format(wave_length) + r'$\mu m$')


# plotting curve 2
# defining the x axis
x_real_space = np.linspace(0, 22.3, 101)
ax2 = fig_phr.add_subplot(312)
ax2.scatter(x_real_space, m_data_2.data.T[1], color='black', marker='x', label=m_data_2.mes_name[-4:])

# plotting fit 2
# before the variable width section
fit_params_2_before = np.array([3.38942773e+04, 1.21251217e-01, 1.34864739e+00, 5.87155053e-01,
                                3.00544331e+00, 8.67836095e+03])
wave_number_before_2 = fit_params_2_before[3]
wave_length_before_2 = np.pi/wave_number_before_2
x_coord_2 = np.linspace(x_real_space[3], x_real_space[29], 500)
data_fit_2_b = decaying_func(fit_params_2_before, x_coord_2)
ax2.plot(x_coord_2, data_fit_2_b, color='blue', label='fit ' + r'$\lambda$' + '=' +
                                                      "{0:.2f}".format(wave_length_before_2) + r'$\mu m$')
# in the variable width section
fit_params_2_variable = np.array([3.44809748e+04, 2.06990788e-01, 2.26241185e+00, 6.04854792e-01,
                                  3.06614836e+00, 1.04238957e+04])
wave_number_variable_2 = fit_params_2_variable[3]
wave_length_variable_2 = np.pi / wave_number_variable_2
x_coord_2 = np.linspace(x_real_space[31], x_real_space[52], 1000)
data_fit_2_v = decaying_func(fit_params_2_variable, x_coord_2)
ax2.plot(x_coord_2, data_fit_2_v, color='green', label='fit ' + r'$\lambda$' + '=' +
                                                      "{0:.2f}".format(wave_length_variable_2) + r'$\mu m$')

# after the variable width section
fit_params_2_after = np.array([5.17196812e+04, 1.24771357e-01, 9.29846429e-01, 6.97055802e-01,
                               2.14802514e+00, 1.45071462e+04])
wave_number_after_2 = fit_params_2_after[3]
wave_length_after_2 = np.pi / wave_number_after_2
x_coord_2 = np.linspace(x_real_space[52], x_real_space[95], 1000)
data_fit_2_a = decaying_func(fit_params_2_after, x_coord_2)
ax2.plot(x_coord_2, data_fit_2_a, color='orange', label='fit ' + r'$\lambda$' + '=' +
                                                      "{0:.2f}".format(wave_length_after_2) + r'$\mu m$')


# plotting curve 3
ax3 = fig_phr.add_subplot(311)
ax3.scatter(x_real_space, m_data_3.data.T[1], color='black', marker='p', label=m_data_3.mes_name[-4:])


# plotting fit 3
fit_params_3_before = np.array([3.84705297e+04, 1.80373919e-01, 1.62730002e+00, 5.06469666e-01,
                                2.95100817e+00, 6.42040819e+03])
wave_number_before_3 = fit_params_3_before[3]
wave_length_before_3 = np.pi/wave_number_before_3
x_coord_3 = np.linspace(x_real_space[3], x_real_space[29], 500)
data_fit_3_b = decaying_func(fit_params_3_before, x_coord_3)
ax3.plot(x_coord_3, data_fit_3_b, color='blue', label='fit ' + r'$\lambda$' + '=' +
                                                      "{0:.2f}".format(wave_length_before_3) + r'$\mu m$')
# in the variable width section
fit_params_3_variable = np.array([3.60297452e+04, 5.95724227e-02, 8.79299100e-01, 6.06959860e-01,
                                  2.41172139e+00, 7.45461188e+03])
wave_number_variable_3 = fit_params_3_variable[3]
wave_length_variable_3 = np.pi / wave_number_variable_3
x_coord_3 = np.linspace(x_real_space[31], x_real_space[52], 1000)
data_fit_3_v =decaying_func(fit_params_3_variable, x_coord_3)
ax3.plot(x_coord_3, data_fit_3_v, color='green', label='fit ' + r'$\lambda$' + '=' +
                                                      "{0:.2f}".format(wave_length_variable_3) + r'$\mu m$')

# after the variable width section
fit_params_3_after = np.array([6.13908015e+04, 1.07411702e-01, 8.55633955e-01, 6.40358429e-01,
                               2.22457811e+00, 1.36521974e+04])
wave_number_after_3 = fit_params_3_after[3]
wave_length_after_3 = np.pi/wave_number_after_3
x_coord_3 = np.linspace(x_real_space[52], x_real_space[95], 1000)
data_fit_3_a =decaying_func(fit_params_3_after, x_coord_2)
ax3.plot(x_coord_3, data_fit_3_a, color='orange', label='fit ' + r'$\lambda$' + '=' +
                                                      "{0:.2f}".format(wave_length_after_3) + r'$\mu m$')


# plotting the range of the variable width  region in the DC line
y_line = np.linspace(0, 1.1*max(m_data_3.data.T[1]), 100000)
x_line = np.array([x_real_space[30] for i in range(len(y_line))])
y_line_2 = np.linspace(0, 1.1*max(m_data_3.data.T[1]), 100000)
x_line_2 = np.array([x_real_space[52] for i in range(len(y_line))])

ax1.plot(x_line, y_line, linestyle='--', color='red', label='DC-line width change '
                                                                '\n(start 6.7' + r'$\mu m$' + ','+
                                                                'end 11.7' + r'$\mu m$' + ')')
ax1.plot(x_line_2, y_line_2, linestyle='--', color='red')
ax1.axvspan(x_real_space[30], x_real_space[52], color='grey', alpha=0.3, label='variable width reigon')

ax2.plot(x_line, y_line, linestyle='--', color='red', label='DC-line width change '
                                                                '\n(start 6.7' + r'$\mu m$' + ','+
                                                                'end 11.7' + r'$\mu m$' + ')')
ax2.plot(x_line_2, y_line_2, linestyle='--', color='red')
ax2.axvspan(x_real_space[30], x_real_space[52], color='grey', alpha=0.3, label='variable width reigon')

ax3.plot(x_line, y_line, linestyle='--', color='red', label='DC-line width change '
                                                                '\n(start 6.7' + r'$\mu m$' + ','+
                                                                'end 11.7' + r'$\mu m$' + ')')
ax3.plot(x_line_2, y_line_2, linestyle='--', color='red')
ax3.axvspan(x_real_space[30], x_real_space[52], color='grey', alpha=0.3, label='variable width reigon')


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

plt.savefig('./output_pics/phase_res_combined_5p1GHz_30mT_0_10_20mA_v2.png', format='png', dpi=100)

plt.show()