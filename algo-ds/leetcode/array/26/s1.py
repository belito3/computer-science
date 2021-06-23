from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 1:
            return length

        i = 0
        for j in range(1, length):
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i += 1
        return i+1


s = Solution()
l = [1,1,2]
length = s.removeDuplicates(l)
for i in range(length):
    print(l[i])
