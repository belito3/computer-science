from stack import Stack

class MyQueue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, val: int) -> None:
        # O(1)
        self.s1.push(val) 

    def pop(self) -> int:
        # Amortized O(1)
        if self.s1.is_empty() and self.s2.is_empty():
            raise Exception("Stack is Empty")

        if self.s2.is_empty():
            # move item from stack1 to stack 2
            self.move()

        val = self.s2.pop()
        return val

        
    def peek(self) -> int:
        # Amortized O(1)
        if self.s2.is_empty():
            self.move()
        val = self.s2.peek()
        return val

    def move(self) -> None:
        # O(n)
        # move item from stack1 to stack2
        while not self.s1.is_empty():
            val = self.s1.pop()
            self.s2.push(val)

    def empty(self) -> bool:
        # O(1)
        return self.s1.is_empty() and self.s2.is_empty()
    
if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    print("Push 1")
    q.push(1)
    print("push 1")
    v = q.peek()
    print(f"peek: {v}")
    v = q.pop()
    print(f"pop: {v}")
    print(f"empty: {q.empty()}")
    

