package main

import (
    "fmt"
)

func main(){
    s := []int{1, 2, 4, 5}
    target := 0 
    fmt.Println(searchInsert(s, target))
}


func searchInsert(nums []int, target int) int {
    head := 0
    tail := len(nums) - 1

    if target > nums[tail] {
        return len(nums)
    }

    if target < nums[head] {
        return head
    }

    for tail >= head {
        mid := head + (tail - head) / 2  // div 
        if nums[mid] == target {
            return mid
        }

        if nums[mid] < target {
            head = mid + 1
        } else {
            tail = mid - 1
        }
    }

    return head
}
