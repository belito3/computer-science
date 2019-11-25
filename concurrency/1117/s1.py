# Explanation: "HOHHHO", "OHHHHO", "HHOHOH", "HOHHOH", "OHHHOH", "HHOOHH", "HOHOHH" and "OHHOHH" are also valid answers.
import threading


class H2O:
    def __init__(self):
        self.__lock = threading.Lock()
        self.__nH = 0
        self.__nO = 0
        self.__releaseHydrogen = None
        self.__releaseOxygen = None

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        with self.__lock:        
            # releaseHydrogen() outputs "H". Do not change or remove this line.
            self.__releaseHydrogen = releaseHydrogen
            self.__nH += 1
            self.__output()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.__lock:
            # releaseOxygen() outputs "O". Do not change or remove this line.
            self.__releaseOxygen = releaseOxygen
            self.__nO += 1
            self.__output()
    
    def __output(self):
        while (self.__nH >= 2) & (self.__nO >= 1): # TODO func __output is wrapped by lock --> __nH and __nO is synchronized
            self.__nH -= 2
            self.__nO -= 1
            self.__releaseHydrogen()
            self.__releaseHydrogen()
            self.__releaseOxygen()
            
            
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
