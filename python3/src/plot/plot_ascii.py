"""
Make plot of a curve in pure text format (ASCII).
Useful for adding plots in doc strings or other
program code.
"""
# This is the same example as in the scitools.aplotter doc string

import numpy as np
x = np.linspace(-2, 2, 81)
y = np.exp(-0.5*x**2)*np.cos(np.pi*x)
#from scitools.aplotter import plot
import matplotlib.pyplot as plt
plt.plot(x, y)
plt.show()
plt.plot(x, y, draw_axes=False)

plt.show()
# Plot symbols (the dot argument) at data points
plt.plot(x, y, plot_slope=False)

plt.show()
# Drop axis labels
plt.plot(x, y, plot_labels=False)

plt.show()
plt.plot(x, y, dot='o', plot_slope=False)

plt.show()
# Store plot in a string
p = plt.plot(x, y, output=str)
plt.show()
print p





