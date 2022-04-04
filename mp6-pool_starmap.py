import multiprocessing as mp
import time

def power(a,n):
    return a**n

if __name__ == '__main__':
    n_process = 4
    pool = mp.Pool(processes=n_process)
    tic = time.time()
    #a1 = pool.starmap( power, [[1,2],[2,2],[3,2],[4,2]])
    a1 = pool.starmap( power, zip(range(10),[2]*10))
    pool.close()
    pool.join()
    toc = time.time()
    print(f"time {n_process} process {toc-tic}")
    print(a1)