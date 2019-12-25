from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head

        h1 = ListNode(None)
        h1.next = head
        
        curr = head
        prev = None
        for i in range(m - 1):            
            h1 = h1.next
            curr = curr.next

        h2 = curr 
        tmp = None
        while m <= n:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp   
            m += 1

        h2.next = tmp
        h1.next = prev
        return h1.next if h1.val is None else head

def create_linked_list(l: List) -> ListNode:
    dummy = current = ListNode(None)
    
    for val in l:
        current.next = ListNode(val)
        current = current.next

    return dummy.next

def print_linked_list(head: ListNode) -> None:
    if head is None:
        print(" ")

    while head is not None:
        print(head.val, end="->")
        head = head.next
    
    print(" ")


s = Solution()
l = create_linked_list([1, 2, 3, 4, 5])
print_linked_list(s.reverseBetween(l, 5, 5))
