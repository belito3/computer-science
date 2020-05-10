package main

import "fmt"

func main(){
    s := []int{1, 2, 3, 4, 5, 6, 7}
    k := 9 
    rotate(s, k)
    fmt.Println(s)
}

func rotate(nums []int, k int) {
    // Cyclic replacements
    // Time: O(n)
    // Space: O(1)
    length := len(nums) 
    k = k % length
    cnt := 0
    for start := 0; cnt < length; start++ {
        current := start        
        temp_num := nums[start] // store number previous to swap later
        for {
            next_id := (current + k) % length 
            // swap temp with nums[next_id]
            temp := nums[next_id]
            nums[next_id] = temp_num
            temp_num = temp
            current = next_id 
            cnt++

            if current == start {
                break
            }
        }
    }
}

func rotate2(nums []int, k int) {
    // using extra slice 
    // time: O(n)
    // space: O(k)
    length := len(nums)
    k = k % length
    s := make([]int, k) // sotre last k element of s 
    for i := 0; i < k; i++ {
        s[i] = nums[length - k + i]
    }

    for i := length - 1; i >= k; i-- {
        nums[i] = nums[i - k]
    }

    for i := 0; i < k; i++ {
        nums[i] = s[i]
    } 
}

func rotate1(nums []int, k int) {
    k = k % len(nums)
    // Brute force
    // time: O(kn)
    // space: O(1)
    for i := 0; i < k; i++ {
        j := len(nums) - 1
        tmp := nums[j]
        for j > 0 {
            nums[j] = nums[j - 1]
            j--
        }
        nums[0] = tmp
    }
}

