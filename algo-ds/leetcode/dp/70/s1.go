package main

import (
    "fmt"
)

func main() {
    for i := 1; i < 10; i++ {
        fmt.Printf("n=%d rs=%d\n", i, climbStairs(i))
    }
}

func climbStairs(n int) int {
    // S2: Fibonacci: F(0) = F(1) = 1, F(n) = F(n-1) + F(n-2)
    // Time: O(n)
    // Space: O(1)
    /*
        Explaintation:
        One can reach i step in one of the two ways:
            1. Taking a single step from (i-1) step
            2. Taking a step of 2 from (i-2) step
        The total number of ways to reach i is equal to sum of reaching (i-1) step and way of reaching (i-2) step
        dp[i] = dp[i-1] + dp[i-2]
        The solutions calculated by the above approach are complete and non-redundant. The two solution sets (n1 and n2) cover all the possible cases on how the final step is taken. And there would be NO overlapping among the final solutions constructed from these two solution sets, because they differ in the final step
        Intuition:
                         0,5
                       /     \
                     1,5      2,5
                    /   \      /  \
                  2,5   3,5   3,5  4,5
                /  \   /  \    /  \   /  \
              3,5 4,5 4,5 5,5 4,5 5,5 5,5  6,5

    */
    if n <= 1 {
        return 1
    }
    cur := 1
    prev := 1
    rs := 0

    for i := 1; i < n; i++ {
        rs = cur + prev
        prev = cur
        cur = rs
    }
    return cur
}

func climbStairs1(n int) int {
    // S1: Brute force
    // 
    /*
        Call x is number of 2, y is number of 1 
        --> 2x + y = n -> x = (n - y) / 2
            + x, y >= 0 --> x = 0, n/2 and y = n - 2*x
            The number of arranements into x + y possitions where x element 2 and y element 1 are: 
                        (x+y)! / x!y! = (n - x) / x!(n-2*)! 
        x: number 2 
        y: number 1
    */
    sum := 0
    for x := 0; x <= n/2; x++ {
        // y = n - 2*x -> x+y = n - x
        sum += factorial(n-x)/(factorial(x) * factorial(n - 2*x))
    }
    return sum
}

func factorial(n int) int {
    rs := 1
    for i := 1; i <=n; i++ {
        rs *= i
    }
    return rs
}
