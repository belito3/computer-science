def num_step(n: int):
    # Time: O(n)
    # Space: O(1)
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    a, b, c = 0, 1, 2
    for i in range(3, n+1):
        temp = a + b + c
        a = b
        b = c
        c = temp
    return c


if __name__ == "__main__":
   n = 5
   print(num_step(5))

