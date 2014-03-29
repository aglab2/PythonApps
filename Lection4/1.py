#нет настоящего параллельного программирования

from threading import Thread

def count(n):
    while n>0:
        n -= 1

count(10000000) # нет много поточность
count(10000000) 

#нет настоящей многопоточности
t1 = Thread(target=count, args=(1000000,))#кортеж из одного элемента, запятая чтобы был именно кортеж
t1.start()

t2 = Thread(target=count, args=(1000000,))
t2.start()
t1.join()#ожидание корректного завершения потоков
t2.join()


import logging
import time

logging.basicConfig(level=logging.DEBUG, format='(%(levelname)s) ((%(threadname)-10s) %(message)s')#логи

def worker():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')

def my_service():
    logging.debug('Starting')
    time.sleep(3)
    logging.debug('Exiting')
    
    
t = Thread(name = 'my_service1', target=worker)
t = Thread(name = 'my_service2', target=worker)
t = Thread(name = 'my_service3', target=my_service)


#демоны - сохранение потока
d = Thread(name='daemon', target=worker)
d.setDaemon(True)
d.start()#можно с join для завершения


class MyThread(Thread):
    def run(self):
        logging.debug('running')
        return

for i in range(5):
    t = MyThread()
    t.start()
    
class MyThreadWA(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None):
        Thread.__init__(self, group, target, name)
        self.args = args
        self.kwargs = kwargs
        return
    def run(self):
        print('hi')    
if __name__ = '__main__' #если вызов из интерпретатора
    pass

import argparse # парсить аргументы
import queue #очереди

dirq = queue.Queue()
dirq.put(seed)
dirq.join()
dirq.task_done()

try:#ловим exception
    pass
except Exception as e, KeyError as k:
    if e.errno == errno.EACCES:
        pass
    raise e #поднять исключения

1 < x < 10 #можно так писать
x = 1 if y % 2 == 0 else 2#условное присваивание

eval('2+3') #выполнение

