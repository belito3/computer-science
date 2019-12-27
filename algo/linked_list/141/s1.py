from typing import List

class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    def hasCycle2(self, head: ListNode) -> bool:
        pass

    # Solution 1: hash table
    # Time: O(N). Space: O(1)
    def hasCycle1(self, head: ListNode) -> bool:
        s = set()
        curr = head
        while curr is not None:
            if curr in s:
                return True
            else:
                s.add(curr)
                curr = curr.next
        return False

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

l = create_linked_list([1, 2, 3, 1, 2, 3])
s = Solution()

print(s.hasCycle(l))

l.next.next.next.next = l.next

print(s.hasCycle(l))
