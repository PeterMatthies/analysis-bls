import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.optimize import leastsq

from mpl_toolkits.mplot3d import Axes3D


def plot_res_curves_2d(data, m_name, m_date, m_type, show=True, save=False):
    fig1 = plt.figure()

    # plotting the data

    proper_date = m_date[:2]+'.'+m_date[2:4]+'.'+m_date[4:]
    title_name = m_type + '\n' + 'along Py stripe' + ' at ' + m_name[-4:] + ' DC'
    fig1.suptitle(title_name, fontweight='bold', fontsize=12)
    ax1 = fig1.add_subplot(111)
    i = 0
    colors = cm.magma(np.linspace(0, 1, len(data.T)/2))
    real_distance = np.linspace(0, 22.3, 100)
    print(real_distance[30])
    for i, color in zip(range(0, len(data.T), 2), colors):
        x = data.T[i]
        y = data.T[i+1]
        print(x)
        print(len(x))
        # plotting the data
        ax1.scatter(real_distance, y, c=color, label='data')


        # plotting the DC step position
        y_line = np.arange(0, max(y) + 15000, 5)
        x_line = np.array([real_distance[30] for i in range(len(y_line))])
        print(real_distance)
        ax1.plot(x_line, y_line, linestyle='--', color='red', label='DC-line\nstep pos (6.7' + r'$\mu m$' + ')')
        print(real_distance[30])

        # fitting part

        # for the measurement without DC

        if '00' in m_name:
            guess_amplitude = np.mean(y)  # params[0]
            guess_decay = 0.2  # params[1]
            guess_x0 = 1.69  # params[2]
            guess_wave_number = 0.85 # params[3]
            guess_phase = 4.88  # params[4]
            guess_y0 = 10000  # params[5]
            guess_params = np.array([guess_amplitude, guess_decay, guess_x0, guess_wave_number, guess_phase, guess_y0])

            decaying_func = lambda params, coord: params[0] * np.exp(-params[1] * coord + params[2]) * \
                                                  np.power(np.cos(params[3] * coord + params[4]), 2) + params[5]
            errfunc = lambda params, coord, y: decaying_func(params, coord) - y

            est_amplitude, est_decay, est_x0, est_wave_number, est_phase, est_y0 = \
                leastsq(errfunc, guess_params, args=(real_distance[3:91], y[3:91]))[0]
            fit_params = np.array([est_amplitude, est_decay, est_x0, est_wave_number, est_phase, est_y0])
            print(fit_params)
            wave_number = fit_params[3]
            wave_length = np.pi / wave_number
            x_coord = np.linspace(real_distance[3], real_distance[91], 1000)
            data_fit = decaying_func(fit_params, x_coord)
            ax1.plot(x_coord, data_fit,
                     label='fit ' + r'$\lambda$' + '=' + "{0:.2f}".format(wave_length) + r'$\mu m$')

        else:
            # fitting before step

            guess_amplitude = np.mean(y)  # params[0]
            guess_decay = -0.03  # params[1]
            guess_x0 = -1.69  # params[2]
            guess_wave_number = 0.7  # params[3]
            # guess_wave_number = 0.1  # params[3]
            guess_phase = 2.88  # params[4]
            guess_y0 = 10000  # params[5]
            guess_params = np.array([guess_amplitude, guess_decay, guess_x0, guess_wave_number, guess_phase, guess_y0])

            decaying_func = lambda params, coord: params[0] * np.exp(-params[1] * coord + params[2]) * \
                                                  np.power(np.cos(params[3] * coord + params[4]), 2) + params[5]
            errfunc = lambda params, coord, y: decaying_func(params, coord) - y


            est_amplitude, est_decay, est_x0, est_wave_number, est_phase, est_y0 = \
                leastsq(errfunc, guess_params, args=(real_distance[3:31], y[3:31]))[0]
            fit_params = np.array([est_amplitude, est_decay, est_x0, est_wave_number, est_phase, est_y0])
            print(fit_params)
            wave_number_before = fit_params[3]
            wave_length_before = np.pi/wave_number_before
            x_coord = np.linspace(real_distance[3], real_distance[29], 500)
            data_fit = decaying_func(fit_params, x_coord)
            ax1.plot(x_coord, data_fit, color='blue', label='fit '+r'$\lambda$'+'='+"{0:.2f}".format(wave_length_before) + r'$\mu m$')

            # fitting after the step

            guess_amplitude = np.mean(y)  # params[0]
            guess_decay = -0.1  # params[1]
            guess_x0 = -0.27  # params[2]
            guess_wave_number = 1.01  # params[3]
            guess_phase = 5.13  # params[4]
            guess_y0 = 10000  # params[5]
            guess_params = np.array([guess_amplitude, guess_decay, guess_x0, guess_wave_number, guess_phase, guess_y0])

            decaying_func = lambda params, coord: params[0] * np.exp(-params[1] * coord + params[2]) * \
                                                  np.power(np.cos(params[3] * coord + params[4]), 2) + params[5]
            errfunc = lambda params, coord, y: decaying_func(params, coord) - y

            fit_params = leastsq(errfunc, guess_params, args=(real_distance[31:91], y[31:91]))[0]
            # fit_params = np.array([est_amplitude, est_decay, est_x0, est_wave_number, est_phase, est_y0])
            print(fit_params)
            wave_number_after = fit_params[3]
            wave_length_before = np.pi / wave_number_after
            x_coord = np.linspace(real_distance[30], real_distance[91], 1000)
            data_fit2 = decaying_func(fit_params, x_coord)
            ax1.plot(x_coord, data_fit2, color='green', label='fit '+r'$\lambda$'+'='+"{0:.2f}".format(wave_length_before) + r'$\mu m$')

    # some things to make plot beautiful
    ax1.grid()
    new_xticks = np.linspace(0, 22.3, 12)
    new_xticks = [int(xtick) for xtick in new_xticks]
    ax1.set_xticks(new_xticks)
    ax1.set_xlim([0, 22.3])
    ax1.set_ylim([0, max(y)+2000])
    ax1.set_xlabel('Position along Py stripe'+r' ($\mu m$)')
    ax1.set_ylabel('Intensity (a.u.)')
    ax1.ticklabel_format(axis='y', style='sci', scilimits=(-3, 3), useOffset=False)
    ax1.yaxis.major.formatter._useMathText = True
    ax1.legend()
    fig1.tight_layout()
    fig1.subplots_adjust(top=0.89)

    if save:
        # m_name_new = m_name[:1]+'p'+m_name[2:]
        save_name = m_date + '_' + m_name + '_' + m_type + '.png'
        plt.savefig('./output_pics/'+save_name, format='png', dpi=100)
    if show:
        plt.show()


