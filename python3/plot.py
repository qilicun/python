#!/usr/bin/env python
import numpy as np
import pylab as pl

t = np.linspace(0.1,10)  
a = 1.5
b = 2.5
z = a*t**b 
noisy_z = z + pl.randn(z.size)*10
pl.clf()
pl.plot(t,z)
pl.plot(t,noisy_z,'k.')
pl.show()
