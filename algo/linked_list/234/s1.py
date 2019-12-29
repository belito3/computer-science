from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        
        if head.next is None:
            return True
        
        l = []
        while head is not None:
            l.append(head.val)
            head = head.next

        length = len(l)
        for i in range(int(length/2)):
            if l[i] != l[length - i - 1]:
                return False

        return True 
    
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

l = create_linked_list([1])
s = Solution()

print(s.isPalindrome(l))

