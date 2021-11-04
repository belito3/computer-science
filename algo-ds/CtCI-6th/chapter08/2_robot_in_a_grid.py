from typing import List


def uniquePaths(m, n) -> int:
    # DP: tabulation
    table = [[0] * n] * m
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                table[i][j] = 1
            else:
                table[i][j] = table[i-1][j] + table[i][j-1]
    return table[m-1][n-1]


def uniquePaths2(m, n) -> int:
    table = [[0 for i in range(n)] for j in range(m)]
    rs = uniquePaths_helper(m-1, n-1, table)
    print(table)
    return rs

def uniquePaths_helper(m: int, n: int, table: List[List[int]]) -> int:
    if m == 0 or n == 0:
        return 1

    if table[m][n] != 0:
        return table[m][n]

    table[m][n] = uniquePaths_helper(m-1, n, table) + uniquePaths_helper(m, n-1, table)
    return table[m][n]


if __name__ == "__main__":
    m = 3
    n = 7
    print(uniquePaths2(m, n))
