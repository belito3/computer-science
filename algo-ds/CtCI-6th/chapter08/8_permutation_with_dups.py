from typing import Set, List


def permutation(string: str):
    # Space: O(n!)
    # Time: O(n!)
    rs = set()
    return permutation_helper(string, 1, len(string), rs)

def permutation_helper(string: str, end: int, length: int, rs: Set[int]):
    if end > length:
        return rs

    if end == 1:
        rs = (str(string[0:end]))
    else:
        char = string[end-1:end]
        rs_temp = set()
        for string2 in rs:
            for i in range(len(string2)+1):
                new_string = string2[0:i] + char + string2[i:len(string2)]
                rs_temp.add(str(new_string))
        rs = rs_temp

    return permutation_helper(string, end+1, length, rs)


if __name__ == "__main__":
    strings = ["a", "aab", "aabb"]
    for string in strings:
        print("=" * 6)
        print(f"input = {string}")
        rs = permutation(string)
        print(f"string = {string}, rs = {rs}")
