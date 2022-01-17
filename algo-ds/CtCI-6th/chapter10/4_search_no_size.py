from typing import  List


class Listy:
    def __init__(self, nums: List[int]):
        self.nums = nums
    def elementAt(self, i: int) -> int:
        if (i > len(self.nums) - 1) or (i < 0):
            return -1
        return self.nums[i]


def searchNoSize(nums: Listy, target: int) -> int:
    # Time: Log(n)
    left, right = 0, findTail(nums)

    while left <= right:
        mid = (left + right) // 2
        if nums.elementAt(mid) == target:
            return mid
        elif nums.elementAt(mid) < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def findTail(nums: Listy) -> int:
    # Time: Log(n)
    if nums.elementAt(0) == -1:
        return -1
    left, right = 0, 1

    # find right
    while nums.elementAt(right) != -1:
        left = right
        right *= 2

    # now, right is more than tail
    t = left
    while left <= right:
        mid = (left + right) // 2
        if nums.elementAt(mid) == -1:
            right = mid - 1
        else:
           t  = mid
           left = mid + 1
    return t


if __name__ == "__main__":
    for i in range(12):
        nums = [j for j in range(i)]
        target = int(0.4 * i)
        listy = Listy(nums)
        i = searchNoSize(listy, target)
        print(f"target = {target}, index = {i}, nums = {nums}")





