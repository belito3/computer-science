import threading

# s1: only event
# s2: only lock
# s3: semaphore
# s4: condition
# ...
# sn: go routine use channel. too ez


class FooBar:
    def __init__(self, n):
        self.n = n
        self.sem_foo = threading.Semaphore(1)
        self.sem_bar = threading.Semaphore(1)
        self.sem_bar.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.sem_foo.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.sem_bar.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.sem_bar.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.sem_foo.release()


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
