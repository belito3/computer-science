package main

import (
	"fmt"
)

func main() {
	height := []int{1, 8, 6, 2, 5, 4, 8, 3, 7}
	a := maxArea(height)
	fmt.Println(a)
}

func maxArea(height []int) int {
	// two pointer approach
	// time: O(n)
	max := 0
	s := 0

	for i, j := 0, len(height)-1; i != j; {
		s = min(height[i], height[j]) * (j - i)
		if s > max {
			max = s
		}

		if height[i] > height[j] {
			j -= 1
		} else {
			i += 1
		}
	}

	return max
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}
