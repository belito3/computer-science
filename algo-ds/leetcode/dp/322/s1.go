package main

import "fmt"

func main() {
	coins := []int{1,2,5}
	amount := 11
	fmt.Printf("coins = %d amount = %d rs = %d\n", coins, amount, coinChange(coins, amount))
}

/*
S1: Recursive - Time 2^x
count(coins, m, amount) = min{count(coins, m-1, amount), count(coins, m-1, amount - couns[m-1]) + 1}
*/

func coinChange(coins []int, amount int) int {
	// S2: DP Optimal Substructure
	// dp[i] is fewest number of conis that we need to make up that i
	// dp[i] = min{dp[i-cj]} + 1 ; cj = coins[j]
	// Time: O(len(coins) * amount)
	// Space: O(amount)
	if amount < 1 {
		return 0
	}

	dp := make([]int, amount+1)
	for i := 1; i <= amount; i++ {
		dp[i] = 1000000
	}

	for i := 0; i < len(coins); i++ {
		for j := coins[i]; j <= amount; j++ {
			dp[j] = min(dp[j], dp[j-coins[i]] + 1)
		}
	}
	if dp[amount] > amount {
		return -1
	}
	return dp[amount]
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}
