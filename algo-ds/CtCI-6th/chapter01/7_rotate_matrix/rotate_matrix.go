package main

import (
	"fmt"
	"math"
)

func main() {
	for i := 1; i < 6; i++ {
		matrix := makeMatrix(i, i)
		rotateMatrix(matrix)
		fmt.Println(matrix)
	}
}


func rotateMatrix(matrix [][]int) {
	// Time: O(n^2): we must touch all element in matrix
	// Space: O(1)
	// Solution: split matrix to layers
	// swap index by index from top <- left <- bottom <- right
	// VE hinh ma tran 4x4: 00 01 02 03, ... -> de tim duoc cac gia tri vong for   
	n := len(matrix)
	numLayer :=  int(math.Ceil(float64(n) / 2.0))
	
	for layer := 0; layer < numLayer; layer++ {
		start := layer
		end := n - start - 1		
		for i:= start; i < end; i++ {
			// temp = top
			//fmt.Println("top: ", start, i)
			temp := matrix[start][i] // temp = top	
			// top = left
			//fmt.Println("left: ", i+1, start)
			matrix[start][i] = matrix[n-i-1][start] // top = left
			// left = bottom
			//fmt.Println("bottom: ", end, n- i - 1)
			matrix[n-i-1][start] = matrix[end][n-i-1]	
			// button = right
			//fmt.Println("right: ", i, end)
			matrix[end][n-i-1] = matrix[i][end] 
			// right = top
			matrix[i][end] = temp
			
		}
	}
				
}


func makeMatrix(m, n int) [][]int {
	matrix := make([][]int, n)
	fmt.Print("[")
	for i := 0; i < m; i++ {
		fmt.Print("[")
		list := make([]int, n)
		for j := 0; j < n; j++ {
			fmt.Print(i*n + j)
			if j != n - 1 {
				fmt.Print(",")
			}
			list[j] = i*n + j
		}
		matrix[i] = list
		fmt.Print("]")
		if i != m - 1 {
			fmt.Print(",")
		}
	}	
	fmt.Print("]")
	fmt.Println()
	return matrix
}
