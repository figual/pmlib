# -*- coding: utf-8 -*-

#======================================================================
# PowerMeter daemon setting classes
#
# This module defines the classes and dictionaries used by settings.py
#======================================================================


## Dictionary of devices
devices={}

## Dictionary of computers
computers={}


## A computer description
#
class Computer(object):

    ## Creates a computer description and adds it to the computers
    ## dictionary
    #
    # @param [in] name  The name of the computer
    # @param [in] ip    The IP address of the computer
    #
    def __init__(self, name, ip):
        self.name=name
        self.ip=ip
        self.devices={}
        # Register the computer
        computers[name]=self
        
    ## Returns a string representation for this computer
    def __repr__(self):
        return "Computer {0} ({1}): {2} device(s)".format(self.name, self.ip, len(self.devices))

    ## Adds a device description to the computer
    #
    # @param [in] device  A device description object
    #
    def add(self, device):
        if not isinstance(device, Device):
            msg="the given device parameter is not a Device object"
            raise SyntaxError, msg
        self.devices[device.name]=device


## A DCMeter device description
#
class DCDevice(AttachedDevice):
    
    ## Creates a DC2Meter device description and adds it to the
    ## devices dictionary
    #
    # @param [in] name           The device name (used for identification, must be unique)
    # @param [in] computer       The computer the device is attached to
    # @param [in] url            The url of this device
    # @param [in] max_frequency  The maximum sample frequency of the device
    #
    def __init__(self, name, computer, url, max_frequency):
        super(DCDevice, self).__init__(name, computer, url, max_frequency)



## A DC2Meter device description
#
class DC2Device(AttachedDevice):
    
    ## Creates a DC2Meter device description and adds it to the
    ## devices dictionary
    #
    # @param [in] name           The device name (used for identification, must be unique)
    # @param [in] computer       The computer the device is attached to
    # @param [in] url            The url of this device
    # @param [in] max_frequency  The maximum sample frequency of the device
    #
    def __init__(self, name, computer, url, max_frequency):
        super(DC2Device, self).__init__(name, computer, url, max_frequency)



## A National Instruments device description
#
class NIDevice(AttachedDevice):
    
    ## Creates a National Instruments device description and adds it
    ## to the devices dictionary
    #
    # @param [in] name           The device name (used for identification, must be unique)
    # @param [in] computer       The computer the device is attached to
    # @param [in] url            The url of this device
    # @param [in] max_frequency  The maximum sample frequency of the device
    #
    def __init__(self, name, computer, url, max_frequency):
        super(NIDevice, self).__init__(name, computer, url, max_frequency)



## A WattsUp device description
#
class WattsUpDevice(AttachedDevice):
    
    ## Creates a WattsUp device description and adds it to the devices
    ## dictionary
    #
    # @param [in] name           The device name (used for identification, must be unique)
    # @param [in] computer       The computer the device is attached to
    # @param [in] url            The url of this device
    # @param [in] max_frequency  The maximum sample frequency of the device
    #
    def __init__(self, name, computer, url, max_frequency):
        super(WattsUpDevice, self).__init__(name, computer, url, max_frequency)

    ## Fake adding of line description to the device
    #
    #  The WattsUp Device does not have lines. This method avoids the
    #  base class method silently been called.
    #
    # @param [in] name        The line name (used for identification)
    # @param [in] voltage     The line voltage
    # @param [in] description A text description of the line
    #
    def add_line(self, name, voltage, description):
        msg="a WattsUp Device can not have lines"
        raise SyntaxError, msg



## A PDU device description
#
class PDUDevice(Device):
    
    ## Creates a PDU device description and adds it to the devices
    ## dictionary
    #
    # @param [in] name           The device name (used for identification, must be unique)
    # @param [in] url            The url of this device
    # @param [in] max_frequency  The maximum sample frequency of the device
    #
    def __init__(self, name, url, max_frequency):
        super(PDUDevice, self).__init__(name, url, max_frequency)


    ## Adds a pdu line description to the device
    #
    #  Before adding the given line description to the device, it
    #  checks that the name of the new line has not been used by a
    #  previously added line.
    #
    # @param [in] name        The line name (used for identification)
    # @param [in] computer    The computer the line is attached to
    # @param [in] voltage     The line voltage
    # @param [in] description An optional text description of the line
    #
    def add_line(self, name, computer, voltage, description=""):
        if self.lines.has_key(name):
            msg="there are at least two lines with the same name, '{0}', in device '{1}'.".format(name, self.name)
            raise SyntaxError, msg
        self.lines[name]=PDULine(name, computer, voltage, description)
        computer.add(self)
