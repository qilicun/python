#!/usr/bin/env python
import numpy as np
from scipy.optimize import leastsq
import pylab as pl

def fun(x, p):
	a, b = p
	return a*x + b

def residuals(p, x, y):
	return fun(x, p) - y

x1 = np.array([1, 2, 3, 4, 5, 6], dtype=float)
y1 = np.array([3, 5, 7, 9, 11, 13], dtype=float)

p0 = [1, 1]
r = leastsq(residuals, p0, args=(x1, y1))

print(r[0])

pl.figure(1)
pl.plot(x1, y1, label="true data")
pl.plot(x1, fun(x1, r[0]), label="fit data")
pl.legend()
pl.show()
