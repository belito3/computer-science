from typing import List

def maxHeight(cuboids: List[List[int]]) -> int:
    rs = 0
    for i in range(len):
        findMaxInCub(i, cuboids)

    return

def findMaxInCub(i, cuboids):
    cub = cuboids[i]
    # rearrnage cub with cub[0] is max
    for j in range(1, len(cub)):
        if cub[j] > cub[0]:
            # swap cub[j] and cub[0]
            cub[0] = cub[j] + cub[0]
            cub[j] = cub[0] - cub[j]
            cub[0] = cub[0] - cub[j]

    cubids[i] = cub



def calSum(sums: List[int], s, height, index1, index2):
    if index2 > len(height):
        sums.append(s)
    else:
