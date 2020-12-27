package main

import (
	"fmt"
	"strings"
)

func main() {
	strs := []string{"flower", "flow", "flight"}
	strs = []string{"dog", "racecar", "car"}
	strs = []string{"ab", "a"}
	strs = []string{"a", "a", "a"}
	fmt.Println(longestCommonPrefix(strs))
}

func longestCommonPrefix(strs []string) string {
	// S2: Vertical scanning
	// Time: O(S)
	// Space: O(1)
	cnt := 0
	if len(strs) == 0 {
		return ""
	}
	for i := 0; i < len(strs[0]); i++ {
		for j := 1; j < len(strs); j++ {
			if i == len(strs[j]) || strs[j][i] != strs[0][i] {
				return strs[0][0 : cnt]
			}
		}
		cnt += 1
	}
	return strs[0][0 : cnt]
}

func longestCommonPrefix1(strs []string) string {
	//S1: Horizontal scanning
	// time: O(S) - where S is the sum of all characters in all strings
	// space: O(1)
	if len(strs) == 0 {
		return ""
	}

	prefix := strs[0]
	for i := 1; i < len(strs); i++ {
		for strings.Index(strs[i], prefix) == -1 {
			prefix = prefix[0: len(prefix) - 1]
			if len(prefix) == 0 {
				return ""
			}
		}
	}
	return prefix
	 
}
