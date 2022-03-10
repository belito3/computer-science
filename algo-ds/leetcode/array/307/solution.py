# https://vnoi.info/wiki/algo/data-structures/segment-tree-extend.md
# https://leetcode.com/articles/a-recursive-approach-to-segment-trees-range-sum-queries-lazy-propagation/#
from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.tree = [0] * 4 * len(nums)
        self.buildTree(0, 0, len(nums)-1)

    def buildTree(self, treeIndex: int, l: int, r: int):
        if l == r:  # leaf node, store value in node 
            self.tree[treeIndex] = self.nums[l]
            return
        
        mid = (l + r) // 2 # recursive deeper for children
        self.buildTree(2*treeIndex + 1, l, mid) # children node left
        self.buildTree(2*treeIndex + 2, mid+1, r) # children node right

        # parents node
        self.tree[treeIndex] = self.tree[2*treeIndex + 1] + self.tree[2*treeIndex + 2]


    def update(self, index: int, val: int) -> None:
        self._update(0, 0, len(self.nums)-1, index, val)

    # Ham cap nhat cay ST, cap cay con goc treeIndex quan ly doan [l, r]
    def _update(self, treeIndex: int, l: int, r: int, arrIndex: int, val: int):
        if arrIndex < l or arrIndex > r:
            # arrIndex nam ngoai doan [l, r]
            return

        if l == r:
            # Doan chi gom 1 phan tu, ko co nut con
            self.tree[treeIndex] = val
            return

        mid = (l + r) // 2

        if arrIndex <= mid:
            # cap nhat nut con ben trai
            self._update(2 * treeIndex + 1, l, mid, arrIndex, val)
        else:
            # cap nhat nut con ben phai 
            self._update(2 * treeIndex + 2, mid + 1, r, arrIndex, val)

        # update parent node
        self.tree[treeIndex] = self.tree[2*treeIndex + 1] + self.tree[2*treeIndex + 2]


    def sumRange(self, left: int, right: int) -> int:
        return self._sumRange(0, 0, len(self.nums)-1, left, right)

    # Ham tinh tong cac phan tu tren cay ST nam trong cay con goc treeIndex - quan ly doan [l, r] 
    def _sumRange(self, treeIndex: int, l: int, r: int, left: int, right: int):
        # Doan [l, r] va [left, right] ko giao nhau, ta bo qua doan nay
        if l > right or r < left:
            return 0

        # Doan [left, right] chua doan [l, r]  
        if left <= l and r <= right:
            return self.tree[treeIndex]

        # [l, r] giao nhau 1 phan
        mid = (l+r) // 2

        # Goi de quy vs cac node con cua treeIndex
        return self._sumRange(2*treeIndex+1, l, mid, left, right) + self._sumRange(2*treeIndex+2, mid+1, r, left, right)
        


if __name__ == "__main__":
    nums = [18, 17, 13, 19, 15, 11, 20, 12, 33, 25]
    numArr = NumArray(nums=nums)
    print(numArr.tree)
    print(numArr.sumRange(0,3)==sum(nums[0:4]))
    numArr.update(1, 20)
    numArr.update(3, 18)
    numArr.update(6, 22)
    print(numArr.tree)

