# -*- coding: utf-8 -*-
import signal as sig
import os
import time
import sys

myName = sys.argv[2]

def handling(num, frame):
	print myName + " received SIGUSR1, gets executed for 1 second. count remaining:", handling.count
	handling.count -= 1
	if handling.count == 0:
		print myName + "'s count is empty, exiting now"
		sys.exit()

handling.count = int(sys.argv[1])
myPID = os.getpid()
print "my name is " + myName + ", i must execute for " + str(handling.count) + "s. my pid is", myPID

sig.signal(sig.SIGUSR1, handling)

time.sleep(1)

while True:
	pass
