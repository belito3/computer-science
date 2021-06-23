package main

import "fmt"

func main() {
	input := [][]int{{2,4,3,9,1,5}, {2,4,3,9,3,5}, {3,3,5,0,0,3,1,4}}
	for _, i := range(input) {
		fmt.Printf("i = %v  rs = %v\n", i, maxProfit(i))
	}
}

func maxProfit(prices []int) int {
	/* 
	Cach giai tong quat voi k transaction, i day
	https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/39608/A-clean-DP-solution-which-generalizes-to-k-transactions
	https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/135704/Detail-explanation-of-DP-solution
	*/
}
func maxProfit1(prices []int) int {
	// brute force
	// Time: O(n*2)
	if len(prices) <= 2 {
		return findMax(prices)
	}
	max := 0

	for i := 2; i < len(prices); i++ {
		max1 := findMax(prices[0:i])
		max2 := findMax(prices[i:])
		if max1 + max2 > max {
			max = max1 + max2
		}
	}
	return max
}

func findMax(prices []int) int {
    if len(prices) <= 1 {
        return 0
    }

    maxFit := 0
    minPrice := prices[0]
    for i := 0; i < len(prices); i++ {
        if prices[i] < minPrice {
             minPrice = prices[i]
         } else if prices[i]-minPrice > maxFit {
             maxFit = prices[i] - minPrice
         }
    }
    return maxFit
}


