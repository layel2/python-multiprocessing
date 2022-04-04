import threading
import time

def testFunc(name):
    print(f"{name} : Start\n")
    time.sleep(2)
    print(f"{name} : End\n")

if __name__ == '__main__':
    x = threading.Thread(target=testFunc, args=['agent A'])
    x2 = threading.Thread(target=testFunc, kwargs={'name':'agent B'})

    x.start()
    x2.start()
    x.join()
    x2.join()
    print("END")