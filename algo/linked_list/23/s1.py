from typing import List
from queue import PriorityQueue

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # Solution 6: Merge with Divide and Conquer
    # Time: O(Nlogk). 116 ms
    # Memory: O(k). 15.6 MB
    def mergeKLists6(self, lists: List[ListNode]) -> ListNode:     
        interval = 1
        lenght = len(lists)
        while interval < lenght:
            for i in range(0, lenght - interval, interval * 2):
                lists[i] = self.merge2List(lists[i], lists[i + interval])
            interval *= 2

        return lists[0]  if lenght > 0 else None

    def merge2List(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = current = ListNode(None)

        while (l1 is not None) and (l2 is not None):
            if l1.val < l2.val:
                current.next = l1 # ko su dung ListNode(l1.val): vi khoi tao moi ton memory va time rat nhieu
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        current.next = l1 or l2 
        
        return dummy.next
        

    # Solution 5: Optimize s4 by Priority Queue (use heap solution)
    # Time complexity: O(N logK)
    #   where k is the number of linked lists
    #   pop and insert to queue: O(logK). find min O(1)
    # Space complexity: O(N)
    def mergeKLists5(self, lists: List[ListNode]) -> ListNode:  # Time: 152ms. Memory: 16MB        
        q = PriorityQueue()
        dummy = current = ListNode(None)

        for i, l in enumerate(lists):
            if l is not None:
                # In the event that two or more of the lists have the same val, 
                # this code will error out since the queue module will compare the second element in the priority queue which is a ListNode object 
                # (and this is not a comparable type).
                q.put((l.val, i, l))

        while not q.empty():
            # get node from queue
            # if next node is not None put to queue
            _, i, node = q.get()
            current.next = node  # Don't use ListNode(node.val) due to consum  memory and time
            current = current.next
            node = node.next
            if node is not None:
                q.put((node.val, i, node))
        
        return dummy.next

    # Solution 4: compare one by one
    # Compare every k nodes (head of every linked list) and get the smallest node
    # Extend the final sorted linked list with selected nodes
    # Time complexity: O(kN)
    #   where k is the number of linked list
    #   when k large: k > log(N). This solution worse than solution 3 (Time Limit Exceeded @@)
    # Space complexity: O(N)
    #   creating a new listed list costs O(n) space
    def mergeKLists4(self, lists: List[ListNode]) -> ListNode:  
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

    # solution 3: Brute force. (Cục súc) (easy game)
    # time: N log(N). 92 ms
    # memory: O(N). 16.7 MB
    def mergeKLists3(self, lists: List[ListNode]) -> ListNode: 
        
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

    # solution 2: MergeSort. Time: 172 ms, Memory: 22.4 MB
    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:  
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

printList(s.mergeKLists5([l1, l2, l3]))


# lists = [l1, l2, l3]
# res = s.mergeKLists(lists)
# printList(res)