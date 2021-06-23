package main

import "fmt"


func main(){
    fmt.Println(generate(5))
}

func generate(numRows int) [][]int {
    s1 := []int{1}
    s2 := []int{1, 1}

    if numRows == 1 {
        return [][]int{s1} 
    }

    s := [][]int{s1, s2}
    if numRows == 2 {
        return s
    }

    for i := 2; i < numRows; i += 1 {
        si := make([]int,i+1) // make slice with size = i
        for j := 0; j <= i; j += 1 {
            if j == 0 || j == i{
                si[j] = 1
            } else {
                si[j] = s[i-1][j-1] + s[i-1][j]
            }
        }
        s = append(s, si)
    }

    return s
}
