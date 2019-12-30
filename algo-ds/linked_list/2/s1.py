# Definition for singly-linked list.
# print(divmod(10, 3))

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy, carry = ListNode(0), 0
        current = dummy

        while l1 or l2:
            val = carry
            if l1 is not None:
                val += l1.val
                l1 = l1.next
            if l2 is not None:
                val += l2.val
                l2 = l2.next
            carry, val = divmod(val, 10)
            current.next = ListNode(val)
            current = current.next

        if carry == 1:
            current.next = ListNode(1)

        return dummy.next

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(None)
        current, node1, node2, carry = dummy, l1, l2, 0

        while node1 or node2 or carry:
            total = (node1.val if node1 else 0) + (node2.val if node2 else 0) + carry

            current.next = ListNode(total % 10)
            current = current.next
            carry = total // 10

            node1 = node1 if node1 is None else node1.next
            node2 = node2 if node2 is None else node2.next
        
        return dummy.next


def create_linked_list(arr):
    dymmy = current = ListNode(0)
    for i, _ in enumerate(arr):
        current.next = ListNode(arr[i])
        current = current.next 
    return dymmy.next

l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])

def print_linked_list(l):
    while l:
        print(l.val)
        l = l.next

s = Solution()
l3 = s.addTwoNumbers2(l1, l2)
print_linked_list(l3)