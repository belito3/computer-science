package main

import "fmt"
import "math"

func main() {
	s := []int{1, 2, 3, 4, 2, 3, 0, 3}
	fmt.Println(maxProfit(s))
}

func maxProfit(prices []int) int {
	// One Pass solution
	// time: O(n)
	// space: O(1)
	if len(prices) == 0 {
		return 0
	}

	oneBuy := math.MaxInt32
	profitOne := 0
	twoBuy := math.MaxInt32
	profitTwo := 0

	for i := 0; i < len(prices); i++ {
		oneBuy = findMin(oneBuy, prices[i])
		profitOne = findMax(profitOne, prices[i]-oneBuy)
		twoBuy = findMin(twoBuy, prices[i]-profitOne)
		profitTwo = findMax(profitTwo, prices[i]-twoBuy)
	}

	return profitTwo
}

func findMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func findMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}
