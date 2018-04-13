#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/13 13:13
# @Author  : long.zhang
# @Contact : long.zhang@opg.global
# @Site    : 
# @File    : test_mp.py
# @Software: PyCharm
# @Desc    :
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/6 14:06
# @Author  : long.zhang
# @Contact : long.zhang@opg.global
# @Site    :
# @File    : CaptureBase.py
# @Software: PyCharm
# @Desc    :
import time
import multiprocessing

# import Queue
# device_que=Queue.Queue()

def test_p(key,queue,lock):
    print 'test_p', id(queue)
    while queue.empty():
        print 'test_p queue is empty'
        time.sleep(15)
    else:
        print queue.qsize()
        with lock:
            x = queue.get()

        time.sleep(1500)
        print x
        queue.put(x)


def test_q(q,l):
    print l
    import time
    print 'test_q',id(q)
    while 1:
        while q.empty():
            print 'q is empty'
            q.put({"https": "27.29.46.179:27579"})
            q.put({"https": "140.237.115.252:20627"})
            q.put({"https": "175.14.79.188:20959"})
            q.put({"https": "106.111.41.212:18873"})

        else:
            print 'q is not empty'
        time.sleep(15)

def a():
    try:
        manager = multiprocessing.Manager()
        #lock and queue is inheritance
        lock = multiprocessing.Manager().Lock()
        queue = manager.Queue()
        pool = multiprocessing.Pool(processes=10)
        pool.apply_async(test_q, (queue, lock,))
        for key in range(100000):
            pool.apply_async(test_p, (key, queue, lock,))  # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去

        pool.close()

        pool.join()
    except Exception,e:
        print e
if __name__ == '__main__':
    a()

