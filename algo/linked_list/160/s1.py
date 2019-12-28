class Solution:
    # Solution 1: Hash table
    # Time: O(m+n)
    # Space: O(m) or O(n)
    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        if headA is None or headB is None:
            return None
        
        s = set()
        
        while headA is not None:
                s.add(headA)
                headA = headA.next
        
        while headB is not None:
            if headB in s:
                return headB
            else:
                s.add(headB)
                headB = headB.next
        return None

    # Solution 2: Two pointer
    # Time: O(m+n)
    # Space: O(1)
    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        pa = headA
        pb = headB
        
        while pa != pb:
            pa = pa.next if pa is not None else headB
            pb = pb.next if pb is not None else headA
            
        return pa
