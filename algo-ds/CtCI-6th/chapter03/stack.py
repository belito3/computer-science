class Stack:
    def __init__(self):
        self.data = []

    def push(self, value) -> None:
        self.data.append(value)

    def pop(self) -> int:
        value = self.data.pop()
        return value

    def peek(self) -> int:
        value = self.data[-1]
        return value

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def __len__(self) -> int:
        return len(data)

