#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/23 20:09
# @Author  : caelansar
# @Site    : 
# @File    : thread_condition.py
# @Software: PyCharm
import threading
import random
# class Thread_A(threading.Thread):
#     def __init__(self,cond_obj, name):
#         super().__init__(name=name)
#         self.cond = cond_obj
#
#     def run(self):
#         self.cond.acquire()
#         self.cond.wait(10)    # wait 10s 等待B的应答, 如果10s后B还没有应答则timeout
#         print(self.name, 'wait 10s')
#         self.cond.release()
#
#
# class Thread_B(threading.Thread):
#     def __init__(self,cond_obj, name):
#         super().__init__(name=name)
#         self.cond = cond_obj
#
#     def run(self):
#         self.cond.acquire()
#         self.cond.notify()
#         '''
#         开始应答A，A接收到应答后被唤醒并执行
#         调用这个方法将从等待池挑选一个线程并通知，收到通知的一个线程将自动调用
#         acquire()尝试获得锁定（进入锁定池）；其他线程仍然在等待池中。调用这个
#         方法不会释放锁定。使用前线程必须已获得锁定，否则将抛出异常。
#         '''
#         print(self.name, 'notify')
#         self.cond.release()
#
# cond = threading.Condition()  # 创建Condition实例
# t1 = Thread_A(cond, 't1')
# t2 = Thread_B(cond, 't2')
# t1.start()
# t2.start()
import time


class Producer(threading.Thread):
    def __init__(self,cond_obj, name):
        super().__init__(name=name)
        self.cond = cond_obj

    def run(self):
        while True:
            self.cond.acquire()
            if len(tasks)>5:
                print('...waiting consumer')
                self.cond.wait()
            else:
                r = random.random()
                tasks.append(r)
                print('{} produce a {}'.format(self.name,r))
                time.sleep(1)
                self.cond.notify()
                self.cond.release()

class Consumer(threading.Thread):
    def __init__(self,cond_obj, name):
        super().__init__(name=name)
        self.cond = cond_obj

    def run(self):
        while True:
            self.cond.acquire()
            if len(tasks) == 0:
                print('...waiting producer')
                self.cond.wait()
            else:
                r = tasks.pop()
                print('{} consum a {}'.format(self.name,r))
                time.sleep(1)
                self.cond.notify()
                self.cond.release()


if __name__ == '__main__':
    tasks = []
    cond = threading.Condition()
    p = Producer(cond,'producer')
    c = Consumer(cond,'consumer')
    p.start()
    c.start()