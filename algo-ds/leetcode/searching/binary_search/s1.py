from typing import List
class Solution:
    def binary_search(self, s: List[int], head: int, tail: int, x: int) -> int:
        # iterative
        # time: O(logn)
        # space: O(1)
        while head <= tail:
            mid = head + (tail - head) // 2
            if s[mid] == x:
                return mid
            elif s[mid] > x:
                tail = mid - 1
            else:
                head = mid + 1
        return -1

    def binary_search1(self, s: List[int], head: int, tail: int, x: int) -> int:
        # recursive
        # time: O(logn)
        # space: O(1), O(logn) call stack space
        if tail >= head:
            mid = head + (tail - head) // 2
            if s[mid] == x:
                return mid
            elif s[mid] < x:
                return self.binary_search(s, mid + 1, tail, x)
            else:
                return self.binary_search(s, head, mid - 1, x)
        return -1

l = [2, 3, 4, 10, 25, 40]
x = 25

s = Solution()
print(s.binary_search(l, 0, len(l) - 1, x))

