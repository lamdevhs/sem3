import os
import time
import sys
import signal as si

time.sleep(1)

print "hello!"

time.sleep(1)

forking = os.fork()

if forking != 0:
	child = forking
	print "[p] child:", child
	time.sleep(10)
	print "[p] terminating child"
	os.kill(child, si.SIGTERM)
else:
	print "[c] child:", os.getpid()
	print "[c] parent:", os.getppid()
	while True:
		print "[c] hiya!"
		time.sleep(1)

