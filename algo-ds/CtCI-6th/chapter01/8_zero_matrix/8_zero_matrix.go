package main

import "fmt"

func main() {
	matrix := makeMatrix(3, 4)
	fmt.Println(matrix)
	zeroMatrix(matrix)
	fmt.Println(matrix)
	
	mat := [][]int{{1,2,3,4}, {5,0,7,8}, {0,10,11,12}, {13,14,15,0}}
	fmt.Println(mat)
	zeroMatrix(mat)
	fmt.Println(mat)
}

func zeroMatrix(matrix [][]int) {
	m := len(matrix)	
	n := len(matrix[0])
	
	isSetColZero := false
	isSetRowZero := false

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if matrix[i][j] == 0 {
				matrix[i][0] = 0
				matrix[0][j] = 0
				if i == 0 {
					isSetRowZero = true
				}
				if j == 0 {
					isSetColZero = true
				}
			}			
		}
	}
	
	// Examine each row
	for i := m - 1; i > 0; i-- {
		if matrix[i][0] == 0 {
			// set entire row i to 0
			fmt.Println("set row ", i)
			zeroHelper(matrix, i)	
		}	
	}	
	
	// Examine each column
	for i := n - 1; i > 0; i-- {
		if matrix[0][i] == 0 {
			// set entire col i to 0
			fmt.Println("set col ", i)
			zeroHelper(matrix, m+i)
		}
	}
	if isSetColZero {
		zeroHelper(matrix, m)
	}
	if isSetRowZero {
		zeroHelper(matrix, 0)
	}
	
	
}

func zeroMatrix1(matrix [][]int) {
	m := len(matrix)
	n := len(matrix[0])
	marker := make([]int, m + n) 	
	
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if matrix[i][j] == 0 {
				// mark  row[i]
				marker[i] = 1
				// mark col[j]
				marker[m+j] = 1	
			}
		}
	}
	
	for k := 0; k < m + n; k++ {
		if marker[k] == 1 {
			zeroHelper(matrix, k)
		}
	} 		
}


func zeroHelper(matrix [][]int, k int) {
	m := len(matrix)
 	n := len(matrix[0])
	if k < m {
		// set entire row[k] to 0 
		for i := 0; i < n; i++ {
			matrix[k][i] = 0
		}
	} else {
		// set entire col[k-m] to 0
		for i := 0; i < m; i++ {
			matrix[i][k-m] = 0
		}
	}

}

func makeMatrix(m, n int) [][]int {
	matrix := make([][]int, m)
	for i := 0; i < m; i++ {
		list := make([]int, n)
		for j := 0; j < n; j++ {
			list[j] = i*n + j
		}
		matrix[i] = list
	}
	return matrix
}
