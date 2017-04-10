# Oersted-field calculation
# origin of coordinate system middle bottom in the cross section of the Au wire

import numpy as np
import matplotlib.pyplot as plt


def calc_field(x_pos, z_pos, width, height, current):
    gamma = (1.2566E-6/(4*np.pi))*current/(width*height)
    x1 = x_pos + width/2
    x2 = x_pos - width/2
    z1 = height - z_pos
    a1 = (np.power(x1, 2) + np.power(z_pos, 2)) / (np.power(x1, 2) + np.power(z1, 2))
    a2 = (np.power(x2, 2) + np.power(z_pos, 2)) / (np.power(x2, 2) + np.power(z1, 2))
    print(gamma, x1, x2, z1, a1, a2)
    return gamma * (0.5 * x1 * np.log(a1) - 0.5 * x2 * np.log(a2) +
                     z_pos * (np.arctan(x1 / z_pos) - np.arctan(x2 / z_pos)) -
                     z1 * (np.arctan(x1 / z1) - np.arctan(x2 / z1)))


# define variables
w = 3e-6  # m
thickness_min = 25e-9  # m
thickness_max = 50e-9  # m
I = 0.15  # A
z0 = 90e-9  # m middle of py stripe
mu0 = 1.2566E-6

# Calculation
print('Oersted field is (mT):', 1000*calc_field(0.0, z0, w, thickness_max, I), '50 nm Au')
print('Oersted field is (mT):', 1000*calc_field(0.0, z0, w, thickness_min, I), '25 nm Au')
#
x_points = np.linspace(-w/2, w/2, 1000)
field_middle_py1 = 1000*calc_field(x_points, z0, w, thickness_max, I)
field_middle_py2 = 1000*calc_field(x_points, z0, w, thickness_min, I)
By1 = 1000*calc_field(x_points, thickness_max, w, thickness_min, I)
By2 = 1000*calc_field(x_points, thickness_max, w, thickness_max, I)
#
#
fig1 = plt.figure()
print('Inplane Oersted in center of Py (mT):', field_middle_py1)
print('Inplane Oersted in center of Py (mT):', field_middle_py2)
ax1 = fig1.add_subplot(111)
ax1.plot(x_points, field_middle_py1, 'bo', label='middle of Py, Au 50nm thick', markersize=4)
ax1.plot(x_points, field_middle_py2, 'rx', label='middle of Py, Au 25 nm thick', markersize=4)
ax1.plot(x_points, By1, 'yo', label='surface of Au, Au 25nm thick', markersize=4)
ax1.plot(x_points, By2, 'gx', label='surface of Au, Au 50nm thick', markersize=4)
# plt.axis([(-w/2 * 1000000), (w/2 * 1000000), 0.0, 50])
ax1.ticklabel_format(axis='x', style='sci', scilimits=(-3, 3), useOffset=False)
ax1.xaxis.major.formatter._useMathText = True
ax1.grid(True)
ax1.set_xlim(-w/2, w/2)
ax1.legend(loc=8)
plt.xlabel("Position across wire (m)")
plt.ylabel(r"$B_{in\hspace{0.2} plane}$ (mT)")
#
# plt.savefig('swsd1_oersted_inplane.png', format='png', dpi=100)
plt.show()
