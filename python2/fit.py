#!/usr/bin/env python
import numpy as np
from scipy.optimize import leastsq
import pylab as pl

def func(x, p):
    a, b, c, d = p
    return a + (b-a) / (1 + 10**((np.log10(c) -x)*d))

def residuals(p, x, y):
    return func(x, p) - y

x = [4, 20, 100, 500]
y = [54.1026704062992, 14.9198246004212, 13.1736075894627, 9.57978170987729]

pl.figure()
pl.plot(x, y, 'bo',label="true data")
p0 = [1, 1, 1, 1] 
plsq = leastsq(residuals, p0, args=(x, y))
print  plsq[0] 

pl.plot(x, func(x, plsq[0]), 'g+', label="fit data")
pl.legend()
pl.show()
