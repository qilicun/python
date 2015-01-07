#!/usr/bin/env python

from scipy import misc
import numpy as np
import matplotlib.pyplot as plt

lena = misc.lena()

copy_lena = lena[30:-30, 30:-30]
y, x = np.ogrid[0:512,0:512]
centerx, centery = (256, 256)
mask = ((y - centery)**2 + (x - centerx)**2) > 230**2
lena[mask] = 0
plt.imshow(lena)
plt.imshow(lena, cmap=plt.cm.gray)
plt.show()
