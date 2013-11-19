# -*- coding: utf-8 -*-

#======================================================================
# INADevice class
#======================================================================

import Device
import pexpect
import time

## A INA device description
#
class INADevice(Device.Device):

    ## Creates a INA device description and adds it to the devices
    ## dictionary
    #
    # @param [in] name           The device name (used for identification, must be unique)
    # @param [in] url            The url of this device
    # @param [in] max_frequency  The maximum sample frequency of the device
    #
    def __init__(self, name, url, max_frequency):
        self.n_lines= 4
        super(INADevice, self).__init__(name, url, max_frequency)
        #self.lines[0]= Line(0, "Main", 220, "Main line")
	fd = open("/sys/bus/i2c/drivers/INA231/4-0045/enable", "w", 1)
	fd.write( "1" )
	fd.close()
 
    ## Adds a INA line description to the device
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
    def add_line(self, number, name, url, computer, voltage, description=""):
        if self.lines.has_key(number):
            msg="there are at least two lines with the same name, '{0}', in device '{1}'.".format(number, self.name)
            raise SyntaxError, msg
        self.lines[number]=Device.INALine(number, name, url, computer, voltage, description)
        if computer:
            computer.add(self)

    ## Read function
    #
    #  Reads data from INADevice, pexpect package is needed in order to run
    #
    def read(self):
    ##  Recoge los datos de consumo leyendo el puerto correpondiente
    ##  Lee del dispositivo de medida DC de todos los canales        
        #child= pexpect.spawn("ssh -l %s %s" % (self.user, self.INAname), timeout=10)
        #child.expect(".* password:", timeout= 10)
        #child.sendline(self.password)
        #child.expect(".*>", timeout= 5)

	fds = [0] * self.n_lines

	for line in range( 0, self.n_lines ):
		fds[line] = open(self.lines[line].url, "r", 1)

        power= [0] * self.n_lines

        power       = [0] * len(self.lines)
        sample      = ["0"] * len(self.lines)

        while self.running:
            #select.select([fd], [], [])
	    for line in range( 0, self.n_lines ):
              sample[line] = fds[line].readline() #.strip(" \n\t\r;").split(',')[3:]
              fds[line].seek(0,0)
              fds[line].flush()
              #print "Sample -> ", sample
              #if len(sample) == 18:
              power[line] = float(sample[line])
  	    yield power

        #while self.running:        
            #ini= time.time()
            #child.sendline ("olReading all power")
            #child.expect("%s>" % (self.user), timeout= 5)
#
            #response= child.before.split("\r\n")
            #for l in response:
                #line= l.split(":")
                #if len(line) == 3:
                    #id_, out_id, sample= line
                    #power[int(id_)-1]= float(sample.strip().split(" ")[0])
            #yield power
#
            #sleep_time= 1 - (time.time() - ini)*0.7
            #if sleep_time > 0: time.sleep(sleep_time)
#
        #child.sendline("exit")

