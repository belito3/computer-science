from typing import List

"""
We need explain: Why we choose longest edge is height
    Example: A[A1 <= A2 <= A3] and B[B1 <= B2 <= B3]
    + if A2 now is height: we have A1 <= B1, A2 <= B3, A3 <= B2
    A3 <= B2, B2 <= B3 ->  A3 <= B3
    A2 <= A3 <= B2 -> A2 <= B2
    Can rotate A with A3 (longest edge) is height
    + Similar with A1 is hight
"""

def maxHeight(cuboids: List[List[int]]) -> int:
    # sort cub[i] in ascending order, height is cub[2]
    length = len(cuboids)
    for i in range(length):
        cuboids[i] = sorted(cuboids[i])

    # sort cuboids with height in descending order
    cuboids.sort(reverse=True)

    # cal max_height if put cuboids[i] on top of cuboids[j]
    max_height = [cuboids[i][2] for i in range(length)]

    for i in range(length):
        mini, midi, maxi = cuboids[i][0], cuboids[i][1], cuboids[i][2]
        for j in range(i):
            minj, midj, maxj = cuboids[j][0], cuboids[j][1], cuboids[j][2]
            if mini <= minj and midi <= midj and maxi <= maxj:
                max_height[i] = max(max_height[i], max_height[j] + maxi)

    return max(max_height)



def maxHeight2(cuboids: List[List[int]]) -> int:
    rs = 0
    for i in range(len(cuboids)):
        findMaxInCub(i, cuboids)

    new = sorted(cuboids, reverse=True) # sort in decending order

    sums = []
    print(f"new = {new}")
    calSum(sums=sums, s=0, cuboids=new, pre=-1, curr=0)
    print(f"sums = {sums}")
    return max(sums)

def findMaxInCub(i, cuboids):
    cub = cuboids[i]
    # rearrnage cub with cub[0] is max
    cub = sorted(cub, reverse=True)
   # for j in range(1, len(cub)):
   #     if cub[j] > cub[0]:
   #         # swap cub[j] and cub[0]
   #         cub[0] = cub[j] + cub[0]
   #         cub[j] = cub[0] - cub[j]
   #         cub[0] = cub[0] - cub[j]

    cuboids[i] = cub



def calSum(sums: List[int], s: int, cuboids: List[List[int]], pre: int, curr: int):
    if curr >= len(cuboids):
        sums.append(s)
    else:
        #print(f"pre = {cuboids[pre]}, curr = {cuboids[curr]}, valid = {checkValid(cuboids, pre, curr)}")
        if checkValid(cuboids, pre, curr):
            calSum(sums, s + cuboids[curr][0], cuboids, curr, curr+1) # with current cuboid
        calSum(sums, s, cuboids, pre, curr+1) # without curr cuboids

def checkValid(cuboids: List[List[int]], pre: int, curr: int) -> bool:
    if pre == -1:
        return True

    l1, d1 = cuboids[pre][1], cuboids[pre][2]
    l2, d2 = cuboids[curr][1], cuboids[curr][2]

    if (l1 >= l2 and d1 >= d2) or (l1 >= d2 and d1 >= l2):
        return True

    return False


if __name__ == "__main__":
    cuboids = [[[50,45,20],[95,37,53],[45,23,12]],
              [[38,25,45],[76,35,3]],
              [[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]],
              [[120, 50, 2], [65, 45, 30], [45, 40, 30], [35,35,20]],
              [[80,50,21], [65,45,30],[45,40,25],[35,35,20]],
              [[53,38,26],[32,46,20],[9,20,48],[76,30,73],[81,50,60],[15,31,94],[100,65,50],[97,78,57],[90,41,86],[50,95,44],[60,39,18],[56,39,98],[53,63,58],[61,97,93],[80,26,30],[90,81,93],[93,7,25],[95,75,78]]]
    for cub in cuboids:
        max_height = maxHeight(cub)
        print(f"cuboids = {cub}, maxHeight = {max_height}")
        print("=" * 13)
