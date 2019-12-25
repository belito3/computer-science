class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # solution 1: interative
    def reserveList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head    
        
        while curr is not None:
            tmp = curr.next
            curr.next = prev
            prev = curr 
            curr = tmp
        return prev

    # solution 2: recursive
    def reserveList2(self, head: ListNode) -> ListNode:
        if(head is None or head.next is None): 
            return head
        
        p = self.reserveList2(head.next)
        head.next.next = head
        head.next = None
        return p

def create_linked_list(l):
    dummy = current = ListNode(None)
    for val in l:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def print_linked_list(head):
    if head is None:
        print(" ")

    while head is not None:
        print(head.val, end="->")
        head = head.next 
    print(" ")


s = Solution()
# [1]
l = create_linked_list([1, 2, 2, 3, 4, 5])

print_linked_list(s.reserveList2(l))
