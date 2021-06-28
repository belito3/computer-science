from linked_list import ListNode, createLinkedList, printLinkedList

def reverse_linked_list(head: ListNode) -> ListNode:
    dummy = None
    p1 = head

    while p1 is not None:
        p2 = p1.next
        p1.next = dummy
        dummy = p1
        p1 = p2
    return dummy

if __name__ == "__main__":
    arr = [[1], [1,2], [1,2,3,4]]
    for a in arr:
        head = createLinkedList(a)
        printLinkedList(head)
        print()
        reverse = reverse_linked_list(head)
        printLinkedList(reverse)
        print()



