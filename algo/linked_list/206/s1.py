class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reserveList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head    
        
        while curr is not None:
            tmp = curr.next
            curr.next = prev
            prev = curr 
            curr = tmp
        return prev

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
l = create_linked_list([])

print_linked_list(s.reserveList(l))
