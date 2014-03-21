#!/usr/bin/python3

import numpy as np
A=np.array([[1,2],[3,4]])
b=np.array([5,6])
x=np.linalg.solve(A,b)
print(x)
