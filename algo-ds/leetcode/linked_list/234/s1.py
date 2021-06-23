from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # solution 2: split to two half ListNode, then compare
    # Time: O(N)
    # Space: O(...)
    def isPalindrome2(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True

        h2 = self.split(head)
        r = self.reverse(h2)

        while r is not None:
            if r.val != head.val:
                return False
            r = r.next
            head = head.next

        return True

    def split(self, head: ListNode) -> ListNode:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        h2 = slow.next
        slow.next = None
        return h2

    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr is not None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev

    # Solution 1: Use List instead.
    # Time: O(N)
    # Space: O(1)
    def isPalindrome1(self, head: ListNode) -> bool:
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

l = create_linked_list([])
s = Solution()

print(s.isPalindrome1(l))
print_linked_list(s.reverse(l))
