from typing import List

def search(arr: List[int], target: int) -> int:
    rotated = find_rotated(arr)
    left, right = 0, len(arr) - 1
    if target == arr[rotated]:
        return rotated
    elif (target > arr[rotated]) and (target <= arr[-1]):
        left, right = rotated, len(arr) - 1
    else:
        left, right = 0, rotated - 1
    print(f"left = {left}, r = {right}, rotated = {rotated}")

    return bs(arr, target, left, right)

def bs(arr: List[int], target: int, left: int, right: int) -> int:

    if left > right:
        return -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def find_rotated(arr: List[int]) -> int:
    # Find rotated - min value
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] > arr[right]:
            left = mid + 1 
        else:
            right = mid

    return left
      




if __name__ == "__main__":
    input_ = [[4,5,6,7,0,1,2], [4,5,6,7,0,1,2], [1], [5,1,3], [6,7,1,2,3,4],[5,7,8,9,1,2]]
    target = [0,3,0,5,2,3]

    for i in range(len(input_)):
        print(f"i = {input_[i]}, target= {target[i]}")
        rs = search(input_[i], target[i])
        print(f"rs = {rs}")
