from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # solution 1: interative
    # solution 2: hash table
    # Time: O(N)
    # Space: O(1)
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = curr = ListNode(None)
        dummy.next = head 
        
        while (curr.next is not None and curr.next.next is not None):
            if curr.next.val == curr.next.next.val:
                dup = curr.next.next
                while dup.next is not None:
                    if dup.val == dup.next.val:
                        dup = dup.next
                    else: 
                        break
                curr.next = dup.next
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

l = create_linked_list([1, 2, 2, 3, 3])

s = Solution()

print_linked_list(s.deleteDuplicates(l))

