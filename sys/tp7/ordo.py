# -*- coding: utf-8 -*-
import signal as sig
import os
import time
import sys



pids = map(int, sys.argv[1:])

print "ordo started. pids are:", pids

def isDead(dirs):
	def _isDead(pid):
		return not str(pid) in dirs
	return _isDead

while True:
	dirs = os.listdir("/proc")
	deadOnes = filter(isDead(dirs), pids)
	print deadOnes
	if len(deadOnes) == len(pids):
		break
	for pid in pids:
		if not pid in deadOnes:
			print "sending USR1 to", pid
			os.kill(pid, sig.SIGUSR1)
			time.sleep(1)

print "all processes exited, ordo exiting"
