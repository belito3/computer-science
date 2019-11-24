import threading


# TODO: Only apply start following order : t1 > t2 > t3
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        printNumber(0)

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        n = self.n
        for i in range(1, n):
            printNumber(i * 10)
        if n % 2 == 0:
            printNumber(n)

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        n = self.n
        if n % 2 == 1:
            printNumber(n)


f = ZeroEvenOdd(10)


t1 = threading.Thread(target=f.zero, args=(print,))
t2 = threading.Thread(target=f.even, args=(print,))
t3 = threading.Thread(target=f.odd, args=(print,))

t1.start()
t2.start()
t3.start()


t1.join()
t2.join()
t3.join()
