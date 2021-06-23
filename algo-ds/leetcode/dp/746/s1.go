package main

import "fmt"

func main() {
	input := [][]int{{10,15,20}, {1, 100, 1, 1, 1, 100, 1, 1, 100, 1}, {10,15}, {0, 2, 2, 1}}
	for _, i := range(input) {
		fmt.Printf("i = %v rs = %v\n", i, minCostClimbingStairs(i))
	}
}

func minCostClimbingStairs(cost []int) int {
	l := len(cost)

	for i := 2; i < l; i++ {
		cost[i] = findMin(cost[i] + cost[i-1], cost[i] + cost[i-2])
	}
	return findMin(cost[l-1], cost[l-2])
}

func findMin(a, b int) int {
	if a > b {
		return b
	}
	return a
}


