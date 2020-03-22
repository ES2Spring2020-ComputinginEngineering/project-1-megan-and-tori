# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import math
import matplotlib.pyplot as plt

#Create array with integers 0 to 100 using linspace
a = np.linspace(0,100)
#Replace all odd numbers in that array with -1

#Create array with multiples of 10 from 0 to 200

#Calculate the y = x^2 (use the prior array for x)

#Caculate period of a pendulumn swing (use x as length of pendulumn)

def period(L):
    g = 9.81
    T = 2*math.pi*(math.sqrt(L/g))
    return round(T, 4)

lengths = np.array([0.2731, 0.3175, 0.3810, 0.4191, 0.4826])

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

print(period(0.3175))



