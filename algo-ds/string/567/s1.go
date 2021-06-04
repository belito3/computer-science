package main

import "fmt"

func main() {
	s := []string{"ab", "eidbaoooo", "ab", "eidboaoo", "a", "b", "", "", "", "a"}
	for i := 0; i < len(s); i += 2 {
		fmt.Printf("s1 = %s, s2 = %s, rs = %t\n", s[i], s[i+1], checkInclusion(s[i], s[i+1]))	
	}
}


func checkInclusion(s1 string, s2 string) bool {
	// Hash table + sliding window
	// Time: (l2 - l1) * 26 + l1
	// Space: O(1)
	if len(s1) > len(s2) {
		return false
	}
	
	// Init letter1 and letter2 
	letter1 := [26]int{}	
	letter2 := [26]int{}
	
	for i := 0; i < len(s1); i++  {
		c1 := s1[i]
		letter1[c1 - 'a'] += 1
		
		c2 := s2[i]
		letter2[c2 - 'a'] +=1
	}
	
	// compare letter1 and letter2
	if letter1 == letter2 {
		return true
	}	
	
	for i := 1; i < len(s2) - len(s1) + 1; i++ {
		// Update letter2
		letter2 = updateLetter(letter2, s2[i-1], s2[i-1+len(s1)])
		//fmt.Printf("letter1 = %v, letter2 = %v\n", letter1, letter2)
		if letter1 == letter2 {
			return true
		}
	}
	return false
}

func updateLetter(letter [26]int, char1, char2 byte) [26]int {
	letter[char1 - 'a'] -= 1
	letter[char2 - 'a'] += 1
	return letter
}


