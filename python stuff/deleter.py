import os
from send2trash import send2trash as die
 
dir = os.path.dirname(os.path.realpath(__file__))
for f in os.listdir(dir):
    if f!="deleter.py":
        die(f)
        print(f, "sent to trash")
input("End me: ")
