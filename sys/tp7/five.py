# -*- coding: utf-8 -*-
import signal as sig


def handling(num, frame):
	if numberGiven:
		print "congrats!"
	else:
		print "game over!"


sig.signal(sig.SIGALRM, handling)

N = 3
sig.alarm(N)

numberGiven = False
print "give me a number in the three next seconds"
nb = input()
numberGiven = True

while(True):
	pass


