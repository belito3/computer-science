package main

import "fmt"

func main() {
	//s := []int{6}
	//s := []int{4}
	s := []int{5, 7, 7, 8, 8, 10}
	target := 10
	fmt.Printf("%v, %v, %v \n", target, s, searchRange(s, target))
}

func searchRange(nums []int, target int) []int {
	start, end := -1, -1
	h, t := 0, len(nums)-1

	for t >= h {
		mid := (h + t) / 2
		if nums[mid] == target {
			// find start
			for a := mid; a >= 0 && nums[a] == target; a-- {
				start = a
			}
			// find end
			for a := mid; a <= len(nums)-1 && nums[a] == target; a++ {
				end = a
			}
			return []int{start, end}

		} else if nums[mid] < target {
			h = mid + 1
		} else {
			t = mid - 1
		}
	}

	return []int{start, end}
}
