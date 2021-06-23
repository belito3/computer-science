from typing import List

class Solution:
    # Solution 1: Math
    # time: O(n)
    # space: O(n)
    def singleNumber(self, nums: List[int]) -> int:
        return int((3 * sum(set(nums)) - sum(nums))/2)

    def singleNumber2(self, nums: List[int]) -> int:
        m = 0
        n = 0

        for r in nums:
            p = m
            q = n
            # m = (r & ~p & q) | (~r & p & ~q)
            m = (r & q) | (~r & p)
            n = (~r & q) | (r & ~p & ~q)
        return n

s = Solution()
print(s.singleNumber([2,2,3,2]))


