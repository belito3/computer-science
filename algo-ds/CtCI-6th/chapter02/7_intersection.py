from linked_list import ListNode, createLinkedList, printLinkedList

def intersection2(head1: ListNode, head2: ListNode) -> ListNode:
    # S2: Two Pointer
    # If two linkedlist have same length, we only need compare one by one
    # else if have diffence length, we assign a to headB, b to headA
    # Time: O(n1 + n2)
    # Space: O(1)
    node1 = head1
    node2 = head2

    while node1 != node2:
        node1 = head2 if node1 is None else  node1.next
        node2 = head1 if node2 is None else  node2.next

    return node1


def intersection1(head1: ListNode, head2: ListNode) -> ListNode:
    # S1: Hash table
    # Time: O(n1 + n2)
    # Space: O(n1)
    lookup = set()
    while head1 is not None:
        lookup.add(head1)
        head1 = head1.next

    while head2 is not None:
        if head2 in lookup:
            return head2
        head2 = head2.next

    return None



if __name__ == "__main__":
   input = [[4,1], [5,6,1,8,4,5]]
   for i in range(0, len(input), 2):
       print("arr1: ", input[i])
       print("arr2: ", input[i+1])
       head1 = createLinkedList(input[i])
       head2 = createLinkedList(input[i+1])

       while head1.next is not None:
           head1 = head1.next
       head2 = head2.next
       head2 = head2.next
       head2 = head2.next
       head1.next = head2
       print("rs: ", intersection(head1, head2).val)



