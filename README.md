# python多线程

线程是进程的一部分，每个线程也有它自身的产生、存在和消亡的过程，多线程可以执行多个任务。任何进程会默认启动一个线程，该线程称为**主线程** (`MainThread`)，主线程又可以启动新的线程。

Python解释器执行代码时，有一个**GIL** (Global Interpreter Lock) 锁，任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，执行别的线程。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。

## 创建线程

创建新的线程有两种方法：

1. 直接创建threading.Thread类的对象，初始化时将可调用对象作为参数传入。
2. 通过继承Thread类，重写它的run方法。

## 线程池

Python中线程与进程使用的同一模块 multiprocessing。使用方法也基本相同，唯一不同的是，from multiprocessing import Pool这样导入的Pool表示的是进程池；from multiprocessing.dummy import Pool这样导入的Pool表示的是线程池。这样就可以实现线程里面的并发了。