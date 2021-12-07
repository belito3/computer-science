from typing import List

def get_parens(num: int) -> List[int]:
    arr = []
    str_ = ["" for i in range(num*2)]
    make_parens(arr, str_, num, num, 0)
    return arr

def make_parens(arr: List[str], str_, leftRe, rightRe, index):
    if leftRe < 0 or leftRe > rightRe:
        return

    if leftRe == 0 and rightRe == 0:
        arr.append("".join(str_))
    else:
        str_[index] = "("
        make_parens(arr, str_, leftRe-1, rightRe, index+1)

        str_[index] = ")"
        make_parens(arr, str_, leftRe, rightRe-1, index+1)


def get_parens3(num: int) -> List[int]:
    rs  = make_parens(num, num)
    return [r[0] for r in rs]


def make_parens3(num: int, limit: int) -> List[int]:
    # DP + count num open and close parenthesis
    if num == 0:
        return [("", 0, 0)]

    rs = make_parens(num-1, limit)
    while rs[0][1] < num or rs[0][2] < num:
        rs_temp = []
        for e in rs:
            p = e[0]
            open_ = e[1]
            close_ = e[2]
            if (open_ == close_):
                rs_temp.append((p+"(", open_+1, close_))
            elif open_ <= limit and open_ > close_:
                if open_ < limit:
                    rs_temp.append((p+"(", open_+1, close_))
                rs_temp.append((p+")", open_, close_+1))
        rs = rs_temp
    return rs_temp


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
    for i in range(5):
        rs = get_parens(i)
        print(f"i={i}: {rs}")



