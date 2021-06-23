from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Find diff
        diff = 0
        for n in nums:
            diff ^= n

        diff &= -diff  # ~(diff - 1)

        num1 = 0
        num2 = 0
        for n in nums:
            if (n & diff) == 0:
                num1 ^= n
            else:
                num2 ^= n

        return [num1, num2]

    def singleNumber2(self, nums: List[int]) -> List[int]:
        s = set()

        for n in nums:
            if n in s:
                s.remove(n)
            else:
                s.add(n)
        return list(s)

s = Solution()
print(s.singleNumber([2,3,4,4,5,5]))