import threading
import time

class loopThread(threading.Thread):
    def __init__(self, event):
        super().__init__()
        self.stopped = event

    def run(self):
        while not self.stopped.wait(1):
            print(f"Running : \t{time.ctime(time.time())}")
        
if __name__ == '__main__':
    stopFlag = threading.Event()
    thread = loopThread(stopFlag)
    print(f"start : \t{time.ctime(time.time())}")
    thread.start()
    time.sleep(6)
    stopFlag.set()
    print(f"end : \t\t{time.ctime(time.time())}")