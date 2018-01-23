#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/23 16:40
# @Author  : caelansar
# @Site    : 
# @File    : thread_lock.py
# @Software: PyCharm

import threading

balance = 0

def changebalance(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for _ in range(100000):
        changebalance(n)

if __name__ == '__main__':
    t1 = threading.Thread(target=run_thread, args=(666,))
    t2 = threading.Thread(target=run_thread, args=(233,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)
    '''
    两个线程执行过程中，存在同时访问 change_it 函数的时候，而 balance = balance - n 语句在CPU中是分开拆分开执行的 :
    先   balance-n 存入临时变量
    然后 balance = 临时变量
    这样当两条线程同时执行change_it 函数时就会发生一加一减的赋值或算数错误。
    '''