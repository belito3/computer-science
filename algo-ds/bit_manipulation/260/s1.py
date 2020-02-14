from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        s = set()

        for n in nums:
            if n in s:
                s.remove(n)
            else:
                s.add(n)
        return list(s)

s = Solution()

print(s.singleNumber([1, 2, 3, 3])
