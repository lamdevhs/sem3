# -*- coding: utf-8 -*-
import signal as sig
import os
import time

def ping(pid, msg):
	def out(num, frame):
		print msg
		time.sleep(1)
		os.kill(pid, sig.SIGUSR1)
	return out
	

forking = os.fork()

if forking == 0:
	print "process child"
	p1 = os.getppid()
	sig.signal(sig.SIGUSR1, ping(p1, "ping (child)"))
else:
	time.sleep(1)
	print "process parent"
	p2 = forking
	sig.signal(sig.SIGUSR1, ping(p2, "pong (parent)"))
	os.kill(p2, sig.SIGUSR1)

while(True):
	pass


