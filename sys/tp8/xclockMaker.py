import os
import time
import sys
import signal as si


def handleUSR1(num, frame):
	handleUSR1.count += 1
	print "received SIGUSR1", handleUSR1.count, "times"
	if handleUSR1.count >= 5:
		print "five counts of SIGUSR1, time to go!"
		sys.exit(0)

handleUSR1.count = 0

def handleUSR2(num, frame):
	forking = os.fork()
	if forking == 0:
		os.execlp("/usr/bin/xclock", "xclock")

si.signal(si.SIGUSR1, handleUSR1)
si.signal(si.SIGUSR2, handleUSR2)

while True:
	pass

