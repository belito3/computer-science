package main

import "fmt"

func main() {
    test := []string{"hello", "ll", "aaaaaa", "bba", "", "a", "a", "a", "mississippi", "issip"}

    for i := 0; i < len(test); i += 2 {
        fmt.Printf("s1=%v  s2=%v  i=%v\n", test[i], test[i+1], strStr1(test[i], test[i+1]))
    }
}

func strStr(haystack string, needle string) int {
	return 0
}

func strStr1(haystack string, needle string) int {
	// S1: Bureforce - Native Search
	// Time: O(n) - O(m*n)
	// Space: O(1)
	if needle == "" {
		return 0
	}
	m := len(haystack)
	n := len(needle)

	for i := 0; i < m - n + 1; i++ {
		j := 0
		for ; j < n; j++ {
			if haystack[i+j] != needle[j] {
				break
			}
		}
		// trick j++
		if j == n {
			return i
		}
	}

	return -1
}


