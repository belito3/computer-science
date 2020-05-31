package main

import "fmt"

func main() {
	s := []int{0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3}
	fmt.Println(s)
	fmt.Println(removeDuplicates(s))
	fmt.Println(s)
}

func removeDuplicates(nums []int) int {
	i := 0
	for _, n := range nums {
		if i < 2 || n > nums[i-2] {
			nums[i] = n
			i++
		}
	}
	return i
}

func removeDuplicates1(nums []int) int {
	// brute force
	l := len(nums)
	if l <= 2 {
		return l
	}

	cnt := 1
	curr := nums[0]

	for i := 1; i < l; i++ {
		if nums[i] == curr {
			cnt++
			if cnt > 2 {
				// move num[i] to last arr
				for j := i + 1; j < len(nums); j++ {
					swap(nums, j-1, j)
				}
				cnt--
				l--
				i--
			}
		} else {
			cnt = 1
			curr = nums[i]
		}
	}

	return l
}

func swap(nums []int, i int, j int) {
	nums[i] = nums[i] + nums[j]
	nums[j] = nums[i] - nums[j]
	nums[i] = nums[i] - nums[j]
}
