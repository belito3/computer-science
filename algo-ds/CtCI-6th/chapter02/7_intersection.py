from linked_list import ListNode, createLinkedList, printLinkedList

def intersection(head1: ListNode, head2: ListNode) -> ListNode:
    # S1: Get length then compare
    # Time: O(m+n)
    # Space: O(1)
    rs1 = get_size_and_tail(head1)
    rs2 = get_size_and_tail(head2)

    if rs1.node != rs2.node:
        return None

    longer = head1
    shorter = head2

    diff = rs1.length - rs2.length

    if diff < 0:
        longer = head2
        shorter = head1
        diff = -diff

    for _ in range(diff):
        longer = longer.next

    # Compare two linked same length
    while longer is not None:
        if longer == shorter:
            return longer
        longer = longer.next
        shorter = shorter.next

    return None


class Result:
    def __init__(self, length, node):
        self.length = length
        self.node = node


def get_size_and_tail(head: ListNode) -> Result:
    node = head

    rs = Result(length=0, node=head)

    while rs.node.next is not None:
        rs.node = rs.node.next
        rs.length += 1

    return rs


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



