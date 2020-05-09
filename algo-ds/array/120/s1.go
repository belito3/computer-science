package main

import "fmt"


func main(){
    in := [][]int{{2}, {3,4}, {6,5,6}, {4,1,8,3}}
    fmt.Println(minimumTotal(in))
}

func minimumTotal(triangle [][]int) int {
    sum := 0
    for i := 0; i < len(triangle); i += 1 {
        sum += findMin(triangle[i])
    } 
    return sum
}


func findMin(s []int) int {
    min := s[0]
    for i := 0; i < len(s); i += 1 {
        if s[i] < min {
            min = s[i]
        }
    } 

    return min
}
