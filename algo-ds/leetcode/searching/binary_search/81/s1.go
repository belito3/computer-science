package main

import "fmt"

func main() {
	//nums := []int{2, 5, 6, 0, 0, 1, 2}
	//target := 7
    //nums := []int{2, 2, 2, 0, 2, 2}
    //target := 3
    nums := []int{2, 2, 2, 2, 2, 2}
    target := 2

	fmt.Printf("target = %v, nums = %v, rs = %v \n", target, nums, search(nums, target))
}

func search(nums []int, target int) bool {
    // time: worst O(N), best O(logN)

    size := len(nums)
    if size == 0 {
        return false
    }

    start, end := 0, size - 1

    for start <= end {
        mid := (start + end) / 2
        if nums[mid] == target {
            return true
        }

        // if nums[start] == nums[mid], nums[mid] might belong to both F and S
        // iterators to search target 
        if !isBinarySearchHelpfull(nums, start, nums[mid]) {
            start++
            continue
        }

        // which array does mid belong to
        pivotArray := existsInFirst(nums, start, nums[mid])
        // which array does target belong to
        targetArray := existsInFirst(nums, start, target)

        if pivotArray != targetArray {
            // mid and target lies in different array
            if pivotArray {
                start = mid + 1
            } else {
                end = mid - 1
            }
        } else {
            // mid and target lies in same array
            if nums[mid] < target {
                start = mid + 1
            } else {
                end = mid - 1
            }
        }

    }
    return false
}

func existsInFirst(nums []int, start, element int) bool {
    return element >= nums[start]
}

// neu nums[start] == nums[mid] -> nums[mid] co the nam trong array first or array second
func isBinarySearchHelpfull(nums []int, start, element int) bool {
    return nums[start] != element
}
