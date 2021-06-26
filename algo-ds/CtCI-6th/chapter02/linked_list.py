from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printLinkedList(node: ListNode):
    while True:
        print(node.val, end="")
        if node.next == None:
            break
        print("->", end="")
        node = node.next

def createLinkedList(arr: List) -> ListNode:
    head = tail = ListNode(val=arr[0])

    for i in range(1, len(arr)):
        node = ListNode(val=arr[i])
        tail.next = node
        tail = tail.next

    return head


if __name__ == "__main__":
    arr = [1, 4, 5, 2, 6, 10]
    print("arr = ", arr)
    node = createdLinkedList(arr)
    printLinkedList(node)

