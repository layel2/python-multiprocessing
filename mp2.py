import multiprocessing as mp

# def func2():
#     return 'eiei'
def func2(q):
    q.put('eiei')
    q.put('hello')


if __name__ == '__main__':
    # p = mp.Process(target=func2)
    q = mp.Queue()
    p = mp.Process(target=func2,args=[q])
    # a = p.start()
    # print(a)
    p.start()
    a = q.get()
    print(a)
    a2 = q.get()
    print(a2)
    