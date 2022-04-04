import threading
import time

def testFunc(name):
    print(f"{name} : Start")
    time.sleep(5)
    print(f"{name} : End")

if __name__ == '__main__':
    x_thread = []
    for i in range(10):
        x_thread.append(threading.Thread(target=testFunc, args=[f"Agent_{i}"]))

    for x in x_thread:
        x.start()

