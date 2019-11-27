import threading
import time
import random
from threading import current_thread
import queue
import collections

# Design Bounded Blocking Queue
# Tìm hiểu thêm về condition 
# https://medium.com/better-programming/synchronization-primitives-in-python-564f89fee732
class BoundedBlockingQueue:
    def __init__(self, capacity):
        self.__max_size = capacity
        self.__q = []
        self.__condition = threading.Condition()

    def enqueue(self, element):
        with self.__condition:
            if len(self.__q) == self.__max_size:
                self.__condition.wait()
            else:
                self.__q.insert(0, element)
                self.__condition.notify_all()

    def dequeue(self):
        with self.__condition:
            if len(self.__q) == 0:
                self.__condition.wait()
            else:
                self.__condition.notify_all()
                return self.__q.pop()                

    def size(self):
        with self.__condition:
            return len(self.__q)

def consumer_thread(q):
    while 1:
        item = q.dequeue()
        print("\n{0} consumed item {1}".format(current_thread().getName(), item))

def producer_thread(q, val):
    item = val
    while 1:
        time.sleep(0.1)
        q.enqueue(item)
        item += 1
        


if __name__ == "__main__":
    blocking_q = BoundedBlockingQueue(5)

    consumerThread1 = threading.Thread(target=consumer_thread, name="consumer-1", args=(blocking_q,))
    consumerThread2 = threading.Thread(target=consumer_thread, name="consumer-2", args=(blocking_q,))
    producerThread1 = threading.Thread(target=producer_thread, name="producer-1", args=(blocking_q, 1))
    #producerThread2 = threading.Thread(target=producer_thread, name="producer-2", args=(blocking_q, 100), daemon=True)

    consumerThread1.start()
    consumerThread2.start()
    producerThread1.start()
    #producerThread2.start()

    consumerThread1.join()
    consumerThread2.join()
    producerThread1.join()
    print("Main thread exiting")