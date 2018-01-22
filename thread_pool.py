#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/22 9:33
# @Author  : caelansar
# @Site    :
# @File    : create_thread1.py
# @Software: PyCharm

from multiprocessing.dummy import Pool as ThreadPool
import time

def func(a):
    time.sleep(2)
    print(a)
if __name__ == '__main__':
    l = [1,2,3,4,5]
    t1 = time.time()
    pool = ThreadPool(5)
    pool.map(func,l)
    pool.close()
    pool.join()
    print('cost: {}s'.format(time.time()-t1))
