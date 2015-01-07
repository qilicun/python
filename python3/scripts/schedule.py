#!/bin/env python
import numpy as np
import read_line

def welspecs(inje_pos, file):
    file.write("\nwelspecs".upper()+"\n")
    inje = "'I'  'G' "+str(inje_pos) + "  1*  'WAT'  0.0  'STD'  'SHUT'  'NO' /"
    prod = "'P'  'G'   1  1   1*  'OIL'  0.0  'STD'  'SHUT'  'NO'  /"
    file.write(inje)
    file.write("\n")
    file.write(prod)
    file.write("\n/\n")

def compdat(inje_pos, file):
    file.write("\ncompdat".upper()+"\n")
    inje="'I'   "+str(inje_pos)+"   1   1   1 'OPEN'   0  .0   0.05 /"
    prod="'P'   1     1   1   1 'OPEN'   0  .0   0.05 /"
    file.write(inje)
    file.write("\n")
    file.write(prod)
    file.write("\n/\n")

def wconhist(orat, wrat, file):
    file.write("\nwconhist".upper()+"\n")
    prod="'P' 'OPEN' 'BHP' "+str(orat)+"  "+str(wrat)+"  4*  10  /"
    file.write(prod)
    file.write("\n/\n")

def wconinjh(wrat, bhp, file):
    file.write("\nwconinjh".upper()+"\n")
    item="'I' 'WAT' 'OPEN'   "+str(wrat)+"   " +str(bhp)+"   6* 'RATE'/"
    file.write(item)
    file.write("\n/\n")

def wpolymer(amount, file):
    file.write("\nwpolymer".upper()+"\n")
    item="I    " + str(amount) + "   0.0   /"
    file.write(item)
    file.write("\n/\n")

data = file("test.txt", 'a+')
input="interpretation_schedule.txt"
dm=read_line.read_to_dict(input)

injecting=np.array(dm["injecting"])
injecting=np.array(injecting).reshape(len(injecting)/5,5)
welspecs(dm["grid"][0], data)
compdat(dm["grid"][0], data)
wpolymer(float(dm["polymer"][0])/1e6,data)
data.write("\nTIME\n")

for i in range(len(injecting[:,0])):
    data.write(str(injecting[:,0][i]))
    data.write("\n")
    wconhist(injecting[:,2][i], injecting[:,2][i], data)
    wconinjh(injecting[:,1][i],float(dm["pressure"][0])+float(injecting[:,4][i]), data)
    j=float(injecting[:,0][i])
    if i != (len(injecting[:,0])-1):
        start=float(injecting[:,0][i])
        stop=float(injecting[:,0][i+1])
        n=int((stop-start)/0.2)
        for j in range(n-1):
            data.write(str(start+(j+1)*0.2)+"\n")
    else:
        data.write("\nEND\n")
