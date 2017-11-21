# -*- coding: utf-8 -*-
import signal as sig


def handling(num, frame):
	print("reception of signal number ", num)

sig.signal(sig.SIGUSR1, handling)

while(True):
	pass


