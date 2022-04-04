import multiprocessing as mp
import time

def job(a):
    print(f"process {a} step 1")
    time.sleep(0.5)
    print(f"process {a} step 2")

if __name__ == '__main__':
    pool = mp.Pool(processes=5)
    for j in range(1,10):
        pool.apply_async(job,args=[j])
    pool.close()
    pool.join()