from typing import List
from queue import PriorityQueue

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # So sanh vs cach giai solution: tai sao time va memory k toi uu bang
    def mergeKLists6(self, lists: List[ListNode]) -> ListNode: 
        # Solution 6: Merge with Divide and Conquer
        if len(lists) == 0:
            return None
        
        if len(lists) == 1:
            return lists[0]
        
        j = 1
        lenght = len(lists)
        while j <= lenght - 1:
            for i in range(0, lenght -1, 2*j):
                if i+j > lenght - 1:
                    break
                lists[i] = self.merge2List(lists[i], lists[i+j])
            j *= 2

        return lists[0] 

    def merge2List(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = current = ListNode(None)

        while (l1 is not None) and (l2 is not None):
            if l1.val < l2.val:
                current.next = ListNode(l1.val)
                current = current.next
                l1 = l1.next
            else:
                current.next = ListNode(l2.val)
                current = current.next
                l2 = l2.next
        
        current.next = l1 or l2
        return dummy.next
        

    def mergeKLists5(self, lists: List[ListNode]) -> ListNode:  # Time: 156ms. Memory: 21.1MB
        # Solution 5: Optimize s4 by Priority Queue
        # Time complexity: O(N logK)
        #   where k is the number of linked lists
        #   pop and insert to queue: O(logK). find min O(1)
        # Space complexity: O(N)
        q = PriorityQueue()
        dummy = current = ListNode(None)

        for l in lists:
            if l is not None:
                q.put((l.val, l))

        while not q.empty():
            # get node from queue
            # if next node is not None put to queue
            _, node = q.get()
            current.next = ListNode(node.val)
            current = current.next
            node = node.next
            if node is not None:
                q.put((node.val, node))
        
        return dummy.next


    def mergeKLists4(self, lists: List[ListNode]) -> ListNode:  
        # Solution 4: compare one by one
        # Compare every k nodes (head of every linked list) and get the smallest node
        # Extend the final sorted linked list with selected nodes
        # Time complexity: O(kN)
        #   where k is the number of linked list
        #   when k large: k > log(N). This solution worse than solution 3 (Time Limit Exceeded @@)
        # Space complexity: O(N)
        #   creating a new listed list costs O(n) space
        dummy = current = ListNode(None)
        lenght = len(lists)
        while True:
            i_min = 0
            min = None
            for i in range(lenght):
                if lists[i] is not None:
                    if min is None:
                        min = lists[i].val
                        i_min = i
                    elif lists[i].val < min:
                        min = lists[i].val
                        i_min = i
            
            if min is None:
                break

            current.next = ListNode(lists[i_min].val)
            current = current.next
            lists[i_min] = lists[i_min].next

        return dummy.next

    def mergeKLists3(self, lists: List[ListNode]) -> ListNode: 
        # solution 3: Brute force. (Cục súc) (easy game)
        # time: N log(N), memory: O(N)
        all_node = []

        # N is the total number of Nodes
        # Step 1: for with time O(N), memory O(N)
        for l in lists:
            while l is not None:
                all_node.append(l.val)
                l = l.next
        current = dummy = ListNode(None)

        # Step 2: time sorted O(N logN), memory O(N)
        # Step 3: for with time O(N)
        for val in sorted(all_node):
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:  # solution 2: MergeSort. Time: 172 ms, Memory: 22.4 MB
        list_all = current = ListNode(None)

        for l in lists:
            while l is not None:
                list_all.next = l
                list_all = list_all.next
                l = l.next
        list_all = current.next

        rs = self.mergeSort(list_all)

        return rs

    def mergeSort(self, h):
        if h == None or h.next == None:
            return h
        
        middle = self.getMiddle(h)
        next_middle = middle.next

        middle.next = None

        left = self.mergeSort(h)
        right = self.mergeSort(next_middle)

        sortedlist = self.sortedMerge(left, right)
        return sortedlist

    def sortedMerge(self, a, b):
        result = None

        if a is None:
            return b
        
        if b is None: 
            return a

        if a.val < b.val:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result
    
    def getMiddle(self, head):
        if (head == None):
            return head
        slow = fast = head

        while (fast.next is not None) and (fast.next.next is not None):
            slow = slow.next
            fast = fast.next.next

        return slow

    def mergeKLists1(self, lists: List[ListNode]) -> ListNode:  # solution 1. (thua cả cục súc, đời này coi như bỏ) Time: 2352 ms. Memory: 16 MB
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
l4 = createLinkedList([2])

printList(s.mergeKLists6([]))


# lists = [l1, l2, l3]
# res = s.mergeKLists(lists)
# printList(res)