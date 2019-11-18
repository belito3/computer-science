import threading

# Lock or semaphore
class Foo:
    def __init__(self):
        self.lock1 = threading.Lock()
        self.lock2 = threading.Lock()

        self.lock1.acquire()
        self.lock2.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.lock1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.lock1.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.lock2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.lock2.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()


foo = Foo()


def print_first():
    print("first")


def print_second():
    print("second")


def print_third():
    print("third")


t1 = threading.Thread(target=foo.first, args=(print_first,))
t2 = threading.Thread(target=foo.second, args=(print_second,))
t3 = threading.Thread(target=foo.third, args=(print_third,))

t3.start()
t1.start()
t2.start()

t3.join()
t1.join()
t2.join()
