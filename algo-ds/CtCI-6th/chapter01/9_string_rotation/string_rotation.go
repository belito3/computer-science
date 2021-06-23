package main

import (
	"fmt"
	"strings"
)	

func main() {
	input := []string{"abcde", "cdeab", "abcde", "abced", "a", "a", "a", "b", "abcde", "bcdea"}
	for i := 0; i < len(input); i += 2 {
		fmt.Printf("s = %s   goal = %s   rs = %t\n", input[i], input[i+1], rotateString(input[i], input[i+1]))
	}
}


func rotateString(s, goal string) bool {
	// spliting s into two part x and y: s = xy
	// rotated of s is: yx
	// then rotate of s is alway substring of ss = xyxy
	if strings.Contains(s+s, goal) && (len(s) == len(goal)) {
		return true
	}
	return false
}


func rotateString1(s, goal string) bool {
	// Brute force
	// Time: O(n^2)
	// Space: O(1)
	if len(s) != len(goal) {
		return false
	} else if s == "" {
		return true
	}
	
	l := len(s)
	for i := 0; i < l; i++ { // Shift i
		equal := false
		for j := 0; j < l; j++ {
			// Compare s[(j + i) % l] with goal[j]
			if s[(j+i)%l] == goal[j] {
				equal = true
			} else {
				equal = false
				break	
			}
		}	
		if equal {
			return true
		}
	}
	return false
}

