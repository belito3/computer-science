class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # tim cac bit chung cua m va n, ke tu ben trai
        while n > m:
            n = n & (n-1)

        return n
