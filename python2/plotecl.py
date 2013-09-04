#!/usr/bin/env python

# import the eclipse python module
import ert.ecl.ecl as ecl
import matplotlib.pyplot as plot

# Documentation of ert.ecl:
# http://wiki.statoil.no/wiki/index.php/Res:ERT-Python
# http://ert.nr.no/wiki/index.php/Ert.ecl
# inline: pydoc ert.ecl


# How to plot eclipse data in python
#====================================================

# read the summary file (add correct path!)
sum = ecl.EclSum("/private/miliu/data/eclipse/eclipse_testset/sim/BASE/BASE")

# get the vectors form the summary file
days = sum.days
wopr = sum.get_values("WOPR:OP_1")
woprh = sum.get_values("WOPRH:OP_1")

# plot the first vector
plot.plot(days, wopr, 'bo')
# plot the historical vector
plot.plot(days, woprh, 'k-')
#set labels
plot.ylabel('WOPR')
plot.xlabel('days')

# make a png file 
plot.savefig("singleplot.png")

# How to make a plot with two sections
days = sum.days
wwct = sum.get_values("WWCT:OP_1")
wopr = sum.get_values("WOPR:OP_1")
woprh = sum.get_values("WOPRH:OP_1")

plot.figure(1)
plot.subplot(211)
plot.plot(days, wwct, 'ro')
plot.ylabel('WWCT')
plot.xlabel('days')

plot.subplot(212)
plot.plot(days, wopr, 'bo')
plot.plot(days, woprh, 'k-')
plot.ylabel('WOPR')
plot.xlabel('days')
 
plot.savefig("doupleplot.png")