def plot_res_curves_3d(data, m_name, m_date, m_type, show=True, save=False):
    fig1 = plt.figure()
    proper_date = m_date[:2]+'.'+m_date[2:4]+'.'+m_date[4:]
    title_name = proper_date + ' ' + m_type + '\n' + m_name + ' along Py stripe'
    fig1.suptitle(title_name, fontweight='bold', fontsize=12)
    ax1 = fig1.add_subplot(111, projection='3d')
    i = 0
    colors = cm.rainbow(np.linspace(0, 1, len(data.T) / 2))
    # dc_values = np.arange(20, -5, -5)
    dc_values = np.arange(0, 20, 1)
    z_values = []
    for dc_v in dc_values:
        z_values.append([dc_v for k in range(len(data[:, 0]))])
    for i, color, z in zip(range(0, len(data.T), 2), colors, z_values):
        x = data.T[i]
        y = data.T[i + 1]
        # z = np.array([i for element in x])
        # ax1.plot(x, z, y, c=color)
        ax1.scatter(x, z, y, c=color)
    ax1.grid()
    ax1.set_xlabel('position (pts)')
    ax1.ticklabel_format(axis='x', style='sci', scilimits=(-3, 3), useOffset=False)
    ax1.xaxis.major.formatter._useMathText = True
    ax1.ticklabel_format(axis='z', style='sci', scilimits=(-3, 3), useOffset=False)
    ax1.zaxis.major.formatter._useMathText = True
    ax1.set_ylabel('DC (mA)')
    ax1.set_zlabel('Intensity (a.u.)')
    if save:
        save_name = m_date + '_' + m_name + '_' + m_type + '.png'
        plt.savefig(save_name, format='png', dpi=100)
    if show:
        plt.show()


def plot_raw_data(data, m_name, m_date, m_type, show=True, save=False):
    fig1 = plt.figure()
    proper_date = m_date[:2] + '.' + m_date[2:4] + '.' + m_date[4:]
    title_name =  m_type + '\n' + ' along Py stripe' + ' at ' + m_name[-4:] + ' DC'
    fig1.suptitle(title_name, fontweight='bold', fontsize=12)
    ax1 = fig1.add_subplot(111)

    cmap = plt.get_cmap('jet')
    cmap.set_under('black')
    # cmap.set_over('black')
    eps1 = np.spacing(0)
    im = ax1.imshow(data.T, origin='lower', aspect='auto', vmin=eps1, vmax=6000, cmap=cmap)

    print(data.T.shape)
    proper_yticks_labels = np.linspace(0, 160, 13)
    ax1.set_yticklabels(proper_yticks_labels)
    ax1.set_yticks(proper_yticks_labels)
    proper_yticks_labels = np.linspace(-9, 3, 13)
    proper_yticks_labels= ["{0:.2f}".format(y_tick) for y_tick in proper_yticks_labels]
    ax1.set_yticklabels(proper_yticks_labels)
    proper_xticks_labels = np.linspace(0, 100, 11)
    ax1.set_xticks(proper_xticks_labels)
    proper_xticks_labels = np.linspace(0, 22.3, 11)
    proper_xticks_labels = [int(x_tick) for x_tick in proper_xticks_labels]
    ax1.set_xticklabels(proper_xticks_labels)

    ax1.set_xlabel('Position along Py stripe'+r' ($\mu m$)')
    ax1.set_ylabel('BLS Frequency (GHz)')

    # fig1.colorbar(im)
    if save:
        save_name = m_date + '_' + m_name + '_' + m_type + '.png'
        plt.savefig(save_name, format='png', dpi=100)
    if show:
        plt.show()