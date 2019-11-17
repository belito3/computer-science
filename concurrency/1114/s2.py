import threading
import time

# TODO: Solution use Event, loop with event


class Foo:
    def __init__(self):
        self.event1 = threading.Event()
        self.event2 = threading.Event()
        # self.event3 = threading.Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        while True:
        # printFirst() outputs "first". Do not change or remove this line.
            printFirst()
            self.event1.set()
            self.event1.clear()
            time.sleep(3)

    def second(self, printSecond: 'Callable[[], None]') -> None:
        while True:
            self.event1.wait()
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.event2.set()
            self.event2.clear()
        # break

    def third(self, printThird: 'Callable[[], None]') -> None:
        while True:
            self.event2.wait()
            # printThird() outputs "third". Do not change or remove this line.
            printThird()
            #break


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
