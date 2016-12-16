import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D


def plot_res_curves_2d(data, m_name, m_date, m_type, show=True, save=False):
    fig1 = plt.figure()
    proper_date = m_date[:2]+'.'+m_date[2:4]+'.'+m_date[4:]
    title_name = proper_date + ' ' + m_type + '\n' + 'along Py stripe at ' + m_name
    fig1.suptitle(title_name, fontweight='bold', fontsize=12)
    ax1 = fig1.add_subplot(111)
    i = 0
    colors = cm.rainbow(np.linspace(0, 1, len(data.T)/2))
    for i, color in zip(range(0, len(data.T), 2), colors):
        x = data.T[i]
        y = data.T[i+1]
        ax1.plot(x, y, c=color)
    ax1.grid()
    ax1.set_xlabel('position (pts)')
    ax1.set_ylabel('Intensity (a.u.)')
    ax1.ticklabel_format(axis='y', style='sci', scilimits=(-3, 3), useOffset=False)
    ax1.yaxis.major.formatter._useMathText = True
    if save:
        m_name_new = m_name[:1]+'p'+m_name[2:]
        save_name = m_date + '_' + m_name_new + '_' + m_type + '.png'
        plt.savefig(save_name, format='png', dpi=100)
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
    dc_values = np.arange(20, -5, -5)
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
