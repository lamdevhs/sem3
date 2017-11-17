import os

res = os.fork()
if res == 0:
	print("still same console")
	os.execlp("/home/nbayard/univ/sys/tp5/a.out", "test")
else:
	print("original")
	
	
