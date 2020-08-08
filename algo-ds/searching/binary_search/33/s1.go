package main

import "fmt"

func main() {
	//s := []int{4, 5, 6, 7, 0, 1, 2}
	//s := []int{7, 6, 5, 4, 3, 2, 1, 0}
	s := []int{4}
	//s := []int{1, 2, 3, 4, 5, 6, 7}
	//s := []int{7, 0, 1, 2, 3, 4, 5, 6}
	target := 4
	fmt.Printf("target= %v, %v : %v \n", target, s, search1(s, target))
}

func search(nums []int, target int) int {
	// time: O(logn)
	// space: O(1)

	// find index roated - min value
	h, t := 0, len(nums)-1
	for t > h {
		m := (h + t) / 2
		if nums[m] > nums[t] {
			h = m + 1
		} else {
			t = m
		}
	}

	fmt.Println("ro: ", h)
	ro := h
	// find interval to search
	if target <= nums[len(nums)-1] {
		h = ro
		t = len(nums) - 1
	} else {
		h = 0
		t = ro - 1
	}
	fmt.Println("h=", h, " t=", t)

	// search
	for t >= h {
		m := (t + h) / 2
		if nums[m] == target {
			return m
		} else if nums[m] > target {
			t = m - 1
		} else {
			h = m + 1
		}
	}

	return -1
}

func search1(nums []int, target int) int {
	// time: O(n)
	// space: O(1)
	// S1: find index pivot rotated then search
	l1, l2, l3 := 0, 0, len(nums)-1

	for i := 0; i < len(nums); i++ {
		if nums[i] == target {
			return i
		} else if (i > 0) && (nums[i] < nums[i-1]) {
			l2 = i
		}
	}

	// search in l1l2
	t := l2
	for t >= l1 {
		m := (t + l1) / 2
		if nums[m] == target {
			return m
		} else if nums[m] < target {
			l1 = m + 1
		} else {
			t = m - 1
		}
	}

	// search in l2l3
	for l3 >= l2 {
		m := (l2 + l3) / 2
		if nums[m] == target {
			return m
		} else if nums[m] < target {
			l2 = m + 1
		} else {
			l3 = m - 1
		}
	}
	return -1
}
