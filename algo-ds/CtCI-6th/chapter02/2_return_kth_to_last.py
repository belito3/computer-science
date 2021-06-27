from linked_list import ListNode, createLinkedList, printLinkedList

def printKthToLast(node: ListNode, k: int) -> ListNode:
    # Recursive
    # Time: O(n)
    # Space: O(n)
    if node == None:
        return 0

    index = printKthToLast(node.next, k) + 1
    if index == k:
        print(k, "th to last node is " + str(node.val))

    return index

    

def return_kth_to_last(node: ListNode, k: int) -> ListNode:
    # Two Point
    # Time: O(N)
    # Space: O(1)
    node1 = node2 = node

    for i in range(k):
        node2 = node2.next

    while node2 is not None:
        node2 = node2.next
        node1 = node1.next

    return node1
    

if __name__ == "__main__":
    arr = [[1, 2, 3, 4], [1]]

    for i in range(len(arr)):
        for j in range(1, len(arr[i])+1):
            print("arr = {} k = {}".format(arr[i], j))
            node = createLinkedList(arr[i])
            target = return_kth_to_last(node, j)
            print("rs :", target.val)

    printKthToLast(createLinkedList(arr[0]), 3)


