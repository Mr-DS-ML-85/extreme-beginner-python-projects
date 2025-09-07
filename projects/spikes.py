import time 
import sys

try:
    while True:
        for i in range (1,9):
            print(f"{'-'*(i * i)}")
            time.sleep(0.1)
        

        for i in range (8, 0, -1):
            print(f"{'-'*(i * i)}")
            time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()