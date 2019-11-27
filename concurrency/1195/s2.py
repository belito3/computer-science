import threading

# TODO: condition (wait with while true) # Chạy chưa đúng

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.cnt = 1
        self.conditon = threading.Condition()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            with self.conditon:
                while (self.cnt % 3 != 0) | (self.cnt % 5 == 0): # (self.cnt % 3 == 0) & (self.cnt % 5 != 0)
                    self.conditon.wait()                
                if self.cnt > self.n:
                    print("fizz break")
                    break
                printFizz()
                self.cnt += 1
                self.conditon.notify_all()                                        

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            with self.conditon:
                while (self.cnt % 5 != 0) | (self.cnt % 3 == 0): # (self.cnt % 5 == 0) & (self.cnt % 3 != 0)
                    self.conditon.wait()
                if self.cnt > self.n:
                    print("buzz break")
                    break
                printBuzz()
                self.cnt += 1
                self.conditon.notify_all()                    

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None: 
        while True:
            with self.conditon:
                while (self.cnt % 3 != 0) | (self.cnt % 5 != 0): # (self.cnt % 3 == 0) & (self.cnt % 5 == 0)
                    self.conditon.wait()
                if self.cnt > self.n:
                    print("fizzbuzz break")
                    break
                printFizzBuzz()
                self.cnt += 1
                self.conditon.notify_all()
                    

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            with self.conditon:
                while (self.cnt % 3 == 0) | (self.cnt % 5 == 0): # (self.cnt % 3 != 0) & (self.cnt % 5 != 0):
                    self.conditon.wait()  
                if self.cnt > self.n:
                    print("number break")
                    return
                printNumber(self.cnt)
                self.cnt += 1
                self.conditon.notify_all()
                    

fb = FizzBuzz(15)


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
