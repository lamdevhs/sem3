# -*- coding: utf-8 -*-
import signal as sig

N = 3

def handling(msg):
	def out(num, frame):
		print msg + str(num)
		sig.alarm(N)
	return out


sig.signal(sig.SIGALRM, handling("hiya everyone! "))

sig.alarm(N)

while(True):
	pass


