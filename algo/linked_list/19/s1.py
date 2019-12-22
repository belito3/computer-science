class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:        
        d = {}
        i = 0
        dummy = current = ListNode(None)

        while head is not None:
            d[i] = head.val
            i += 1
            head = head.next
        
        if n > len(d):
            n_th_remove = 0
        else:
            n_th_remove = len(d) - n
        
        if n_th_remove in d:
            del d[n_th_remove]

        for key in d:
            current.next = ListNode(d[key])
            current = current.next
        
        return dummy.next


def create_linked_list(arr):
    dummy = current = ListNode(None)

    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def print_linked_list(head):
    if head is None:
        print(" ")
        return

    while head is not None:
        print(head.val, end="->")
        head = head.next

    print(" ")

s = Solution()
# [1, 2, 3, 4, 5], [4,5,4]
l1 = create_linked_list([4,5,4])

print_linked_list(s.removeNthFromEnd(l1, 4))