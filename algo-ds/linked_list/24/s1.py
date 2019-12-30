class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 96.68 % faster ^^
# For example, given 1->2->3->4, you should return the list as 2->1->4->3.
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        if (head is None) or (head.next is None):
            return head

        dummy = ListNode(None)

        while (head is not None) and (head.next is not None):
            # if (head is None) or (head.next is None):
            #     break
            
            if dummy.next is None:
                dummy.next = head.next

            n1 = head
            n2 = head.next
            head = head.next.next

            n2.next = n1
            n1.next = head if (head is None or head.next is None) else head.next
            
        return dummy.next


def printList(l: ListNode) -> None:
    if l == None:
        print(" ")
        return 

    while l is not None:
        print(l.val, end= " ")
        l = l.next

    print(" ")

def createLinkedList(arr: []) -> ListNode:
    current = dummy = ListNode(None)

    for v in arr:
        current.next = ListNode(v)
        current = current.next

    return dummy.next

# Test case: [], [1], [1, 2, 3], [1, 2, 3 ,4]
l1 = createLinkedList([1, 2, 3])
printList(l1)

s = Solution()
printList(s.swapPairs(l1))