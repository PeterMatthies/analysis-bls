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
fig_phr = plt.figure()
title_name = 'Phase resolved line scan along Py stripe\n 6GHz, 30mT'
fig_phr.suptitle(title_name, fontweight='bold', fontsize=12)
ax = fig_phr.add_subplot(111)

# shifting curves by fixed amount so they are clearer to see on the plot
m_data_2.data.T[1] += 1.0*max(m_data_3.data.T[1])
m_data_3.data.T[1] += 2.1*max(m_data_3.data.T[1])

# plotting each of the curves
ax.scatter(x_real_space, m_data_1.data.T[1], color='black', marker='.', label=m_data_1.mes_name[-4:])
ax.scatter(x_real_space, m_data_2.data.T[1], color='black', marker='x',label=m_data_2.mes_name[-4:])
ax.scatter(x_real_space, m_data_3.data.T[1], color='black', marker='p', label=m_data_3.mes_name[-4:])

# plotting the position of the step in the DC line
y_line = np.linspace(0, 1.1*max(m_data_3.data.T[1]), 100000)
x_line = np.array([x_real_space[30] for i in range(len(y_line))])
ax.plot(x_line, y_line, linestyle='--', color='red', label='DC-line\nstep pos (6.7' + r'$\mu m$' + ')')

# plotting fit 1
fit_params_1 = np.array([1.28697228e+03, 1.53982330e-01, 1.67576877e+00, 1.11037877e+00,
                         4.50999392e+00, 1.46674641e+03])
wave_number = fit_params_1[3]
wave_length = np.pi / wave_number
print(wave_length)
x_coord_1 = np.linspace(x_real_space[3], x_real_space[91], 1000)
data_fit_1 = decaying_func(fit_params_1, x_coord_1)
print(data_fit_1)
ax.plot(x_coord_1, data_fit_1, color= 'orange', label='fit ' + r'$\lambda$' + '=' + "{0:.2f}".format(wave_length) + r'$\mu m$')

# plotting fit 2
fit_params_2_before = np.array([5.38533554e+03, 2.09031869e-01, 1.59725107e+00, 9.89025845e-01, 1.22621132e+00,
                                2.01963278e+03])

wave_number_before_2 = fit_params_2_before[3]
wave_length_before_2 = np.pi/wave_number_before_2
x_coord = np.linspace(x_real_space[3], x_real_space[29], 500)
data_fit_2_b = decaying_func(fit_params_2_before, x_coord) + 1.0*max(m_data_3.data.T[1])
ax.plot(x_coord, data_fit_2_b, color='blue', label='fit '+r'$\lambda$'+'='+"{0:.2f}".format(wave_length_before_2) + r'$\mu m$')


# making the plot beautiful - axes labels, ticks, limits etc.
ax.grid()
new_xticks = np.linspace(0, 22.3, 12)
new_xticks = [int(xtick) for xtick in new_xticks]
ax.set_xticks(new_xticks)
# ax.set_xlim([0, 21])
# ax.set_ylim([0, 1.1*max(m_data_3.data.T[1])])
ax.set_xlabel('Position along Py stripe' + r' ($\mu m$)')
ax.set_ylabel('Intensity (a.u.)')
ax.ticklabel_format(axis='y', style='sci', scilimits=(-3, 3), useOffset=False)
ax.yaxis.major.formatter._useMathText = True
ax.legend()
fig_phr.tight_layout()
fig_phr.subplots_adjust(top=0.89)

plt.show()