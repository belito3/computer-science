package main

import "fmt"

func main() {
	nums := []int{-2, 1, -3, 4, -1, 2, 1, -5, 4}
	fmt.Println(maxSubArray(nums))
}

func maxSubArray(nums []int) int {
	if len(nums) == 1 {
		return nums[0]
	}
	for i := 1; i < len(nums); i++ {
		if nums[i-1] > 0 {
			nums[i] += nums[i-1]
		}
	}

	max := nums[0]
	for _, v := range nums {
		if v > max {
			max = v
		}
	}

	return max
}

func maxSubArray2(nums []int) int {
	// Approach 2: Kadane's algorithm
	// Time: O(n)
	// Space: O(1)

	if len(nums) == 1 {
		return nums[0]
	}

	max := nums[0]
	localMax := nums[0]

	for i := 1; i < len(nums); i++ {
		localMax = getMax(nums[i], nums[i]+localMax)
		if localMax > max {
			max = localMax
		}
	}

	return max

}

func getMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func maxSubArray1(nums []int) int {
	// Approach 1; Brute force
	// Time: O(n^2)
	// Space: O(1)
	max := nums[0]
	for i := 0; i < len(nums)-1; i++ {
		for j := i + 1; j < len(nums); j++ {
			sum := getSum(nums[i:j])
			if sum > max {
				max = sum
			}
		}
	}

	return max
}

func getSum(nums []int) int {
	s := 0
	for _, v := range nums {
		s += v
	}
	return s
}
