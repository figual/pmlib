import pexpect
#import getpass
import time
from datetime import datetime

child = pexpect.spawn('ssh -l apc apc.act.uji.es')
print "ssh session login successful"
#s.sendline('yes')
#s.prompt()
child.expect(".* password:")
#child.expect("password:")
child.sendline ('apc')
child.expect('.*>')
#f=open('resultados.txt', 'w')
#i=0
#t1=datetime.fromtimestamp(time.time())
while(1):
        child.sendline ('olReading all power')  # run a command
        child.expect('apc>')
       # t2=datetime.fromtimestamp(time.time())
       # i=i+1
       # f.write("iteracion "+str(i)+"\n")
       # print "iteracion "+str(i)
       # f.write("hora: "+ str(t2)+"\n")
       # print "hora: "+ str(t2)
       # f.write("diferencia con anterior muestra: " + str(t2-t1)+"\n")
       # print "diferencia con anterior muestra: " + str(t2-t1)
      #  t1=t2
 #       print child.before         # print everything before the prompt.
        lista=child.before.split('\r\n')#.split(':')[2]
	power= [0]*24


        for l in lista:
  	            if l.find("Outlet") != -1:
                        id_, out_id, sample= l.split(":")
                        power[int(id_)-1]= float(sample.strip().split(" ")[0])
	#print lista
	print power
         #print valores
f.close()

