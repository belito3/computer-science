package main

import "fmt"

func main() {
	s := []int{1, 2, 3, 4, 5}
	fmt.Println(maxProfit(s))

}

func maxProfit(prices []int) int {
	max := 0

	if len(prices) <= 1 {
		return max
	}

	for i := 1; i < len(prices); i++ {
		if prices[i] > prices[i-1] {
			max += prices[i] - prices[i-1]
		}
	}

	return max
}
