'''
---------------------------------------------------------------------
Example python code for fitting a simple model to data with errors
in both x and y

Uses routines from scipy.stats for Ordinary Least Squares regression
and scipy.odr, for Orthogonal Distance Regression

                                           Roderick Brown, 31/3/2020
---------------------------------------------------------------------
'''
%matplotlib inline

# -*- coding: utf-8 -*-

# Import required modules
import numpy as np
import scipy.odr.odrpack as odrpack
from scipy import stats
#from scipy.optimize import curve_fit
import csv
import matplotlib.pyplot as plt

# Provide path to data file to read data from
#filename = '/Users/rod/src/python/python/python/mull_gravity.txt' # Simple tab delimeted ascii text file with data to be read in

# create some data
size = 15 # number of values to generate
true_intercept = 1.5
true_slope = 2.0
np.random.seed(321) # set random seed so repeated runs are identical

X = np.linspace(5, 20, size) # create 'size' (size is defined above) equally spaced  x values starting from 5 to 20
# y = a + b*x
Y = true_intercept + true_slope * X # calculate the y values (insert new function here if you add a more complex model)

# add some outliers, i.e. "real" outliers, set variance..."add" as in just make them up :-)
x_outliers = [18.1,18.3,18.7]
y_outliers = [25.,21.,24.]
sy_outliers = [6.,7.,5.] #np.random.normal(scale=10., size=len(y_outliers))
sx_outliers = [1.,0.8,0.5] #np.random.normal(scale=0.5, size=len(x_outliers))

# generate errors on "real" data using normal distribution (variance is constant)
SY = np.random.normal(scale=2., size=len(Y))
SX = np.random.normal(scale=0.8, size=len(X))
# add noise/errors to sampled data
Xdata = X + SX
Ydata = Y + SY

Xvalues = np.append(Xdata,x_outliers)
Yvalues = np.append(Ydata,y_outliers)
Xerrors = np.append(SX,sx_outliers)
Yerrors = np.append(SY,sy_outliers)
#append the outliers to the sampled data


residuals=[]

#print (X)
#print (SX)
#print (SY)
#print (Xdata)
#print (Ydata)

'''
# Read x,y data into 2D array from text file using numpy genfromtxt
#data = np.genfromtxt(filename, comments="#", usecols=(0,1,2,3))

X=data[:,0]       # Assign first column to x variable
SX=data[:,1]      # Assign second column to sx, stddev of x variable
Y=data[:,2]       # Assign third column to y variable 
SY=data[:,3]      # Assign fourth column to sy, stddev of y variable

'''

# Run OLS regression using scipy linear regression routine, stats.linregress
slope_ols, intercept_ols, r_value, p_value, std_err = stats.linregress(Xvalues,Yvalues)

# Print some stats for fit to screen
print ('OLS slope: ',slope_ols)
print ('OLS intercept: ',intercept_ols)
print ('R: ',r_value**2)

# Scipy's ODR, Orthogonal Distance Regression library (errors on x, y data included)
#-----------------------------------------------------------

# Here we define our model that we wish to fit to the data, array B is an array that holds the model parameters to be estimated
def linear(B,x): # define a linear model with B[0] as slope and B[1] as intercept
    return(B[0]*x + B[1])

# Do ODR regression
#---------------------------------------------------------------------
# Instantiate a model object using the spherical model defined above
model = odrpack.Model(linear)

# Instantiate a real data object to hold the observed data
data = odrpack.RealData(Xvalues, Yvalues, sx=Xerrors, sy=Yerrors)

# Pass data object and spherical model object to ODR solver
odrsolver = odrpack.ODR(data, model, beta0=[1.,1.])

# Run the ODR object and store output in myoutput#
myoutput = odrsolver.run()

# Print summary of output of ODR to stdout (i.e. screen)
myoutput.pprint()

# Extract some useful stats and store them in named variables to use later
slope_odr=myoutput.beta[0]
err_slope_odr=myoutput.sd_beta[0]
intercept_odr=myoutput.beta[1]
err_intercept_odr=myoutput.sd_beta[1]

# Calculate fitted value of y at each x location, and the residuals
# at each location using optimum parameters returned by ODR regression
modelY = []
for i in range (0,len(Xvalues)):
     modelY.append(intercept_odr+ slope_odr*Xvalues[i])
     residuals.append(modelY[i]-Yvalues[i])

# Print essential parameters and error estimates to stdout, i.e. screen
print ('\nODR regression')

print (f"slope: {slope_odr:.2f}  +/- {err_slope_odr:.2f}") # Using new f string formatting style

print ('\nintercept: ', intercept_odr, ' +/- ',err_intercept_odr,' >>> Using unformatted print')

print ('intercept: {:03.2f} +/- {:03.2f} >>> Using old str.format style'.format(intercept_odr, err_intercept_odr))

print (f"intercept: {intercept_odr:.2f} +/- {err_intercept_odr:.2f} >>> Using new f string format style")

# Draw plot (basically a simple x,y graph, uses matplotlib routines from pyplot)
#--------------------------------------------------------
plt.figure(1)

# Set various axes and labels etc
plt.title('Linear regression')
plt.xlabel('X value')
plt.ylabel('Y value')
# Set min, max values for x,y axes
#plt.axis([-30000,50000,-15.,70.])

# Plot true line
plt.plot(X,Y,'k--',linewidth=2, label='True line')
# plot sampled data with errors

# Place all kwargs for xy data plot style in a dictionary, arguably tidier and easier to read/edit
style_data = {'marker':'o','markersize':6, 'markerfacecolor':'w', 'markeredgecolor':'k',\
              'elinewidth':1.5,'linewidth':0, 'label':'Sampled data'}
plt.errorbar(Xvalues, Yvalues, Yerrors, Xerrors, **style_data)

# Plot predictions for ODR and OLS methods
# Place all kwargs for plot style in a dictionary. tidier and easier to read/edit
style_odr={'color':'blue','linewidth':2,'linestyle':'-','label':'ODR prediction'}
style_ols={'color':'red','linewidth':2,'linestyle':'-','label':'OLS prediction'}

plt.plot(Xdata,(slope_odr*Xdata+intercept_odr), **style_odr)
plt.plot(Xdata,(slope_ols*Xdata+intercept_ols), **style_ols)

# Plot residuals (i.e. model - observed)
#plt.plot(x,residuals, '+', markersize=6, markerfacecolor='w', markeredgecolor='r', label='ODR Residuals')


#Plot legend
plt.legend(loc='upper left')

# Write plot to pdf file
#plt.savefig('regression_example.pdf', format='pdf')

# Show. i.e. draw, the plot on screen
plt.show()
