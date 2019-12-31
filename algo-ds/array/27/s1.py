from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0

        i = 0

        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
s = Solution()
l = [1,2,3,1,1]
length = s.removeElement(l, 1)
for i in range(length):
    print(l[i])
print(l)
