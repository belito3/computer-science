class Solution:
    def hammingWeight(self, n: int) -> int:
        num = 0
        while n != 0:
            num += 1
            n &= (n-1)

        return num
