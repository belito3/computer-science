from linked_list import ListNode, createLinkedList, printLinkedList


def loop_detection(head: ListNode) -> ListNode:
    # Two Point
    # Space: O(1)
    """
    1. Why do FastRunner and SlowRunner will collied?
       It is impossible to they don't meet.
       Suppose FastRunner run over SlowRunner, it mean Slow at spot i and Fast at spot (i+1).
       But at previous step, Slow at spot i-1, and Fast at spot (i+1) - 2 = i-1.
       That is, they would have collied.

    2. When do they would have collied?
        Call k is length from head to first loop.
             LOOP_SIZE is length loop
        When Slow at spot 0 in loop, Fast have been runned 2k spot and at k spot in loop.
        Because k can be greater than LOOP_SZIE, so we donate Fast at K spot in loop, with K = mod(LOOP_SIZE, k), k = M * LOOP_SIZE + K.
        -> Fast at spot K in loop, so Fast behind Slow (at spot 0) is LOOP_SIZE - K.
        Because Fast run over Slow 1 spot each time, so they are collied after LOOP_SIZE-K time, at (LOOP_SIZE - K) spot in loop


    3. How do you return node start of loop?
        Because, Slow and Fast are collied at LOOP_SIZE - K in loop, this point need K step to reach to fist start loop.
        It is correct k, when slow go from head to first loop

    """
    if (head is None) or (head.next is None):
        return None

    fast = slow = head

    is_has_cycle = False

    while (fast is not None) and (fast.next is not None):
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            is_has_cycle = True
            break

    # Check it has not circle
    if is_has_cycle is False:
        return None

    # Find fisrt node of loop
    slow = head
    while True:
        if slow == fast:
            return slow
        slow = slow.next
        fast = fast.next


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



