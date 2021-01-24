package main

import (
	"fmt"

)

func main() {
	s := []string{"A man, a plan, a canal: Panama", "race a car", "   ", " a   ", " a   a ", ".,"}
	for _, str := range(s) {
		fmt.Printf("str = %v, rs = %v\n", str, isPalindrome(str))
	}
}

func isPalindrome(s string) bool {
	// Time: O(n)
	// Space: O(1)
	l := len(s)
	if l == 0 {
		return true
	}

	h := 0
	t := l - 1
	v1, v2  := false, false
	var c1, c2 byte
	for h <= t {
		// find head
		if !v1 || !v2 {
			if !v1 {
				v1, c1 = isValidChar(s[h])
				if !v1 {
					h += 1 
				}
			}

			if !v2 {
				v2, c2 = isValidChar(s[t])
				if !v2 {
					t -= 1
				}
			}
			continue
		}
		fmt.Printf("c1 = %c, c2 = %c\n", c1, c2)
		fmt.Printf("h = %v, t = %v \n", h, t)

		if (c1 != c2) && v1 && v2 {
			return false
		}
		h += 1
		t -= 1
		v1 = false
		v2 = false
	}
	return true
}


func isValidChar(s byte) (v bool, c byte) {
	v = false
	c = s
	if (s >= '0' && s <= '9') || (s >= 'A' && s <= 'Z') || (s >= 'a' && s <= 'z') {
		v = true
	}
	if (s >= 'a' && s <= 'z') {
		s -= ' '
		c = s
	}
	return
}
