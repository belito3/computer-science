package main

import "fmt"

func main() {
    test := []string{"hello", "ll", "aaaaaa", "bba", "", "a", "a", "a", "mississippi", "issip"}

    for i := 0; i < len(test); i += 2 {
        fmt.Printf("s1=%v  s2=%v  i=%v\n", test[i], test[i+1], strStr(test[i], test[i+1]))
    }
    fmt.Println(computeLPS("AAACAAAA"))
}

func strStr(haystack string, needle string) int {
	m := len(haystack)
	n := len(needle)

	if n == 0 {
		return 0
	}

	lps := computeLPS(needle)

	for i, j := 0, 0; i < m; {
		if needle[j] == haystack[i] {
			i += 1
			j += 1
		}
		if j == n {
			return i - j
		}

		if i < m && haystack[i] != needle[j] {
			if j == 0 {
				i += 1
			} else {
				j = lps[j-1]
			}
		}
	}

	return -1
}

func computeLPS(needle string) []int {
	M := len(needle)
	lps := make([]int, M)

	lps[0] = 0
	i := 1
	l := 0
	for i < M {
		if needle[i] == needle[l] {
			l += 1
			lps[i] = l
			i += 1
		} else {
			if l != 0 {
				l = lps[l-1] // ???/
			} else {
				lps[i] = 0
				i += 1
			}

		}
	}
	return lps
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


