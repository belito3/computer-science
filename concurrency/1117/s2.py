import threading

# https://leetcode.com/problems/building-h2o/discuss/420871/Python-solution-with-two-semaphores-and-one-lock
class H2O:
    def __init__(self):
        pass

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()


def print_hydrogen():
    print('H')

def print_oxygen():
    print('O')

h2o = H2O()


def test(string):
    threads = []
    for s in string:
        if s == "H":
            thread = threading.Thread(target=h2o.hydrogen, args=(print_hydrogen,))
            threads.append(thread)
            thread.start()

        elif s == "O":
            thread = threading.Thread(target=h2o.oxygen, args=(print_oxygen,))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()
    

if __name__ == "__main__":
    test("OOHHHHHH0")