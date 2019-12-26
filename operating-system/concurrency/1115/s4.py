import threading

# s1: only event
# s2: only lock
# s3: semaphore
# s4: condition TODO: ??? ko hieu
# ...
# sn: go routine use channel. too ez


class FooBar:
    def __init__(self, n):
        self.n = n
        self.trigger = 0
        self.lock = threading.Lock()
        self.foo_print = threading.Condition(self.lock)
        self.bar_print = threading.Condition(self.lock)

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            with self.lock:
                while self.trigger != 0:
                    self.bar_print.wait()   # khởi tạo khóa nội, đặt trạng thái là locked
                # printFoo() outputs "foo". Do not change or remove this line.
                printFoo()
                self.trigger = 1
                self.foo_print.notify_all()   # unlock internal lock. lần đầu chạy thì chưa có khóa này.

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            with self.lock:
                while self.trigger != 1:
                    self.foo_print.wait()
                # printBar() outputs "bar". Do not change or remove this line.
                printBar()
                self.trigger = 0
                self.bar_print.notify_all()


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
