package main

import "fmt"

func main(){
    //s := []int{4, 5, 6, 7, 0, 1, 2}
    //s := []int{2, 2, 2, 0, 2, 2, 2}
    //s := []int{2}
    s := []int{2, 2,2, 0}
    //s := []int{3, 2}
    fmt.Printf("s = %v, min = %v\n", s, findMin(s))
}

func findMin(nums []int) int {
   if len(nums) == 0 {
        return 0
   }

   last := len(nums) - 1
   min := nums[last]
   left, right := 0, last

   for left <= right {
       mid := (left + right) / 2

       if nums[mid] > nums[last] {
           // mid lies in array 1
           left = mid + 1
       } else {
           // mid and min lies in array 2 
           if nums[mid] < min {
               min = nums[mid]
           }
           right -= 1
       }
   }
   return min
}


