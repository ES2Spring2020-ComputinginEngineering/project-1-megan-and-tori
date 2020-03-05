##################
# Megan and Tori
#################

import microbit as mb
import radio  # Needs to be imported separately


# Change the channel if other microbits are interfering. (Default=7)
radio.on()  # Turn on radio
radio.config(channel=14, length =100)

print('Program Started')
mb.display.show(mb.Image.HAPPY, delay=1000, clear=True)

fout=open('data', 'w')

# Wait for start message before beginning printing
incoming = ''
while not incoming == 'start':
    incoming = radio.receive()
print('start')


while True:
    incoming = radio.receive() # Read from radio
    # Incoming is string sent from logger
    # Need to parse it and reformat as a tuple for the MU plotter
    if incoming is not None: # message was received
        mb.display.show(mb.Image.HEART, delay=100, clear=True, wait=False)
#         for i in range(3):
#             incoming = incoming.replace(' ', '')
        #fout.write(incoming)
        cut = incoming.split(',')
        #putting in tuple
        thing0 = int(cut[0])/1000 #in seconds
        thing1 = int(cut[1])
        thing2 = int(cut[2])
        thing3 = int(cut[3])
        hold = (thing0, thing1, thing2, thing3)
        print(hold)
        mb.sleep(10)