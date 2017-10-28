from django.test import TestCase
import time
from multiprocessing.pool import Pool
import gevent
from  gevent import select, Greenlet
import random

#测试二
# start = time.time()
# tic = lambda : 'at %1.1f seconds' % (time.time() - start)

# def gr1():
#     # Busy waits for a second, but we don't want to stick around...
#     print('Gr1 Started Polling: ', tic())
#     select.select([], [], [], 1)
#     print('Gr1 Ended Polling: ', tic())
#
#
# def gr2():
#     # Busy waits for a second, but we don't want to stick around...
#     print('Gr2 Started Polling: ', tic())
#     select.select([], [], [], 3)
#     print('Gr2 Ended Polling: ', tic())
#
#
# def gr3():
#     print("Gr3 Hey lets do some stuff while the greenlets poll, at", tic())
#     gevent.sleep(1)
#
# gevent.joinall(
#     [
#         gevent.spawn(gr1),
#         gevent.spawn(gr2),
#         gevent.spawn(gr3),
#     ]
# )

#测试一
# def foo():
#     print('Running in foo')
#     gevent.sleep(0)
#     print('Explicit context switch to foo again')
#
#
# def bar():
#     print('Explicit context to bar')
#     gevent.sleep(0)
#     print('Implicit context switch back to bar')
#
#
# gevent.joinall([
#     gevent.spawn(foo),
#     gevent.spawn(bar),
# ])

#测试三
# def task(pid):
#     gevent.sleep(random.randint(0,2)* 0.001)
#     print('Task', pid, 'done')
#
# def synchronous():
#     for i in range(1, 10):
#         task(i)
#
# def asynchronous():
#     threads = [gevent.spawn(task, i) for i in range(1, 10)]
#     print(threads)
#     gevent.joinall(threads)
#
# print('Synchronoue : ')
# synchronous()
#
# print('Asynchronous :')
# asynchronous()

#测试四
# def echo(i):
#     time.sleep(0.001)
#     return i
#
# p = Pool(10)
# run1 = [a for a in p.imap_unordered(echo, range(10))]
# run2 = [a for a in p.imap_unordered(echo, range(10))]
# run3 = [a for a in p.imap_unordered(echo, range(10))]
# run4 = [a for a in p.imap_unordered(echo, range(10))]
#
# print(run1 == run2 == run3 == run4)

#c测试5
# def foo(message, n):
#     gevent.sleep(n)
#     print(message)
#
# thread1 = Greenlet.spawn(foo, 'Hello world', 1)
#
# thread2 = gevent.spawn(foo, 'I live !', 2)
#
# thread3 = gevent.spawn(lambda x : (x + 1), 2)
#
# threads = [thread1, thread2, thread3]
#
# gevent.joinall(threads)

# #测试6
# class MyGreenlet(Greenlet):
#     def __init__(self, message, n):
#         Greenlet.__init__(self)
#         self.message = message
#         self.n = n
#
#     def run(self):
#         print(self.message)
#         gevent.sleep(self.n)
#
# g = MyGreenlet("Hi there !", 2)
# g.run()