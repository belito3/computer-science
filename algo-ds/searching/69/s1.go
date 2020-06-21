package main

import (
    "fmt"
)

func main(){
    var s [20]int
    for i := 0; i < 20; i++ {
        s[i] = i 
    }
    for i, x := range s {
        fmt.Println(i, mySqrt(x))
    }
}

func mySqrt(x int) int {
    // Binary search
    // Time: O(logn)
    // Space: O(1)
    head := 0
    tail := x 
    mid := tail - head / 2

    for tail > head {
         p1 := mid * mid
         p2 := (mid + 1) * (mid + 1)
         if p1 <= x && p2 > x {
            return mid 
        } else if p1 < x {
            head = mid + 1
            mid += (tail - mid) / 2
        } else if p1 > x {
            tail = mid - 1
            mid = (mid - 0) / 2
        }
    }

    return head
}
