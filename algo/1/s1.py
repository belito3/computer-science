from typing import List

# Time: O(n)
# Space: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i, num in enumerate(nums):
            num2 = target - num
            if num2 in lookup:
                return [lookup[num2], i]
            lookup[num] = i

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num1 in enumerate(nums):
            num2 = target - num1
            nums_tmp = nums[i+1:]

            if num2 in nums_tmp:
                return [i, i + 1 + nums_tmp.index(num2)]
            

s = Solution()
print(s.twoSum2([3, 2, 4], 6))