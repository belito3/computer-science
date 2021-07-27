class SetOfStack:
    """
    Heapq, two point....
    """
    def __init__(self):
        pass


class ResultFull:
    def __init__(self):
        self.is_full = False
        self.index = -1

class ResultEmpty:
    def __init__(self):
        self.is_empty = False
        self.index = -1

class SetOfStack1:
    """
    S1: Brute of force:
    TLE
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [[0] * self.capacity]
        self.sizes = [0]

    def push(self, value) -> None:
        rs = self.check_full()
        if rs.is_full:
            new_stack = [0] * self.capacity
            self.data.append(new_stack)
            self.sizes.append(0)
            rs.index = len(self.data) - 1

        self.push_at(rs.index, value)


    def pop(self) -> int:
        rs = self.check_empty()
        if rs.is_empty:
            return -1

        val = self.pop_at(rs.index)
        return val


    def peek(self) -> int:
        pass

    def pop_at(self, index: int) -> int:
        if (index > len(self.sizes) - 1) or (self.sizes[index] == 0):
            return -1
        top = self.sizes[index] - 1
        val = self.data[index][top]
        self.data[index][top] = 0
        self.sizes[index] -= 1
        return val

    def push_at(self, index: int, val: int) -> None:
        top = self.sizes[index]
        self.data[index][top] = val
        self.sizes[index] += 1
    
    def check_full(self) -> ResultFull:
        rs = ResultFull()
        for i in range(len(self.sizes)):
            if self.sizes[i] != self.capacity:
                rs.index = i
                return rs
        rs.is_full = True
        return rs

    def check_empty(self) -> ResultEmpty:
        rs = ResultEmpty()
        for i in range(len(self.sizes)-1, -1, -1):
            if self.sizes[i] != 0:
                rs.index = i
                return rs

        rs.is_empty = True
        return rs

class StackError(Exception):
    """"""
class StackIsFull(StackError):
    """"""

class StackISEmpty(StackError):
    """"""


if __name__ == "__main__":

    stack_size = 5
    stacks = SetOfStack(stack_size)
    
    for i in range(15):
        stacks.push(i)

    print(f"after push: {stacks.data}")

    print("pop: ", end="")
    for i in range(15):
        val = stacks.pop()
        print(f"{val}", end = " ")

    stack_size2 = 2
    s = SetOfStack(stack_size2)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    print()
    print(f"The stack are now: {s.data}")

    v = s.pop_at(0)
    print(f"Return {v}. The stack are now: {s.data}")
    s.push(20) 
    print(f"The stack are now: {s.data}")
    s.push(21)
    print(f"The stack are now: {s.data}")

    v = s.pop_at(0)
    print(f"Return {v}. The stack are now: {s.data}")

    v = s.pop_at(2)
    print(f"Return {v}. The stack are now: {s.data}")

    v = s.pop()
    print(f"Return {v}. The stack are now: {s.data}")
    v = s.pop()
    print(f"Return {v}. The stack are now: {s.data}")
    v = s.pop()
    print(f"Return {v}. The stack are now: {s.data}")

    v = s.pop()
    print(f"Return {v}. The stack are empty: {s.data}")
    v = s.pop()
    print(f"Return {v}. The stack are empty: {v}")








