import threading


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.cnt = 1
        self.conditon = threading.Condition()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for _ in range(self.n):
            with self.conditon:
                if (self.cnt % 3 == 0) & (self.cnt % 5 != 0):
                    printFizz()
                    self.conditon.notify_all()
                else:
                    self.conditon.wait()
                self.cnt += 1

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for _ in range(self.n):
            with self.conditon:
                if (self.cnt % 5 == 0) & (self.cnt % 3 != 0):
                    printBuzz()
                    self.conditon.notify_all()
                else:
                    self.conditon.wait()
                self.cnt += 1

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for _ in range(self.n):
            with self.conditon:
                if self.cnt % 15 == 0:
                    printFizzBuzz()
                    self.conditon.notify_all()
                else:
                    self.conditon.wait()
                self.cnt += 1

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n):
            with self.conditon:
                if (self.cnt % 3 != 0) & (self.cnt % 5 != 0):
                    printNumber(self.cnt)
                    self.conditon.notify_all()
                else:
                    self.conditon.wait()
                self.cnt += 1


fb = FizzBuzz(6)


def print_fizz():
    print("fizz")


def print_buzz():
    print("buzz")


def print_fizzbuzz():
    print("fizzbuzz")


t1 = threading.Thread(target=fb.fizz, args=(print_fizz,))
t2 = threading.Thread(target=fb.buzz, args=(print_buzz,))
t3 = threading.Thread(target=fb.fizzbuzz, args=(print_fizzbuzz,))
t4 = threading.Thread(target=fb.number, args=(print,))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()
