//https://www.spoj.com/problems/COINS/
package main

import "fmt"

func main() {
    for i := 0; i < 10; i++ {
        fmt.Printf("i = %d, p = %d\n", i, maxCoinProfit(i))
    }
    //fmt.Println(maxCoinProfit(12))
}

func maxCoinProfit(n int) int {
    dp := make([]int, n+1)

    for i := 1; i <= n; i++ {
        dp[i] = findMax(i, i/2 + i/3 + i/4)
    }
    return dp[n]
}

func findMax(a, b int) int {
    if a > b {
        return a
    }
    return b
}
