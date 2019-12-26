# s1: event
# s2: no-lock
# s3: lock
# s4: semaphore
# s5: ...
# https://leetcode.com/problems/print-zero-even-odd/discuss/337499/5-Python-solutions-using-threading-(Barrier-Condition-Event-Lock-Semaphore)-with-explanation
import threading


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zero_event = threading.Event()
        self.even_event = threading.Event()
        self.odd_event = threading.Event()
        self.zero_event.set()

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            self.zero_event.wait()
            printNumber(0)
            self.zero_event.clear()
            if i & 1 == 0:
                self.odd_event.set()
            else:
                self.even_event.set()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.even_event.wait()
            printNumber(i)
            self.even_event.clear()
            self.zero_event.set()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.odd_event.wait()
            printNumber(i)
            self.odd_event.clear()
            self.zero_event.set()


f = ZeroEvenOdd(5)
t1 = threading.Thread(target=f.zero, args=(print,))
t2 = threading.Thread(target=f.even, args=(print,))
t3 = threading.Thread(target=f.odd, args=(print,))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
