class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, val) -> None:
        return self.data.append(val)

    def pop(self) -> int:
        val = self.data.pop()
        return val

    def peek(self) -> int:
        return self.data[-1]
        
    def is_empty(self) -> bool:
        return len(self.data) == 0

    def __len__(self) -> int:
        return len(self.data)


def sort_stack(s1: Stack):
    # Time: best case O(n). Worst case O(n*2)
    # Space: O(n)

    s2 = Stack()
    
    # Make stack2 is decreasing order from top
    while not s1.is_empty():
        val = s1.pop()

        while not s2.is_empty() and  s2.peek() > val:
            x = s2.pop()
            s1.push(x)

        s2.push(val)

    # Push item from stack2 to stack 1 
    while not s2.is_empty():
        val = s2.pop()
        s1.push(val)



if __name__ == "__main__":
    arr = [1, 4, 4, 3, 2, 5]
    
    s = Stack()
    for i in arr:
        s.push(i)
    print(f"stack: {s.data}")

    sort_stack(s)
    print(f"after sort: {s.data}")


