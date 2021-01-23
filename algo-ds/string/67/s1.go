package main

import (
	"fmt"
	"strings"
)


func main() {
	s := []string{"100", "101", "0", "1", "0", "0", "1", "1", "11", "1", "1010", "1011"}
	for i := 0; i < len(s); i += 2 {
		fmt.Printf("a = %v b = %v rs = %v\n", s[i], s[i+1], addBinary(s[i], s[i+1]))
	}
}

func addBinary(a string, b string) string {
	// Time: O(n)
	// Space: O(n)
	l1 := len(a) - 1
	l2 := len(b) - 1

	c := 0 // carry
	rs := 0
	tmp1 := 0
	tmp2 := 0
	var str strings.Builder

	for l1 >= 0 || l2 >= 0 {
		if l1 >= 0 {
			tmp1 = convBinary(a[l1])
		} else {
			tmp1 = 0
		}

		if l2 >= 0 {
			tmp2 = convBinary(b[l2])
		} else {
			tmp2 = 0
		}

		rs = tmp1&1 + tmp2&1 + c
		c = rs >> 1
		rs = rs & 1
		if rs == 1 {
			str.WriteByte('1')
		} else {
			str.WriteByte('0')
		}
		l1 -= 1
		l2 -= 1
	}

	if c == 1 {
		str.WriteByte('1')
	}

	var str2 strings.Builder
	t := str.String()
	for i := len(t) - 1; i >= 0; i -= 1 {
		str2.WriteByte(t[i])
	}
	return str2.String()
}


func convBinary(c byte) int {
	if c == '1' {
		return 1
	}
	return 0
}
