package main

import "fmt"

func main() {
	tests := []string{"aabcb", "", " ", "aa ", "a", "Tact Coa", "abc"}
	for _, t := range(tests) {
		fmt.Printf("s = %s, rs = %t\n", t, isPalindromePemutation(t))
	}
}

func isPalindromePemutation(str string) bool {
	// Assume all character is ASCII
	var freq [26]int
	odd, num := 0, 0
	for _, s := range str {
		c := toLowerCase(s)	
		if c != ' ' {
			freq[c-'a'] += 1
			num += 1
		} 
	}  
	
	// Count odd letter
	for i := 0; i < 26; i++ {
		if freq[i] & 1 != 0 {
			odd++
		}
		if odd > 1 {
			return false
		}	
	}
	//fmt.Printf("num = %d, odd = %d \n", num, odd)
	
	if (num & 1 == 0 && odd == 0) || (num & 1 != 0 && odd == 1) {
		return true
	}	
	return false
}

func toLowerCase(c rune) rune {
	if c >= 'A' && c <= 'Z' {
		return c + ' ' 
	}
	return c
}
