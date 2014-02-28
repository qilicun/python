#!/usr/bin/env python

# 1-sample t-test
from scipy import stats

one_sample_data = [177.3, 182.7, 169.6, 176.3, 180.3, 179.4, 178.5, 177.2, 181.8, 176.5]

one_sample = stats.ttest_1samp(one_sample_data, 175.3)

print "The t-statistic is %.3f and the p-value is %.3f." % one_sample

# unpaired t-test

female = [63.8, 56.4, 55.2, 58.5, 64.0, 51.6, 54.6, 71.0]
male = [75.5, 83.9, 75.7, 72.5, 56.2, 73.4, 67.7, 87.9]
two_sample = stats.ttest_ind(male, female)
print "The t-statistic is %.3f and the p-value is %.3f." % two_sample

# assuming unequal population variances
two_sample_diff_var = stats.ttest_ind(male, female, equal_var=False)

print "If we assume unequal variances than the t-statistic is %.3f and the p-value is %.3f." % two_sample_diff_var

#Paried t-test
baseline = [67.2, 67.4, 71.5, 77.6, 86.0, 89.1, 59.5, 81.9, 105.5]
follow_up = [62.4, 64.6, 70.4, 62.6, 80.1, 73.2, 58.2, 71.0, 101.0]

paired_sample = stats.ttest_rel(baseline, follow_up)

print "The t-statistic is %.3f and the p-value is %.3f." % paired_sample
