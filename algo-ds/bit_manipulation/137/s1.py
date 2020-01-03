from typing import List

class Solution:
    # Solution 1: Math
    # time: O(n)
    # space: O(n)
    def singleNumber(self, nums: List[int]) -> int:
        return int((3 * sum(set(nums)) - sum(nums))/2)
s = Solution()
print(s.singleNumber([2,2,3,2]))

# Python3 code to find the element that
# appears once

def getSingle(arr, n):
    ones = 0
    twos = 0

    for i in range(n):
        # one & arr[i]" gives the bits that
        # are there in both 'ones' and new
        # element from arr[]. We add these
        # bits to 'twos' using bitwise OR
        twos = twos | (ones & arr[i])
        print("twos: ", twos)
        # one & arr[i]" gives the bits that
        # are there in both 'ones' and new
        # element from arr[]. We add these
        # bits to 'twos' using bitwise OR
        ones = ones ^ arr[i]
        print("ones: ", ones)
        # The common bits are those bits
        # which appear third time. So these
        # bits should not be there in both
        # 'ones' and 'twos'. common_bit_mask
        # contains all these bits as 0, so
        # that the bits can be removed from
        # 'ones' and 'twos'
        common_bit_mask = ~(ones & twos)

        # Remove common bits (the bits that
        # appear third time) from 'ones'
        ones &= common_bit_mask

        # Remove common bits (the bits that
        # appear third time) from 'twos'
        twos &= common_bit_mask
    return ones

# driver code
arr = [3, 3, 2, 3]
n = len(arr)
print("The element with single occurrence is ",
        getSingle(arr, n))
