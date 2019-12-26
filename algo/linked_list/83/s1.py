from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeDuplicates(self, head: ListNode) -> ListNode:
        val = None
        current = dummy = ListNode(None)
        current.next = head
 
        while current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                val = current.next.val
                current = current.next    
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

l = create_linked_list([])

s = Solution()

print_linked_list(s.removeDuplicates(l))
    
