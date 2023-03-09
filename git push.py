import os 
import time
value = input("Enter file name")

os.popen(f"git add {value}")
time.sleep(1)
os.popen("^C")
time.sleep(1)
os.popen("git commit -m 'changes'")
os.popen("^C")
time.sleep(1)
os.popen("git push")
time.sleep(5)
os.popen("^C")