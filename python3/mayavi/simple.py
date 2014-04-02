#!/usr/bin/env python

import numpy as np

r, theta = np.mgrid[0:10, -np.pi:np.pi:10j]

x = r * np.cos(theta)
y = r * np.sin(theta)
z = np.sin(r) / r

from mayavi import mlab

mlab.mesh(x, y, z, colormap='gist_earth', extent=[0, 1, 0, 1, 0, 1])
mlab.mesh(x, y, z, extent=[0, 1, 0, 1, 0, 1], representation='wireframe', line_width=1, color=(0.5, 0.5, 0.5))
