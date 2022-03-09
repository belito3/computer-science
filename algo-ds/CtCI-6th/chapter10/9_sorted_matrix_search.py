from typing import List

def searchMatrix(mat: List[List[int]], target: int) -> bool:
    # Time: O(m+n)
    row, col = 0, len(mat[0]) - 1
    r = len(mat)
    c = len(mat[0])
    while row < r and col >= 0:
        if mat[row][col] == target:
            return True
        elif mat[row][col] < target:
            row += 1
        else:
            col -= 1
    return False

def searchMatrix2(mat: List[List[int]], target: int) -> bool:
    # Find max of min row
    row = -1
    low, high = 0, len(mat) - 1

    while low <= high:
        mid = (low + high) // 2
        if mat[mid][0] == target:
            return True
        elif mat[mid][0] < target:
            low = mid + 1
            row = mid
        else:
            high = mid - 1

    if row == -1:
        return False

    # Find max of min col
    col = -1
    left, right = 0, len(mat[0]) - 1
    while left <= right:
        mid = (left+right) // 2
        if mat[0][mid] == target:
            return True
        elif mat[0][mid] < target:
            left = mid + 1
            col = mid
        else:
            right = mid - 1

    if col == -1:
        return False

    for r in range(1, row+1):
        if bs(mat[r][1:col+1], target):
            return True
    return False

def bs(arr: List[int], target: int) -> bool:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

def searchMatrix1(mat: List[List[int]], target: int) -> bool:
    # First number of row larger than last number of row previous
    # Log(m) + log(n)
    # S1: Binary search
    # Find row
    row = -1
    low = 0
    high = len(mat) - 1

    while low <= high:
        mid = (low + high) // 2
        if mat[mid][0] == target:
            return True
        elif mat[mid][0] < target:
            row = mid
            low = mid + 1
        else:
            high = mid - 1

    if row == -1:
        # All number in mat bigger than target
        return False
    print(row)
    # Find col
    left, right = 0, len(mat[0]) -1
    while left <= right:
        mid = (left + right) // 2
        if mat[row][mid] == target:
            return True
        elif mat[row][mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

if __name__ == "__main__":
    matrix = [[1,3,5,7], [10,11,16,20], [23,30,34,60]]
    targets = [3, 60, 1, 13, 7, 20]

    print(f"mat = {matrix}")
    for target in targets:
        print(f"target = {target}")
        print(f"{searchMatrix(matrix, target)}")

