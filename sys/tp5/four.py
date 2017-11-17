import time
import os

res = os.fork()

if res == 0:
	n = 10
	print("i am luke, and i'mma wait " + str(n) + " secs before eating my sandwich")
	time.sleep(n)
	print("i, luke, am eating my sandwich")
else:
	n = 5
	print("i am darth vader, and i'mma wait " + str(n) + " secs before eating my sandwich cuz i'm famished")
	time.sleep(n)
	print("i, darth vader, am eating my sandwitch")
