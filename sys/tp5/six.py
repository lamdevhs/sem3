import os
import time

res = os.fork()

if res == 0:
	n = 10
	print("i am luke and i must kill darth vader in " + str(n) + "s")
	time.sleep(n)
	print("lightsaber attack!")
	vader = os.getppid()
	os.kill(vader, 9)

else:
	while(True):
		time.sleep(1)
		print("i am darth vader")
