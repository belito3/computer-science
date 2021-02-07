//https://www.geeksforgeeks.org/subset-sum-problem-dp-25/
package main

import "fmt"

func main() {
	set1 := []int{3, 34, 4, 12, 5, 2}
	fmt.Printf("set = %d sum = %d rs = %t\n", set1, 9, isSubsetSum(set1, 9))
	fmt.Printf("set = %d sum = %d rs = %t\n", set1, 30, isSubsetSum(set1, 30))
}

func isSubsetSum(set []int, sum int) bool {
	// Time: O(len(set)*sum)
	// Space: O(len(set)*sum)
	l := len(set)
	d := make([][]bool, l)
	for i := range d {
		d[i] = make([]bool, sum+1)
	}
	for j := 0; j <= sum; j++ {
		// j is current sum
		for i := 0; i < l; i++ {
			if set[i] == j {
				d[i][j] = true
			} else if set[i] > j {
				if i >=1 {
					d[i][j] = d[i-1][j]
				} else {
					d[i][j] = false
				}
			} else { // set [i] < j
				if i < 1 {
					d[i][j] = false
				} else {
					d[i][j] = d[i-1][j] || d[i-1][j-set[i]]
				}
			}
		}
	}
	for i := 0; i < l; i++ {
		if d[i][sum] {
			return true
		}
	}
	return false
}

func isSubsetSum1(set []int, sum int) bool {
	// S1: recursion
	// Time: O(2^n)
	return subsetSum(set, len(set)-1, sum)
}

func subsetSum(set []int, n, sum int) bool {
	if n < 0 {
		return false
	}
	if set[n] == sum {
		return true
	}
	if set[n] > sum {
		return subsetSum(set, n-1, sum)
	}
	// set[n] < sum
	return subsetSum(set, n-1, sum - set[n]) || subsetSum(set, n-1, sum)
}


