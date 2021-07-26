from stack import Stack

class StackMin(Stack):
    def __init__(self):
        super().__init__()
        self.min_stack = Stack()

    def push(self, value) -> None:
        super().push(value)
        # Update min
        if self.min_stack.is_empty() or (self.min_stack.peek() >= value):
            self.min_stack.push(value)

    def pop(self) -> int:
        value = super().pop()
        if value == self.min_stack.peek():
            self.min_stack.pop()

        return value

    def peek(self) -> int:
        return super().peek()

    def min(self) -> int:
        return self.min_stack.peek()

if __name__ == "__main__":
    input = [-2, 0, -3, 1]

    s = StackMin()
    for i in input:
        print(f"push {i}")
        s.push(i)
        m = s.min()
        print(f"min: {m}")

    s.pop()
    print("pop")
    m = s.min()
    print(f"min: {m}")
    s.pop()
    print("pop")
    m = s.min()
    print(f"min: {m}")



