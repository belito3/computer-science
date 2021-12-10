from typing import List

def coins(num: int) -> int:
    mem = [0 for i in range(num+1)]
    # Init mem[0->4] = 1
    v_init = 5
    if num + 1 < v_init:
        v_init = num+1
    for i in range(v_init):
        mem[i] = 1

    return num_way(num, mem)
    
    
def num_way(num: int, mem: List[int]) -> int:
    if mem[num] != 0:
        return mem[num]

    f1, f5, f10, f25 = 0, 0, 0, 0
    if num >= 25:
        f25 = num_way(num-25, mem)

    if num >= 10:
        f10 = num_way(num-10, mem)

    if num >= 5:
        f5 = num_way(num-5, mem)

    if num >= 1:
        f1 = num_way(num-1, mem)

    return f1 + f5 + f10 + f25 


"""
f(n) = f(n-1) + f(n-5) + f(n - 10) + f(n - 25)
f0 = 1
f1-4 = 1
f(5) = f(4) + f(0) = 2 
f(6) = f(5) + f(1) = 3

"""

if __name__ == "__main__":
    for i in range(30):
        rs = coins(i)
        print(f"coins = {i}, rs = {rs}")
