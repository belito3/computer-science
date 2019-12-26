import threading

# TODO: Dining Philosopher problem

n = 1 # n is the number of times each philosopher will call the function.

# output[i] = [a, b, c] (three integers)
# - a is the id of a philosopher.
# - b specifies the fork: {1 : left, 2 : right}.
# - c specifies the operation: {1 : pick, 2 : put, 3 : eat}.

[[4,2,1],[4,1,1],[0,1,1],[2,2,1],[2,1,1],
[2,0,3],[2,1,2],[2,2,2],[4,0,3],[4,1,2],
[0,2,1],[4,2,2],[3,2,1],[3,1,1],[0,0,3],
[0,1,2],[0,2,2],[1,2,1],[1,1,1],[3,0,3],
[3,1,2],[3,2,2],[1,0,3],[1,1,2],[1,2,2]]


class DiningPhilosophers:
    def __init__(self):
        self.__lock = [threading.Lock() for _ in range(5)]

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        
        first, second = (philosopher +4) % 5, philosopher % 5

        if philosopher & 1 == 0:
            left, right = first, second
        else:
            left, right = second, first

        with self.__lock[left]:
            with self.__lock[right]:
                pickLeftFork()
                pickRightFork()
                eat()
                putLeftFork()
                putRightFork()

