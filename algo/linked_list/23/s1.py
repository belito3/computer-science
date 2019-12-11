from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:  # solution 2
        list_all = current = ListNode(None)

        for l in lists:
            if l is not None:
                list_all.next = l
                list_all = list_all.next
        list_all = current.next

        current = dummy = ListNode(None)
        


    def mergeKLists1(self, lists: List[ListNode]) -> ListNode:  # solution 1, Time complexity ??
        current = dummy = ListNode(None)

        d = {}

        for i, l in enumerate(lists):
            if l is not None:
                d[i] = l.val

        while d: # if d not empty
            # find node have min value (min key)
            i_min = min(d, key=d.get)
            
            print("i_min: ", i_min)  # index node min
            for l in lists:
                printList(l)
            print("=============")

            # point current node to node min
            current.next = lists[i_min]
            current = current.next
            # move node_min to next node
            lists[i_min] = lists[i_min].next

            if lists[i_min] is not None:
                # update nodes must examning
                d[i_min] = lists[i_min].val
            else:
                # remove node in lists
                del d[i_min]
            
        return dummy.next
    

    def sortListNode(self, lists: List[ListNode]) -> List[ListNode]:
        # sort list node following ascending order
        for i in range(len(lists)):
            for j in range(i+1, len(lists)):
                if lists[j].val < lists[i].val:
                    tmp = lists[i]
                    lists[i] = lists[j]
                    lists[j] = tmp
        return lists


def printList(head: ListNode) -> None:
    if head is None:
        print(" ")

    while head is not None:
        print(head.val, end=" ")
        head = head.next

    print(" ")

def createLinkedList(arr: List[int]) -> ListNode:
    current = dummy = ListNode(None)
    for v in arr:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

s = Solution()
# [[1,4,5],[1,3,4],[2,6]]
l0 = createLinkedList([])
l1 = createLinkedList([1,4,5])
l2 = createLinkedList([1,3,4])
l3 = createLinkedList([2,6])

printList(s.mergeKLists([l0, l1, l2]))

# lists = [l1, l2, l3]
# res = s.mergeKLists(lists)
# printList(res)