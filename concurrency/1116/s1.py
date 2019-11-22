# s1: event
# s2: lock
# s3: semaphore
# s4: ...
# https://leetcode.com/problems/print-zero-even-odd/discuss/337499/5-Python-solutions-using-threading-(Barrier-Condition-Event-Lock-Semaphore)-with-explanation
import threading


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.cnt = 0
        self.zero_event = threading.Event()
        self.odd_even_event = threading.Event()
        self.zero_event.set()


    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        while self.cnt < self.n:
            self.zero_event.wait()
            printNumber(0)
            self.zero_event.clear()
            self.cnt += 1
            self.odd_even_event.set()
        
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        while self.cnt < self.n:
            self.odd_even_event.wait()
            if (self.cnt & 1) == 0: 
                printNumber(self.cnt)
                self.odd_even_event.clear()
                self.zero_event.set()
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        while self.cnt < self.n:  
            #print("aa")          
            self.odd_even_event.wait()
            if (self.cnt & 1) == 1:
                printNumber(self.cnt)
                self.odd_even_event.clear()
                self.zero_event.set()

f = ZeroEvenOdd(1)
t1 = threading.Thread(target=f.zero, args=(print,))
t2 = threading.Thread(target=f.even, args=(print,))
t3 = threading.Thread(target=f.odd, args=(print,))

t1.start()
t2.start()
t3.start()


t1.join()
t2.join()
t3.join()
