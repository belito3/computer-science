from linked_list import ListNode, createLinkedList, printLinkedList

def sum_reverse(node1: ListNode, node2: ListNode) -> ListNode:
    """
    617 + 295 = 912
    7 -> 1 -> 6 + 5 -> 9 -> 2 = 2 -> 1 -> 9
    """
    dummy = rs = ListNode()
    carry = 0

    while (node1 is not None) or (node2 is not None):
        if node1 is None:
            num1 = 0
            num2 = node2.val
            node2 = node2.next
        elif node2 is None:
            num1 = node1.val
            num2 = 0
            node1 = node1.next
        else:
            num1 = node1.val
            num2 = node2.val
            node1 = node1.next
            node2 = node2.next

        sum = num1 + num2 + carry
        carry = sum // 10
        sum = sum - carry * 10
        rs.next = ListNode(sum)
        rs = rs.next

    if carry != 0:
        rs.next = ListNode(carry)
        rs = rs.next

    return dummy.next


if __name__ == "__main__":
    arr = [[2,4,3], [5,6,4], [0], [0], [9,9,9,9,9,9,9], [9,9,9,9]]

    for i in range(0, len(arr), 2):
        print("arr1 = ", arr[i])
        print("arr2 = ", arr[i+1])
        node1 = createLinkedList(arr[i])
        node2 = createLinkedList(arr[i+1])
        rs = sum_reverse(node1, node2)
        printLinkedList(rs)
        print()



