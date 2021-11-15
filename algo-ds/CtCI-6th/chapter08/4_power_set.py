from typing import List

def power_set(arr: List[int]) -> List[List[int]]:
    rs = []

    for a in arr:
        temp = []
        for a2 in rs:
            print(f"a2 = {a2}")
            a3 = a2.append(a)
            temp.append(a3)
        rs.append([a])
        print(rs)
        if len(temp) > 0:
            rs.append(temp)

    return rs


if __name__ == "__main__":
    input_ = [1, 2, 3]
    rs = power_set(input_)
    print(rs)

