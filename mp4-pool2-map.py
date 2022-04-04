import multiprocessing as mp
import time

def job(a):
    return a**100000

if __name__ == '__main__':
    n_process = 8
    pool = mp.Pool(processes=n_process)
    tic = time.time()
    a1 = pool.map(job,range(1000))
    pool.close()
    pool.join()
    toc = time.time()
    print(f"time {n_process} process {toc-tic}")
    tic = time.time()
    a2 = list(map(job,range(1000)))
    toc = time.time()
    print(f"time 1 process {toc-tic}")
    print(len(a1))
    