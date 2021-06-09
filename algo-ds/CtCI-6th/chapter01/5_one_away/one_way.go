package main

import ( 
	"fmt"
	"math"
)

func main() {
	input := []string{"pale", "ple", "pales", "pale", "pale", "bale", "pale", "bake", "acv", "abcv", "axv", "acvb", "abc", "abc", "abc", "abx"}
	for i := 0; i < len(input); i += 2 {
		fmt.Printf("str1 = %s, str2 = %s, rs = %t\n", input[i], input[i+1], oneWay(input[i], input[i+1]))
	}

}


func oneWay(str1, str2 string) bool {
	// Can you do all three check in a single pass ? 
	// O(n): n is length of shorter string
	l1 := len(str1)
	l2 := len(str2)
	
	if math.Abs(float64(l1 - l1)) > 1 {
		return false
	}
	
	var s1, s2 string
	
	if l1 > l2 {
		s1 = str1
		s2 = str2
	} else {
		s1 = str2
		s2 = str1
	}	
	
	i, j := 0, 0
	foundDifference := false

	for i < l1 && j < l2 {
		if s1[i] != s2[j] {
			if foundDifference {
				return false
			}
			foundDifference = true
			if l1 != l2 {
				i++
			} else {
				i++
				j++
			}
		} else {
			i++	
			j++
		}
		
	}	
	return true 
}


func oneWay2(str1, str2 string) bool {
	// Do these need to be two separate check ?
	l1 := len(str1)
	l2 := len(str2)
	
	if math.Abs(float64(l1 - l2)) > 1 {
		return false
	}	
	
	min := findMin(l1, l2)
	
	for i := 0; i < min; i++ {
		if str1[i] != str2[i] {
			if l1 == l2 && i != min - 1 {
				fmt.Println("check replace")
				return isSliceEqual(str1[i+1:min], str2[i+1:min])
			} else if l1 < l2 {
				fmt.Println("check add")
				return isSliceEqual(str1[i:l1], str2[i+1:l2])
			} 
			// check delete
			fmt.Println("check delete")
			return isSliceEqual(str1[i+1:l1], str2[i:l2])
		}
	}
	fmt.Println("equal")
	return true
}

func findMin(n1, n2 int) int {
	if n1 > n2 {
		return n2
	}
	return n1
}

func oneWay1(str1, str2 string) bool {
	// Time: O(N)
	// Space: O(1)
	l1 := len(str1)
	l2 := len(str2)

	if l1 + 1 == l2 {
		// check delete
		fmt.Println("check add")
		for i := 0; i < l1; i++ {
			if str1[i] !=  str2[i] {
				return isSliceEqual(str1[i:l1], str2[i+1:l2])
			}
		}
		return true
	} else if l1 == l2 {
		// check replace
		fmt.Println("check replace")
		for i := 0; i < l1 - 1; i++ {
			if str1[i] != str2[i] {
				return isSliceEqual(str1[i+1:l1], str2[i+1:l2])
			}
		}
		return true
	} else if l1 == l2 + 1 {
		// check add
		fmt.Println("check delete")
		for i := 0; i < l2; i++ {
			if str1[i] != str2[i] {
				return isSliceEqual(str1[i+1:l1], str2[i:l2])
			}
		}
		return true
	}	
	return false
}


func isSliceEqual(str1, str2 string) bool {
	for i := 0; i < len(str1); i++ {
		if str1[i] != str2[i] {
			return false
		}
	}
	return true
}
