#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/23 21:07
# @Author  : caelansar
# @Site    : 
# @File    : thread_queue.py
# @Software: PyCharm
import random, threading, time
from queue import Queue

# Producer thread
class Producer(threading.Thread):
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.data = queue

    def run(self):
        for i in range(10):  # 随机产生10个数字 ，可以修改为任意大小
            randomnum = random.randint(1, 99)
            print("%s is producing %d to the queue!" % (self.getName(), randomnum))
            self.data.put(randomnum)
            time.sleep(1)
        print("%s: %s finished!" % (time.ctime(), self.getName()))

# Consumer thread
class Consumer_even(threading.Thread):
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.data = queue

    def run(self):
        while 1:
            try:
                val_even = self.data.get(1, 5)
                if val_even % 2 == 0:
                    print("%s is consuming. %d in the queue is consumed!" % (self.getName(), val_even))
                    time.sleep(2)
                else:
                    self.data.put(val_even)
                    time.sleep(2)
            except:  # 等待输入，超过5秒  抛异常
                print("%s: %s finished!" % (time.ctime(), self.getName()))
                break

class Consumer_odd(threading.Thread):
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.data = queue

    def run(self):
        while 1:
            try:
                val_odd = self.data.get(1, 5)
                if val_odd % 2 != 0:
                    print("%s is consuming. %d in the queue is consumed!" % (self.getName(), val_odd))
                    time.sleep(2)
                else:
                    self.data.put(val_odd)
                    time.sleep(2)
            except: # 等待输入，超过5秒  抛异常
                print("%s: %s finished!" % (time.ctime(), self.getName()))
                break

# Main thread
def main():
    queue = Queue()
    producer = Producer('Producer', queue)
    consumer_even = Consumer_even('Con_even.', queue)
    consumer_odd = Consumer_odd('Con_odd.', queue)
    producer.start()
    consumer_even.start()
    consumer_odd.start()
    producer.join()
    consumer_even.join()
    consumer_odd.join()
    print('All threads terminate!')


if __name__ == '__main__':
    main()