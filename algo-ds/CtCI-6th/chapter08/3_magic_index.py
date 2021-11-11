from typing import List


def get_magic_index(arr: List[int]):
    return bs(arr, 0, len(arr) - 1)


def bs(arr: List[int], start: int, end: int) -> int:
    if start > end:
        return -1

    mid = int((start + end) / 2)
    mid_value = arr[mid]
    if mid_value == mid:
        return mid

    left = min(mid_value, mid - 1)
    right = max(mid_value, mid + 1)

    left_value = bs(arr, start, left)
    if left_value > 0:
        return left_value

    right_value = bs(arr, right, end)
    return right_value


if __name__ == "__main__":
    arr = [[3, 4, 4, 4, 4, 5, 7], [1, 1, 1], [0, 2, 3, 4, 5], [-1, 0, 1, 3, 5], [0, 0, 1, 1, 4, 6]]
    for a in arr:
        print(f"arr = {a}, {get_magic_index(a)}")

