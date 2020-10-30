#!/usr/bin/env python
# coding: utf-8

# # Interactive line fitting
# Run the code in the cell below. A graph of some synthetic x and y data and a defauly straight line model should be generated. Use the interactive sliders to adjust the slope and intercept of the straight line so that it fits the observed data as closely as possible.

# In[4]:


'''
Example of interactive plot using ipywidgets interact function

Plots a set of x y valye pairs with some random noise on y,
then allows the parameters of a straight line to be adjusted
using interactive slider widgets.
                                       Roderick Brown 12/4/20
'''

#get_ipython().run_line_magic('matplotlib', 'inline')

# Import required packages
from ipywidgets import interact
import matplotlib.pyplot as plt
import numpy as np

# Define function to plot data and straight line
def xyline(slope,intercept):
     npoints = 5
     xmin = 1
     xmax = 10
     sy = 2. # Set stddev of normal distribution to draw y valu errors from
     m = 2.0 # Set slope for synthetc data
     c = 8.  # Set intercept for synthetic data

     np.random.seed(12345) # set random seed so repeated runs are identical
     xdata = np.linspace(xmin,xmax-1,npoints)
     yerr = np.random.normal(scale=sy,size=len(xdata))
     ydata = xdata*m + c + yerr

     plt.figure(1)
     # Set x and y values for interactive line to plot
     x = np.linspace(0, 10, num=100)
     y = x*slope + intercept

     # Plot data points
     style_data = {'marker':'o','markersize':6, 'markerfacecolor':'w', 'markeredgecolor':'k',              'elinewidth':1.5,'linewidth':0, 'label':'data'}

     plt.errorbar(xdata,ydata,2*sy,**style_data)

     # Plot the straight line
     plt.plot(x, (x*slope+intercept),'r-',label='model line')

     plt.ylim(-10, 40)
     plt.xlim(0, xmax)
     plt.legend(loc='upper left')
     plt.show()

# Call the function using ipywidgets interact
interact(xyline,slope=(-8.0,8.0,1.0), intercept=(-15, 15, 1.0))


# In[ ]:





# In[ ]:
