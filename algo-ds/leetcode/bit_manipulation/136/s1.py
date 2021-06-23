from typing import List

class Solution:
    # solution 1: List
    # time: O(n)
    # space: O(n)
    def singleNumber1(self, nums: List[int]) -> int:
        list_no_duplicate = [] # space O(n)

        for val in nums: # O(n)
            # if val not in list_no_duplicate: # O(n)
            #     list_no_duplicate.append(val) # O(1)
            # else:
            #     list_no_duplicate.remove(val) # O(n/2) (TH xau nhat length = n/2)
            try:
                list_no_duplicate.remove(val) # O(n)
            except:
                list_no_duplicate.append(val)
        return list_no_duplicate.pop() # O(1)

    # solution 2: hash table
    # time: O(n)
    # space: O(n)
    def singleNumber2(self, nums: List[int]) -> int:
        d = set()

        for val in nums: # O(n)
            try:
                d.remove(val) # O(1)
            except:
                d.add(val) # O(1)
        return d.pop() # O(1)

    # solution 3: Math. 2 * (a+b+c) - (2*a + 2*b + c)
    # time: O(n)
    # space: O(n). set need space for elements in nums
    def singleNumber3(self, nums: List[int]) -> int:
        # sum: O(n)
        return 2*sum(set(nums)) -  sum(nums) # O(n + n + n) = O(n)

    # solution 4: Bit Manipulation
    # time: O(n)
    # space: O(1)
    def singleNumber4(self, nums: List[int]) -> int:
        a = 0
        for val in nums:
            a = a ^ val
        return a

s = Solution()
print(s.singleNumber4([4,2,1,2,1]))
