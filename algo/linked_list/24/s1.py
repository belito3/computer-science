class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# For example, given 1->2->3->4, you should return the list as 2->1->4->3.
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(None)

        while True:
            if (head is None) or (head.next is None):
                break
            
            if dummy.next is None:
                dummy.next = head.next

            n1 = head
            n2 = head.next

            n1.next = n2.next
            n2.next = n1
            head = n1.next
            # n1.next = head.next if head is not None else head
            
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

l1 = createLinkedList([2, 3, 4, 5])
printList(l1)

s = Solution()
# s.swapPairs(l1)
printList(s.swapPairs(l1))