from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Bayer-Moore:
        # Time: O(n). Space: O(1)
        # Dung bien count de loai bo phan tu thieu so
        cnt = 0
        candidate = None

        for num in nums:
            if cnt == 0:
                candidate = num
            cnt += 1 if (candidate==num) else -1

        return candidate


    def majorityElement3(self, nums: List[int]) -> int:
        # Sorted: O(nlogn)

        l = sorted(nums)

        return l[int(len(nums)/2)]


    def majorityElement2(self, nums: List[int]) -> int:
        # Hash table
        d = {}
        l = len(nums)/2

        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] = d[n] + 1

            if d[n] > l:
                return n

        return 0


s = Solution()
l = [2,2,1,1,1,2,2]
print(s.majorityElement(l))

