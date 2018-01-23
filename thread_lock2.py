#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/23 16:49
# @Author  : caelansar
# @Site    : 
# @File    : thread_lock2.py
# @Software: PyCharm
import threading

balance = 0

def changebalance(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(1000000):
        try:
            # 添加锁
            lock.acquire()
            changebalance(n)
        finally:
            # 释放锁
            lock.release()

if __name__ == '__main__':
    lock = threading.Lock()

    t1 = threading.Thread(target=run_thread, args=(666,))
    t2 = threading.Thread(target=run_thread, args=(233,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)
    '''
    当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止。
    获得锁的线程用完后一定要释放锁，否则等待锁的线程将永远等待下去，成为死线程。通过try...finally来确保锁一定会被释放。
    '''
