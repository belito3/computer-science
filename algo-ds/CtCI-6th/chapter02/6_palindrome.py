from linked_list import ListNode, printLinkedList, createLinkedList

def isPalindrome(head: ListNode) -> bool:
    pass

def isPalindromeWithLength(head: ListNode, l: int) -> bool:
    # recursive

def isPalindome1(head: ListNode) -> bool:
    # S1: reserve and compare
    # if list is palindrome, it must be same backward and forward
    # => create reverse linked list, then compare

def isPalindrome2(head: ListNode) -> bool:
    # S2: Stack
    # Time: O(n)
    # Space: O(n)
    stack = []

    dummy = head
    l = 0  # length
    while dummy is not None:
        l += 1
        stack.append(dummy.val)
        dummy = dummy.next

    while head is not None:
        if l < 0:
            break
        val = stack.pop()
        if head.val != val:
            return False
        head = head.next
        l -= 1

    return True



if __name__ == "__main__":
    input = [[1], [1, 2], [1, 2, 2, 1], [2, 2], [1,2,3,2,1], [1,2,3,4,2,1]]
    for arr in input:
        head = createLinkedList(arr)
        print("a = {} rs = {}".format(arr, isPalindrome(head)))
