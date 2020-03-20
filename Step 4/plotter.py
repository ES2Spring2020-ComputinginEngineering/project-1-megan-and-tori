
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 18:10:17 2020

@author: megan
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig
import os
path = "/Users/megan/Documents/GitHub/project-1-megan-and-tori/Step 4"
os.chdir(path)


fin = open('test data 4.csv',"r")
line = fin.readline()
#print(line)

timez = []
x_accel = []
y_accel = []
z_accel = []
for ln in fin: #putting data into 4 lists
    temp = ln.split(',')
    timez.append(float(temp[0]))
    x_accel.append(float(temp[1]))
    y_accel.append(float(temp[2]))
    z_accel.append(float(temp[3]))

plt.figure(1)
# Plot waveforms and their peaks
plt.plot(timez, x_accel, 'r-')
plt.title('X-Acceleration by Time')

plt.figure(2)
plt.plot(timez, y_accel, 'b-')
plt.title('Y-Acceleration by Time')

plt.figure(3)
plt.plot(timez, z_accel, 'g-')
plt.title('Z_Acceleration by Time')

# Apply median filter to both original and noisy wave
x_filt = sig.medfilt(x_accel)
y_filt = sig.medfilt(y_accel)
z_filt = sig.medfilt(z_accel)

# Find peaks of all waves
x_pks, _ = sig.find_peaks(x_filt)
y_pks, _ = sig.find_peaks(y_accel)
z_pks, _ = sig.find_peaks(z_accel)


plt.tight_layout()
plt.show()

count = 0
for i in range(370):
    for j in range(21):
        if x_accel[i] == x_pks[j]:
            count += 1

 #Plot waveforms and their peaks
plt.figure(4)
plt.plot(timez, x_filt, 'r-') #, timez[x_pks], x_filt[x_pks], 'b.'
plt.plot(timez, x_pks, 'b.')
plt.title('Original')
#plt.subplot(2,2,2)
#plt.plot(time, y_noisy, 'r-', time[y_noisy_pks], y_noisy[y_noisy_pks], 'b.')
#plt.title('Noisy')
#
#plt.subplot(2,2,3)
#plt.plot(time, y_filt, 'r-', time[y_filt_pks], y_filt[y_filt_pks], 'b.')
#plt.title('Original Median Filtered')
#plt.subplot(2,2,4)
#plt.plot(time, y_noisy_filt,'r-', time[y_noisy_filt_pks], y_noisy_filt[y_noisy_filt_pks], 'b.')
#plt.title('Noisy Median Filtered')

plt.tight_layout()
plt.show()




time = np.arange(1,15,0.1) # create array with start, stop, and step size (similar concept to indices for list slicing)
y = np.cos(time)

# don't worry too much about this, but I'm adding random noise to the sine wave

#y_noisy = y + noise
#noise = 0.3 * (np.random.rand(time.size) - 0.5)


# Apply median filter to both original and noisy wave
#y_filt = sig.medfilt(y)
#y_noisy_filt = sig.medfilt(y_noisy)
#
## Find peaks of all waves
#y_pks, _ = sig.find_peaks(y)
#y_noisy_pks, _ = sig.find_peaks(y_noisy)
#y_filt_pks, _ = sig.find_peaks(y_filt)
#y_noisy_filt_pks, _ = sig.find_peaks(y_noisy_filt)


# Plot waveforms and their peaks
#plt.subplot(2,2,1)
#plt.plot(timez, x_accel, 'r-', time[y_pks], y[y_pks], 'b.')
#plt.title('Original')
#plt.subplot(2,2,2)
#plt.plot(time, y_noisy, 'r-', time[y_noisy_pks], y_noisy[y_noisy_pks], 'b.')
#plt.title('Noisy')
#
#plt.subplot(2,2,3)
#plt.plot(time, y_filt, 'r-', time[y_filt_pks], y_filt[y_filt_pks], 'b.')
#plt.title('Original Median Filtered')
#plt.subplot(2,2,4)
#plt.plot(time, y_noisy_filt,'r-', time[y_noisy_filt_pks], y_noisy_filt[y_noisy_filt_pks], 'b.')
#plt.title('Noisy Median Filtered')
#
#plt.tight_layout()
#plt.show()