package main

import "fmt"

func main() {
	s := []string{"", "abc", "bascs"}	
	for _, word := range s {
		fmt.Printf("s = %s, isUnique = %v\n", word, isUnique(word))
	}
	 
}

/* Assumes only letters a through z */
func isUnique(word string) bool {
	// S3: bit manipulation
	// Need 26 bit to indicate character x whether is contained in string word 
	// Time O(n)
	// Space O(1)
	if len(word) > 26 {
		return false
	}
	
	check := 0
	for _, w := range word {
		tmp := 1 << (w - 'a') 
		if check & tmp > 0 {
			return false
		} else {
			check |= tmp
		}	
	}
	return true	
}
func isUnique2(word string) bool {
	// S2: Hash table
	// Time: O(n)
   	// Space: O(n)
	m := make(map[rune]bool)
	for _, c := range word {
		if m[c] {
			return false
		} else {
			m[c] = true
		}

	}	
	return true
}

func isUnique1(word string) bool {
	// S1: Brute force: time O(n^2), space O(1)
	l := len(word)
	if l < 2 {
		return true
	}

	for i := 0; i <= l-2; i++ {
		for j := i + 1; j <= l - 1; j++ {
			if word[i] == word[j] {
				return false
			}
		} 	
	}
	return true
}
