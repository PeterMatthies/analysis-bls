#########################################################################
####################### IMPORTING REQUIRED MODULES ######################

import numpy
import pylab
from scipy.optimize import leastsq # Levenberg-Marquadt Algorithm #

#########################################################################
############################# LOADING DATA ##############################

path_to_data = './m_data/02082017_dr_pyref/'
data_file = 'm6_50mT_50inc.txt'
a = numpy.loadtxt(path_to_data+data_file)
x = a[:, 0]
y = a[:, 1]
ind_stokes = (x > -15.5) & (x < -2.9)
x = x[ind_stokes]
y = y[ind_stokes]
# pylab.scatter(x, y)
# pylab.show()
########################################################################
########################## DEFINING FUNCTIONS ##########################

def lorentzian(x,p):
    numerator =  (p[0]**2 )
    denominator = ( x - (p[1]) )**2 + p[0]**2
    y = p[2]*(numerator/denominator)
    return y

def residuals(p,y,x):
    err = y - lorentzian(x,p)
    return err

#########################################################################
######################## BACKGROUND SUBTRACTION #########################

# defining the 'background' part of the spectrum #
ind_bg_low = (x > -15.5) & (x < -14.0)
ind_bg_high = (x > -10.0) & (x < -3.0)

x_bg = numpy.concatenate((x[ind_bg_low],x[ind_bg_high]))
y_bg = numpy.concatenate((y[ind_bg_low],y[ind_bg_high]))
# pylab.plot(x_bg,y_bg)

# fitting the background to a line #
m, c = numpy.polyfit(x_bg, y_bg, 1)

# removing fitted background #
background = m*x + c
y_bg_corr = y - background
# pylab.plot(x,y_bg_corr)
# pylab.show()
#########################################################################
############################# FITTING DATA ## ###########################

# initial values #
p = [0.3, -11.1, 144]  # [hwhm, peak center, intensity] #

# optimization #
pbest = leastsq(residuals,p,args=(y_bg_corr,x),full_output=1)
best_parameters = pbest[0]

# fit to data #
x_fit = numpy.linspace(min(x), max(x), 1000)
fit = lorentzian(x_fit,best_parameters)
print(best_parameters)

#########################################################################
############################## PLOTTING #################################

pylab.plot(x, y_bg_corr,'go')
# pylab.bar(x, y)
pylab.plot(x_fit, fit,'r-',lw=2)
pylab.xlabel(r'$\omega$ (cm$^{-1}$)', fontsize=18)
pylab.ylabel('Intensity (a.u.)', fontsize=18)

pylab.show()