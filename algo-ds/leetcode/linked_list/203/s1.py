from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = curr = ListNode(None)
        curr.next = head

        while curr.next is not None:
            if curr.next.val == val:
                curr.next = curr.next.next 
            else:
                curr = curr.next
        return dummy.next
        
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

l = create_linked_list([3,1,3,3,2,3])

s = Solution()

print_linked_list(s.removeElements(l, 3))
