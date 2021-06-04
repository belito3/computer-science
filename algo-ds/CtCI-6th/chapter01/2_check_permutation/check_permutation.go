package main

import (
	"fmt"
	"sort"
	"strings"
)

func main() {
	s := []string{"hello", "olleh", "asd", "as", "", "a", "a", "", "asdf", "asde", "apple", "papel", "carrot", "tarroc", "hello", "llloh"}
	for i := 0; i < len(s); i += 2 {
		fmt.Printf("s1 = %s, s2 = %s, rs = %t\n", s[i], s[i+1], isPermutation(s[i], s[i+1]))
	}
}

//
func isPermutation2(str1, str2 string) bool {
	// Sort string
	// Time O(nlogn)
	// Space O(n)
	if len(str1) != len(str2) {
		return false
	}	

	str3 := SortString(str1)
	fmt.Println("sorted: ", str3)
	str4 := SortString(str2)	
        fmt.Println("sorted: ", str4)
	for i := 0; i < len(str3); i++ {
		if str3[i] != str4[i] {
			return false
		}
	}
	return true
		
}

func SortString(str string) string {
	sp := strings.Split(str, "")
	sort.Strings(sp)
	return	strings.Join(sp, "")
}

func isPermutation(str1, str2 string) bool {
	// Hash table
	// Time: O(N)
	// Space: O(N)
	if len(str1) != len(str2) {
		return false
	}

	m := [128]int{} // Assume character of set string are  ASCII
	for _, s := range str1 {
		m[s] += 1
	}
	
	for _, s := range str2 {
		m[s] -= 1
		if m[s] < 0 {
			return false
		}
	}

	return true
}


