package main

import (
	"fmt"
	"math"
)

func main() {
	s := []int{2, 1, 2, 1, 0, 1, 2, 1}
	fmt.Println(maxProfit(s))
}

func maxProfit(prices []int) int {
	// One pass
	// Time: O(n)
	maxFit := 0
	minPrice := math.MaxInt32

	for i := 0; i < len(prices); i++ {
		if prices[i] < minPrice {
			minPrice = prices[i]
		} else if prices[i]-minPrice > maxFit {
			maxFit = prices[i] - minPrice
		}
	}

	return maxFit
}

func maxProfit1(prices []int) int {
	// 1. Brust force
	// time: O(n^2)
	max := 0

	if len(prices) <= 1 {
		return max
	}

	for i := 0; i < len(prices)-1; i++ {
		for j := i + 1; j < len(prices); j++ {
			if prices[i] < prices[j] {
				max = findMax(max, prices[j]-prices[i])
			}
		}
	}
	return max
}

func findMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func findMin(a, b int) int {
	if a > b {
		return b
	}
	return a
}
