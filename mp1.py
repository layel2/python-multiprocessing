import multiprocessing as mp
import time

def testFunc(name):
    print(f"{name} : Start")
    time.sleep(2)
    print(f"{name} : End")

def asd(*args):
    print('wsd')

if __name__ == '__main__':
    p = mp.Process(target=testFunc, args=['agent A'])
    p.start()
    p.join()
    print("END")