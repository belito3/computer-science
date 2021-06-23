package main

import (
	"fmt"
	"strings"
)


func main() {
        input := []string{"", "", "abcde", "cdeab", "abcde", "abced", "a", "a", "a", "b", "abcde", "bcdea"}
        for i := 0; i < len(input); i += 2 {
                fmt.Printf("s = %s   goal = %s   rs = %t\n", input[i], input[i+1], rotateString(input[i], input[i+1]))
        }
}


func rotateString(s, goal string) bool {
	// spliting s into two part x = 0,i and y = i:len-1	
	// check contained new string yx with goal
	if len(s) != len(goal) {
		return false
	} else if len(s) == 0 {
		return true	
	}
	
	for i := 0; i < len(s); i++ {
		firstPart := s[0:i]
		secondPart := s[i:len(s)]
		newS := secondPart + firstPart
		if newS == goal {
			return true	
		}	
	}
	return false
}


func rotateString2(s, goal string) bool {
	// S2 Simple check
	// Time O(n^2): string.Contains
	// Space O(1)
	// All rotated of s is contained by s + s
	// create new string s+s with 2length. Not good
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

