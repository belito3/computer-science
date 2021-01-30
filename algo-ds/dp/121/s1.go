package main

import (
	"fmt"
)

func main() {
	input := [][]int{{7,1,5,3,6,4}, {7,6,4,3,1}, {2,3,2,2}, {3,3,5,0,0,3,1,4}, {3,2,6,5,0,3}}
	for _, i := range(input) {
		fmt.Printf("i=%v rs=%v\n", i, maxProfit(i))
	}
}

func maxProfit(prices []int) int {
	mProfix := 0
	if len(prices) < 2 {
		return mProfix
	}

	min := prices[0]
	for i := 1; i < len(prices); i++ {
		p := prices[i] - min
		if p > mProfix {
			mProfix = p
		} else if p < 0 {
			min = prices[i]
		}
	}
	return  mProfix
}
