from linked_list import ListNode, createLinkedList, printLinkedList

def delete_middle_node(head: ListNode):
    prev = slow = fast = head

    while True:
        if fast.next is not None:
            prev = slow
            fast = fast.next.next
            if fast is not None:
                prev = slow
                slow = slow.next
            else:
                # number node in ll is even, remove slow node
                prev.next = prev.next.next
                break
        else:
            # number node in ll is odd, remove slow node
            if prev.next is not None:
                prev.next = prev.next.next
            break


if __name__ == "__main__":
    arr = [[1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5]]

    for a in arr:
        print("arr = ", a)
        head = createLinkedList(a)
        delete_middle_node(head)
        print()
        printLinkedList(head)
        print()

