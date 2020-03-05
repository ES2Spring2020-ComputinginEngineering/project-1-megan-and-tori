##################
# Megan and Tori
#################

import microbit as mb
import radio  # Needs to be imported separately
# Change the channel if other microbits are interfering. (Default=7)
radio.on()  # Turn on radio
radio.config(channel=14, length=100)

print('Program Started')
mb.display.show(mb.Image.HAPPY)

while not mb.button_b.is_pressed():  # wait for button B to be pressed to begin logging
    mb.sleep(10)

time0 = mb.running_time() #get the current running time
radio.send('start') # Send the word 'start' to start the receiver
mb.sleep(1000)
mb.display.show(mb.Image.HEART)  # Display Heart while logging


# Read and send accelerometer data repeatedly until button B is pressed again
while not mb.button_b.is_pressed():
    # Need to collect accelerometer and time measurements
    # Need to format into a single string
    # Send the string over the radio
    message = str(mb.running_time()-time0) + ', ' + str(mb.accelerometer.get_x()) + ', ' + str(mb.accelerometer.get_y()) + ', ' + str(mb.accelerometer.get_z())
    #print(message)
    radio.send(message)
    mb.sleep(10)



mb.display.show(mb.Image.SQUARE)  # Display Square when program ends