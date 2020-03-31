#Project 1 Part 5
#Numerical Simulation Model
#*****************************************
# YOUR NAME: Victoria Pontikes and Megan Houchin
# NUMBER OF HOURS TO COMPLETE: 2.5 hours
"""
Created on Sun Mar 22 14:03:04 2020

@author: Victoria
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.signal as sig

length = 0.3175

def update_system(acc,pos,vel,time1,time2):
    # position and velocity update below
    global length
    dt = time2-time1
    posNext = pos+vel*dt
    velNext = vel+acc*dt
    accNext = (-9.81/length)*math.sin(pos) 
    return posNext,velNext, accNext

def print_system(time,pos,vel):
    print("TIME:     ", time)
    print("POSITION: ", pos)
    print("VELOCITY: ", vel, "\n")

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


# initial conditions
pos = [-math.pi/6]
vel = [0]
acc = [0]
time = np.linspace(0,20,100000)


i = 1
while i < len(time):
    # update position and velocity using previous values and time step
    posNext, velNext, accNext = update_system(acc[i-1],pos[i-1],vel[i-1],time[i-1],time[i])
    pos.append(posNext)
    vel.append(velNext)
    acc.append(accNext)
    i += 1

fig, (axp,axv,axa) = plt.subplots(3, figsize=[10,8])
axp.plot(time,pos)
axv.plot(time,vel)
axa.plot(time,acc)
plt.show()

#finds peaks of position function
pos_pks, _ = sig.find_peaks(pos)

#counts amount of peaks in position wave
count_pos = []
for j in pos_pks:
        count_pos.append(time[j])

#finds average period of y wave        
period_pos = []
period(count_pos, period_pos)
print('The average y period is', end = ' ')
print(round(avg(period_pos), 2))
    