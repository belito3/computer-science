//https://www.geeksforgeeks.org/coin-change-dp-7/
package main

import "fmt"

func main() {
    coins := []int{1,2,3}
    amount := 4
    fmt.Printf("coins = %d, amount = %d, count = %d\n", coins, amount, coinChange(coins, amount))
}


func coinChange(coins []int, amount int) int {
    // S2: Overlapping substructure - bottom up 
    // Tuong tu bai stair step - cong thuc fobinacci 
    // dp[i] wil be storing the number of solutions for value i. 
    // dp[i] = dp[i-coins_0] + dp[i-coins_1] + ... + dp[i-coins_n-1]
    //  + dp[i-coins_j] = 0 with i - coins_j < 0
    dp := make([]int, amount+1)
    dp[0] = 1 
    for i := 0; i < len(coins); i++ {
        for j := coins[i]; j <= amount; j++ {
            dp[j] += dp[j-coins[i]]
        }
    }
    return dp[amount]
}


func coinChange2(coins []int, amount int) int {
    // S2: Overlapping substructure - bottom up(From formular recursive 's S1)
    // dp[i][j]: i = 0 -> m, j = 0 -> n 
    // if A[i] > j: dp[i][j] = dp[i-1][j]
    // else: dp[i][j] = dp[i-1][j] + dp[i][j - A[j]]
    // Time: len(coins) * amount
    // Space: len(coins) * amount
    m := len(coins)
    dp := make([][]int, m+1)
    for i:= 0; i < m+1; i++ {
        dp[i] = make([]int, amount+1)
    }

    for i := 0; i <= m; i++ {
        dp[i][0] = 1
    }

    //for i := 0; i <= amount; i++ {
    //    dp[0][i] = 1
    //}

    for i := 1; i <= m; i++ {
        for j := 1; j <= amount; j++ {
            fmt.Println(i, j)
            if coins[i-1] > j {
                dp[i][j] = dp[i-1][j]
            } else {
                dp[i][j] = dp[i-1][j] + dp[i][j - coins[i-1]]
            }
        }
    }
    fmt.Println(dp)
    return dp[m][amount]
}

func coinChange1(coins []int, amount int) int {
    // S1: recursive
    // Time: O(2^n)
    return count(coins, len(coins)-1, amount)
}

func count(coins []int, m, amount int) int {
    if amount == 0 {
        return 1
    }

    if amount < 0 || m < 0 {
        return 0
    }

    // co it nhat 1 phan tu m la so hang tham gia vao tong
    // hoac ko co phan tu m tham gia vao trong tong 
    return count(coins, m, amount - coins[m]) + count(coins, m-1, amount)
}
