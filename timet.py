import time

def countdown(sec):
    sec = int(sec)
    for i in range(sec):
        print(sec)
        sec -= 1
        time.sleep(1)
    
