from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        r = self.reverse(head)
        s = i = 0
        print_linked_list(r)
        while r is not None:
            s += r.val * (2**i)
            r = r.next
            i += 1

        return s

    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr is not None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev

def create_linked_list(l: List) -> ListNode:
    dummy = current = ListNode(None)
    for val in l:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def print_linked_list(head: ListNode) -> None:
    if head is None:
        print(" ")
        return

    while head is not None:
        print(head.val, end="->")
        head = head.next
    print(" ")

l = create_linked_list([1,0,1])

s = Solution()
print(s.getDecimalValue(l))
