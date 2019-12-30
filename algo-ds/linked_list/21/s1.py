class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        current = dummy = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                current.next = ListNode(l1.val)
                l1 = l1.next
            else:    
                current.next = ListNode(l2.val)
                l2 = l2.next
            current = current.next
        current.next = l1 or l2
        return dummy.next
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:        
        # TODO: solution use recursive
        current = None

        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val < l2.val:
            current = l1
            current.next = self.mergeTwoLists(l1.next, l2)
        else:
            current = l2
            current.next = self.mergeTwoLists(l1, l2.next)
        return current


        

def create_linked_list(arr):
    dymmy = current = ListNode(0)
    for i, _ in enumerate(arr):
        current.next = ListNode(arr[i])
        current = current.next 
    return dymmy.next

l1 = create_linked_list([2, 6, 3])
l2 = create_linked_list([5, 4, 4])

def print_linked_list(l):
    while l:
        print(l.val)
        l = l.next

s = Solution()
l3 = s.mergeTwoLists(l1, l2)
print_linked_list(l3)