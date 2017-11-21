# -*- coding: utf-8 -*-
import signal as sig

def handling(msg):
	def out(num, frame):
		print msg + str(num)
	return out


sig.signal(sig.SIGUSR1, handling("signal user 1 handler: "))
sig.signal(sig.SIGUSR2, handling("signal user 2 handler: "))
sig.signal(sig.SIGINT, sig.SIG_IGN)

while(True):
	pass


