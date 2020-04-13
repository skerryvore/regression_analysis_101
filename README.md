[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/skerryvore/linear_regression_101/master)

![regression_banner25cm](https://user-images.githubusercontent.com/5646482/79122519-bd6c2d00-7d8f-11ea-9732-471f6bfe0168.png)

# regression_analysis_101
Estimating the parameters of a model by optimising the fit of the model to empirical data is a staple of computational data science. 

This repository contains a set of Jupyter notebooks that demonstrate how to implement a range of regression methods and a Bayesian MCMC method. These are demosntrated for a variety of geoscience type applications, e.g. fitting an iscochron to isotope data to estimate an age, fitting a simple spherical object gravity model to observed Bouguer gravity anomaly data from the Isle of Mull in Scotland, and estimating parameters for a simple continental geotherm model based on PT estimates derived from mantle xenolith geochemistry. Various other routine housekeeping (e.g. reading and writing data files) and plotting techniques (using `Matplotlib` routines) are also illustrated.

A minimal example is fitting a simple linear model, i.e. a straight line, ![formula](https://render.githubusercontent.com/render/math?math=y=mx%2Bc)
, to some set of measurements of **y** (commonly called the dependent variable or response variable) for a given range of **x** values (commonly called the predicter variable or independent variable), to estimate the slope, _m_, and intercept _c_, of the line.

A routine method for achieving this is Ordinary Least Squares regression (OLS). The routine in the scipy package that implements this is `scipy.stats.linregress`. OLS is quick and straightforward, but does not take account of the magnitude of measurement uncertainties on _x_ or _y_ values. Orthogonal Direction Regression (ODR) enables measurement errors in both variables to be accounted for, and is particularly appropropriate if the measured data includes outliers with large errors.

An alternative to using regression techniques to estimating model parameters is to use a Bayesian approach and a Markov Chain Monte Carlo sampling strategy.

![pyMC3_Figure_3](https://user-images.githubusercontent.com/5646482/79071016-2b055400-7cd1-11ea-8228-e54777c30753.png)

An advantage of the Bayesian MCMC technique is that you can treat both the model parameters and the observed data as uncertain, and estimate their likely values (credible intervals) and the posterior probability distributions. This can be implemented in python using the `pyMC3` package.

![pyMC3_Figure_1](https://user-images.githubusercontent.com/5646482/79071026-3193cb80-7cd1-11ea-87eb-4ca1488b3fb0.png)
![pyMC3_Figure_2](https://user-images.githubusercontent.com/5646482/79071020-2e004480-7cd1-11ea-97d1-d5c263812f36.png)







