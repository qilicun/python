#from scitools.std import *
import matplotlib.pyplot as plt
import numpy as np
import time, glob, os

def f(x, m, s):
    return (1.0/(np.sqrt(2*np.pi)*s))*np.exp(-0.5*((x-m)/s)**2)

m = 0
s_max = 2
s_min = 0.2
x = np.linspace(m -3*s_max, m + 3*s_max, 1000)
y1 = f(x, 0, 0.2)
y2 = f(x, 0, 1)
y3 = f(x, 0, 2)
plt.plot(x, y1, x, y2, x, y3)
plt.legend(('s=0.2', 's=1', 's=2'))
plt.savefig('tmp.eps')
plt.show()
