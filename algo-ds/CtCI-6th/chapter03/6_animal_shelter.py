class Animal:
    def __init__(self, name: str = ""):
        self.name = name
        # Order is used as a sort of timestamp 
        self.order = 0

    
class Dog(Animal):
    def __init__(self, name: str = ""):
        super().__init__(name=name)

class Cat(Animal):
    def __init__(self, name: str = ""):
        super().__init__(name=name)


class Node:
    def __init__(self, val: Animal):
        self.val = val
        self.next = None

class ListNode:
    def __init__(self, head=None):
        self.head = head

    def add_last(self, node: Node):
        if self.head is None:
            self.head = node 
            return 

        head = self.head
        while head.next is not None:
            head = head.next
        head.next = node
    
    def peak(self) -> Node:
        return self.head


    def pop_head(self) -> Node:
        current = self.head

        if current is None:
            raise Exception("list node empty")
        self.head = self.head.next
        return current

                
    def size(self) -> int:
        size = 0
        head = self.head

        while head is not None:
            size += 1
            head = head.next


class AnimalQueue:
    def __init__(self):
        self.order = 0
        self.dogs = ListNode(None)
        self.cats = ListNode(None)

    def enqueue(self, a: Animal) -> None:
        a.order = self.order 
        self.order += 1

        if isinstance(a, Cat):
            self.cats.add_last(Node(a))
        else: # Dog
            self.dogs.add_last(Node(a))
            

    def dequeue_cat(self) -> Animal:
        node = self.cats.pop_head()
        return node.val

    def dequeue_dog(self) -> Animal:
        node = self.dogs.pop_head()
        return node.val

    def dequeue_any(self) -> Animal:
        if (self.dogs.peak() is None) and (self.cats.peak() is None):
            raise Exception("Queue is empty")

        if self.dogs.peak() is None:
            return self.cats.pop_head().val

        if self.cats.peak() is None:
            return self.dogs.pop_head().val

        cat = self.cats.peak()
        dog = self.dogs.peak()

        if cat.val.order < dog.val.order:
            return self.cats.pop_head().val

        return self.dogs.pop_head().val


if __name__ == "__main__":
    q = AnimalQueue()
    print("push to queue: cat1, cat2, dog1, dog2, cat3")
    q.enqueue(Cat("cat1"))
    q.enqueue(Cat("cat2"))
    q.enqueue(Dog("dog1"))
    q.enqueue(Dog("dog2"))
    q.enqueue(Cat("cat3"))

    print(f"dequeue_cat: {q.dequeue_cat().name}")
    print(f"dequeue_dog: {q.dequeue_dog().name}")
    print(f"dequeue_any: {q.dequeue_any().name}")
    print(f"dequeue_dog: {q.dequeue_dog().name}")
    print(f"dequeue_dog: {q.dequeue_dog().name}")


         
