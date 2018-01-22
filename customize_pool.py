#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/22 9:40
# @Author  : caelansar
# @Site    :
# @File    : create_thread1.py
# @Software: PyCharm

# import threading
# import time
# from queue import Queue
#
# def task():
#     time.sleep(1)
#     return 666
#
# class Worker(threading.Thread):
#     def __init__(self,queue):
#         super().__init__()
#         self.q = queue
#         self.daemon = True
#         self.start()
#     def run(self):
#         while True:
#             f = self.q.get()
#             try:
#                 print('using {}.....tasks result {}'.format(self.name,f()))
#             except Exception as e:
#                 print('error: ',e)
#             finally:
#                 self.q.task_done()
# class ThreadPool():
#     def __init__(self,thread_num):
#         self.q = Queue(thread_num)
#         for i in range(thread_num):
#             Worker(self.q)
#
#     def add_task(self,f):
#         self.q.put(f)
#     def wait_complete(self):
#         self.q.join()
#
# if __name__ == '__main__':
#     pool = ThreadPool(4)
#     for i in range(8):
#         pool.add_task(task)
#
#     pool.wait_complete()

from queue import Queue
from threading import Thread
from multiprocessing import cpu_count
import time

class MyThreadPool():
    def __init__(self, threads=None):
        self.queue = Queue()
        if not threads:
            threads = cpu_count()
            # print(threads)
        for i in range(threads):
            # 生成threads个线程
            t = Thread(target=self.work, name='Thread-'+str(i), daemon=True)# 设置为守护线程，当主线程结束时，该线程池销毁
            print('create a thread {}'.format(t.name))
            t.start()
    def apply_async(self,task):
        # 在每一次put时会给一个内部数加一，表示收到一个任务
        self.queue.put(task)
    def join(self):
        # 阻塞，直到queue中的数据均被删除或者处理。为队列中的每一项都调用一次。
        self.queue.join()
        # 所有数据被get并不会解除 join 阻塞，只有全部数据都被处理完（task_done调用次数等于get次数）了才会 解除 join 阻塞。
    def close(self):
        pass

    def work(self):
        # 该方法传递到target参数内，是线程池内线程所做的工作
        while True:
            try:
                task = self.queue.get()
                print(task())
            finally:
                self.queue.task_done()# 把queue里面的内部数减一

def task():
    time.sleep(1)
    return 666

if __name__ == '__main__':
    threadpool = MyThreadPool()
    for i in range(8):
        threadpool.apply_async(task)
    threadpool.join()









