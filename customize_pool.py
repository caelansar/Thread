#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/22 9:40
# @Author  : caelansar
# @Site    :
# @File    : create_thread1.py
# @Software: PyCharm

import threading
import time
from queue import Queue

def task():
    time.sleep(1)
    return 666

class Worker(threading.Thread):
    def __init__(self,queue):
        super().__init__()
        self.q = queue
        self.daemon = True
        self.start()
    def run(self):
        while True:
            f = self.q.get()
            try:
                print('using {}.....tasks result {}'.format(self.name,f()))
            except Exception as e:
                print('error: ',e)
            finally:
                self.q.task_done()
class ThreadPool():
    def __init__(self,thread_num):
        self.q = Queue(thread_num)
        for i in range(thread_num):
            Worker(self.q)

    def add_task(self,f):
        self.q.put(f)
    def wait_complete(self):
        self.q.join()

if __name__ == '__main__':
    pool = ThreadPool(4)
    for i in range(8):
        pool.add_task(task)

    pool.wait_complete()


