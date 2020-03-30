# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import math
import matplotlib.pyplot as plt

def period(L):
    g = 9.81
    T = 2*math.pi*(math.sqrt(L/g))
    periods.append(round(T,4))
    return periods

lengths = np.array([0.2731, 0.3175, 0.3810, 0.4191, 0.4826])
periods = []

for i in lengths:
    period(i)


#hold = []
#for i in range(len(lengths)):
#    hold.append(period(lengths[i]))
#    
#print(hold)
#
#
#plt.plot(lengths, hold, 'cd-')
#plt.xlabel("Lengths (meters)")
#plt.ylabel("Periods (seconds)")
#plt.show()
#plt.figure(figsize = (16,9))

print(periods)

plt.figure(1)
plt.plot(lengths, periods)
plt.show

