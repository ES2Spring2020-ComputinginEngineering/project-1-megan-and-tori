
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
path = "/Users/megan/Documents/GitHub/project-1-megan-and-tori"
os.chdir(path)


fin = open('test data L1.csv',"r")
line = fin.readline()
print(line)

timez = []
x_accel = []
y_accel = []
z_accel = []
for ln in fin: #putting data into 4 lists
    temp = ln.split(',')
    timez.append(temp[0])
    x_accel.append(temp[1])
    y_accel.append(temp[2])
    z_accel.append(temp[3])

# Plot waveforms and their peaks
plt.subplot(3,1,1)
plt.plot(timez, x_accel, 'r-')
plt.title('X-Acceleration by Time')
#left, right = plt.xlim()  # return the current xlim
#plt.xlim((left, right))   # set the xlim to left, right
#plt.xlim(left, right)     # set the xlim to left, right
#plt.xlim(right=10)  # adjust the right leaving left unchanged
#plt.xlim(left=0)  # adjust the left leaving right unchanged
#bottom, top = plt.ylim()  # return the current xlim
#plt.ylim((bottom, top))   # set the xlim to left, right
#plt.ylim(bottom, top)     # set the xlim to left, right
#plt.ylim(top=1400)  # adjust the right leaving left unchanged
#plt.ylim(bottom=700)  # adjust the left leaving right unchanged
plt.plot([-2, 0, 2, 4, 6, 8, 10, 12], [700, 800, 900, 1000, 1100, 1200, 1300, 1400])


#plt.subplot(3,1,2)
#plt.plot(timez, y_accel, 'r-')
#plt.title('Y-Acceleration by Time')
#
#plt.subplot(3,1,3)
#plt.plot(timez, z_accel, 'r-')
#plt.title('Z_Acceleration by Time')


plt.tight_layout()
plt.show()

time = np.arange(1,15,0.1) # create array with start, stop, and step size (similar concept to indices for list slicing)
y = np.cos(time)

# don't worry too much about this, but I'm adding random noise to the sine wave
noise = 0.3 * (np.random.rand(time.size) - 0.5)
y_noisy = y + noise



# Apply median filter to both original and noisy wave
y_filt = sig.medfilt(y)
y_noisy_filt = sig.medfilt(y_noisy)

# Find peaks of all waves
y_pks, _ = sig.find_peaks(y)
y_noisy_pks, _ = sig.find_peaks(y_noisy)
y_filt_pks, _ = sig.find_peaks(y_filt)
y_noisy_filt_pks, _ = sig.find_peaks(y_noisy_filt)


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