import os

print("i am your father")

res = os.fork()

if res == 0:
	print("no! this is impossible!")
else:
	print("join me on the dark side, luke whose pid is " + str(res) + "!")
