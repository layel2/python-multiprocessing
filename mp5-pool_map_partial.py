import multiprocessing as mp
from functools import partial
import time

def power(a,n):
    return a**n

if __name__ == '__main__':
    n_process = 4
    pool = mp.Pool(processes=n_process)
    tic = time.time()
    a1 = pool.map( partial(power, n=2) ,range(10))
    pool.close()
    pool.join()
    toc = time.time()
    print(f"time {n_process} process {toc-tic}")
    print(a1)
    # tic = time.time()
    # a2 = list(map(job,range(1000)))
    # toc = time.time()
    # print(f"time 1 process {toc-tic}")
    # print(len(a1))
    