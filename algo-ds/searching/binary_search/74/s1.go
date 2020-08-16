package main

import "fmt"

func main() {
	mat := [][]int{{1, 3, 5, 7},
		{10, 11, 16, 20},
		{23, 30, 34, 50}}
	target := 25
	fmt.Printf("target = %v, mat = %v, rs = %v\n", target, mat, searchMatrix(mat, target))
}

func searchMatrix(matrix [][]int, target int) bool {
	// time: nlogm
	// space: 1
	for i := 0; i < len(matrix); i++ {
		nums := matrix[i]
		if len(nums) == 0 {
			return false
		}

		if nums[len(nums)-1] >= target {
			if bs(nums, target) {
				return true
			}
		}
	}

	return false
}

func bs(nums []int, target int) bool {
	l, r := 0, len(nums)-1
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
