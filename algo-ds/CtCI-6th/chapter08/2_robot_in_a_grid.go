package main 

import "fmt"


func main() {
    m := 3
    n := 7
    fmt.Println(uniquePaths(m, n))
}

func uniquePaths(m, n int) int {
    mat := make_matrix(m, n)
    return helper(m-1, n-1, mat)
}

func helper(m, n int, mat [][]int) int {
    if m == 0 || n == 0 {
        mat[m][n] = 1
        return 1
    }

    if mat[m][n] != 0 {
        return mat[m][n]
    }

    mat[m][n] = helper(m-1, n, mat) + helper(m, n-1, mat)
    return mat[m][n]
}

func make_matrix(m, n int) [][]int {
    mat := make([][]int, m)
    for i := 0; i < m; i += 1 {
        mat[i]= make([]int, n)
    }
    return mat
}
