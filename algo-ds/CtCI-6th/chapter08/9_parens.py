from typing import List

def get_parens(num: int) ->  List[int]:
    rs = []
    return make_parens(rs, num)

def make_parens(rs, num):
    if num <= 0:
        rs = [("", 0, 0)] # prefix, open parenthesis, close parenthesis

    rs_temp = []
    for i in range(len(rs)):
        p, open_, close_ = rs[i][0], rs[i][1],  rs[i][2]

        if open_ == close_:
            if open_ == num:
                rs_temp.append(rs[i])
            else: # open < num
                rs_temp.append((p + "(", open_+1, close_))
        elif open_ > close_:
            rs_temp.append((p + "(", open_+1, close_))
            rs_temp.append((p + ")", open_, close_+1))

    rs = rs_temp

    done = (rs[0][1] == num) and (rs[0][2] == num)
    print(f"open {rs[0][1]} , close {rs[0][2]}, num = {num}, done = {done}")
    if not done:
        rs = make_parens(rs, num)
    return rs

if __name__ == "__main__":
    for i in range(4):
        rs = get_parens(i)
        print(f"i={i}: {rs}")



