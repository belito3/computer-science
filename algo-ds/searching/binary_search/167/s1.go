package main

import "fmt"

func main() {
	s := []int{2, 2, 3, 4, 5, 6, 7}
	fmt.Println(twoSum(s, 10))
}

func twoSum(numbers []int, target int) []int {
	// Binary search
	// Time: nO(logn)
	// Space: O(1)
	for i := 0; i < len(numbers)-1; i++ {
		x := target - numbers[i]
		h, t := i+1, len(numbers)-1

		for t >= h {
			mid := (h + t) / 2

			if numbers[mid] == x {
				return []int{i + 1, mid + 1}
			} else if numbers[mid] < x {
				h = mid + 1
			} else {
				t = mid - 1
			}
		}
	}

	return []int{-1, -1}
}
