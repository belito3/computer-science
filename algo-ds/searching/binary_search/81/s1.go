package main

import "fmt"

func main() {
	nums := []int{2, 5, 6, 0, 0, 1, 2}
	target := 7
	fmt.Printf("target = %v, nums = %v, rs = %v \n", target, nums, search(nums, target))
}

func search(nums []int, target int) bool {
	if len(nums) == 0 {
		return false
	}

	l, r := 0, len(nums)-1
	// find rotated point
	for l < r {
		m := (l + r) / 2
		if nums[m] > nums[r] {
			l = m + 1
		} else {
			r = m
		}
	}

	// l is rotated point
	if nums[l] <= target || len(nums) == 1 {
		// search in (l, len(nums) - 1)
		if bs(nums, l, len(nums)-1, target) {
			return true
		}
	}

	// search in (0, l - 1)
	return bs(nums, 0, l-1, target)
}

func bs(nums []int, l, r, target int) bool {
	for l <= r {
		m := (l + r) / 2
		if nums[m] == target {
			return true
		} else if nums[m] < target {
			l = m + 1
		} else {
			r = m - 1
		}
	}
	return false
}
