from typing import List


def getQueen(N: int) -> List[List[int]]:
    result = []
    column = [0 for i in range(N)]


def placeQueen(result: List[List[int]], N: int, columns: List[int], row: int) -> List[List[int]]:
    if row == N:
        result.append(columns.copy)
    else:
        for col in range(N):
            if checkValid(columns, row, col):
                columns[row] = col
                placeQueen(result, N, columns, row+1)


def checkValid(columns: List[int], row: int, col: int) -> bool:
    # Check row_i, col_i with
    for r in range(row):
        c = columns[r]
        if c == col:
            return False

        distance = abs(col - c)
        if abs(row -r) == distance:
            return False
    return True
