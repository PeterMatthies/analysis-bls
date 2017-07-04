# Oersted-field calculation

import numpy as np
import matplotlib.pyplot as plt


def c_density(current, width, height):
    return current/(width*height)


def gamma(i_dens):
    return (1.2566E-6/(4*np.pi))*i_dens


def calc_h(p_zero, z_zero, width, height, current):
    return (gamma(c_density(current, width, height))/2)*(p_zero*\
           np.log(1+(np.power(height, 2)+z_zero*height)/(np.power(p_zero, 2)+np.power(z_zero, 2)))+\
           2*(z_zero+height)*np.arctan(p_zero/(z_zero+height))-2*z_zero*np.arctan(p_zero/z_zero))


def field_inplane(x_pos, z_pos, width, height, current):
    x1 = x_pos + width / 2
    x2 = x_pos - width / 2
    return calc_h(x1, z_pos, width, height, current) - \
           calc_h(x2, z_pos, width, height, current)

# define variables
w = 3e-6  # m
thickness_min = 25e-9  # m
thickness_max = 50e-9  # m
I = 0.05  # A
z0 = 65e-9 # m middle of py stripe
mu0 = 1.2566E-6

ImA = I*1000
print(ImA)

# Calculation
print('Oersted field is (mT):', 1000*field_inplane(0.0, z0, w, thickness_max, I), '50 nm Au')
print('Oersted field is (mT):', 1000*field_inplane(0.0, z0, w, thickness_min, I), '25 nm Au')

x_points = np.linspace(-w/2, w/2, 1000)
field_middle_py1 = 1000*field_inplane(x_points, z0, w, thickness_max, I)
field_middle_py2 = 1000*field_inplane(x_points, z0, w, thickness_min, I)
By1 = 1000*field_inplane(x_points, 0, w, thickness_min, I)
By2 = 1000*field_inplane(x_points, 0, w, thickness_max, I)


fig1 = plt.figure()
# print('Inplane Oersted in center of Py (mT):', field_middle_py1)
# print('Inplane Oersted in center of Py (mT):', field_middle_py2)
ax1 = fig1.add_subplot(111)
ax1.plot(x_points, field_middle_py1, 'bo', label='middle of Py, Au 50nm thick', markersize=4)
ax1.plot(x_points, field_middle_py2, 'rx', label='middle of Py, Au 25 nm thick', markersize=4)
ax1.plot(x_points, By1, 'yo', label='surface of Au, Au 25nm thick', markersize=4)
ax1.plot(x_points, By2, 'gx', label='surface of Au, Au 50nm thick', markersize=4)
# plt.axis([-w/2, w/2, 7.0, 16])
plt.xlim([-w/2, w/2])
ax1.ticklabel_format(axis='x', style='sci', scilimits=(-3, 3), useOffset=False)
ax1.xaxis.major.formatter._useMathText = True
ax1.grid(True)
ax1.legend(loc=8)
plt.xlabel("Position across wire (m)")
plt.ylabel(r"$B_{in\hspace{0.2} plane}$ (mT)")
plt.tight_layout()

plt.savefig('swsd1_oersted_inplane_'+str(ImA)+'mA.png', format='png', dpi=100)
plt.show()
