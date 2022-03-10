from typing import List

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        pass


def getPermutation2(arr):
    rs = []
    num = 0
    getPermutationDistinct(arr, num, rs)
    return rs


def getPermutationDistinct(arr: List[int], num: int, rs: List[int]):
    if len(arr) == 0:
        rs.append(num)

    table = [False] * 10

    for i in range(len(arr)):
        if table[arr[i]] is False:
            num2 = num * 10 + arr[i]
            new_arr = arr[:i] + arr[i+1:]
            getPermutationDistinct(new_arr, num2, rs)
            table[arr[i]] = True


def getPermutation1(arr):
    # With duplicate
    rs = []
    num = 0
    getPermutationWithDuplicate(arr, num, rs)
    return rs

def getPermutationWithDuplicate(arr, num, rs) -> List[int]:
    # With duplicate
    if len(arr) == 0:
        rs.append(num)

    for i in range(len(arr)):
        num2 = num * 10 + arr[i]
        new_arr = arr[:i] + arr[i+1:]
        getPermutationWithDuplicate(new_arr, num2, rs)



if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    rs = getPermutation1(arr)
    print(rs)

    arr = [1, 2, 2]
    rs = getPermutation2(arr)
    print(rs)



