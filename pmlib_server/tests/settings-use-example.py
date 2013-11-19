# -*- coding: utf-8 -*-

#======================================================================
# PowerMeter daemon settings use example
#======================================================================

import settings

def header(txt):
    print "------------------------------------------------------------"
    print "{0:^60}".format(txt)
    print "------------------------------------------------------------"
    

## Shows the information given by the settings file
def main():

    # Show all the computers
    header("Computers")
    for computer in settings.computers.values():
        print computer
    print
    print

    # Show all the devices
    header("Devices")
    for device in settings.devices.values():
        print device
    print
    print
    
    # Access the devices of a given computer
    header("Devices in computer 'lorca'")
    for device in settings.computers['lorca'].devices.values():
        print device
    print
    print

    header("Devices in computer 'matserv'")
    for device in settings.computers['matserv'].devices.values():
        print device
    print
    print

    # Access to which computer a given device is attached to
    header("Computer to which device 'DCMeter' is attached")
    print settings.devices["DCMeter"].computer
    print
    print

    # Access the lines of a given device
    header("Lines in device 'DCMeter'")
    for line in settings.devices["DCMeter"].lines.values():
        print line
    print
    print

    header("Lines in device 'PDU'")
    for line in settings.devices["PDU"].lines.values():
        print line
    print
    print

    # Access individual properties of a given line of a given device
    header("Properties of line 'DC 12V' of device 'DCMeter'")
    line=settings.devices["DCMeter"].lines[0]
    print "Line name: {0}".format(line.name)
    print "Line voltage: {0}".format(line.voltage)
    print "Line description: '{0}'".format(line.description)
    print

    settings.devices["DCMeter"].run()
    print
    
if __name__=="__main__":
   main()
