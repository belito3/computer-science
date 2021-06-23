package main

import "fmt"

func main() {
	nums := []int{-1, 0, 1, 2, -1, -4}
	fmt.Println(threeSum(nums))
}

func threeSum(nums []int) [][]int {
	rs := make([][]int, 0)
	for i := 0; i < len(nums)-3; i++ {
		for j := i + 1; j < len(nums)-2; j++ {
			for k := j + 1; k < len(nums)-1; k++ {
				if nums[i]+nums[j] == -nums[k] {
					rs = append(rs, []int{nums[i], nums[j], nums[k]})
				}
			}

		}
	}
	return rs
}
