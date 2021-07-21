#!/usr/bin/python3
import time
import os
os.system("python src_index.py")
os.system("git add --all")
os.system("git commit -m updated"+time.strftime("%H:%M:%S"))
os.system("git push origin master")
