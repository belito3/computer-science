from linked_list import ListNode, createLinkedList, printLinkedList


def loop_detection(head: ListNode) -> ListNode:
    # Two Point
    # Space: O(1)
    if (head is None) or (head.next is None):
        return None

    fast = slow = head

    while (fast is not None) and (fast.next is not None):
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow

    return None

def loop_detection1(head: ListNode) -> ListNode:
    # Hash table
    # Time: O(n)
    # Space: O(n)
    lookup = set()

    while head is not None:
        if head in lookup:
            return head
        lookup.add(head)
        head = head.next

    return None



