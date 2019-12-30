class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Example:

# Given this linked list: 1->2->3->4->5

# For k = 2, you should return: 2->1->4->3->5

# For k = 3, you should return: 3->2->1->4->5

class Solution:
    # s1: brute force
    # s2: slove problem 206, 92 before   
    def reverseKGroup2(self, head: ListNode, k: int) -> ListNode:

    def reverseKGroup1(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head
        l = []
        while head is not None:
            l.append(head.val)
            head = head.next
        
        start = 0
        end = k
        for i in range(len(l) // k):
            if len(l[start:end])==k:
                l[start:end] = l[start:end][::-1]
            start += k
            end += k
		
        dummy = current = ListNode(None)
        for val in l:
            current.next = ListNode(val) # consume much memory
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
l = create_linked_list([1, 2, 3, 4, 5])

print_linked_list(s.reverseKGroup2(l, 2))
