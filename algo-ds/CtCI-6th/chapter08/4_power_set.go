package main

import "fmt"


func main() {
    input_ := []int{1, 2, 3} 
    fmt.Println(powerSet(input_))
}

func powerSet(arr []int) [][]int {
    // Time and space: O(n*2^n)
    // 2^n subset and n is maximum number element of set
    rs := make([][]int, 0)

    for _, a1 := range arr {
        for _, a2 := range rs {
            a3 := append(a2, a1) 
            fmt.Println(a3)
            rs = append(rs, a3)
        }
        rs = append(rs, []int{a1})
    }
    return rs
}
