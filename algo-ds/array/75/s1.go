package main

import "fmt"

func main(){
    s := []int{1, 1, 0, 0, 2, 0, 1, 2, 1}
    //s := []int{2,1,2}
    //s := []int{1,0,0}
    //s := []int{2, 0, 2, 1, 1, 0}
    //s := []int{2,2}
    //s := []int{0,0,0}
    //s := []int{1,2,0}
    fmt.Println(s)
    sortColors(s)
    fmt.Println(s)
}

func sortColors(nums []int){
    last0 := 0
    first2 := len(nums) - 1

    for i := 0; i < len(nums); i++ {
        if  i > first2 {
            break
        }

        if nums[i] == 0 {
            swap(nums, i, last0)
            last0++
            fmt.Println("detect 0: ", nums)
        } else if nums[i] == 2 {
            // find nums != 2
            for nums[first2] == 2 && first2 > i{
                first2--
            }

            if nums[first2] == 2 {
                break
            }

            swap(nums, i, first2)
            if nums[i] == 0 {  
                i--
            }
            
            first2--
            fmt.Println("detect 2: ", nums)
        }
    }
}


func swap(nums []int, i int, j int){
    // swap without use intermediate variable
    nums[i] = nums[i] + nums[j]
    nums[j] = nums[i] - nums[j]
    nums[i] = nums[i] - nums[j]
}



