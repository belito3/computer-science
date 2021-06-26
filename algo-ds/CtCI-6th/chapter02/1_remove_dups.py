from linked_list import ListNode, createLinkedList, printLinkedList
import time

def remove_duplicates(node: ListNode):
    # Hash table
    # Time O(N)
    # Space O(N)
    runner = node
    table = {node.val}

    while (runner is not None) and (runner.next is not None):
        if runner.next.val in table:
           # remove next node
            runner.next = runner.next.next
        else:
            runner = runner.next
            table.add(runner.val)

   

def remove_duplicates1(node: ListNode):
    # Two point
    # Time: O(n^2)
    # Space: O(1)
    node1 = node2 = node

    while (node1 is not None) and (node1.next is not None): 
        if node2.next.val == node1.val:
            # renove node2.next
            node2.next = node2.next.next
        else:
            node2 = node2.next
                
        if (node2 is None) or (node2.next is None):
            node1 = node1.next
            node2 = node1

        #print("node1: ", node1.val)
        #print("node2: ", node2.val)
    return node

if __name__ == "__main__":
    arr = [[1, 2, 3, 5, 1, 6, 2, 10], [1], [1, 1], [1, 2]]
    for a in arr:
       print(a)
       node = createLinkedList(a)
       remove_duplicates(node)
       printLinkedList(node)
       print()
