#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/22 9:28
# @Author  : caelansar
# @Site    : 
# @File    : create_thread1.py
# @Software: PyCharm

import threading
import time
def func():
    print('currrent thread:{}'.format(threading.current_thread().name))
    time.sleep(2)
    print('thread {} end'.format(threading.current_thread().name))
if __name__ == '__main__':
    print('main thread {} '.format(threading.current_thread().name))
    t1 = threading.Thread(target=func,name='t1')
    t1.setDaemon(True)# 设置t1线程为守护线程
    t2 = threading.Thread(target=func,name='t2')
    t1.start()
    t2.start()
    print('end')# 打印出这句话时主线程还未结束，因为t2是非守护线程，程序会等待非守护线程结束后才退出

