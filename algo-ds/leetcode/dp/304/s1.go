package main

import "fmt"

func main() {
    // input: [[]],
    input := [][]int{{3,0,1,4,2},{5,6,3,2,1},{1,2,0,1,5},{4,1,0,1,7},{1,0,3,0,5}}
    mat := Constructor(input)
    rects := [][]int{{2,1,4,3}, {0,0,0,1}} 
    for _, r := range(rects) {
        fmt.Printf("(%d, %d) -> (%d, %d)\n", r[0], r[1], r[2], r[3])
        fmt.Println("rs: ", mat.SumRegion(r[0], r[1], r[2], r[3]))
    }
}

type NumMatrix struct {
    sum [][]int
}

func Constructor(matrix [][]int) NumMatrix {
    // Time query: o(1)
    // Time pre-computation: O(m*n)
    // Space: O(m*n)
    if len(matrix) == 0 || len(matrix[0]) == 0{
         return NumMatrix{}
    }
    m := len(matrix)
    n := len(matrix[0])
    fmt.Println("m , n", m, n)
    sum := make([][]int, m+1)
    for i := 0; i < m+1; i++ {
        sum[i] = make([]int, n+1)
    }

    //var sum [m+1][n+1]int

    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            sum[i+1][j+1] = matrix[i][j] + sum[i+1][j]
        }
    }
    //fmt.Println("a1 :", sum)

    for j := 0; j < n; j++ {
        for i := 0; i < m; i++ {
            sum[i+1][j+1]= sum[i][j+1] + sum[i+1][j+1]
        }
    }

    //fmt.Println("a2: ", sum)
    return NumMatrix{sum: sum}
}

func (this *NumMatrix) SumRegion(row1 int, col1 int, row2 int, col2 int) int {
    return this.sum[row2+1][col2+1] - this.sum[row1][col2+1] - (this.sum[row2+1][col1] - this.sum[row1][col1])
}


