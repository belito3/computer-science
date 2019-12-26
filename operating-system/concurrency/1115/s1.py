import threading

# s1: only event
# s2: only lock
# s2: condition with lock
# s3: semaphore
# ...
# sn: go routine use channel. too ez


class FooBar:
    def __init__(self, n):
        self.n = n
        self.event1 = threading.Event()
        self.event2 = threading.Event()
        self.event2.set()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.event2.wait()
            self.event2.clear()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.event1.set()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.event1.wait()
            self.event1.clear()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.event2.set()


n = 5
foo_bar = FooBar(n)


def print_foo():
    print("foo")


def print_bar():
    print("bar")


t1 = threading.Thread(target=foo_bar.foo, args=(print_foo,))
t2 = threading.Thread(target=foo_bar.bar, args=(print_bar,))

t1.start()
t2.start()

t1.join()
t2.join()
