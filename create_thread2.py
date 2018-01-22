#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/22 9:30
# @Author  : caelansar
# @Site    :
# @File    : create_thread1.py
# @Software: PyCharm

import threading
import time

class MyThread(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name
    def run(self):
        print('currrent thread:{}'.format(self.name))
        time.sleep(2)
        print('thread {} end'.format(self.name))

if __name__ == '__main__':
    t1 = MyThread('thread1')
    t2 = MyThread('thread2')
    t1.start()
    t2.start()

