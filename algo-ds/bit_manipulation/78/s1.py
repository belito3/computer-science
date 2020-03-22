from typing import List

class Solution:
    # golang bitmask runtime 0 ms (online submission)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Time: N * 2**N
        # Space: N * 2 ** N
        # Recursion
        rs = [[]]
        for n in nums:
            temp = []
            for e in rs:
                a = e + [n]
                temp.append(a)
            rs += temp

        return rs

    def subsets1(self, nums: List[int]) -> List[List[int]]:
        # Time: N * 2**N (N: length of nums)
        # Space: N * 2**N (keep all subsets of length N, since each of N elemets could be presents or absent)
        # Lexicograpic (binary sorted) subsets
        length = len(nums)
        n = 2 ** length
        rs = []

        for i in range(n):
            # generate bismask, from 000 to 111
            bit_mask =  bin(i|n)[3:]
            a = [] # store subset
            for j in range(length):
                if bit_mask[j]=='1':
                    a.append(nums[j])
            rs.append(a)

        return rs

s = Solution()
print(s.subsets([1,2]))




