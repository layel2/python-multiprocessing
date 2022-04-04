import threading
import time

def testFunc(name):
    print(f"Running : \t{time.ctime(time.time())}")

if __name__ == '__main__':
    x = threading.Timer(3,testFunc,args=['agent_1'])
    print(f"start : \t{time.ctime(time.time())}")
    x.start()
    time.sleep(5)
    print(f"end : \t\t{time.ctime(time.time())}")
    x.cancel()