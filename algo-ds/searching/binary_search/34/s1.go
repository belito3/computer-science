package main

import "fmt"

func main() {
	//s := []int{6}
	//s := []int{4}
	//s := []int{5, 7, 7, 8, 8, 10, 10}
	s := []int{5, 7, 7, 8, 8, 10}
	target := 8
	fmt.Printf("%v, %v, %v \n", target, s, searchRange(s, target))
}

func searchRange(nums []int, target int) []int {
	// S3: 2 bs
	l, r := 0, len(nums)-1
	rs := []int{-1, -1}

	// find last position
	for r >= l {
		m := (l + r) / 2
		if nums[m] <= target {
			l = m + 1
		} else {
			r = m - 1
		}
	}

	if l > 0 && nums[l-1] == target {
		rs[0] = l - 1
		rs[1] = l - 1
	}

	// find first position
	l, r = 0, len(nums)-1
	for r >= l {
		m := (l + r) / 2
		if nums[m] >= target {
			r = m - 1
		} else {
			l = m + 1
		}
	}
	if r < len(nums)-2 && nums[r+1] == target {
		rs[0] = r + 1
	}

	return rs
}

func searchRange2(nums []int, target int) []int {
	// s2: 3 bs
	start, end := -1, -1
	left, right := 0, len(nums)-1

	for left <= right {
		mid := (left + right) / 2
		//fmt.Printf("mid=%v, left=%v, right=%v \n", mid, left, right)
		if nums[mid] == target {
			start = mid
			end = mid
			// find start: (left, start)
			for left < start {
				tmp := (left + start) / 2
				if nums[tmp] == target {
					start = tmp
				} else {
					// nums[tmp] < target
					left = tmp + 1
				}
			}

			// find end: from end + 1 to  right
			for end < right {
				tmp := (end + 1 + right) / 2
				if nums[tmp] == target {
					end = tmp
				} else {
					// nums[tmp] > target
					right = tmp - 1
				}
			}
			return []int{start, end}
		} else if nums[mid] < target {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}

	return []int{start, end}
}

func searchRange1(nums []int, target int) []int {
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
