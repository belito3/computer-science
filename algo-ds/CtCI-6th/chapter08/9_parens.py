from typing import List

def get_parens(num: int) -> List[int]:
    pass


def make_parens(num: int) -> List[int]:
    if num == 0:
        return [("", 0, 0)]

    rs = make_parens(num-1)
    for


def get_parens2(num: int) ->  List[int]:
    rs = make_parens(num)
    return list(rs)


def make_parens2(num: int):
    # DP with hash table
    # Time: O(2^n)
    # Space: O(2^n)
    if num <= 1:
        return {"()"}

    rs = make_parens(num-1)
    rs_temp = set()
    for p in rs:
        for i in range(len(p) + 1):
            str_ = str(p[0:i] + "()" + p[i:])
            rs_temp.add(str_)
    return rs_temp



def make_parens1(num):
    # S1: Brute force
    # Time: O(2^n/2 -> 2^n)  -> Only need select position for open parenthesis "("
    # Space: O(2^n/2 -> 2^n)
    rs = [("", 0, 0)]
    if num <= 0:
         # prefix, open parenthesis, close parenthesis
        return rs

    while (rs[0][1] < num) or (rs[0][2] < num):
        rs_temp = []
        for i in range(len(rs)):
            p, open_, close_ = rs[i][0], rs[i][1],  rs[i][2]

            if open_ == close_:
                if open_ == num:
                    rs_temp.append(rs[i])
                else: # open < num
                    rs_temp.append((p + "(", open_+1, close_))
            elif open_ > close_:
                if open_ < num:
                    rs_temp.append((p + "(", open_+1, close_))
                if close_ < num:
                    rs_temp.append((p + ")", open_, close_+1))
        rs = rs_temp
    return rs

if __name__ == "__main__":
    for i in range(4):
        rs = get_parens(i)
        print(f"i={i}: {rs}")



