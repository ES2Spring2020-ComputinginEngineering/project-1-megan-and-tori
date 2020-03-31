#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 18:10:17 2020
@author: megan
"""

import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.signal as sig
import os
path = "C:/Users/Victoria/Documents/GitHub/project-1-megan-and-tori/Step 4"
os.chdir(path)

def period(count,list):
    for i in range(len(count)):
        if i+1 >= len(count):
            break
        else:
            diff = abs(count[i+1] - count[i])
            list.append(diff)
    return list
        
def avg(list):
    add = 0
    for i in list:
        add = add + i
    return add/(len(list))

def find_angle_from_horizontal(list):
    #due to our microbit orientation, the horizontal is dependent on y so all calculations will be based on y
    acc_x = float(list[1])
    acc_y = float(list[2])
    acc_z = float(list[3])
    top = acc_y 
    #the equation has the y acceleration on the top, and we are going to index a list with all the original values to find y accel
    #since the original list is [time, x accel, y accel, z accel], we index accordingly
    bottom = math.sqrt((acc_x)**2 +(acc_z)**2)
    tilt_angle = math.atan2(top, bottom)
    tiltY = (tilt_angle * 180) / math.pi
    theta.append(tiltY)
    #theta is initialized above the function call
    

fin = open('test data L2-a.csv',"r")

timez = []
x_accel = []
y_accel = []
z_accel = []
theta = []

for ln in fin: #putting data into 4 lists
    temp1 = ln.strip()
    temp = temp1.split(',')
    timez.append(float(temp[0]))
    x_accel.append(float(temp[1]))
    y_accel.append(float(temp[2]))
    z_accel.append(float(temp[3]))
    
    find_angle_from_horizontal(temp) 

fin.close()


# Apply median filter to all waves
x_filt = sig.medfilt(x_accel)
y_filt = sig.medfilt(y_accel)
z_filt = sig.medfilt(z_accel)
          
            
#Plot waves of accelerations vs time
plt.figure(1)
plt.plot(np.array(timez), np.array(x_filt,), 'r-')#, 'r-', np.array(timez[x_pks]), np.array(x_filt[x_pks]), 'b.')
plt.title('X Acceleration vs Time')

plt.figure(2)
plt.plot(np.array(timez), np.array(y_filt), 'g-')#, 'r-', np.array(timez[x_pks]), np.array(x_filt[x_pks]), 'b.')
plt.title('Y Acceleration vs Time')

plt.figure(3)
plt.plot(np.array(timez), np.array(z_filt), 'b-')#, 'r-', np.array(timez[x_pks]), np.array(x_filt[x_pks]), 'b.')
plt.title('Z Acceleration vs Time')

#Plots theta vs time
plt.figure(4)
plt.plot(np.array(timez), np.array(theta), 'r-')
plt.title('Theta vs Time')

plt.tight_layout()
plt.show()


# Find peaks of y wave since y is the direction of motion
#NOTE: height and distance varies based on data (and false peaks in data)
y_pks, _ = sig.find_peaks(y_filt, height = 140, distance = 20)


#Count the amount of y peaks
count_y = []
for j in y_pks:
        count_y.append(timez[j])

#Finds average period of y wave        
period_y = []
period(count_y, period_y)
print('The average y period is', end = ' ')
print(round(avg(period_y), 2))

    