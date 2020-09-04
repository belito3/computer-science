# import threading

# class FooBar:
#     def __init__(self, n):
#         self.n = n

#     def foo(self, printFoo: 'Callable[[], None]') -> None:
#         for i in range(self.n):
#             # printFoo() outputs "foo". Do not change or remove this line.
#             printFoo()

#     def bar(self, printBar: 'Callable[[], None]') -> None:
#         for i in range(self.n):
#             # printBar() outputs "bar". Do not change or remove this line.
#             printBar()

# n = 5

# foo_bar = FooBar(n)


# def print_foo():
#     print("foo")


# def print_bar():
#     print("bar")


# t1 = threading.Thread(target=foo_bar.foo, args=(print_foo,))
# t2 = threading.Thread(target=foo_bar.bar, args=(print_bar,))

# t1.start()
# t2.start()

# t1.join()
# t2.join()


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
        # 1. Khởi tạo lock: foo_lock và bar_lock đều ở trạng thái unlocked
        self.foo_lock = threading.Lock()
        self.bar_lock = threading.Lock()
        # 2. Call acquire() --> khóa bar_lock lại, trạng thái của bar_lock là locked
        self.bar_lock.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            # 3.1.1 Trạng thái foo_lock đang là unlocked, code được thực thi tiếp 
            # sau đó chuyển trạng thái foor_lock sang locked
            self.foo_lock.acquire()
            # 3.2. printFoo được thực thi
            printFoo()  # Critical Section
            # 3.3. release bar_lock: chuyển trạng thái bar_lock sang unlocked -> đi đến bước 3.4
            self.bar_lock.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            # 3.1.2 Trạng thái bar_lock đang là locked, block thực thi cho đến khi bar_lock call release()
            self.bar_lock.acquire()
            # 3.4 bar_lock ở trạng thái unlocked 
            # printBar được thực thi và chuyển trạng thái bar_lock sang locked
            printBar() # Critical Section
            # 3.5. release foo_lock: chuyển trạng thái foo_lock sang unlocked -> đi đến bước 3.1.1
            self.foo_lock.release()


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
