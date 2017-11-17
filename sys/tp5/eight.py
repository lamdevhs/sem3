import os
import time

print("let's make some clocks")

for i in range(10):
	lastClock = os.fork()
	if lastClock == 0:
		os.execlp("/usr/bin/xclock", "xclock")
	else:
		print("i made one clock!")

time.sleep(1)
print("i wanna kill time!")


def isInt(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

proc = "/proc"
subdirs = os.listdir(proc)
for pid in subdirs:
	if not isInt(pid):
		continue
	comm = proc + "/" + pid + "/comm"
	fd = open(comm, "r")
	name = fd.readline()
	fd.close()
	if "xclock" in name:
		os.kill(int(pid), 9)
		print("one clock killed!")
	
print("all clocks killed B)")
