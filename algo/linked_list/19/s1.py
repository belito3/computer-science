class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd3(self, head: ListNode, n: int) -> ListNode:
        start = end = dummy = ListNode(None)
        dummy.next = head

        for i in range(n+1):
            end = end.next
        
        while end is not None:
            start = start.next
            end = end.next

        start.next = start.next.next
        return dummy.next

    # Solution 2: One pass algorithm. Use constant gap start and end node = n
    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        start = end = head
        i = 0
        while end.next is not None:
            end = end.next
            i += 1
            if i > n:  # Distance begin-end: n + 1
                start = start.next
        
        if i+1 <= n:  # if length of LinkedList = n
            return head.next

        start.next = start.next.next if start.next is not None else None
        return head

    
    # Solution 1: Two pass algorithm. Find node remove from begin list
    # Time complexity: O(N).  
    # 28 ms, faster than 90.95% of Python3
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:        
        length = 0
        dummy = current = ListNode(None)
        tmp_node = head

        while tmp_node is not None:  # O(N)
            length += 1
            tmp_node = tmp_node.next
        
        if n > length:
            n_th_remove = 0
        else:
            n_th_remove = length - n
        
        i = 0
        while head is not None:   # O(N)
            if i == n_th_remove:
                current.next = head.next
                break
            else:
                current.next = head
            current = current.next
            head = head.next
            i += 1
        
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
l1 = create_linked_list([1, 2, 3, 4, 5])

print_linked_list(s.removeNthFromEnd3(l1, 6))