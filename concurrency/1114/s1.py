import threading

# TODO: Solution use mutex


class Foo:
    def __init__(self):
        self.lock = threading.Lock()
        self.first_completed = threading.Condition(lock=self.lock)
        self.second_completed = threading.Condition(lock=self.lock)
        self.counter = 0

    def first(self, printFirst: 'Callable[[], None]') -> None:
        with self.lock:
            printFirst()
            self.counter += 1
            self.first_completed.notify_all()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.lock:
            while self.counter != 1:
                self.first_completed.wait()  # wait and release lock
            printSecond()
            self.counter += 1
            self.second_completed.notify_all()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.lock:
            while self.counter != 2:
                self.second_completed.wait()
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

