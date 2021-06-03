package main

import "fmt"

func main() {
	s := []string{"", "abc", "bascs"}	
	for _, word := range s {
		fmt.Printf("s = %s, isUnique = %v\n", word, isUnique(word))
	}
	 
}

func isUnique(word string) bool {
	// S2: Hash table
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
