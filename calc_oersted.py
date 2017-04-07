# Oersted-field calculation

import numpy as np
import matplotlib.pyplot as plt

# define variables
width = 3  # µm
thickness_min = 0.025  # µm
thickness_max = 0.05  # µm
I = 0.02  # A
d = 0.015  # µm (distance to surface of oersted wire)
y_steps = 100
mu0 = 1.2566E-6

# Calculation
# Origin of the coordinate system is the center of the wire cross section

a = width / (2 * 1000000)
b_min = thickness_min / (2 * 1000000)
b_max = thickness_max / (2 * 1000000)
distance_to_py_center = 65e-9
py_stripe_middle1 = thickness_max / (2 * 1000000) + distance_to_py_center
py_stripe_middle2 = thickness_min / (2 * 1000000) + distance_to_py_center
print(py_stripe_middle1, py_stripe_middle2)


def calculate_field(y, b, z):
    return 1000 * ((-I * mu0) / (8 * np.pi * a * b)) * (
        (a - y) * (0.5 * np.log(((np.power(b - z, 2)) + (np.power(a - y, 2))) / ((np.power(-b - z, 2)) +
                                                                                 (np.power(a - y, 2)))) +
                   ((b - z) / (a - y)) * np.arctan(((a - y) / (b - z))) - ((-b - z) / (a - y)) *
                   np.arctan(((a - y) / (-b - z)))) -
        (-a - y) * (
            0.5 * np.log(
                ((np.power(b - z, 2)) + (np.power(-a - y, 2))) / ((np.power(-a - y, 2)) + (np.power(-b - z, 2)))) + (
                (b - z) / (-a - y)) * np.arctan(((-a - y) / (b - z))) -
            ((-b - z) / (-a - y)) * np.arctan(((-a - y) / (-b - z)))))
    # B in mT, that's why: factor 1000


y_coord = np.linspace(-a, a, y_steps)
y2 = 1000000 * y_coord
z_coord = b_min + (d / 1000000)
By1 = calculate_field(y_coord, b_min, z_coord)
z_coord = b_max + (d / 1000000)
By2 = calculate_field(y_coord, b_max, z_coord)

field_middle_py1 = calculate_field(y_coord, b_max, py_stripe_middle1)
field_middle_py2 = calculate_field(y_coord, b_min, py_stripe_middle2)


# Output

# print("B_in_plane min (mT): ", By1)
# print("B_in_plane max (mT): ", By2)
plt.figure()
print('Inplane Oersted in center of Py (mT):', field_middle_py1)
print('Inplane Oersted in center of Py (mT):', field_middle_py2)

plt.plot(y2, field_middle_py1, 'bo', label='middle of Py, Au 50nm thick')
plt.plot(y2, field_middle_py2, 'rx', label='middle of Py, Au 25 nm thick')
plt.plot(y2, By1, 'yo', label='surface of Au, Au 25nm thick')
plt.plot(y2, By2, 'gx', label='surface of Au, Au 50nm thick')
plt.axis([(-a * 1000000), (a * 1000000), 2.0, 4.5])
plt.xlabel("Position across wire (µm)")
plt.ylabel(r"$B_{in\hspace{0.2} plane}$ (mT)")
plt.grid(True)
plt.legend()
# plt.savefig('swsd1_oersted_inplane.png', format='png', dpi=100)
plt.show()
