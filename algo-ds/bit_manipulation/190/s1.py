class Solution:
    def reverseBits(self, n: int) -> int:
        n_bin = format(n, '032b')
        n_bin_rev = n_bin[::-1]

        return int(n_bin_rev, 2)

    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = (res << 1) + (n&1)
            n >>= 1

        return res
