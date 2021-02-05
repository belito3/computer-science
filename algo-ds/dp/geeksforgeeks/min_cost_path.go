// https://www.geeksforgeeks.org/min-cost-path-dp-6/
package main

import "fmt"

func main() {
    fmt.Println(minPathSum([][]int{{1,2,3},{4,8,2},{1,5,3}}))
    fmt.Println(minPathSum([][]int{{1,3,1},{1,5,1},{4,2,1}}))
    fmt.Println(minPathSum([][]int{{1,2,3},{4,5,6}}))
}

func minPathSum(grid [][]int) int {
    // DP: optimal substructure 
    //if len(grid) == 0 || len(grid[0]) == 0 {
    //    return 0
    //}

    m := len(grid)
    n := len(grid[0])
    // calculate cost row[0]
    for j := 1; j < n; j++ {
        grid[0][j] += grid[0][j-1]
    }

    // calculate cost col[0]
    for i := 1; i < m; i++ {
        grid[i][0] += grid[i-1][0]
    }

    for i := 1; i < m; i++ {
        for j := 1; j < n; j++ {
            grid[i][j] += findMin([]int{grid[i-1][j], grid[i][j-1]})
        }
    }
    return grid[m-1][n-1]
}

func findMin(s []int) int {
    min := s[0]
    for i := 1; i < len(s); i++ {
       if s[i] < min {
           min = s[i]
       }
    }
    return min
}
