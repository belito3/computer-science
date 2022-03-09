"""
N = 32000 ~ 2^5 * 2 ^ 10 = 2 ^ 15
Memory: 4KB = 2^2 * 2 ^10 B = 2 ^ 15 Bit

We can use each bit represent a number is present
"""

from typing import List
from BitVector import BitVector


def findDuplicate(array: List[int]):
    vec = BitVector(size=32000)
    for num in array:
        if vec[num] != 0:
            print(num)
        else:
            vec[num] = 1


if __name__ == "__main__":
    arr = [1, 2, 2, 3]
    findDuplicate(arr)
