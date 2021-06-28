from linked_list import ListNode, createLinkedList, printLinkedList

def partition_list(head: ListNode, val: int):
    # Two Pointer
    # Time: O(N)
    # Space: O(1)
    left = dummy_left = None
    right = dummy_right = None

    while head is not None:
        if head.val < val:
            # append to left
            if left is None:
                left = dummy_left = head
            else:
                left.next = head
                left = left.next
        else:
            # append to right
            if right is None:
                right = dummy_right = head
            else:
                right.next = head
                right = right.next
        head = head.next

    if left != None:
        left.next = dummy_right
    else:
        return dummy_right

    if right != None:
        right.next = None

    return dummy_left

if __name__ == "__main__":
    arr = [[2, 1], [1, 4, 3, 2, 5, 2], [1]]
    k = [2, 3, 1]

    for a, i in zip(arr, k):
        print("input: ", a, "x: ", i)
        head = createLinkedList(a)
        rs = partition_list(head, i)
        printLinkedList(rs)
        print()

