package main

import "fmt"

func main(){
    fmt.Println(getRow(3))

}

func getRow(rowIndex int) []int {

    if rowIndex == 0 {
        return []int{1}
    }

    if rowIndex == 1 {
        return []int{1, 1}
    }

    s := make([]int, rowIndex+1)
    s[0] = 1
    s[1] = 1

    for i := 2; i < rowIndex + 1; i++ {
        // Gen row i-th
        for j := i; j > 0; j -= 1 {
            if s[j] == i {
                s[j] = 1
            } else {
                s[j] = s[j] + s[j-1]
            }
        }
    }
    return s
}
