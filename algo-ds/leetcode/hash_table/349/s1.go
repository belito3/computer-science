package main

import "fmt"

func main() {
	nums1 := []int{1, 2, 2, 1}
	nums2 := []int{2, 2}

	fmt.Println(intersection(nums1, nums2))
}

func intersection(nums1 []int, nums2 []int) []int {
	// Set
	// Time: O(m + n)
	// Space: O(m + n) in the worst when all elements in the array different
	rs := []int{}

	set := map[int]int{}

	for i := range nums1 {
		set[nums1[i]] = 1
	}

	for i := range nums2 {
		v, ok := set[nums2[i]]
		if v > 0 && ok {
			set[nums2[i]]--
			rs = append(rs, nums2[i])
		}
	}

	return rs
}
