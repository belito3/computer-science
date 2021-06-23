package main

import "fmt"

func main(){
    nums1 := []int{1,1,0}
    m := 2
    nums2 := []int{2}
    n := 1
    merge(nums1, m, nums2, n)
}


func merge(nums1 []int, m int, nums2 []int, n int){
    i := 0
    j := 0
    last := m 

    for i < m + n && j < n {
        if nums1[i] > nums2[j]{
            shift1(nums1, i)
            nums1[i] = nums2[j]
            j += 1
            last += 1
        }
        i += 1
    }

    for j < n{
        nums1[last] = nums2[j]
        j += 1
        last += 1
    }
    fmt.Println("nums1", nums1)

}

func shift1(nums []int, i int){
    j := len(nums) - 1
    for j > i {
        nums[j] = nums[j-1]
        j -= 1
    } 
}


