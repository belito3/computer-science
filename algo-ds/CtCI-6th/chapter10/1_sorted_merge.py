from typing import List

def sorted_merge(nums1: List[int], nums2: List[int], len1, len2):
    # Time: O(a+b)
    last1 = len1 - 1
    last2 = len2 - 1
    merge_index = len1 + len2 - 1

    while last2 >= 0 and last1 >=0:
        if nums1[last1] > nums2[last2]:
            nums1[merge_index] = nums1[last1]
            last1 -= 1
        else:
            nums1[merge_index] = nums2[last2]
            last2 -= 1
        merge_index -= 1

    for i in range(last2,-1,-1):
        nums1[merge_index] = nums2[i]
        merge_index -= 1

def sorted_merge2(a: List[int], b: List[int], lena, lenb):
    # Time: a+b -> a *b
    # Space: O(1)
    i = 0
    while i < lena:
        if a[i] > b[0]:
            swap(a, b, i, 0)
            sort_first(b)
        i += 1

    for e in b:
        a[i] = e
        i += 1

def swap(a, b, i, j):
    a[i] += b[j]
    b[j] = a[i] - b[j]
    a[i] = a[i] - b[j]

def sort_first(b):
    i = 0
    for j in range(1, len(b)):
        if b[i] > b[j]:
            b[i] = b[i] + b[j]
            b[j] = b[i] - b[j]
            b[i] = b[i] - b[j]
            i = j

if __name__ == "__main__":
    a = [[1,4,5,10,0,0,0], [1,0], [7,8,9,0,0], [0]]
    b = [[2,3,9], [2], [4,10], []]

    for i in range(len(a)):
        print("=" * 10)
        print(f"a[i] = {a[i]}, b[i] = {b[i]}")
        sorted_merge(a[i], b[i], len(a[i]) - len(b[i]), len(b[i]))
        print(f"a[i] = {a[i]}")
