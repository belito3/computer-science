import threading

# s1: event,
# s2: condition with lock
# s3: semaphore
# ...
# sn: go routine use channel. too ez
class FooBar:
    def __init__(self, n):
        self.n = n
        #self.lock = threading.Lock()
        self.foo_complete = threading.Condition()
        self.bar_complete = threading.Condition()
        self.cnt = 0

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.foo_complete.notify_all()
            self.bar_complete.wait()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.foo_complete.wait()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.bar_complete.notify_all()


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
