import os

print("look at me! look at my pid, at my name! aren't they cool?")
dummy = input()
os.execlp("/usr/bin/xclock", "cool_xclock")
