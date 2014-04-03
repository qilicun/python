#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
image = np.random.rand(30,30)
plt.imshow(image, cmap=plt.cm.hot)
plt.colorbar()
plt.show()
