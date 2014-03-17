#!/usr/bin/env python

import itertools as it
from scipy import stats

#x1 = [1, 2, 3, 4, 5]
#x2 = ['a', 'b', 'c', 'd', 'e']

female = [63.8, 56.4, 55.2, 58.5, 64.0, 51.6, 54.6, 71.0]
male = [75.5, 83.9, 75.7, 72.5, 56.2, 73.4, 67.7, 87.9]

#print list(it.combinations(x1, 3))
#print list(it.combinations(x2, 3))

for n in range(1,len(male)+1):
    for i in list(it.combinations(female,n)):
        for j in list(it.combinations(male,n)):
            two_sample = stats.ttest_ind(i, j)
            print ("The t-statistic is %.3f and the p-value is %.3f." % two_sample)
