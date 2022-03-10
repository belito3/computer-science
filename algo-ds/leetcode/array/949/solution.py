from typing import List

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        times = getPermutation2(arr)
        print(times)
        times = sorted(times)

        for i in range(len(times)-1, -1, -1):
            if checkTimeValid(times[i]):
                return times[i][0:2] + ":" + times[i][2:4]

        return ""

def checkTimeValid(time: str) -> bool:
    """
    H1H2:M1M2

    H1:  0 <= H1 <= 2  
    if H1 == 2 -> 0 <= H2 <= 3
    M1: 0 <= M1 <= 5
    """
    print(f"time: {time}")
    h1, h2, m1, m2 = int(time[0]), int(time[1]), int(time[2]), int(time[3])
    if h1 > 2:
        return False

    if h1 == 2 and h2 > 3:
        return False

    if m1 > 5: 
        return False
    return True

def getPermutation2(arr):
    rs = []
    num = ""
    getPermutationDistinct(arr, num, rs)
    return rs


def getPermutationDistinct(arr: List[int], num: str, rs: List[int]):
    if len(arr) == 0:
        rs.append(num)

    table = [False] * 10

    for i in range(len(arr)):
        if table[arr[i]] is False:
            num2 = num + str(arr[i])
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

    arr = [[1,2,3,4], [0,0,0,0]]
    for a in arr:
        s = Solution()
        print(s.largestTimeFromDigits(a))


