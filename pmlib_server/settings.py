#======================================================================
# PowerMeter daemon settings
#======================================================================

from daemon.devices import *
from daemon.modules import *

#----------------------------------------------------------------------
# General section
#----------------------------------------------------------------------

# IP and Port in which the daemon will be listening (default: 6526)
#IP="192.168.1.1"
IP="127.0.0.1"
PORT=6526

# Log file name (default: "/var/log/powermeter.log")
LOGFILENAME="log/powermeter.log"

#----------------------------------------------------------------------
# Computers section
#----------------------------------------------------------------------

odroid= Computer(name="odroid", ip="0.0.0.0")

INA=INADevice(name="ODROID", url="", max_frequency=10)
INA.add_line(number=0,  name="A15",  url="/sys/bus/i2c/drivers/INA231/4-0040/sensor_W", computer=odroid,  voltage=220, description="A15")
INA.add_line(number=1,  name="A7",  url="/sys/bus/i2c/drivers/INA231/4-0045/sensor_W", computer=odroid,  voltage=220, description="A7")
INA.add_line(number=2,  name="Memory",  url="/sys/bus/i2c/drivers/INA231/4-0041/sensor_W", computer=odroid,  voltage=220, description="Memory")
INA.add_line(number=3,  name="GPU",  url="/sys/bus/i2c/drivers/INA231/4-0044/sensor_W", computer=odroid,  voltage=220, description="GPU")

