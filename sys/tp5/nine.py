import os
import time

print("let's make some clocks")

for i in range(10):
	lastClock = os.fork()
	if lastClock != 0:
		print("i made one clock! pid = " + str(lastClock))
		os.execlp("/usr/bin/xclock", "xclock")


print("i wanna kill time! one clock at a time!")


def isInt(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

proc = "/proc"

while(True):
	time.sleep(1)
	clockFound = False
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
			print("one clock found at pid = "+ pid +" and killed!")
			clockFound = True
			break
	if clockFound == False:
		print("no more clocks to kill, mission accomplished!")
		break
